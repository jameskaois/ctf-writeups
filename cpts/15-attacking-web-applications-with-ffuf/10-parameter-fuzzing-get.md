# Section 10: Parameter Fuzzing - GET

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Using what you learned in this section, run a parameter fuzzing scan on this page. What is the parameter accepted by this webpage?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://admin.academy.htb:30474/admin/admin.php?FUZZ=key -fs 798
'
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://admin.academy.htb:30474/admin/admin.php?FUZZ=key
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 798
________________________________________________

user                    [Status: 200, Size: 783, Words: 221, Lines: 54, Duration: 167ms]
:: Progress: [6453/6453] :: Job [1/1] :: 239 req/sec :: Duration: [0:00:30] :: Errors: 0 ::
```

**Answer:** `user`

---

[Back to Module Index](./README.md)
