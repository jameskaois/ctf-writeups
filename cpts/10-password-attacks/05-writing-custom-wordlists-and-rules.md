# Section 05: Writing Custom Wordlists and Rules

Module: 10. Password Attacks

---

## Questions & Answers

### 1. What is Mark's password?

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ vim osint.wordlist 
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ vim mark.rule     
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ hashcat --force osint.wordlist -r mark.rule --stdout | sort -u > mut_password.list
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ cat mut_password.list 
alex
Alex
alex1998!
Alex1998
Alex1998!
baseball
Baseball
baseball1998!
Baseball1998
Baseball1998!
Bell@
Bell@1998!
bella
Bella
bella1998!
Bella1998
Bella1998!
B@seb@ll
B@seb@ll1998!
maria
Maria
maria1998!
Maria1998
Maria1998!
mark
Mark
mark1998!
Mark1998
Mark1998!
markwhite
Markwhite
markwhite1998!
Markwhite1998
Markwhite1998!
M@ri@
M@ri@1998!
M@rk
M@rk1998!
M@rkwhite
M@rkwhite1998!
Nexur@
Nexur@1998!
nexura
Nexura
nexura1998!
Nexura1998
Nexura1998!
Sanfrancisc0
sanfrancisco
Sanfrancisco
sanfrancisco1998!
Sanfrancisco1998
Sanfrancisco1998!
S@nfr@ncisc01998!
S@nfr@ncisco
white
White
white1998!
White1998
White1998!
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ echo "97268a8ae45ac7d15c3cea4ce6ea550b" > hash.txt

                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ hashcat -m 0 hash.txt osint.wordlist -r mark.rule -o cracked.txt
hashcat (v7.1.2) starting

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #01: cpu--0x000, 1464/2929 MB (512 MB allocatable), 8MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 8

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory allocated for this attack: 514 MB (2664 MB free)

Dictionary cache hit:
* Filename..: osint.wordlist
* Passwords.: 9
* Bytes.....: 67
* Keyspace..: 72

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Hashcat is expecting at least 8192 base words but only got 0.1% of that.
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.           

                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 0 (MD5)
Hash.Target......: 97268a8ae45ac7d15c3cea4ce6ea550b
Time.Started.....: Tue Aug  4 08:17:41 2026 (0 secs)
Time.Estimated...: Tue Aug  4 08:17:41 2026 (0 secs)
Kernel.Feature...: Pure Kernel (password length 0-256 bytes)
Guess.Base.......: File (osint.wordlist)
Guess.Mod........: Rules (mark.rule)
Guess.Queue......: 1/1 (100.00%)
Speed.#01........:    51444 H/s (0.02ms) @ Accel:1024 Loops:8 Thr:1 Vec:4
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 72/72 (100.00%)
Rejected.........: 0/72 (0.00%)
Restore.Point....: 0/9 (0.00%)
Restore.Sub.#01..: Salt:0 Amplifier:0-8 Iteration:0-8
Candidate.Engine.: Device Generator
Candidates.#01...: mark -> sanfrancisco1998!

Started: Tue Aug  4 08:17:40 2026
Stopped: Tue Aug  4 08:17:43 2026
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ cat cracked.txt      
97268a8ae45ac7d15c3cea4ce6ea550b:Baseball1998!
```

**Answer:** `Baseball1998!`

---

[Back to Module Index](./README.md)
