# Section 03: Introduction to John The Ripper

Module: 10. Password Attacks

---

## Questions & Answers

### 1. Use single-crack mode to crack r0lf's password.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ john --single passwd                                                        
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 ASIMD 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
NAITSABES        (r0lf)     
1g 0:00:00:00 DONE (2026-08-04 07:43) 4.761g/s 2057p/s 2057c/s 2057C/s NAITSABESFL0R..rSebastiannaitsabeSr
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

**Answer:** `NAITSABES`

---

### 2. Use wordlist-mode with rockyou.txt to crack the RIPEMD-128 password.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ echo "193069ceb0461e1d40d216e32c79c704" > hash.txt                                
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents]
└─$ john --format=ripemd-128 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

Using default input encoding: UTF-8
Loaded 1 password hash (ripemd-128, RIPEMD 128 [32/64])
Warning: no OpenMP support for this hash type, consider --fork=8
Press 'q' or Ctrl-C to abort, almost any other key for status
50cent           (?)     
1g 0:00:00:00 DONE (2026-08-04 07:49) 50.00g/s 25600p/s 25600c/s 25600C/s angelo..letmein
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

**Answer:** `50cent`

---

[Back to Module Index](./README.md)
