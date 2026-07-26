# Section 05: Digging DNS

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. Which IP address maps to inlanefreight.com?

Context:
```bash
┌──(jameskaois㉿kali)-[~/Downloads]
└─$ dig  inlanefreight.com               
;; communications error to 98.192.249.101#53: timed out
^C                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Downloads]
└─$ dig inlanefreight.com  
^[[1;5C;; communications error to 98.192.249.101#53: timed out
;; communications error to 98.192.249.101#53: timed out
;; communications error to 98.192.249.101#53: timed out

; <<>> DiG 9.20.20-1-Debian <<>> inlanefreight.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 64400
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;inlanefreight.com.             IN      A

;; ANSWER SECTION:
inlanefreight.com.      300     IN      A       134.209.24.248

;; Query time: 108 msec
;; SERVER: 116.97.90.124#53(116.97.90.124) (UDP)
;; WHEN: Sat Jul 25 10:47:10 +07 2026
;; MSG SIZE  rcvd: 62
```
**Answer:** `134.209.24.248`

---

### 2. Which domain is returned when querying the PTR record for 134.209.24.248?

Context:
```bash
┌──(jameskaois㉿kali)-[~/Downloads]
└─$ nslookup 134.209.24.248
;; communications error to 98.192.249.101#53: timed out
^[[1;5C;; communications error to 98.192.249.101#53: timed out
;; communications error to 98.192.249.101#53: timed out
248.24.209.134.in-addr.arpa     name = inlanefreight.com.

Authoritative answers can be found from:
```

**Answer:** `inlanefreight.com`

---

### 3. What is the full domain returned when you query the mail records for facebook.com?

Context:
```bash
┌──(jameskaois㉿kali)-[~/Downloads]
└─$ dig facebook.com MX
;; communications error to 98.192.249.101#53: timed out
;; communications error to 98.192.249.101#53: timed out
;; communications error to 98.192.249.101#53: timed out

; <<>> DiG 9.20.20-1-Debian <<>> facebook.com MX
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6177
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;facebook.com.                  IN      MX

;; ANSWER SECTION:
facebook.com.           3600    IN      MX      10 smtpin.vvv.facebook.com.

;; Query time: 40 msec
;; SERVER: 116.97.90.124#53(116.97.90.124) (UDP)
;; WHEN: Sat Jul 25 10:56:47 +07 2026
;; MSG SIZE  rcvd: 68
```

**Answer:** `smtpin.vvv.facebook.com`

---

[Back to Module Index](./README.md)
