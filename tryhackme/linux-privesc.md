# Linux PrivEsc - TryHackMe

Practice your Linux Privilege Escalation skills on an intentionally misconfigured Debian VM with multiple ways to get root! SSH is available. Credentials: user:password321

## Overview

- **Room URL:** [https://tryhackme.com/room/linuxprivesc](https://tryhackme.com/room/linuxprivesc)
- **Difficulty:** Medium
- **Time to complete:** 75

## Walkthrough

### 1. Deploy the Vulnerable Debian VM

- <p>Deploy the machine and login to the "user" account using SSH.</p>

```bash
sudo openvpn <file>.ovpn
```

_No answer needed!_

- <p>Run the "id" command. What is the result?</p>

```bash
user@debian:~$ id

uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)
```

**=> Answer: `uid=1000(user) gid=1000(user) groups=1000(user),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev)`**

### 2. Service Exploits

_No hints needed!_

### 3. Weak File Permissions - Readable /etc/shadow

- <p>What is the root user's password hash?</p>

```bash
cat /etc/shadow
```

**=> Answer: `$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::`**

- <p>What hashing algorithm was used to produce the root user's password hash?<br /></p>
- Copy the entire user root and its hash password: `root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::`

```bash
vim hash.txt
# Paste the user root above

john --wordlist-/usr/share/wordlists/rockyou.txt hash.txt
```

- You can find the hashing algorithm from the result of john-the-ripper.

![Guide image](./screenshots/linux-privesc-1.png)

**=> Answer: `sha512crypt`**

- <p><span style="font-size:1rem;">What is the root user's password?</span></p>

**=> Answer: `password123`**

### 4. Weak File Permissions - Writable /etc/shadow

_No answer needed!_

### 5. Weak File Permissions - Writable /etc/passwd

- <p>Run the "id" command as the newroot user. What is the result?</p>
- Follow step-by-step guide of the challenge you can get access as `newroot` user.

**=> Answer: `uid=0(root) gid=0(root) groups=0(root)`**

### 6. Sudo - Shell Escape Sequences

- <p>How many programs is "user" allowed to run via sudo? </p>

```bash
sudo -l
```

**=> Answer: `11`**

- <p>One program on the list doesn't have a shell escape sequence on GTFOBins. Which is it?</p>

**=> Answer: `apache2`**

### 7. Sudo - Environment Variables

_No answer needed!_

### 8. Cron Jobs - File Permissions

_No answer needed!_

### 9. Cron Jobs - PATH Environment Variable

- <p>What is the value of the PATH variable in /etc/crontab?</p>

```bash
cat /etc/crontab

# ...
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
# ...
```

**=> Answer: `/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin`**

### 10. Cron Jobs - Wildcards

_No answer needed!_

### 11. SUID / SGID Executables - Known Exploits

_No answer needed!_

### 12. SUID / SGID Executables - Shared Object Injection

_No answer needed!_

### 13. SUID / SGID Executables - Environment Variables

_No answer needed!_

### 14. SUID / SGID Executables - Abusing Shell Features (#1)

_No answer needed!_

### 15. SUID / SGID Executables - Abusing Shell Features (#2)

_No answer needed!_

### 16. Passwords & Keys - History Files

- <p>What is the full mysql command the user executed?</p>

```bash
cat ~/.*history | less
```

**=> Answer: `mysql -h somehost.local -uroot -ppassword123`**

### 17. Passwords & Keys - Config Files

- <p>What file did you find the root user's credentials in?   </p>

```bash
user@debian:~$ cat /home/user/myvpn.ovpn

client
dev tun
proto udp
remote 10.10.10.10 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
tls-client
remote-cert-tls server
auth-user-pass /etc/openvpn/auth.txt
comp-lzo
verb 1
reneg-sec 0

user@debian:~$ cat /etc/openvpn/auth.txt

root
password123

```

**=> Answer: `/etc/openvpn/auth.txt`**

### 18. Passwords &amp; Keys - SSH Keys

_No answer needed!_

### 19. NFS

- <p>What is the name of the option that disables root squashing?</p>

**=> Answer: `no_root_squash`**

### 20. Kernel Exploits

_No answer needed!_

### 21. Privilege Escalation Scripts

_No answer needed!_
