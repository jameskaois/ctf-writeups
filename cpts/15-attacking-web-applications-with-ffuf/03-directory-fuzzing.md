# Section 03: Directory Fuzzing

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. In addition to the directory we found above, there is another directory that can be found. What is it?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ locate directory-list-2.3-small.txt
/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt
/usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://154.57.164.82:30474/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.82:30474/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

#                       [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# Copyright 2007 James Fisher [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# directory-list-2.3-small.txt [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
forum                   [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 167ms]
# Attribution-Share Alike 3.0 License. To view a copy of this [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 2158ms]
# or send a letter to Creative Commons, 171 Second Street, [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 2160ms]
#                       [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 3165ms]
blog                    [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 4169ms]
```

**Answer:** `forum`

---

[Back to Module Index](./README.md)
