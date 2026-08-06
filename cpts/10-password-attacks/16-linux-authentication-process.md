# Section 16: Linux Authentication Process

Module: 10. Password Attacks

---

## Questions & Answers

### 1. Download the attached ZIP file (linux-authentication-process.zip), and use single crack mode to find martin's password. What is it?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ grep -E '^(martin|sarah):' shadow > hashes.txt
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ cat hashes.txt 
martin:$6$0XiU8Oe/pGpxWvdq$n6TgiYUVAXBUOO11C155Ea8nNpSVtFFVQveY6yExlOdPu99hY4V9Chi1KEy/lAluVFuVcvi8QCO1mCG6ra70A1:20015:0:99999:7:::
sarah:$6$EBOM5vJAV1TPvrdP$LqsLyYkoGzAGt4ihyvfhvBrrGpVjV976B3dEubi9i95P5cDx1U6BrE9G020PWuaeI6JSNaIDIbn43uskRDG0U/:20017:0:99999:7:::
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
mariposa         (sarah)     
Martin1          (martin)     
2g 0:00:00:22 DONE (2026-08-04 22:01) 0.08837g/s 6742p/s 6764c/s 6764C/s Muhammad..850112
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

**Answer:** `Martin1`

---

### 2. Use a wordlist attack to find sarah's password. What is it?

Context:


**Answer:** `mariposa`

---

[Back to Module Index](./README.md)
