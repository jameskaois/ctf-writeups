# Section 05: Recursive Fuzzing

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Try to repeat what you learned so far to find more files/directories. One of them should give you a flag. What is the content of the flag?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://154.57.164.82:30474/FUZZ -recursion -recursion-depth 1 -e .php 

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
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

# on at least 3 different hosts.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 167ms]
.php                    [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 167ms]
# directory-list-2.3-small.txt.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
#                       [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
#                       [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
#.php                   [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# or send a letter to Creative Commons, 171 Second Street,.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# Copyright 2007 James Fisher.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# Attribution-Share Alike 3.0 License. To view a copy of this [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# Attribution-Share Alike 3.0 License. To view a copy of this.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
# Priority-ordered case-sensitive list, where entries were found [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 167ms]
# Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 168ms]
#.php                   [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
# Priority-ordered case-sensitive list, where entries were found.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
#.php                   [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
# license, visit http://creativecommons.org/licenses/by-sa/3.0/.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
# on at least 3 different hosts [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
# This work is licensed under the Creative Commons [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
# Copyright 2007 James Fisher [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
#.php                   [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 169ms]
# directory-list-2.3-small.txt [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
# or send a letter to Creative Commons, 171 Second Street, [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
# license, visit http://creativecommons.org/licenses/by-sa/3.0/ [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
                        [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
#                       [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
# This work is licensed under the Creative Commons.php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
index.php               [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
#                       [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 171ms]
# Suite 300, San Francisco, California, 94105, USA..php [Status: 200, Size: 986, Words: 423, Lines: 56, Duration: 170ms]
blog                    [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 167ms]
[INFO] Adding a new job to the queue: http://154.57.164.82:30474/blog/FUZZ

forum                   [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 167ms]

┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ curl http://154.57.164.82:30474/forum/flag.php
HTB{fuzz1n6_7h3_w3b!}
```

**Answer:** `HTB{fuzz1n6_7h3_w3b!}`

---

[Back to Module Index](./README.md)
