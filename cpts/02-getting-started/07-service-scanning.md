# Section 07: Service Scanning

Module: 02. Getting Started

---

## Questions & Answers

### 1. Perform an Nmap scan of the target. What does Nmap display as the version of the service running on port 8080?

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ nmap -sC -sV 10.129.132.119
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 05:50 EDT
Nmap scan report for 10.129.132.119
Host is up (0.16s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.14.112
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Feb 25  2021 pub
22/tcp   open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 a0:01:d7:79:e9:d2:09:2a:b8:d9:b4:9a:6c:00:0c:1c (RSA)
|   256 2b:99:b2:1f:ec:1a:5a:c6:b7:be:b5:50:d1:0e:a9:df (ECDSA)
|_  256 e4:f8:17:8d:d4:71:d1:4e:d4:0e:bd:f0:29:4f:6d:14 (ED25519)
80/tcp   open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-title: PHP 7.4.3 - phpinfo()
|_http-server-header: Apache/2.4.41 (Ubuntu)
139/tcp  open  netbios-ssn Samba smbd 4
445/tcp  open  netbios-ssn Samba smbd 4
2323/tcp open  telnet      Linux telnetd
8080/tcp open  http        Apache Tomcat
|_http-title: Apache Tomcat
|_http-open-proxy: Proxy might be redirecting requests
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: GS-SVCSCAN, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-time: 
|   date: 2026-07-23T09:50:49
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: -1s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 34.40 seconds
```

**Answer:** `Apache Tomcat`

---

### 2. Perform an Nmap scan of the target and identify the non-default port that the telnet service is running on.

Context:
```bash
2323/tcp open  telnet      Linux telnetd
```

**Answer:** `2323`

---

### 3. List the SMB shares available on the target host. Connect to the available share as the bob user. Once connected, access the folder called 'flag' and submit the contents of the flag.txt file.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ smbclient -N -L \\\\10.129.132.119

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	users           Disk      
	IPC$            IPC       IPC Service (gs-svcscan server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ smbclient \\\\10.129.132.119\\users
Password for [WORKGROUP\htb-ac-2162140]:
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_ACCESS_DENIED listing \*
smb: \> ^C
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ smbclient -U bob \\\\10.129.132.119\\users
Password for [WORKGROUP\bob]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Feb 25 18:06:52 2021
  ..                                  D        0  Thu Feb 25 15:05:31 2021
  flag                                D        0  Thu Feb 25 18:09:26 2021
  bob                                 D        0  Thu Feb 25 16:42:23 2021

		4062912 blocks of size 1024. 1350288 blocks available
smb: \> get flag
NT_STATUS_FILE_IS_A_DIRECTORY opening remote file \flag
smb: \> cd flag
smb: \flag\> ls
  .                                   D        0  Thu Feb 25 18:09:26 2021
  ..                                  D        0  Thu Feb 25 18:06:52 2021
  flag.txt                            N       33  Thu Feb 25 18:09:26 2021
get
		4062912 blocks of size 1024. 1350288 blocks available
smb: \flag\> get flag.txt
getting file \flag\flag.txt of size 33 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \flag\> ^C
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ cat flag.txt
dceece590f3284c3866305eb2473d099
```

**Answer:** `dceece590f3284c3866305eb2473d099`

---


[Back to Module Index](./README.md)