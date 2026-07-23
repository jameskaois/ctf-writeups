# Section 05: Saving the Results

Module: 03. Network Attacks

---

## Questions & Answers

### 1. Perform a full TCP port scan on your target and create an HTML report. Submit the number of the highest port as the answer.

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

**Answer:** `31337`

---

[Back to Module Index](./README.md)
