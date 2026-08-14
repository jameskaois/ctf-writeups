# Section 03: File System

Optional Module: Windows Fundamentals

---

## Questions & Answers

### 1. What system user has full control over the c:\users directory?

Context:
```powershell
PS C:\Users\htb-student> icacls c:\users
c:\users Everyone:(OI)(CI)(RX)
         NT AUTHORITY\SYSTEM:(OI)(CI)(F)
         BUILTIN\Administrators:(OI)(CI)(F)
         WS01\bob.smith:(OI)(CI)(F)
         BUILTIN\Users:(OI)(CI)(RX)

Successfully processed 1 files; Failed processing 0 files
```

**Answer:** `bob.smith`

---

[Back to Module Index](./README.md)
