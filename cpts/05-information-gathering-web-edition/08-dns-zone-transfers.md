# Section 08: DNS Zone Transfers

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. After performing a zone transfer for the domain inlanefreight.htb on the target system, how many DNS records are retrieved from the target system's name server? Provide your answer as an integer, e.g, 123.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Downloads]
└─$ dig axfr inlanefreight.htb @10.129.137.47

; <<>> DiG 9.20.20-1-Debian <<>> axfr inlanefreight.htb @10.129.137.47
;; global options: +cmd
inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.
admin.inlanefreight.htb. 604800 IN      A       10.10.34.2
ftp.admin.inlanefreight.htb. 604800 IN  A       10.10.34.2
careers.inlanefreight.htb. 604800 IN    A       10.10.34.50
dc1.inlanefreight.htb.  604800  IN      A       10.10.34.16
dc2.inlanefreight.htb.  604800  IN      A       10.10.34.11
internal.inlanefreight.htb. 604800 IN   A       127.0.0.1
admin.internal.inlanefreight.htb. 604800 IN A   10.10.1.11
wsus.internal.inlanefreight.htb. 604800 IN A    10.10.1.240
ir.inlanefreight.htb.   604800  IN      A       10.10.45.5
dev.ir.inlanefreight.htb. 604800 IN     A       10.10.45.6
ns.inlanefreight.htb.   604800  IN      A       127.0.0.1
resources.inlanefreight.htb. 604800 IN  A       10.10.34.100
securemessaging.inlanefreight.htb. 604800 IN A  10.10.34.52
test1.inlanefreight.htb. 604800 IN      A       10.10.34.101
us.inlanefreight.htb.   604800  IN      A       10.10.200.5
cluster14.us.inlanefreight.htb. 604800 IN A     10.10.200.14
messagecenter.us.inlanefreight.htb. 604800 IN A 10.10.200.10
ww02.inlanefreight.htb. 604800  IN      A       10.10.34.112
www1.inlanefreight.htb. 604800  IN      A       10.10.34.111
inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 212 msec
;; SERVER: 10.129.137.47#53(10.129.137.47) (TCP)
;; WHEN: Sat Jul 25 18:55:25 +07 2026
;; XFR size: 22 records (messages 1, bytes 594)
```
**Answer:** `22`

---

### 2. Within the zone record transferred above, find the ip address for ftp.admin.inlanefreight.htb. Respond only with the IP address, eg 127.0.0.1

Context:
```bash
ftp.admin.inlanefreight.htb. 604800 IN  A       10.10.34.2
```
**Answer:** `10.10.34.2`

---

### 3. Within the same zone record, identify the largest IP address allocated within the 10.10.200 IP range. Respond with the full IP address, eg 10.10.200.1

Context:
```bash
cluster14.us.inlanefreight.htb. 604800 IN A     10.10.200.14
messagecenter.us.inlanefreight.htb. 604800 IN A 10.10.200.10
```
**Answer:** `10.10.200.14`

---

[Back to Module Index](./README.md)
