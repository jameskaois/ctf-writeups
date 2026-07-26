# Section 11: Fingerprinting

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. Determine the Apache version running on app.inlanefreight.local on the target system. (Format: 0.0.0)

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ curl -s -I -H "Host: app.inlanefreight.local" http://10.129.137.61
HTTP/1.1 200 OK
Date: Sat, 25 Jul 2026 12:26:09 GMT
Server: Apache/2.4.41 (Ubuntu)
Set-Cookie: 72af8f2b24261272e581a49f5c56de40=ll91k7ve2vtia36vo6eod7or7o; path=/; HttpOnly
Permissions-Policy: interest-cohort=()
Expires: Wed, 17 Aug 2005 00:00:00 GMT
Last-Modified: Sat, 25 Jul 2026 12:26:09 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Type: text/html; charset=utf-8
```
**Answer:** `2.4.41`

---

### 2. Which CMS is used on app.inlanefreight.local on the target system? Respond with the name only, e.g., WordPress.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ whatweb -H "Host: app.inlanefreight.local" http://10.129.137.61 

http://10.129.137.61 [200 OK] Apache[2.4.41], Bootstrap, Cookies[72af8f2b24261272e581a49f5c56de40], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], HttpOnly[72af8f2b24261272e581a49f5c56de40], IP[10.129.137.61], JQuery, MetaGenerator[Joomla! - Open Source Content Management], OpenSearch[http://app.inlanefreight.local/index.php/component/search/?layout=blog&amp;id=9&amp;Itemid=101&amp;format=opensearch], Script, Title[Home], UncommonHeaders[permissions-policy]
```
**Answer:** `Joomla`

---

### 3. On which operating system is the dev.inlanefreight.local webserver running in the target system? Respond with the name only, e.g., Debian.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ curl -s -I -H "Host: dev.inlanefreight.local" http://10.129.137.61
HTTP/1.1 200 OK
Date: Sat, 25 Jul 2026 12:27:58 GMT
Server: Apache/2.4.41 (Ubuntu)
Set-Cookie: 02a93f6429c54209e06c64b77be2180d=ipuj4hi8vtl2fsg47qm8q244oi; path=/; HttpOnly
Expires: Wed, 17 Aug 2005 00:00:00 GMT
Last-Modified: Sat, 25 Jul 2026 12:28:10 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Type: text/html; charset=utf-8
```
**Answer:** `Ubuntu`

---

[Back to Module Index](./README.md)
