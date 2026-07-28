# Section 03: Linux File Transfer Methods

Module: 07. File Transfers

---

## Questions & Answers

### 1. Download the file flag.txt from the web root using Python from the Pwnbox. Submit the contents of the file as your answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.184]─[htb-ac-2162140@htb-efv5zomuca]─[~]
└──╼ [★]$ curl http://10.129.234.168/flag.txt
5d21cf3da9c0ccb94f709e2559f3ea50
```

**Answer:** `5d21cf3da9c0ccb94f709e2559f3ea50`

---

### 2. Upload the attached file named upload_nix.zip to the target using the method of your choice. Once uploaded, SSH to the box, extract the file, and run "hasher <extracted file>" from the command line. Submit the generated hash as your answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.184]─[htb-ac-2162140@htb-efv5zomuca]─[~]
└──╼ [★]$ ssh htb-student@10.129.234.168
The authenticity of host '10.129.234.168 (10.129.234.168)' can't be established.
ED25519 key fingerprint is SHA256:z4rcb3qcf0IdRnoTBNEJ4i8TlDystDA4uOJFxVcb41E.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.234.168' (ED25519) to the list of known hosts.
htb-student@10.129.234.168's password: 
Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.4.0-47-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon 27 Jul 2026 07:38:04 AM UTC

  System load:             0.75
  Usage of /:              29.5% of 15.68GB
  Memory usage:            10%
  Swap usage:              0%
  Processes:               151
  Users logged in:         0
  IPv4 address for ens192: 10.129.234.168
  IPv6 address for ens192: dead:beef::a0de:adff:fee1:3140


71 updates can be installed immediately.
0 of these updates are security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Wed Sep  9 22:42:43 2020 from 10.10.14.4
htb-student@nix04:~$ pwd
/home/htb-student
htb-student@nix04:~$ echo "UEsDBAoAAAAAAEqEKVFRlJcKIAAAACAAAAAOAAAAdXBsb2FkX25peC50eHQwNDgwOTBiYzdlZDA0Zjc1ODY1ODk3NWRmOGY4NjJjOFBLAQI/AAoAAAAAAEqEKVFRlJcKIAAAACAAAAAOACQAAAAAAAAAIAAAAAAAAAB1cGxvYWRfbml4LnR4dAoAIAAAAAAAAQAYAHGdOpjohtYB0cK75fqG1gHXv2od5obWAVBLBQYAAAAAAQABAGAAAABMAAAAAAA=
> " | base64 -d > upload_nix.zip
htb-student@nix04:~$ unzip upload_nix.zip 

Command 'unzip' not found, but can be installed with:

apt install unzip
Please ask your administrator.

htb-student@nix04:~$ python3 -m zipfile -e upload_nix.zip .
htb-student@nix04:~$ ls
upload_nix.txt  upload_nix.zip
htb-student@nix04:~$ hasher upload_nix.txt 
159cfe5c65054bbadb2761cfa359c8b0
```

**Answer:** `159cfe5c65054bbadb2761cfa359c8b0`

---

[Back to Module Index](./README.md)
