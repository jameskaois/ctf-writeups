# Section 09: DNS

Module: 04. Footprinting

---

## Questions & Answers

### 1. Interact with the target DNS using its IP address and enumerate the FQDN of it for the "inlanefreight.htb" domain.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ dig ns inlanefreight.htb @10.129.134.70

; <<>> DiG 9.20.18-1~deb13u1-Debian <<>> ns inlanefreight.htb @10.129.134.70
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43825
;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 2
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: c255644deaf88308010000006a62bbe1a666d11118cbef6d (good)
;; QUESTION SECTION:
;inlanefreight.htb.		IN	NS

;; ANSWER SECTION:
inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.

;; ADDITIONAL SECTION:
ns.inlanefreight.htb.	604800	IN	A	127.0.0.1

;; Query time: 153 msec
;; SERVER: 10.129.134.70#53(10.129.134.70) (UDP)
;; WHEN: Thu Jul 23 21:12:02 EDT 2026
;; MSG SIZE  rcvd: 107
```

**Answer:** `ns.inlanefreight.htb`

---

### 2. Identify if its possible to perform a zone transfer and submit the TXT record as the answer. (Format: HTB{...})

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ dig axfr internal.inlanefreight.htb @10.129.134.70

; <<>> DiG 9.20.18-1~deb13u1-Debian <<>> axfr internal.inlanefreight.htb @10.129.134.70
;; global options: +cmd
internal.inlanefreight.htb. 604800 IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
internal.inlanefreight.htb. 604800 IN	TXT	"MS=ms97310371"
internal.inlanefreight.htb. 604800 IN	TXT	"HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}"
internal.inlanefreight.htb. 604800 IN	TXT	"atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
internal.inlanefreight.htb. 604800 IN	TXT	"v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
internal.inlanefreight.htb. 604800 IN	NS	ns.inlanefreight.htb.
dc1.internal.inlanefreight.htb.	604800 IN A	10.129.34.16
dc2.internal.inlanefreight.htb.	604800 IN A	10.129.34.11
mail1.internal.inlanefreight.htb. 604800 IN A	10.129.18.200
ns.internal.inlanefreight.htb. 604800 IN A	127.0.0.1
vpn.internal.inlanefreight.htb.	604800 IN A	10.129.1.6
ws1.internal.inlanefreight.htb.	604800 IN A	10.129.1.34
ws2.internal.inlanefreight.htb.	604800 IN A	10.129.1.35
wsus.internal.inlanefreight.htb. 604800	IN A	10.129.18.2
internal.inlanefreight.htb. 604800 IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 156 msec
;; SERVER: 10.129.134.70#53(10.129.134.70) (TCP)
;; WHEN: Thu Jul 23 21:14:48 EDT 2026
;; XFR size: 15 records (messages 1, bytes 677)
```

**Answer:** `HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}`

---

### 3. What is the IPv4 address of the hostname DC1?

Context:
```bash
dc1.internal.inlanefreight.htb.	604800 IN A	10.129.34.16
```

**Answer:** `10.129.34.16`

---

### 4. What is the FQDN of the host where the last octet ends with "x.x.x.203"?

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ dnsenum --dnsserver 10.129.134.70 --enum -p 0 -s 0 -^Csubdomains.txt -f /usr/share/wordlists/seclists/Discovery/DNS/fierce-hostlist.txt dev.inlanefreight.htb
dnsenum VERSION:1.3.1
Unknown option: ^csubdomains.txt

-----   dev.inlanefreight.htb   -----


Host's addresses:
__________________



Name Servers:
______________

ns.inlanefreight.htb.                    604800   IN    A         127.0.0.1


Mail (MX) Servers:
___________________



Trying Zone Transfers and getting Bind Versions:
_________________________________________________

unresolvable name: ns.inlanefreight.htb at /usr/bin/dnsenum line 892 thread 2.

Trying Zone Transfer for dev.inlanefreight.htb on ns.inlanefreight.htb ... 
AXFR record query failed: no nameservers


Brute forcing with /usr/share/wordlists/seclists/Discovery/DNS/fierce-hostlist.txt:
____________________________________________________________________________________

dev1.dev.inlanefreight.htb.              604800   IN    A         10.12.3.6
ns.dev.inlanefreight.htb.                604800   IN    A         127.0.0.1
win2k.dev.inlanefreight.htb.             604800   IN    A        10.12.3.203


Launching Whois Queries:
_________________________



dev.inlanefreight.htb_____________________



Performing reverse lookup on 0 ip addresses:
_____________________________________________


0 results out of 0 IP addresses.


dev.inlanefreight.htb ip blocks:
_________________________________
```

**Answer:** `win2k.dev.inlanefreight.htb`

---

[Back to Module Index](./README.md)
