# Section 16: Living Off The Land

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Enumerate the host's security configuration information and provide its AMProductVersion.

Context:
```powershell
PS C:\Tools> Get-MpComputerStatus


AMEngineVersion                 : 0.0.0.0
AMProductVersion                : 4.18.2109.6
AMRunningMode                   : Not running
AMServiceEnabled                : False
AMServiceVersion                : 0.0.0.0
AntispywareEnabled              : False
AntispywareSignatureAge         : 4294967295
AntispywareSignatureLastUpdated :
AntispywareSignatureVersion     : 0.0.0.0
AntivirusEnabled                : False
AntivirusSignatureAge           : 4294967295
AntivirusSignatureLastUpdated   :
AntivirusSignatureVersion       : 0.0.0.0
BehaviorMonitorEnabled          : False
ComputerID                      : 077DD3DD-5AF2-43E2-900E-D8B5FF616DFA
ComputerState                   : 0
FullScanAge                     : 4294967295
FullScanEndTime                 :
FullScanStartTime               :
IoavProtectionEnabled           : False
IsTamperProtected               : False
IsVirtualMachine                : True
LastFullScanSource              : 0
LastQuickScanSource             : 0
NISEnabled                      : False
NISEngineVersion                : 0.0.0.0
NISSignatureAge                 : 4294967295
NISSignatureLastUpdated         :
NISSignatureVersion             : 0.0.0.0
OnAccessProtectionEnabled       : False
QuickScanAge                    : 4294967295
QuickScanEndTime                :
QuickScanStartTime              :
RealTimeProtectionEnabled       : False
RealTimeScanDirection           : 0
TamperProtectionSource          : N/A
TDTMode                         : N/A
TDTStatus                       : N/A
TDTTelemetry                    : N/A
PSComputerName                  :
```

**Answer:** `4.18.2109.6`

---

### 2. What PowerView function allows us to test if a user has administrative access to a local or remote host?

Context:
```powershell
PS C:\Tools> net localgroup administrators
Alias name     administrators
Comment        Administrators have complete and unrestricted access to the computer/domain

Members

-------------------------------------------------------------------------------
Administrator
INLANEFREIGHT\adunn
INLANEFREIGHT\Domain Admins
INLANEFREIGHT\Domain Users
The command completed successfully.
```

**Answer:** `adunn`

---

### 3. Utilizing techniques learned in this section, find the flag hidden in the description field of a disabled account with administrative privileges. Submit the flag as the answer.

Context:
```powershell
PS C:\Tools> Get-ADGroupMember -Identity "Domain Admins" |
>>     Get-ADUser |
>>     Where-Object {$_.Enabled -eq $false} |
>>     Select-Object Name, SamAccountName, Enabled
>>

Name       SamAccountName Enabled
----       -------------- -------
Betty Ross bross            False
Get-ADUser : Cannot find an object with identity: 'CN=Secadmins,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL'
under: 'DC=INLANEFREIGHT,DC=LOCAL'.
At line:2 char:5
+     Get-ADUser |
+     ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (CN=Secadmins,OU...REIGHT,DC=LOCAL:ADUser) [Get-ADUser], ADIdentityNotFo
   undException
    + FullyQualifiedErrorId : ActiveDirectoryCmdlet:Microsoft.ActiveDirectory.Management.ADIdentityNotFoundException,M
   icrosoft.ActiveDirectory.Management.Commands.GetADUser



PS C:\Tools> net user bross /domain
The request will be processed at a domain controller for domain INLANEFREIGHT.LOCAL.

User name                    bross
Full Name                    Betty Ross
Comment                      HTB{LD@P_I$_W1ld}
User's comment
Country/region code          000 (System Default)
Account active               No
Account expires              Never

Password last set            10/27/2021 10:37:07 AM
Password expires             Never
Password changeable          10/28/2021 10:37:07 AM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   Never

Logon hours allowed          All

Local Group Memberships
Global Group memberships     *File Share G Drive   *File Share H Drive
                             *Printer Access       *Contractors
                             *Domain Admins        *Domain Users
                             *VPN Users            *Shared Calendar Read
The command completed successfully.
```

**Answer:** `HTB{LD@P_I$_W1ld}`

---

[Back to Module Index](./README.md)
