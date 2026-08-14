# Section 05: Windows Registry

Optional Module: Windows Fundamentals

---

## Questions & Answers

### 1. Use reg.exe to disable UAC on the target system. After modifying EnableLUA, what hexadecimal value is returned by reg query?

Context:
- Disable UAC then restart the target
```powershell
reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f
```
```powershell
PS C:\Users\htb-student> reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System
    EnableLUA    REG_DWORD    0x0
```

**Answer:** `0x0`

---

### 2. Which registry hive stores settings for the currently logged-on user? Format: AAAA_BBBBBBB_CCCC

**Answer:** `HKEY_CURRENT_USER`

---

### 3. What data type is used by the EnableLUA value?

**Answer:** `REG_DWORD`

---

### 4. What data type is used for storing multiple text strings in the Windows Registry?

**Answer:** `REG_MULTI_SZ`

---

[Back to Module Index](./README.md)
