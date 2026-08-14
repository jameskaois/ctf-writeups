# Section 01: Introduction to Windows

Optional Module: Windows Fundamentals

---

## Questions & Answers

### 1. What is the Build Number of the target workstation?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.216]─[htb-ac-2162140@htb-yj7gs2tppt-htb-cloud-com]─[~]
└──╼ [★]$ KRB5_CONFIG=/dev/null xfreerdp /v:10.129.49.244 /u:htb-student /p:'Academy_WinFun!' /dynamic-resolution /cert:ignore +clipboard
```
```powershell
PS C:\Users\htb-student> Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber

Version    BuildNumber
-------    -----------
10.0.19041 19041


PS C:\Users\htb-student>
```

**Answer:** `19041`

---

### 2. Which Windows NT version is installed on the workstation? (i.e. Windows X - case sensitive)


**Answer:** `Windows 10`

---

[Back to Module Index](./README.md)
