# Section 13: Attacking DNS

Module: 11. Attacking Common Services

---

## Questions & Answers

### 1. Find all available DNS records for the "inlanefreight.htb" domain on the target name server and submit the flag found as a DNS record as the answer.

Context:
```bash
┌──(kali㉿kali)-[~/Desktop/Tools/subbrute]
└─$ python3 subbrute.py inlanefreight.htb -s names.txt -r resolvers.txt 
/home/kali/Desktop/Tools/subbrute/subbrute.py:462: SyntaxWarning: invalid escape sequence '\.'
  permute_filter = re.compile("^[a-zA-Z0-9]{" + str(self.permute_len) + "}\.")
Warning: Fewer than 16 resolvers per process, consider adding more nameservers to resolvers.txt.
inlanefreight.htb
hr.inlanefreight.htb
┌──(kali㉿kali)-[~/Desktop/Tools/subbrute]
└─$ dig AXFR @inlanefreight.htb hr.inlanefreight.htb

; <<>> DiG 9.20.4-4-Debian <<>> AXFR @inlanefreight.htb hr.inlanefreight.htb
; (1 server found)
;; global options: +cmd
hr.inlanefreight.htb.   604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
hr.inlanefreight.htb.   604800  IN      TXT     "HTB{LUIHNFAS2871SJK1259991}"
hr.inlanefreight.htb.   604800  IN      NS      ns.inlanefreight.htb.
ns.hr.inlanefreight.htb. 604800 IN      A       127.0.0.1
hr.inlanefreight.htb.   604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 28 msec
;; SERVER: 10.129.203.6#53(inlanefreight.htb) (TCP)
;; WHEN: Thu Mar 20 17:38:39 UTC 2025
;; XFR size: 5 records (messages 1, bytes 230)
```

**Answer:** `HTB{LUIHNFAS2871SJK1259991}`

---


[Back to Module Index](./README.md)
