# Metasploit: Introduction - TryHackMe

An introduction to the main components of the Metasploit Framework.

## Overview

- **Room URL:** [https://tryhackme.com/room/metasploitintro](https://tryhackme.com/room/metasploitintro)
- **Difficulty:** Easy
- **Time to complete:** 30

## Walkthrough

### 1. Introduction to Metasploit

_No hints needed!_

### 2. Main Components of Metasploit

- What is the name of the code taking advantage of a flaw on the target system?<br />

**=> Answer: `Exploit`**

- <p>What is the name of the code that runs on the target system to achieve the attacker's goal? <br /></p>

**=> Answer: `Payload`**

- What are self-contained payloads called?<br />

**=> Answer: `Singles`**

- <p>Is "<span style="color:rgb(14, 16, 26);background:transparent;margin-top:0pt;margin-bottom:0pt">windows/x64/pingback_reverse_tcp" among singles or staged payload? <br /></span></p>

**=> Answer: `Singles`**

### 3. Msfconsole

- How would you search for a module related to Apache?<br />

**=> Answer: `search apache`**

- <p>Who provided the auxiliary/scanner/ssh/ssh_login module?<br /></p>

```bash
msf6 > use auxiliary/scanner/ssh/ssh_login
msf6 auxiliary(scanner/ssh/ssh_login) > info
```

![Guide image](./screenshots/metasploit-introduction-1.png)

**=> Answer: `todb`**

### 4. Working with modules

- How would you set the LPORT value to 6666?<br />

**=> Answer: `set LPORT 6666`**

- How would you set the global value for RHOSTS  to 10.10.19.23 ? <br />

**=> Answer: `setg RHOSTS 10.10.19.23`**

- What command would you use to clear a set payload?<br />

**=> Answer: `unset PAYLOAD`**

- What command do you use to proceed with the exploitation phase?<br />

**=> Answer: `exploit`**

### 5. Summary

_No hints needed!_
