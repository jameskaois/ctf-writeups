# Section 09: Filtering Results

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Try running a VHost fuzzing scan on 'academy.htb', and see what other VHosts you get. What other VHosts did you get?

Context:
```bash
─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u http://academy.htb:30474/ -H 'Host: FUZZ.academy.htb' -fs 986

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://academy.htb:30474/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.academy.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 986
________________________________________________

admin                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
test                    [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
```

**Answer:** `test.academy.htb`

---

[Back to Module Index](./README.md)
