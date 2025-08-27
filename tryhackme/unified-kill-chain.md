# Unified Kill Chain - TryHackMe 

The Unified Kill Chain is a framework which establishes the phases of an attack, and a means of identifying and mitigating risk to IT assets.

## Overview
- **Room URL:** [https://tryhackme.com/room/unifiedkillchain](https://tryhackme.com/room/unifiedkillchain)
- **Difficulty:** Easy
- **Time to complete:** 40

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. What is a "Kill Chain"
- <p>Where does the term "Kill Chain" originate from?</p><p>For this answer, you must fill in the blank!: The <b>********</b></p>

**=> Answer: `military`**

### 3. What is "Threat Modelling"
- What is the technical term for a piece of software or hardware in IT (Information Technology?)

**=> Answer: `asset`**

### 4. Introducing the Unified Kill Chain
- In what year was the Unified Kill Chain framework released?

**=> Answer: `2017`**

- <p>According to the Unified Kill Chain, how many phases are there to an attack?</p>

**=> Answer: `18`**

- <p>What is the name of the attack phase where an attacker employs techniques to evade detection?</p>

**=> Answer: `Defense Evasion`**

- <p>What is the name of the attack phase where an attacker employs techniques to remove data from a network?<br /></p>

**=> Answer: `Exfiltration`**

- <p>What is the name of the attack phase where an attacker achieves their objectives?<br /></p>

**=> Answer: `Objectives`**

### 5. Phase: In (Initial Foothold)
- What is an example of a tactic to gain a foothold using emails?

**=> Answer: `Phishing`**

- <p>Impersonating an employee to request a password reset is a form of what?</p>

**=> Answer: `Social Engineering`**

- <p>An adversary setting up the Command &amp; Control server infrastructure is what phase of the Unified Kill Chain?</p>

**=> Answer: `Weaponization`**

- <p>Exploiting a vulnerability present on a system is what phase of the Unified Kill Chain?</p>

**=> Answer: `Exploitation`**

- <p>Moving from one system to another is an example of?</p>

**=> Answer: `Pivoting`**

- <p>Leaving behind a malicious service that allows the adversary to log back into the target is what?</p>

**=> Answer: `Persistence`**

### 6. Phase: Through (Network Propagation)
- As a SOC analyst, you pick up numerous alerts pointing to failed login attempts from an administrator account. What stage of the kill chain would an attacker be seeking to achieve?

**=> Answer: `Privilege Escalation`**

- <p>Mimikatz, a known post-exploitation tool, was recently detected running on the IT Manager’s computer. Security logs show that Mimikatz attempted to access memory spaces typically used by Windows to store user authentication secrets. Considering the usual capabilities and purpose of Mimikatz, what is the primary objective of this tool in such an attack scenario?</p>

**=> Answer: `Credential dumping`**

### 7. Phase: Out (Action on Objectives)
- While monitoring the network as a SOC analyst, you realise that there is a spike in the network activity, and all the traffic is outbound to an unknown IP address. What stage could describe this activity?

**=> Answer: `Exfiltration`**

- <p>Personally identifiable information (PII) has been released to the public by an adversary, and your organisation is facing scrutiny for the breach. What part of the CIA triad would be affected by this action?</p>

**=> Answer: `Confidentiality`**

### 8. Practical
- Match the scenario prompt to the correct phase of the Unified Kill Chain to reveal the flag at the end. What is the flag?

**=> Answer: `THM{UKC_SCENARIO}`**

### 9. Conclusion
*No hints needed!*