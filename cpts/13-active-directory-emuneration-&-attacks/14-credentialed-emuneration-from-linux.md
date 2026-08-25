# Section 14: Credentialed Enumeration - from Linux

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. What AD User has a RID equal to Decimal 1170?

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $rpcclient -U "" -N 172.16.5.5
rpcclient $> queryuser 0x492
	User Name   :	mmorgan
	Full Name   :	Matthew Morgan
	Home Drive  :	
	Dir Drive   :	
	Profile Path:	
	Logon Script:	
	Description :	
	Workstations:	
	Comment     :	
	Remote Dial :
	Logon Time               :	Thu, 10 Mar 2022 14:48:06 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 31 Dec 1969 19:00:00 EST
	Password last set Time   :	Tue, 05 Apr 2022 15:34:55 EDT
	Password can change Time :	Wed, 06 Apr 2022 15:34:55 EDT
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0x492
	group_rid:	0x201
	acb_info :	0x00010210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000018
	padding1[0..7]...
	logon_hrs[0..21]...
```

**Answer:** `mmorgan`

---

### 2. What is the membercount: of the "Interns" group?

Context:
```bash
┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $sudo crackmapexec smb 172.16.5.5 -u forend -p Klmcargo2 --groups
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [*] Windows 10.0 Build 17763 x64 (name:ACADEMY-EA-DC01) (domain:INLANEFREIGHT.LOCAL) (signing:True) (SMBv1:False)
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [+] INLANEFREIGHT.LOCAL\forend:Klmcargo2 
SMB         172.16.5.5      445    ACADEMY-EA-DC01  [+] Enumerated domain group(s)
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Administrators                           membercount: 3
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Users                                    membercount: 4
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Guests                                   membercount: 2
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Print Operators                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Backup Operators                         membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Replicator                               membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Remote Desktop Users                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Network Configuration Operators          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Performance Monitor Users                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Performance Log Users                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Distributed COM Users                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  IIS_IUSRS                                membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Cryptographic Operators                  membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Event Log Readers                        membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Certificate Service DCOM Access          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  RDS Remote Access Servers                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  RDS Endpoint Servers                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  RDS Management Servers                   membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Hyper-V Administrators                   membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Access Control Assistance Operators      membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Remote Management Users                  membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Storage Replica Administrators           membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Domain Computers                         membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Domain Controllers                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Schema Admins                            membercount: 3
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Enterprise Admins                        membercount: 3
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Cert Publishers                          membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Domain Admins                            membercount: 19
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Domain Users                             membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Domain Guests                            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Group Policy Creator Owners              membercount: 2
SMB         172.16.5.5      445    ACADEMY-EA-DC01  RAS and IAS Servers                      membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Server Operators                         membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Account Operators                        membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Pre-Windows 2000 Compatible Access       membercount: 3
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Incoming Forest Trust Builders           membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Windows Authorization Access Group       membercount: 2
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Terminal Server License Servers          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Allowed RODC Password Replication Group  membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Denied RODC Password Replication Group   membercount: 8
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Read-only Domain Controllers             membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Enterprise Read-only Domain Controllers  membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Cloneable Domain Controllers             membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Protected Users                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Key Admins                               membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Enterprise Key Admins                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  DnsAdmins                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  DnsUpdateProxy                           membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Contractors                              membercount: 138
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Accounting                               membercount: 15
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Engineering                              membercount: 19
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Executives                               membercount: 10
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Human Resources                          membercount: 36
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Marketing                                membercount: 15
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Operations                               membercount: 16
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Project Management                       membercount: 17
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Sales                                    membercount: 313
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Senior Management                        membercount: 24
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Service Accounts                         membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Information Technology                   membercount: 51
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Management                               membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Tier 1 Admins                            membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Tier 2 Admins                            membercount: 7
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Tier 3 Admins                            membercount: 6
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Tier 4 Admins                            membercount: 5
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Help Desk Level 1                        membercount: 26
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Local Admins                             membercount: 19
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Executive Assistants                     membercount: 8
SMB         172.16.5.5      445    ACADEMY-EA-DC01  CEO                                      membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  CFO                                      membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  CTO                                      membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Computer Group Management                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Exchange Administrator                   membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Exchange User Management                 membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Groups Management                        membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  High-Impact Server Management            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Low-Impact Server Management             membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Medium-Impact Server Management          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Mission-Critical Server Management       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Lync Administrator                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  RBAC Management                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Restricted Users Management              membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Role Group Management                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Servers Management                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Skype User Management                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Standard Computers Management            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Tier Admin Users Management              membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Fileshare Management                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Distribution Group Management            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  GPO Management                           membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Standard Users Management                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Users Management                         membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Print Service Management                 membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Finance                                  membercount: 19
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Purchasing                               membercount: 15
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Shipping                                 membercount: 25
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Warehouse                                membercount: 44
SMB         172.16.5.5      445    ACADEMY-EA-DC01  File Share Admin                         membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  File Share F Drive                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  File Share G Drive                       membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  File Share H Drive                       membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  File Share J Drive                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Printer Access                           membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  MFP Access                               membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  ERP Admin                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  ERP Payment Access                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  ERP Sales                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  ERP Read                                 membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Sales Report Admin                       membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Sales Report Read                        membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Inventory Report Admin                   membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Inventory Report Read                    membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  PLM Admin                                membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  PLM RW                                   membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  PLM Read                                 membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Server Admin                             membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Desktop Admin                            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Merch App Admin                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Merch App Read                           membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Shared Calendar Admin                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Shared Calendar RW                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Shared Calendar Read                     membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  VPN Users                                membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Interns                                  membercount: 10
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Website Admin                            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Barracuda_all_access                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Supervisors Warehouse                    membercount: 15
SMB         172.16.5.5      445    ACADEMY-EA-DC01  QA_users                                 membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Calendar Access                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Nars360_users                            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Finance_billing_ilfreight                membercount: 6
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Nas Group                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Front Desk                               membercount: 6
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Billing                                  membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Finance_old                              membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Barracuda_facebook_access                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Barracuda_parked_sites                   membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Barracuda_youtube_exempt                 membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Rackspace_vpn_access                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Collaboration_users                      membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Ehr_group                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Msp_users                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Billing_users                            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Frontoffice_users                        membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Executive_users                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Communications_users                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Facilities_users                         membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Finance_mgt                              membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Development_users                        membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  SQL Admins                               membercount: 10
SMB         172.16.5.5      445    ACADEMY-EA-DC01  SQL Dev                                  membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  SQL QA                                   membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  SQL Servers                              membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  IT Security                              membercount: 18
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Network Ops                              membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Secadmins                                membercount: 10
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Temp Employees                           membercount: 37
SMB         172.16.5.5      445    ACADEMY-EA-DC01  MSSP Connect                             membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Organization Management                  membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Recipient Management                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  View-Only Organization Management        membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Public Folder Management                 membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  UM Management                            membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Help Desk                                membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Records Management                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Discovery Management                     membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Server Management                        membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Delegated Setup                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Hygiene Management                       membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Compliance Management                    membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Security Reader                          membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Security Administrator                   membercount: 0
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Exchange Servers                         membercount: 2
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Exchange Trusted Subsystem               membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Managed Availability Servers             membercount: 2
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Exchange Windows Permissions             membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  ExchangeLegacyInterop                    membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  $H25000-1RTRKC5S507F                     membercount: 1
SMB         172.16.5.5      445    ACADEMY-EA-DC01  Dev Accounts                             membercount: 2
```

**Answer:** `10`

---


[Back to Module Index](./README.md)
