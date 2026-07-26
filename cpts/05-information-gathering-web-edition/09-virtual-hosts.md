# Section 09: Virtual Hosts

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "web"? Answer using the full domain, e.g. "x.inlanefreight.htb"

Context:
```bash
vim /etc/hosts
# add 154.57.164.69 inlanefreight.htb
grep -h ^web /usr/share/wordlists/seclists/Discovery/DNS/* > web.txt
┌──(jameskaois㉿kali)-[~/Documents]
└─$ gobuster vhost -u http://inlanefreight.htb:30777 -w ./web.txt --append-domain 
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://inlanefreight.htb:30777
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  ./web.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
web17611.inlanefreight.htb:30777 Status: 200 [Size: 106]
```
**Answer:** `web17611.inlanefreight.htb`

---

### 2. Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "vm"? Answer using the full domain, e.g. "x.inlanefreight.htb"

Context:
```bash
grep -h ^vm /usr/share/wordlists/seclists/Discovery/DNS/* > vm.txt
┌──(jameskaois㉿kali)-[~/Documents]
└─$ gobuster vhost -u http://inlanefreight.htb:30777 -w ./vm.txt --append-domain
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://inlanefreight.htb:30777
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  ./vm.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
vm5.inlanefreight.htb:30777 Status: 200 [Size: 96]
```
**Answer:** `vm5.inlanefreight.htb`

---

### 3. Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "br"? Answer using the full domain, e.g. "x.inlanefreight.htb"

Context:
```bash
grep -h ^br /usr/share/wordlists/seclists/Discovery/DNS/* > br.txt
┌──(jameskaois㉿kali)-[~/Documents]
└─$ gobuster vhost -u http://inlanefreight.htb:30777 -w ./br.txt --append-domain
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://inlanefreight.htb:30777
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  ./br.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
browse.inlanefreight.htb:30777 Status: 200 [Size: 102]
```
**Answer:** `browse.inlanefreight.htb`

---

### 4. Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "a"? Answer using the full domain, e.g. "x.inlanefreight.htb"

Context:
```bash
grep -h ^a /usr/share/wordlists/seclists/Discovery/DNS/* > a.txt
┌──(jameskaois㉿kali)-[~/Documents]
└─$ gobuster vhost -u http://inlanefreight.htb:30777 -w ./a.txt --append-domain
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://inlanefreight.htb:30777
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  ./a.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
admin.inlanefreight.htb:30777 Status: 200 [Size: 100]
```
**Answer:** `admin.inlanefreight.htb`

---

### 5. Brute-force vhosts on the target system. What is the full subdomain that is prefixed with "su"? Answer using the full domain, e.g. "x.inlanefreight.htb"

Context:
```bash
grep -h ^su /usr/share/wordlists/seclists/Discovery/DNS/* > su.txt
┌──(jameskaois㉿kali)-[~/Documents]
└─$ gobuster vhost -u http://inlanefreight.htb:30777 -w ./su.txt --append-domain
===============================================================
Gobuster v3.8.2
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://inlanefreight.htb:30777
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  ./su.txt
[+] User Agent:                gobuster/3.8.2
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
support.inlanefreight.htb:30777 Status: 200 [Size: 104]
```
**Answer:** `support.inlanefreight.htb`

---


[Back to Module Index](./README.md)
