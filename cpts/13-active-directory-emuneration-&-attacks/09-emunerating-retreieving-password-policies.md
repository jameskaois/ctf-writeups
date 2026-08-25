# Section 09: Enumerating & Retrieving Password Policies

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. What is the default Minimum password length when a new domain is created? (One number)

**Answer:** `7`

---

### 2. What is the minPwdLength set to in the INLANEFREIGHT.LOCAL domain? (One number)

Context:
```bash
┌─[htb-student@ea-attack01]─[/opt]
└──╼ $enum4linux -P 172.16.5.5
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Aug 18 04:58:35 2026

 ========================== 
|    Target Information    |
 ========================== 
Target ........... 172.16.5.5
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ================================================== 
|    Enumerating Workgroup/Domain on 172.16.5.5    |
 ================================================== 
[+] Got domain/workgroup name: INLANEFREIGHT

 =================================== 
|    Session Check on 172.16.5.5    |
 =================================== 
[+] Server 172.16.5.5 allows sessions using username '', password ''

 ========================================= 
|    Getting domain SID for 172.16.5.5    |
 ========================================= 
Domain Name: INLANEFREIGHT
Domain Sid: S-1-5-21-3842939050-3880317879-2865463114
[+] Host is part of a domain (not a workgroup)

 ================================================== 
|    Password Policy Information for 172.16.5.5    |
 ================================================== 


[+] Attaching to 172.16.5.5 using a NULL share

[+] Trying protocol 139/SMB...

	[!] Protocol failed: Cannot request session (Called Name:172.16.5.5)

[+] Trying protocol 445/SMB...

[+] Found domain(s):

	[+] INLANEFREIGHT
	[+] Builtin

[+] Password Info for Domain: INLANEFREIGHT

	[+] Minimum password length: 8
	[+] Password history length: 24
	[+] Maximum password age: Not Set
	[+] Password Complexity Flags: 000001

		[+] Domain Refuse Password Change: 0
		[+] Domain Password Store Cleartext: 0
		[+] Domain Password Lockout Admins: 0
		[+] Domain Password No Clear Change: 0
		[+] Domain Password No Anon Change: 0
		[+] Domain Password Complex: 1

	[+] Minimum password age: 1 day 4 minutes 
	[+] Reset Account Lockout Counter: 30 minutes 
	[+] Locked Account Duration: 30 minutes 
	[+] Account Lockout Threshold: 5
	[+] Forced Log off Time: Not Set


[+] Retieved partial password policy with rpcclient:

Password Complexity: Enabled
Minimum Password Length: 8

enum4linux complete on Tue Aug 18 04:58:37 2026
```

**Answer:** `8`

---

[Back to Module Index](./README.md)
