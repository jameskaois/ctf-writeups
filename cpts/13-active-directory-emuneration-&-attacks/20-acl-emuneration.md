# Section 20: ACL Emuneration

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. What is the rights GUID for User-Force-Change-Password?

**Answer:** `00299570-246d-11d0-a768-00aa006e0529`

---

### 2. What flag can we use with PowerView to show us the ObjectAceType in a human-readable format during our enumeration?

**Answer:** `ResolveGUIDs`

---

### 3. What privileges does the user damundsen have over the Help Desk Level 1 group?

Context:
```powershell
PS C:\Windows\system32> cd C:\Tools\
PS C:\Tools> Import-Module .\PowerView.ps1
PS C:\Tools> Get-DomainObjectAcl -Identity "Help Desk Level 1" | Where-Object { $_.SecurityIdentifier -match (Convert-NameToSid damundsen) }
>>


ObjectDN              : CN=Help Desk Level 1,OU=Security Groups,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
ObjectSID             : S-1-5-21-3842939050-3880317879-2865463114-4022
ActiveDirectoryRights : ListChildren, ReadProperty, GenericWrite
BinaryLength          : 36
AceQualifier          : AccessAllowed
IsCallback            : False
OpaqueLength          : 0
AccessMask            : 131132
SecurityIdentifier    : S-1-5-21-3842939050-3880317879-2865463114-1176
AceType               : AccessAllowed
AceFlags              : ContainerInherit
IsInherited           : False
InheritanceFlags      : ContainerInherit
PropagationFlags      : None
AuditFlags            : None
```

**Answer:** `GenericWrite`

---

### 4. Using the skills learned in this section, enumerate the ActiveDirectoryRights that the user forend has over the user dpayne (Dagmar Payne).

Context:
```powershell
PS C:\Tools> $UserSID = (Get-DomainUser -Identity forend).objectsid
>> Get-DomainObjectAcl -Identity dpayne -ResolveGUIDs | Where-Object { $_.SecurityIdentifier -eq $UserSID } | Select-Object ActiveDirectoryRights
>>

ActiveDirectoryRights
---------------------
           GenericAll
```

**Answer:** `GenericAll`

---

### 5. What is the ObjectAceType of the first right that the forend user has over the GPO Management group? (two words in the format Word-Word)

Context:
```powershell
PS C:\Tools> $UserSID = Convert-NameToSid forend
>>
PS C:\Tools> Get-DomainObjectACL -Identity "GPO Management" -ResolveGUIDs | Where-Object { $_.SecurityIdentifier -eq $UserSID } | Select-Object ActiveDirectoryRights, ObjectAceType
>>

                      ActiveDirectoryRights ObjectAceType
                      --------------------- -------------
                                       Self Self-Membership
ReadProperty, WriteProperty, GenericExecute
```

**Answer:** `Self-Membership`

---

[Back to Module Index](./README.md)
