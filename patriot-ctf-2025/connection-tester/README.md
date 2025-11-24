# Connection Tester — Patriot CTF 2025

> **Room / Challenge:** Connection Tester (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** Patriot CTF 2025
- **Challenge:** Connection Tester (web)
- **Target / URL:** `http://18.212.136.134:9080/`
- **Date:** `24-11-2025`

---

## Goal

Leveraging SQLi and Command Injection to get the flag.

## My Solution

The app has a login form and there isn't any credentials given, so tried some simple SQL Injection to bypass the login, normally `admin` account existed so inject:

```
Username: admin' --
Password: anything
```

We successfully logged in as `admin`, then there is a connection input, it will ping, so we can use Command Injection to make the server doing other things than `ping`. Payload:

```bash
; cat flag.txt #
```

By this, we can get the flag
