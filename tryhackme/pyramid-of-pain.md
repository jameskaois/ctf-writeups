# Pyramid Of Pain  - TryHackMe 

Learn what is the Pyramid of Pain and how to utilize this model to determine the level of difficulty it will cause for an adversary to change the indicators associated with them, and their campaign. 

## Overview
- **Room URL:** [https://tryhackme.com/room/pyramidofpainax](https://tryhackme.com/room/pyramidofpainax)
- **Difficulty:** Easy
- **Time to complete:** 30

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. Hash Values (Trivial)
- Analyse the report associated with the hash "b8ef959a9176aef07fdca8705254a163b50b49a17217a4ff0107487f59d4a35d" <a href="https://assets.tryhackme.com/additional/pyramidofpain/t3-virustotal.pdf" target="_blank">here.</a> What is the filename of the sample?

**=> Answer: `Sales_Receipt 5606.xls`**

### 3. IP Address (Easy)
- Read the following<a href="https://assets.tryhackme.com/additional/pyramidofpain/task3-anyrun.pdf" target="_blank"> report</a> to answer this question. What is the <b>first IP address</b> the malicious process (<b>PID 1632</b>) attempts to communicate with? 

![Guide Image](./screenshots/pyramid-of-pain-1.png)

**=> Answer: `50.87.136.52`**

- Read the following<a href="https://assets.tryhackme.com/additional/pyramidofpain/task3-anyrun.pdf" target="_blank"> report</a> to answer this question. What is the <b>first domain name</b> the malicious process ((<span style="font-weight:bolder">PID 1632</span>) attempts to communicate with?

![Guide Image](./screenshots/pyramid-of-pain-1.png)

**=> Answer: `craftingalegacy.com`**

### 4. Domain Names (Simple)
- Go to <a href="https://app.any.run/tasks/a66178de-7596-4a05-945d-704dbf6b3b90" target="_blank">this report on app.any.run</a> and provide the first <b>suspicious</b> domain request you are seeing, you will be using this report to answer the remaining questions of this task.

**=> Answer: `craftingalegacy.com`**

- <p>What term refers to an address used to access websites?</p>

**=> Answer: `Domain Name`**

- <p>What type of attack uses Unicode characters in the domain name to imitate the a known domain?</p>

**=> Answer: `Punycode attack`**

- Provide the redirected website for the shortened URL using a preview: https://tinyurl.com/bw7t8p4u

**=> Answer: `https://tryhackme.com/`**

### 5. Host Artifacts (Annoying)
- A process named <b>regidle.exe</b> makes a POST request to an IP address based in the United States (US) on <b>port 8080</b>. What is the IP address?

![Guide Image](./screenshots/pyramid-of-pain-2.png)

**=> Answer: `96.126.101.6`**

- <p>The actor drops a malicious executable (EXE). What is the name of this executable?</p>

![Guide Image](./screenshots/pyramid-of-pain-3.png)

**=> Answer: `G_jugk.exe`**

- <p>Look at this <a href="https://assets.tryhackme.com/additional/pyramidofpain/vtotal2.png" target="_blank">report</a> by Virustotal. How many vendors determine this host to be malicious?</p>

**=> Answer: `9`**

### 6. Network Artifacts (Annoying)
- What browser uses the User-Agent string shown in the screenshot above?

**=> Answer: `Internet Explorer`**

- <p>How many POST requests are in the screenshot from the pcap file?</p>

**=> Answer: `6`**

### 7. Tools (Challenging)
- Provide the method used to determine similarity between the files 

**=> Answer: `Fuzzy Hashing`**

- <p>Provide the alternative name for fuzzy hashes without the abbreviation </p>

**=> Answer: `context triggered piecewise hashes `**

### 8. TTPs (Tough)
- Navigate to ATT&amp;CK Matrix webpage. How many techniques fall under the Exfiltration category?

**=> Answer: `9`**

- <p>Chimera is a China-based hacking group that has been active since 2018. What is the name of the commercial, remote access tool they use for C2 beacons and data exfiltration?</p>
- Visit [https://attack.mitre.org/groups/G0114/](https://attack.mitre.org/groups/G0114/)

**=> Answer: `Cobalt Strike`**

### 9. Practical: The Pyramid of Pain
- Complete the static site. What is the flag?

**=> Answer: `THM{PYRAMIDS_COMPLETE}`**

### 10. Conclusion 
*No hints needed!*