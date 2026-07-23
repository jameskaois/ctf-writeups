# Section 08: Web Emuneration

Module: 02. Getting Started

---

## Questions & Answers

### 1. 

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://154.57.164.83:30616/FUZZ -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.83:30616/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

index.php               [Status: 200, Size: 990, Words: 424, Lines: 55, Duration: 156ms]
robots.txt              [Status: 200, Size: 45, Words: 3, Lines: 2, Duration: 154ms]
wordpress               [Status: 301, Size: 327, Words: 20, Lines: 10, Duration: 162ms]

┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://154.57.164.83:30616/robots.txt
User-agent: *
Disallow: /admin-login-page.php
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://154.57.164.83:30616/admin-login-page.php

<!DOCTYPE html>
<html>
<style>
    body {
        background-color: #151D2B;
    }

    form {
        background-color: #1A2332;
        width: 25%;
        margin: auto;
        border-radius: 10px;
        color: white;
        font-family: Arial, Helvetica, sans-serif;
    }

    input[type=text],
    input[type=password] {
        background-color: #101927;
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #101927;
        box-sizing: border-box;
        border-radius: 10px;
        color: white;
    }

    button {
        background-color: #2A86FF;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        cursor: pointer;
        width: 100%;
        border-radius: 10px;
    }

    button:hover {
        opacity: 0.8;
    }

    .container {
        padding: 16px;
    }
</style>

<body>
                <form name='login' autocomplete='off' class='form' action='' method='post'>
            <div class='control'>
                <h1>
                    Admin Panel
                </h1>
            </div>
            <div class="container">
                <label for="username"><b>Username</b></label>
                <input name='username' placeholder='Username' type='text'>

                <label for="password"><b>Password</b></label>
                <input name='password' placeholder='Password' type='password'>

                <!-- TODO: remove test credentials admin:password123 -->

                <button type="submit" formmethod='post'>Login</button>
            </div>
        </form>
    </body>

</html>
```
Login with `admin:password123` in `/admin-login-page.php` and got the flag.

**Answer:** `HTB{w3b_3num3r4710n_r3v34l5_53cr375}`

---

[Back to Module Index](./README.md)