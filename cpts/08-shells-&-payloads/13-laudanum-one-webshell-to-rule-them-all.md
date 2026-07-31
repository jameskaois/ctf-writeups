# Section 13: Laudanum, One Webshell to Rule Them All

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. Establish a web shell session with the target using the concepts covered in this section. Submit the full path of the directory you land in. (Format: c:\path\you\land\in)

Context: 
- Add domain to `/etc/hosts`:
```bash
┌─[eu-academy-1]─[10.10.15.239]─[htb-ac-2162140@htb-kv4lm3xyok]─[~]
└──╼ [★]$ sudo vim /etc/hosts
┌─[eu-academy-1]─[10.10.15.239]─[htb-ac-2162140@htb-kv4lm3xyok]─[~]
└──╼ [★]$ cat /etc/hosts
127.0.0.1	localhost
127.0.1.1	pwnbox7.1

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
127.0.0.1 localhost
127.0.1.1 htb-kv4lm3xyok htb-kv4lm3xyok.htb-cloud.com
10.129.42.197 status.inlanefreight.local
┌─[eu-academy-1]─[10.10.15.239]─[htb-ac-2162140@htb-kv4lm3xyok]─[~]
└──╼ [★]$ 
```
- Upload the `demo.aspx`, then run query `cd`:
```
STDOUT:

c:\windows\system32\inetsrv
```


**Answer:** `c:\windows\system32\inetsrv`

---

### 2. Where is the Laudanum aspx web shell located on Pwnbox? Submit the full path. (Format: /path/to/laudanum/aspx)


**Answer:** `/usr/share/laudanum/aspx/shell.aspx`

---

[Back to Module Index](./README.md)
