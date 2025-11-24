# Feedback Fallout — Patriot CTF 2025

> **Room / Challenge:** Feedback Fallout (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** Patriot CTF 2025
- **Challenge:** Feedback Fallout (web)
- **Date:** `24-11-2025`

---

## Goal

This challenge is built based on CVE-2021-44228, leveraging this and get the flag.

## My Solution

This web challenge takes me so much time to tried to get RCE but then I figured out that to solve this challenge is just guess the secret variable from the server :((.

The web app just have a feedback form which will make a POST request to `/feedback`. Based on the description and the hint on the page, we can guess that this web app is vulnerable because using Log4j which is well known with the vulnerability CVE-2021-44228. We can tried using `${user.name}` we can get `root` in the response.

The flag is stored in the secret `SECRET_FLAG`, submit `${env:SECRET_FLAG}`, examining the response of the POST request to `/feedback` and we can get the flag.

```json
{
  "status": "success",
  "logs": "[2025-02-01 12:34:56] [SESSION:ABC123] User feedback: FLAG{…}"
}
```
