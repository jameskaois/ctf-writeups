# Windows Fundamentals 3 - TryHackMe 

In part 3 of the Windows Fundamentals module, learn about the built-in Microsoft tools that help keep the device secure, such as Windows Updates, Windows Security, BitLocker, and more...

## Overview
- **Room URL:** [https://tryhackme.com/room/windowsfundamentals3xzx](https://tryhackme.com/room/windowsfundamentals3xzx)
- **Difficulty:** Info
- **Time to complete:** 30

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. Windows Updates
- There were two definition updates installed in the attached VM. On what date were these updates installed?
```
- Press Windows + R, Type control /name Microsoft.WindowsUpdate
- Click View Update History > Definition Updates
- You will see 2 installed updates
```
![Guide image](./screenshots/windows-fundamentals-3-1.png)
**=> Answer: `5/3/2021`**

### 3. Windows Security
- Checking the Security section on your VM, which area needs immediate attention?
![Guide image](./screenshots/windows-fundamentals-3-2.png)
**=> Answer: `Virus & threat protection`**

### 4. Virus &amp; threat protection
- Specifically, what is turned off that Windows is notifying you to turn on?
![Guide image](./screenshots/windows-fundamentals-3-3.png)
**=> Answer: `Real-time protection`**

### 5. Firewall &amp; network protection
- If you were connected to airport Wi-Fi, what most likely will be the active firewall profile?

**=> Answer: `Public network`**

### 6. App &amp; browser control
*No hints needed!*

### 7. Device security
- What is the TPM?

**=> Answer: `Trusted Platform Module`**

### 8. BitLocker
- <p>We should use a removable drive on systems <strong>without</strong> a TPM version 1.2 or later. What does this removable drive contain?</p>
```
- Visit https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/
```
![Guide image](./screenshots/windows-fundamentals-3-4.png)
**=> Answer: `startup key`**

### 9. Volume Shadow Copy Service
- What is VSS?

**=> Answer: `Volume Shadow Copy Service`**

### 10. Conclusion
*No hints needed!*

