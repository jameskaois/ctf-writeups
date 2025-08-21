# Introductory Researching - TryHackMe 

A brief introduction to research skills for pentesting.

## Overview
- **Room URL:** [https://tryhackme.com/room/introtoresearch](https://tryhackme.com/room/introtoresearch)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. Example Research Question
- <p>In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)?</p>

**=> Answer: `Repeater`**

- <p>What hash format are modern Windows login passwords stored in?<br /></p>

**=> Answer: `NTLM`**

- <p>What are automated tasks called in Linux?</p>

**=> Answer: `Cron Jobs`**

- <p>What number base could you use as a shorthand for base 2 (binary)?</p>

**=> Answer: `Base 16`**

- <p>If a password hash starts with $6$, what format is it (Unix variant)?</p>

**=> Answer: `sha512crypt`**

### 3. Vulnerability Searching
- <p>What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?</p>

**=> Answer: `CVE-2020-10385`**

- <p>There was a Local Privilege Escalation vulnerability found in the <i>Debian</i> version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability?</p>

**=> Answer: `CVE-2016-1240`**

- <p>What is the very first CVE found in the VLC media player?</p>

**=> Answer: `CVE-2007-0017`**

- <p>If you wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would you use?</p>

**=> Answer: `CVE-2019-18634`**

### 4. Manual Pages
- <p>SCP is a tool used to copy files from one computer to another. <br /><i>What switch would you use to copy an entire directory?</i></p>

**=> Answer: `-r`**

- <p>fdisk is a command used to view and alter the partitioning scheme used on your hard drive.<br /><i>What switch would you use to list the current partitions?</i></p>

**=> Answer: `-l`**

- <p>nano is an easy-to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with.<br /><i>What switch would you use to make a backup when opening a file with nano?</i></p>

**=> Answer: `-B`**

- <p>Netcat is a basic tool used to manually send and receive network requests. <br /><i>What <b>command</b> would you use to start netcat in listen mode, using port 12345?</i></p>

**=> Answer: `nc -l -p 12345`**

### 5. Final Thoughts
*No hints needed!*

