# Section 11: Firewall and IDS/IPS Evasion - Medium Lab

Module: 03. Network Emuneration with Nmap

---

## Questions & Answers

### 1. After the configurations are transferred to the system, our client wants to know if it is possible to find out our target's DNS server version. Submit the DNS server version of the target as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-t1ir3k1k57]─[~]
└──╼ [★]$ sudo nmap 10.129.132.252 -Pn -sV -p 53 -n --disable-arp-ping --source-port 53 -sS -sU --script banner
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 08:39 EDT
Nmap scan report for 10.129.132.252
Host is up (0.16s latency).

PORT   STATE    SERVICE VERSION
53/tcp filtered domain
53/udp open     domain  (unknown banner: HTB{GoTtgUnyze9Psw4vGjcuMpHRp})
| fingerprint-strings: 
|   DNS-SD: 
|     _services
|     _dns-sd
|     _udp
|     local
|     ROOT-SERVERS
|   DNSVersionBindReq: 
|     version
|     bind
|     HTB{GoTtgUnyze9Psw4vGjcuMpHRp}
|   NBTStat: 
|     CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
|_    ROOT-SERVERS
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-UDP:V=7.95%I=7%D=7/23%Time=6A620B9D%P=x86_64-pc-linux-gnu%r(DNSV
SF:ersionBindReq,57,"\0\x06\x85\0\0\x01\0\x01\0\x01\0\0\x07version\x04bind
SF:\0\0\x10\0\x03\xc0\x0c\0\x10\0\x03\0\0\0\0\0\x1f\x1eHTB{GoTtgUnyze9Psw4
SF:vGjcuMpHRp}\xc0\x0c\0\x02\0\x03\0\0\0\0\0\x02\xc0\x0c")%r(DNSStatusRequ
SF:est,C,"\0\0\x90\x04\0\0\0\0\0\0\0\0")%r(DNS-SD,101,"\0\0\x80\x80\0\x01\
SF:0\0\0\r\0\0\t_services\x07_dns-sd\x04_udp\x05local\0\0\x0c\0\x01\0\0\x0
SF:2\0\x01\x006\xee\x80\0\x14\x01C\x0cROOT-SERVERS\x03NET\0\0\0\x02\0\x01\
SF:x006\xee\x80\0\x04\x01E\xc0;\0\0\x02\0\x01\x006\xee\x80\0\x04\x01I\xc0;
SF:\0\0\x02\0\x01\x006\xee\x80\0\x04\x01G\xc0;\0\0\x02\0\x01\x006\xee\x80\
SF:0\x04\x01H\xc0;\0\0\x02\0\x01\x006\xee\x80\0\x04\x01L\xc0;\0\0\x02\0\x0
SF:1\x006\xee\x80\0\x04\x01A\xc0;\0\0\x02\0\x01\x006\xee\x80\0\x04\x01B\xc
SF:0;\0\0\x02\0\x01\x006\xee\x80\0\x04\x01J\xc0;\0\0\x02\0\x01\x006\xee\x8
SF:0\0\x04\x01F\xc0;\0\0\x02\0\x01\x006\xee\x80\0\x04\x01K\xc0;\0\0\x02\0\
SF:x01\x006\xee\x80\0\x04\x01D\xc0;\0\0\x02\0\x01\x006\xee\x80\0\x04\x01M\
SF:xc0;")%r(RPCCheck,C,"r\xfe\x98\x01\0\0\0\0\0\0\0\0")%r(NBTStat,105,"\x8
SF:0\xf0\x80\x90\0\x01\0\0\0\r\0\0\x20CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\0\0
SF:!\0\x01\0\0\x02\0\x01\x006\xee\x80\0\x14\x01F\x0cROOT-SERVERS\x03NET\0\
SF:0\0\x02\0\x01\x006\xee\x80\0\x04\x01D\xc0\?\0\0\x02\0\x01\x006\xee\x80\
SF:0\x04\x01C\xc0\?\0\0\x02\0\x01\x006\xee\x80\0\x04\x01M\xc0\?\0\0\x02\0\
SF:x01\x006\xee\x80\0\x04\x01E\xc0\?\0\0\x02\0\x01\x006\xee\x80\0\x04\x01I
SF:\xc0\?\0\0\x02\0\x01\x006\xee\x80\0\x04\x01H\xc0\?\0\0\x02\0\x01\x006\x
SF:ee\x80\0\x04\x01A\xc0\?\0\0\x02\0\x01\x006\xee\x80\0\x04\x01L\xc0\?\0\0
SF:\x02\0\x01\x006\xee\x80\0\x04\x01B\xc0\?\0\0\x02\0\x01\x006\xee\x80\0\x
SF:04\x01J\xc0\?\0\0\x02\0\x01\x006\xee\x80\0\x04\x01K\xc0\?\0\0\x02\0\x01
SF:\x006\xee\x80\0\x04\x01G\xc0\?");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.48 seconds
```

**Answer:** `HTB{GoTtgUnyze9Psw4vGjcuMpHRp}`

---

[Back to Module Index](./README.md)
