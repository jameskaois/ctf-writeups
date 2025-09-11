# Kenobi - TryHackMe

Walkthrough on exploiting a Linux machine. Enumerate Samba for shares, manipulate a vulnerable version of proftpd and escalate your privileges with path variable manipulation.

## Overview

- **Room URL:** [https://tryhackme.com/room/kenobi](https://tryhackme.com/room/kenobi)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough

### 1. Deploy the vulnerable machine

- <p>Scan the machine with nmap, how many ports are open?</p>

```bash
nmap <MACHINE_IP> -vvv
```

![Guide image](./screenshots/kenobi-1.png)
**=> Answer: `7`**

### 2. Enumerating Samba for shares

- <p>Using nmap we can enumerate a machine for SMB shares.</p><p>Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!</p><p><span style="color:rgb(206, 0, 0)">nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP</span></p><p>SMB has two ports, 445 and 139.</p><p><img src="https://i.imgur.com/bkgVNy3.png" style="width:457px;height:201.336px" /></p><p>Using the nmap command above, how many shares have been found?</p>

```bash
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.44.222

# or

smbclient -L //<MACHINE_IP>/ -N
```

![Guide image](./screenshots/kenobi-2.png)

**=> Answer: `3`**

- <p>On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.</p><p><span style="color:rgb(206, 0, 0)">smbclient //</span><span style="color:rgb(206, 0, 0)">MACHINE_IP</span><span style="color:rgb(206, 0, 0)">/anonymous</span></p><p>Using your machine, connect to the machines network share.</p><p><img src="https://i.imgur.com/B1FXBt8.png" style="width:516px" /></p><p>Once you're connected, list the files on the share. What is the file can you see?</p>

```bash
smbclient //<MACHINE_IP>/anonymous
smb: \> ls
```

![Guide image](./screenshots/kenobi-3.png)

**=> Answer: `log.txt`**

- <p>You can recursively download the SMB share too. Submit the username and password as nothing.</p><p><span style="color:rgb(206, 0, 0)">smbget -R smb://</span><span style="color:rgb(206, 0, 0)">MACHINE_IP</span><span style="color:rgb(206, 0, 0)">/anonymous</span></p><p>Open the file on the share. There is a few interesting things found.</p><ul><li>Information generated for Kenobi when generating an SSH key for the user</li><li>Information about the ProFTPD server.</li></ul><p>What port is FTP running on?</p>

```bash
nmap <MACHINE_IP>
```

![Guide image](./screenshots/kenobi-1.png)

**=> Answer: `21`**

- <p>Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. </p><p>In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.</p><p><span style="color:rgb(206, 0, 0)">nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP</span></p><p>What mount can we see?</p>

```bash
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount <MACHINE_IP>
```

![Guide image](./screenshots/kenobi-4.png)

**=> Answer: `/var`**

### 3. Gain initial access with ProFtpd

- <p>Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port.</p><p>What is the version?</p>

```bash
netcat <MACHINE_IP> 21
```

![Guide image](./screenshots/kenobi-5.png)

**=> Answer: `1.3.5`**

- <p>We can use searchsploit to find exploits for a particular software version.</p><p>Searchsploit is basically just a command line search tool for exploit-db.com.</p><p>How many exploits are there for the ProFTPd running?</p>

```bash
searchsploit ProFTPd 1.3.5
```

![Guide image](./screenshots/kenobi-6.png)

**=> Answer: `4`**

- <p>Lets mount the /var/tmp directory to our machine</p><p><span style="color:rgb(206, 0, 0)">mkdir /mnt/kenobiNFS<br />mount MACHINE_IP:/var /mnt/kenobiNFS<br />ls -la /mnt/kenobiNFS</span></p><p><img src="https://i.imgur.com/v8Ln4fu.png" style="width:495px;height:302.063px" /></p><p>We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.</p><p><img src="https://i.imgur.com/Vy4KkEl.png" style="width:493px" /></p><p>What is Kenobi's user flag (/home/kenobi/user.txt)?</p>

```bash
# follow the above steps

cat /home/kenobi/user.txt
```

![Guide image](./screenshots/kenobi-7.png)

**=> Answer: `d0b0f3f53b6caa532a83915e19224899`**

### 4. Privilege Escalation with Path Variable Manipulation

- <p>SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.</p><p>To search the a system for these type of files run the following: <span style="color:rgb(206, 0, 0)">find / -perm -u=s -type f 2&gt;/dev/null</span></p><p><span>What file looks particularly out of the ordinary?</span></p>

```bash
find / -perm -u=s -type f 2&gt;/dev/null
```

![Guide image](./screenshots/kenobi-8.png)

**=> Answer: `/usr/bin/menu`**

- <p>Run the binary, how many options appear?</p>

```bash
menu
```

![Guide image](./screenshots/kenobi-9.png)

**=> Answer: `3`**

- <p>What is the root flag (/root/root.txt)?</p>

**=> Answer: `177b3cd8562289f37382721c28381f02`**
