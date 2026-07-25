# Section 10: SMTP

Module: 04. Footprinting

---

## Questions & Answers

### 1. Enumerate the SMTP service and submit the banner, including its version as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ nc -nv 10.129.134.70 25
Connection to 10.129.134.70 25 port [tcp/*] succeeded!
220 InFreight ESMTP v2.11
```

**Answer:** `InFreight ESMTP v2.11`

---

### 2. Enumerate the SMTP service even further and find the username that exists on the system. Submit it as the answer.

Context:
```bash
─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ smtp-user-enum -M VRFY -U footprint.txt -t 10.129.134.70 -w 20
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Usernames file ........... footprint.txt
Target count ............. 1
Username count ........... 102
Target TCP port .......... 25
Query timeout ............ 20 secs
Target domain ............ 

######## Scan started at Thu Jul 23 21:29:45 2026 #########
10.129.134.70: robin exists
```

**Answer:** `robin`

---

[Back to Module Index](./README.md)
