# DNS in Detail - TryHackMe 

Learn how DNS works and how it helps you access internet services.

## Overview
- **Room URL:** [https://tryhackme.com/room/dnsindetail](https://tryhackme.com/room/dnsindetail)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough
### 1. What is DNS?
- What does DNS stand for?<br />

**=> Answer: `Domain Name System`**

### 2. Domain Hierarchy
- What is the maximum length of a subdomain?<br />

**=> Answer: `63`**

- <p>Which of the following characters cannot be used in a subdomain ( 3 b _ - )?<br /></p>

**=> Answer: `_`**

- <p>What is the maximum length of a domain name?<br /></p>

**=> Answer: `253`**

- <p>What type of TLD is .co.uk?<br /></p>

**=> Answer: `ccTLD`**

### 3. Record Types
- What type of record would be used to advise where to send email?<br />

**=> Answer: `MX`**

- <p>What type of record handles IPv6 addresses?<br /></p>

**=> Answer: `AAAA`**

### 4. Making A Request
- What field specifies how long a DNS record should be cached for?<br />

**=> Answer: `TTL`**

- <p>What type of DNS Server is usually provided by your ISP?<br /></p>

**=> Answer: `recursive`**

- <p>What type of server holds all the records for a domain?<br /></p>

**=> Answer: `authoritative`**

### 5. Practical
- <p>What is the CNAME of shop.website.thm?<br /></p>
```bash
nslookup --type=CNAME shop.website.thm

Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
shop.website.thm canonical name = shops.myshopify.com
```
**=> Answer: `shops.myshopify.com`**

- <p>What is the value of the TXT record of website.thm?<br /></p>
```bash
nslookup --type=TXT website.thm

Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
website.thm text = "THM{7012BBA60997F35A9516C2E16D2944FF}"
```
**=> Answer: `THM{7012BBA60997F35A9516C2E16D2944FF}`**

- What is the numerical priority value for the MX record?
```bash
nslookup --type=MX website.thm

Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
website.thm mail exchanger = 30 alt4.aspmx.l.google.com
```
**=> Answer: `30`**

- <p>What is the IP address for the A record of www.website.thm?<br /></p>
```bash
nslookup --type=A www.website.thm

Server: 127.0.0.53
Address: 127.0.0.53#53

Non-authoritative answer:
Name: www.website.thm
Address: 10.10.10.10
```
**=> Answer: `10.10.10.10`**

