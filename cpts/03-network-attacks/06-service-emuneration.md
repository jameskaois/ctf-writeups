# Section 06: Service Emuneration

Module: 03. Network Attacks

---

## Questions & Answers

### 1. Enumerate all ports and their services. One of the services contains the flag you have to submit as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ sudo nmap -p- -sV 10.129.2.49
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 06:43 EDT
Nmap scan report for 10.129.2.49
Host is up (0.16s latency).
Not shown: 65528 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http        Apache httpd 2.4.29 ((Ubuntu))
110/tcp   open  pop3        Dovecot pop3d
139/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp   open  imap        Dovecot imapd (Ubuntu)
445/tcp   open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
31337/tcp open  Elite?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31337-TCP:V=7.95%I=7%D=7/23%Time=6A61F126%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,1F,"220\x20HTB{pr0F7pDv3r510nb4nn3r}\r\n");
Service Info: Host: NIX-NMAP-DEFAULT; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 358.75 seconds
```

**Answer:** `HTB{pr0F7pDv3r510nb4nn3r}`

---

[Back to Module Index](./README.md)
