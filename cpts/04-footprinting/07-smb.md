# Section 07: SMB

Module: 04. Footprinting

---

## Questions & Answers

### 1. What version of the SMB server is running on the target system? Submit the entire banner as the answer.

Context:
```bash
─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ nmap -sC -sV 10.129.134.68 -v
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 20:55 EDT

139/tcp  open  netbios-ssn Samba smbd 4
445/tcp  open  netbios-ssn Samba smbd 4
```

**Answer:** `Samba smbd 4`

---

### 2. What is the name of the accessible share on the target?

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ smbclient -N -L \\\\10.129.134.68

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	sambashare      Disk      InFreight SMB v3.1
	IPC$            IPC       IPC Service (InlaneFreight SMB server (Samba, Ubuntu))
SMB1 disabled -- no workgroup available
```

**Answer:** `sambashare`

---

### 3. Connect to the discovered share and find the flag.txt file. Submit the contents as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ smbclient \\\\10.129.134.68\\sambashare
Password for [WORKGROUP\htb-ac-2162140]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Nov  8 08:43:14 2021
  ..                                  D        0  Mon Nov  8 10:53:19 2021
  .profile                            H      807  Tue Feb 25 07:03:22 2020
  contents                            D        0  Mon Nov  8 08:43:45 2021
  .bash_logout                        H      220  Tue Feb 25 07:03:22 2020
  .bashrc                             H     3771  Tue Feb 25 07:03:22 2020

		4062912 blocks of size 1024. 414248 blocks available
smb: \> cd contents
smb: \contents\> ls
  .                                   D        0  Mon Nov  8 08:43:45 2021
  ..                                  D        0  Mon Nov  8 08:43:14 2021
  flag.txt                            N       38  Mon Nov  8 08:43:45 2021

		4062912 blocks of size 1024. 414248 blocks available
smb: \contents\> get flag.txt
getting file \contents\flag.txt of size 38 as flag.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \contents\> exit
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ cat flag.txt
HTB{o873nz4xdo873n4zo873zn4fksuhldsf}
```

**Answer:** `HTB{o873nz4xdo873n4zo873zn4fksuhldsf}`

---

### 4. Find out which domain the server belongs to.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ rpcclient -U "" 10.129.134.68
rpcclient $> querydominfo
Domain:		DEVOPS
Server:		DEVSMB
Comment:	InlaneFreight SMB server (Samba, Ubuntu)
Total Users:	0
Total Groups:	0
Total Aliases:	0
Sequence No:	1784854969
Force Logoff:	4294967295
Domain Server State:	0x1
Server Role:	ROLE_DOMAIN_PDC
Unknown 3:	0x1
```

**Answer:** `DEVOPS`

---

### 5. Find additional information about the specific share we found previously and submit the customized version of that specific share as the answer.

Context:
```bash
rpcclient $> netsharegetinfo sambashare
netname: sambashare
	remark:	InFreight SMB v3.1
	path:	C:\home\sambauser\
	password:	
	type:	0x0
	perms:	0
	max_uses:	-1
	num_uses:	1
revision: 1
type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE 
DACL
	ACL	Num ACEs:	1	revision:	2
	---
	ACE
		type: ACCESS ALLOWED (0) flags: 0x00 
		Specific bits: 0x1ff
		Permissions: 0x1f01ff: SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS 
		SID: S-1-1-0
```

**Answer:** `InFreight SMB v3.1`

---

### 6. What is the full system path of that specific share? (format: "/directory/names")

Context:
```bash
rpcclient $> netsharegetinfo sambashare
netname: sambashare
	remark:	InFreight SMB v3.1
	path:	C:\home\sambauser\
	password:	
	type:	0x0
	perms:	0
	max_uses:	-1
	num_uses:	1
revision: 1
type: 0x8004: SEC_DESC_DACL_PRESENT SEC_DESC_SELF_RELATIVE 
DACL
	ACL	Num ACEs:	1	revision:	2
	---
	ACE
		type: ACCESS ALLOWED (0) flags: 0x00 
		Specific bits: 0x1ff
		Permissions: 0x1f01ff: SYNCHRONIZE_ACCESS WRITE_OWNER_ACCESS WRITE_DAC_ACCESS READ_CONTROL_ACCESS DELETE_ACCESS 
		SID: S-1-1-0
```

**Answer:** `/home/sambauser`

---

[Back to Module Index](./README.md)
