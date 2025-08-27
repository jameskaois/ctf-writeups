# Cyber Kill Chain  - TryHackMe 

The Cyber Kill Chain framework is designed for identification and prevention of the network intrusions. You will learn what the adversaries need to do in order to achieve their goals.

## Overview
- **Room URL:** [https://tryhackme.com/room/cyberkillchainzmt](https://tryhackme.com/room/cyberkillchainzmt)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. Reconnaissance
- What is the name of the Intel Gathering Tool that is a web-based interface to the common tools and resources for open-source intelligence?

**=> Answer: `OSINT Framework`**

- <p>What is the definition for the email gathering process during the stage of reconnaissance?</p>

**=> Answer: `email harvesting`**

### 3. Weaponization
- This term is referred to as a group of commands that perform a specific task. You can think of them as subroutines or functions that contain the code that most users use to automate routine tasks. But malicious actors tend to use them for malicious purposes and include them in Microsoft Office documents. Can you provide the term for it? 

**=> Answer: `macro`**

### 4. Delivery
- What is the name of the attack when it is performed against a specific group of people, and the attacker seeks to infect the website that the mentioned group of people is constantly visiting.

**=> Answer: `Watering hole attack`**

### 5. Exploitation
- Can you provide the name for a cyberattack targeting a software vulnerability that is unknown to the antivirus or software vendors?

**=> Answer: `zero-day`**

### 6. Installation
- Can you provide the technique used to modify file time attributes to hide new or changes to existing files?

**=> Answer: `Timestomping`**

- <p>Can you name the malicious script planted by an attacker on the webserver to maintain access to the compromised system and enables the webserver to be accessed remotely?</p>

**=> Answer: `web shell`**

### 7. Command &amp; Control
- What is the C2 communication where the victim makes regular DNS requests to a DNS server and domain which belong to an attacker. 

**=> Answer: `DNS Tunneling`**

### 8. Actions on Objectives (Exfiltration)
- Can you provide a technology included in Microsoft Windows that can create backup copies or snapshots of files or volumes on the computer, even when they are in use? 

**=> Answer: `Shadow Copy`**

### 9. Practice Analysis 
- What is the flag after you complete the static site?
```
Weaponization: Powershell
Delivery: spearphishing attachment
Exploitation: exploit public-facing application
Installation: dynamic linker hijacking
Command & Control: fallback channels
Actions on Objectives: data from local system
```

**=> Answer: `THM{7HR347_1N73L_12_4w35om3}`**

### 10. Conclusion
*No hints needed!*