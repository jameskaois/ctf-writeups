# Section 07: Nmap Scripting Engine

Module: 03. Network Emuneration with Nmap

---

## Questions & Answers

### 1. Use NSE and its scripts to find the flag that one of the services contain and submit it as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ nmap -p 80 --script http-enum,http-title,http-headers 10.129.2.49
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 06:38 EDT
Nmap scan report for 10.129.2.49
Host is up (0.16s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-headers: 
|   Date: Thu, 23 Jul 2026 10:38:06 GMT
|   Server: Apache/2.4.29 (Ubuntu)
|   Last-Modified: Thu, 10 Sep 2020 02:14:12 GMT
|   ETag: "2c39-5aeec1fc9d59d"
|   Accept-Ranges: bytes
|   Content-Length: 11321
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-enum: 
|_  /robots.txt: Robots file

Nmap done: 1 IP address (1 host up) scanned in 22.51 seconds
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://10.129.2.49/robots.txt
User-agent: *

Allow: /

HTB{873nniuc71bu6usbs1i96as6dsv26}
```

**Answer:** `HTB{873nniuc71bu6usbs1i96as6dsv26}`

---

[Back to Module Index](./README.md)
