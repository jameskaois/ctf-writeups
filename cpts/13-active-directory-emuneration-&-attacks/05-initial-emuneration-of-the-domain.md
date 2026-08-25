# Section 05: Initial Emuneration of the Domain

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. From your scans, what is the "commonName" of host 172.16.5.5 ?

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $sudo nmap -A 172.16.5.5 
Starting Nmap 7.92 ( https://nmap.org ) at 2026-08-18 00:59 EDT
Stats: 0:00:08 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 8.33% done; ETC: 01:00 (0:01:06 remaining)
Nmap scan report for inlanefreight.local (172.16.5.5)
Host is up (0.0020s latency).
Not shown: 988 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-08-18 04:59:21Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT
| Not valid before: 2026-07-22T08:52:23
|_Not valid after:  2027-07-22T08:52:23
|_ssl-date: 2026-08-18T05:00:20+00:00; 0s from scanner time.
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT
| Not valid before: 2026-07-22T08:52:23
|_Not valid after:  2027-07-22T08:52:23
|_ssl-date: 2026-08-18T05:00:20+00:00; 0s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT
| Not valid before: 2026-07-22T08:52:23
|_Not valid after:  2027-07-22T08:52:23
|_ssl-date: 2026-08-18T05:00:20+00:00; 0s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT.LOCAL, DNS:INLANEFREIGHT
| Not valid before: 2026-07-22T08:52:23
|_Not valid after:  2027-07-22T08:52:23
|_ssl-date: 2026-08-18T05:00:20+00:00; 0s from scanner time.
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-08-18T05:00:20+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: ACADEMY-EA-DC01
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-18T05:00:12+00:00
| ssl-cert: Subject: commonName=ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL
| Not valid before: 2026-07-21T08:46:17
|_Not valid after:  2027-01-20T08:46:17
MAC Address: 00:50:56:8A:C3:D1 (VMware)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=8/18%OT=53%CT=1%CU=36150%PV=Y%DS=1%DC=D%G=Y%M=005056%T
OS:M=6A83E6E4%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=2%ISR=10D%TI=I%CI=I%II=I
OS:%SS=S%TS=U)OPS(O1=M5B4NW8NNS%O2=M5B4NW8NNS%O3=M5B4NW8%O4=M5B4NW8NNS%O5=M
OS:5B4NW8NNS%O6=M5B4NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70
OS:)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M5B4NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+
OS:%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
OS:T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A
OS:=O%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPC
OS:K=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
Service Info: Host: ACADEMY-EA-DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_nbstat: NetBIOS name: ACADEMY-EA-DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:8a:c3:d1 (VMware)
| smb2-time: 
|   date: 2026-08-18T05:00:12
|_  start_date: N/A

TRACEROUTE
HOP RTT     ADDRESS
1   1.99 ms inlanefreight.local (172.16.5.5)
```

**Answer:** `ACADEMY-EA-DC01.INLANEFREIGHT.LOCAL`

---

### 2. What host is running "Microsoft SQL Server 2019 15.00.2000.00"? (IP address, not Resolved name)

Context:
```bash
┌─[htb-student@ea-attack01]─[~]
└──╼ $fping -asgq 172.16.5.0/23
172.16.5.5
172.16.5.130
172.16.5.225

     510 targets
       3 alive
     507 unreachable
       0 unknown addresses

    2028 timeouts (waiting for response)
    2031 ICMP Echos sent
       3 ICMP Echo Replies received
    2028 other ICMP received

 0.061 ms (min round trip time)
 0.301 ms (avg round trip time)
 0.458 ms (max round trip time)
       15.264 sec (elapsed real time)

┌─[✗]─[htb-student@ea-attack01]─[~]
└──╼ $ifconfig
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
        ether 02:42:b0:d0:e0:1d  txqueuelen 0  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens192: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.129.162.3  netmask 255.255.0.0  broadcast 10.129.255.255
        inet6 fe80::ba2f:62a3:e5d7:f3e7  prefixlen 64  scopeid 0x20<link>
        inet6 dead:beef::3983:5781:1e09:a84f  prefixlen 64  scopeid 0x0<global>
        ether 00:50:56:8a:6e:fd  txqueuelen 1000  (Ethernet)
        RX packets 3044  bytes 295953 (289.0 KiB)
        RX errors 0  dropped 77  overruns 0  frame 0
        TX packets 598  bytes 74618 (72.8 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ens224: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.16.5.225  netmask 255.255.254.0  broadcast 172.16.5.255
        inet6 fe80::32e6:baa0:e3aa:25da  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:8a:0d:dc  txqueuelen 1000  (Ethernet)
        RX packets 11650  bytes 1047292 (1022.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3508  bytes 202206 (197.4 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 2046  bytes 228272 (222.9 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 2046  bytes 228272 (222.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

┌─[htb-student@ea-attack01]─[~]
└──╼ $sudo nmap -A 172.16.5.130
Starting Nmap 7.92 ( https://nmap.org ) at 2026-08-18 01:02 EDT
Stats: 0:00:43 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:01:34 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 99.91% done; ETC: 01:04 (0:00:00 remaining)
Nmap scan report for 172.16.5.130
Host is up (0.0022s latency).
Not shown: 992 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds?
808/tcp   open  ccproxy-http?
1433/tcp  open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ssl-date: 2026-08-18T05:04:32+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2026-08-18T04:40:07
|_Not valid after:  2056-08-18T04:40:07
| ms-sql-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: ACADEMY-EA-FILE
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: ACADEMY-EA-FILE.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|_  Product_Version: 10.0.17763
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: ACADEMY-EA-FILE
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: ACADEMY-EA-FILE.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-18T05:03:28+00:00
|_ssl-date: 2026-08-18T05:04:32+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=ACADEMY-EA-FILE.INLANEFREIGHT.LOCAL
| Not valid before: 2026-07-21T08:47:09
|_Not valid after:  2027-01-20T08:47:09
16001/tcp open  mc-nmf        .NET Message Framing
MAC Address: 00:50:56:8A:2A:A7 (VMware)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=8/18%OT=80%CT=1%CU=37455%PV=Y%DS=1%DC=D%G=Y%M=005056%T
OS:M=6A83E7E7%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=1%ISR=109%TI=I%CI=I%II=I
OS:%SS=S%TS=U)OPS(O1=M5B4NW8NNS%O2=M5B4NW8NNS%O3=M5B4NW8%O4=M5B4NW8NNS%O5=M
OS:5B4NW8NNS%O6=M5B4NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70
OS:)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M5B4NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+
OS:%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
OS:T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A
OS:=O%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPC
OS:K=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: ACADEMY-EA-FILE, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:8a:2a:a7 (VMware)
| smb2-time: 
|   date: 2026-08-18T05:03:28
|_  start_date: N/A
| ms-sql-info: 
|   172.16.5.130:1433: 
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433

TRACEROUTE
HOP RTT     ADDRESS
1   2.16 ms 172.16.5.130

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 115.26 seconds

```

**Answer:** `172.16.5.130`

---

[Back to Module Index](./README.md)
