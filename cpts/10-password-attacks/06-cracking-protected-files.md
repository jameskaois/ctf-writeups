# Section 06: Cracking Protected Files

Module: 10. Password Attacks

---

## Questions & Answers

### 1. Download the attached ZIP archive (cracking-protected-files.zip), and crack the file within. What is the password?

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ office2john Confidential.xlsx > hash.txt      
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ cat hash.txt 
Confidential.xlsx:$office$*2013*100000*256*16*cb0e251cdec92e97eeb38e595cd4eb09*58758c88f3bb25e43e1e21adbd4b6e50*0057c1ae71b0023424ba705607dc0df1d9a786974bb957a821cfd7e39129eb15
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Office, 2007/2010/2013 [SHA1 128/128 ASIMD 4x / SHA512 128/128 ASIMD 2x AES])
Cost 1 (MS Office version) is 2013 for all loaded hashes
Cost 2 (iteration count) is 100000 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
beethoven        (Confidential.xlsx)     
1g 0:00:00:58 DONE (2026-08-04 08:27) 0.01705g/s 114.0p/s 114.0c/s 114.0C/s 98765432..beethoven
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

**Answer:** `beethoven`

---

[Back to Module Index](./README.md)
