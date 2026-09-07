# Section 07: Sub-domain Fuzzing

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Try running a sub-domain fuzzing test on 'inlanefreight.com' to find a customer sub-domain portal. What is the full domain of it?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u https://FUZZ.inlanefreight.com/

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://FUZZ.inlanefreight.com/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

ns3                     [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 216ms]
support                 [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 289ms]
blog                    [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 307ms]
www                     [Status: 200, Size: 22266, Words: 2903, Lines: 316, Duration: 320ms]
my                      [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 208ms]
customer                [Status: 301, Size: 0, Words: 1, Lines: 1, Duration: 208ms]
```

**Answer:** `customer.inlanefreight.com`

---

[Back to Module Index](./README.md)
