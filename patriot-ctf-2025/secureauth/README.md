# 🔐 SecureAuth™ — Patriot CTF 2025

> **Room / Challenge:** 🔐 SecureAuth™ (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** Patriot CTF 2025
- **Challenge:** 🔐 SecureAuth™ (web)
- **Date:** `24-11-2025`

---

## Goal

This app is vulnerable to wrong logic coding and SQL Injection, tried and get the flag

## My Solution

Logged as `guest` with password `guest123`, it takes us to the home page and there is a message: `⚠️ Admin privileges required for flag access`. So we have to log in as admin. Initially, I tried to decode the cookie value and encode a new one with admin privileges however I don't know the secret key so it is impossible.

Then I logged out and tried some SQL Injection and found an unusual way to logged in as admin:

```json
{
  "username": "admin",
  "password": "",
  "remember": true
}
```

This returns the flag. The app is vulnerable with Python Type Juggling
