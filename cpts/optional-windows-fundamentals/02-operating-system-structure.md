# Section 02: Operating System Structure

Optional Module: Windows Fundamentals

---

## Questions & Answers

### 1. Find the non-standard directory in the C drive. Submit the contents of the flag file saved in this directory.

Context:
```powershell
PS C:\Users\htb-student> dir C:\


    Directory: C:\


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         8/23/2021  10:20 AM                75afac25577675a9bfafd2405602
d-----          9/7/2020   1:41 PM                Academy
d-----         12/7/2019   1:14 AM                PerfLogs
d-r---         1/31/2022   4:05 PM                Program Files
d-r---         1/31/2022   3:01 PM                Program Files (x86)
d-r---         1/31/2022   3:02 PM                Users
d-----         1/31/2022   4:07 PM                Windows


PS C:\Users\htb-student> dir C:\75afac25577675a9bfafd2405602\
dir : Access to the path 'C:\75afac25577675a9bfafd2405602' is denied.
At line:1 char:1
+ dir C:\75afac25577675a9bfafd2405602\
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (C:\75afac25577675a9bfafd2405602\:String) [Get-ChildItem], Unauthorize
   dAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell.Commands.GetChildItemCommand

PS C:\Users\htb-student> dir C:\Academy\


    Directory: C:\Academy


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          9/7/2020  12:17 PM             32 flag.txt


PS C:\Users\htb-student> type C:\Academy\flag.txt
c8fe8d977d3a0c655ed7cf81e4d13c75
PS C:\Users\htb-student>
```

**Answer:** `c8fe8d977d3a0c655ed7cf81e4d13c75`

---

[Back to Module Index](./README.md)
