# Section 06: FTP

Module: 04. Footprinting

---

## Questions & Answers

### 1. Which version of the FTP server is running on the target system? Submit the entire banner as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ nc -nv 10.129.134.68 21
Connection to 10.129.134.68 21 port [tcp/*] succeeded!
220 InFreight FTP v1.1
```

**Answer:** `InFreight FTP v1.1`

---

### 2. Enumerate the FTP server and find the flag.txt file. Submit the contents of it as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ ftp -p 10.129.134.68
Connected to 10.129.134.68.
220 InFreight FTP v1.1
Name (10.129.134.68:root): anonymous
331 Anonymous login ok, send your complete email address as your password
Password: 
230 Anonymous access granted, restrictions apply
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||7201|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
226 Transfer complete
ftp> cd ftpuser
550 ftpuser: No such file or directory
ftp> ls
229 Entering Extended Passive Mode (|||2492|)
150 Opening ASCII mode data connection for file list
-rw-r--r--   1 ftpuser  ftpuser        39 Nov  8  2021 flag.txt
226 Transfer complete
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||37257|)
150 Opening BINARY mode data connection for flag.txt (39 bytes)
    39       65.21 KiB/s 
226 Transfer complete
39 bytes received in 00:00 (0.24 KiB/s)
ftp> 
ftp> exit
221 Goodbye.
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ cat flag.txt
HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}
```

**Answer:** `HTB{b7skjr4c76zhsds7fzhd4k3ujg7nhdjre}`

---

[Back to Module Index](./README.md)
