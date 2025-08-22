# Web Application Security - TryHackMe 

Learn about web applications and explore some of their common security issues.

## Overview
- **Room URL:** [https://tryhackme.com/room/introwebapplicationsecurity](https://tryhackme.com/room/introwebapplicationsecurity)
- **Difficulty:** Easy
- **Time to complete:** 90

## Walkthrough
### 1. Introduction
- What do you need to access a web application?

**=> Answer: `Browser`**

### 2. Web Application Security Risks
- <div>You discovered that the login page allows an unlimited number of login attempts without trying to slow down the user or lock the account. What is the category of this security risk?</div>

**=> Answer: `Identification and Authentication Failure`**

- <p>You noticed that the username and password are sent in cleartext without encryption. What is the category of this security risk?<br /></p>

**=> Answer: `Cryptographic Failures`**

### 3. Practical Example of Web Application Security
- <div>Check the other users to discover which user account was used to make the malicious changes and revert them. After reverting the changes, what is the flag that you have received?</div>

> Access the browser with the URL `...?user_id=9` and revert all recent activities to get the flag.

**=> Answer: `THM{IDOR_EXPLORED}`**

