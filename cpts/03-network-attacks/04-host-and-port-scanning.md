# Section 04: Host and Port Scanning

Module: 03. Network Attacks

---

## Questions & Answers

### 1. Find all TCP ports on your target. Submit the total number of found TCP ports as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ nmap 10.129.2.49
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 06:23 EDT
Nmap scan report for 10.129.2.49
Host is up (0.16s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
110/tcp   open  pop3
139/tcp   open  netbios-ssn
143/tcp   open  imap
445/tcp   open  microsoft-ds
31337/tcp open  Elite

Nmap done: 1 IP address (1 host up) scanned in 13.78 seconds
```

**Answer:** `7`

---

### 2. Enumerate the hostname of your target and submit it as the answer. (case-sensitive)

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ nmap --script smb-os-discovery 10.129.2.49
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 06:27 EDT
Nmap scan report for 10.129.2.49
Host is up (0.16s latency).
Not shown: 993 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
110/tcp   open  pop3
139/tcp   open  netbios-ssn
143/tcp   open  imap
445/tcp   open  microsoft-ds
31337/tcp open  Elite

Host script results:
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: nix-nmap-default
|   NetBIOS computer name: NIX-NMAP-DEFAULT\x00
|   Domain name: \x00
|   FQDN: nix-nmap-default
|_  System time: 2026-07-23T12:27:38+02:00

Nmap done: 1 IP address (1 host up) scanned in 15.39 seconds
```

**Answer:** `nix-nmap-default`

---

[Back to Module Index](./README.md)
