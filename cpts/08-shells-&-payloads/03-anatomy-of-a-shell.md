# Section 03: Anatomy of a Shell

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. Which two shell languages did we experiment with in this section? (Format: shellname&shellname)

Context:

```bash
┌─[eu-academy-1]─[10.10.15.177]─[htb-ac-2162140@htb-krw6dyt2ty]─[~]
└──╼ [★]$ ps
    PID TTY          TIME CMD
  11796 pts/0    00:00:00 bash
  12030 pts/0    00:00:00 ps
```
```powershell
PowerShell 7.6.0
Welcome to Parrot OS 

Welcome to Pwnbox, Powered by Parrot OS
PS [10.10.15.177] /home/htb-ac-2162140 > 
```

**Answer:** `bash&powershell`

---

### 2. In Pwnbox issue the $PSversiontable variable using PowerShell. Submit the edition of PowerShell that is running as the answer.

Context:

```powershell
PS [10.10.15.177] /home/htb-ac-2162140 > $PSversiontable

Name                           Value
----                           -----
PSVersion                      7.6.0
PSEdition                      Core
GitCommitId                    7.6.0
OS                             Parrot Security 7.1 (echo)
Platform                       Unix
PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0…}
PSRemotingProtocolVersion      2.4
SerializationVersion           1.1.0.1
WSManStackVersion              3.0
```

**Answer:** `Core`

---

[Back to Module Index](./README.md)
