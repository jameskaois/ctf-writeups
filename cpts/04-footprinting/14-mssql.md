# Section 14: MSSQL

Module: 04. Footprinting

---

## Questions & Answers

### 1. Enumerate the target using the concepts taught in this section. List the hostname of MSSQL server.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$  sudo nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 10.129.134.82
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 22:36 EDT
Nmap scan report for 10.129.134.82
Host is up (0.16s latency).

Bug in ms-sql-hasdbaccess: no string output.
PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-empty-password: 
|_  10.129.134.82\MSSQLSERVER: 
| ms-sql-dac: 
|   10.129.134.82\MSSQLSERVER: 
|     port: 1434
|     state: closed
|_    error: ERROR
| ms-sql-ntlm-info: 
|   10.129.134.82\MSSQLSERVER: 
|     Target_Name: ILF-SQL-01
|     NetBIOS_Domain_Name: ILF-SQL-01
|     NetBIOS_Computer_Name: ILF-SQL-01
|     DNS_Domain_Name: ILF-SQL-01
|     DNS_Computer_Name: ILF-SQL-01
|_    Product_Version: 10.0.17763
| ms-sql-config: 
|   10.129.134.82\MSSQLSERVER: 
|_  ERROR: Bad username or password
| ms-sql-info: 
|   10.129.134.82\MSSQLSERVER: 
|     Instance name: MSSQLSERVER
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|     TCP port: 1433
|     Named pipe: \\10.129.134.82\pipe\sql\query
|_    Clustered: false
| ms-sql-xp-cmdshell: 
|_  (Use --script-args=ms-sql-xp-cmdshell.cmd='<CMD>' to change command.)
| ms-sql-dump-hashes: 
|_  10.129.134.82\MSSQLSERVER: ERROR: Bad username or password
|_ms-sql-tables: ERROR: Script execution failed (use -d to debug)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.21 seconds
```

**Answer:** `ILF-SQL-01`

---

### 2. Connect to the MSSQL instance running on the target using the account (backdoor:Password1), then list the non-default database present on the server.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ mssqlclient.py backdoor:Password1@10.129.134.82 -windows-auth
Impacket v0.14.0.dev0+20260407.172353.7fc084ad - Copyright Fortra, LLC and its affiliated companies 

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(ILF-SQL-01): Line 1: Changed database context to 'master'.
[*] INFO(ILF-SQL-01): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server 2019 RTM (15.0.2000)
[!] Press help for extra shell commands
SQL (ILF-SQL-01\backdoor  dbo@master)> SELECT name FROM sys.databases;
name        
---------   
master      
tempdb      
model       
msdb        
Employees   
SQL (ILF-SQL-01\backdoor  dbo@master)> 
```

**Answer:** `Employees`

---

[Back to Module Index](./README.md)
