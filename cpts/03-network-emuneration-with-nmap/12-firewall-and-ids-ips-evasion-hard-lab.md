# Section 12: Firewall and IDS/IPS Evasion - Hard Lab

Module: 03. Network Emuneration with Nmap

---

## Questions & Answers

### 1. Now our client wants to know if it is possible to find out the version of the running services. Identify the version of service our client was talking about and submit the flag as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-t1ir3k1k57]─[~]
└──╼ [★]$ sudo ncat -nv -s 10.10.14.112 --source-port 53 10.129.133.1 50000
Ncat: Version 7.95 ( https://nmap.org/ncat )
Ncat: Connected to 10.129.133.1:50000.
220 HTB{kjnsdf2n982n1827eh76238s98di1w6}

# 10.10.14.112 is our machine IP
# 10.129.133.1 is target machine IP
```

**Answer:** `HTB{kjnsdf2n982n1827eh76238s98di1w6}`

---

[Back to Module Index](./README.md)
