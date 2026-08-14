# Section 09: Interacting with the Windows Operating System

Optional Module: Windows Fundamentals

---

## Questions & Answers

### 1. What is the alias set for the ipconfig.exe command?

Context:
```powershell
Get-Alias

Alias           ifconfig -> ipconfig.exe
```

**Answer:** `ifconfig`

---

### 2. Find the Execution Policy set for the LocalMachine scope.

Context:
```powershell
PS C:\Users\htb-student> Get-ExecutionPolicy -List

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process          Bypass
  CurrentUser       Undefined
 LocalMachine    Unrestricted
```

**Answer:** `Unrestricted`

---

[Back to Module Index](./README.md)
