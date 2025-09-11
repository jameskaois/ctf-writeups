# Vulnversity - TryHackMe

Learn about active recon, web app attacks and privilege escalation.

## Overview

- **Room URL:** [https://tryhackme.com/room/vulnversity](https://tryhackme.com/room/vulnversity)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough

### 1. Deploy the machine

_No hints needed!_

### 2. Reconnaissance

- <p>Scan the box; how many ports are open?</p>

```bash
nmap -p- <MACHINE_IP>
```

**=> Answer: `6`**

- <p>What version of the squid proxy is running on the machine?</p>

```bash
nmap -p- -A <MACHINE_IP>
```

**=> Answer: `4.10`**

- <p>How many ports will Nmap scan if the flag <b>-p-400 </b>was used?</p>

**=> Answer: `400`**

- <p>What is the most likely operating system this machine is running?</p>

```bash
nmap -O <MACHINE_IP>
```

- Run web app, Windows, Unix, Linux => Ubuntu
  **=> Answer: `Ubuntu`**

- <p>What port is the web server running on?</p>

```bash
nmap -p- -A <MACHINE_IP>
```

**=> Answer: `3333`**

- <p>What is the flag for enabling verbose mode using Nmap?<br /></p>

**=> Answer: `-v`**

### 3. Locating directories using Gobuster

- <p>What is the directory that has an upload form page?</p>

```bash
gobuster dir -u http://<MACHINE_IP>:3333 -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt
```

**=> Answer: `/internal/`**

### 4. Compromise the Webserver

- What common file type you'd want to upload to exploit the server is blocked? Try a couple to find out.

**=> Answer: `.php`**

- <p>What extension is allowed after running the above exercise?</p>

**=> Answer: `.phtml`**

- <p>What is the name of the user who manages the webserver?</p>

**=> Answer: `bill`**

- <p>What is the user flag?</p>

**=> Answer: `8bd7992fbe8a6ad22a63361004cfcedb`**

### 5. Privilege Escalation

- <p><span style="font-size:1.6rem">On the system, search for all SUID files. Which file stands out?</span><br /></p>

**=> Answer: `/bin/systemctl`**

- <p>What is the root flag value?</p>

**=> Answer: `a58ff8579f0a9270368d33a9966c7fd5`**
