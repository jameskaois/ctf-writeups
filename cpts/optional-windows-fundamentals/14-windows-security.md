# Section 14: Windows Security

Optional Module: Windows Fundamentals

---

## Questions & Answers

### 1. Find the SID of the bob.smith user.

Context:
```cmd
C:\Users\htb-student>wmic useraccount get name,sid
Name                SID
Administrator       S-1-5-21-2614195641-1726409526-3792725429-500
bob.smith           S-1-5-21-2614195641-1726409526-3792725429-1003
DefaultAccount      S-1-5-21-2614195641-1726409526-3792725429-503
defaultuser0        S-1-5-21-2614195641-1726409526-3792725429-1000
Guest               S-1-5-21-2614195641-1726409526-3792725429-501
htb-student         S-1-5-21-2614195641-1726409526-3792725429-1002
mrb3n               S-1-5-21-2614195641-1726409526-3792725429-1001
WDAGUtilityAccount  S-1-5-21-2614195641-1726409526-3792725429-504
```

**Answer:** `S-1-5-21-2614195641-1726409526-3792725429-1003`

---

### 2. What 3rd party security application is disabled at startup for the current user? (The answer is case sensitive).

Context:
```cmd
C:\Users\htb-student>reg query "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run"

HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\StartupApproved\Run
    OneDrive    REG_BINARY    03000000D674D894ED16D801
    NordVPN    REG_BINARY    03000000EABC5C91ED16D801
```

**Answer:** `NordVPN`

---

[Back to Module Index](./README.md)
