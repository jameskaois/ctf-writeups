# Section 10: Web Server Pivoting with Rpivot

Module: 12. Pivoting, Tunneling, and Port Forwarding

---

## Questions & Answers

### 1. From which host will rpivot's server.py need to be run from? The Pivot Host or Attack Host? Submit Pivot Host or Attack Host as the answer.

**Answer:** `Attack Host`

---

### 2. From which host will rpivot's client.py need to be run from? The Pivot Host or Attack Host. Submit Pivot Host or Attack Host as the answer.

**Answer:** `Pivot Host`

---

### 3. Using the concepts taught in this section, connect to the web server on the internal network. Submit the flag presented on the home page as the answer.

Context:
- Run `server.py` on our host:
```bash
┌──(jameskaois㉿kali)-[~/Documents/rpivot]
└─$ python2 server.py --proxy-port 9050 --server-port 9999 --server-ip 0.0.0.0
```
- Move `client.py` to pivot host and run it:
```bash
┌──(jameskaois㉿kali)-[~/Documents/rpivot]
└─$ scp client.py ubuntu@10.129.108.5:/home/ubuntu 
The authenticity of host '10.129.108.5 (10.129.108.5)' can't be established.
ED25519 key fingerprint is: SHA256:AtNYHXCA7dVpi58LB+uuPe9xvc2lJwA6y7q82kZoBNM
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:47: [hashed name]
    ~/.ssh/known_hosts:58: [hashed name]
    ~/.ssh/known_hosts:59: [hashed name]
    ~/.ssh/known_hosts:60: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.129.108.5' (ED25519) to the list of known hosts.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
ubuntu@10.129.108.5's password: 
client.py                                                                                                                                                         100%   21KB  41.6KB/s   00:00    
ubuntu@WEB01:$ python2 client.py --server-ip 10.10.14.18 --server-port 9999
```
- On our attack host, confirm new connection:
```bash
New connection from host 10.129.202.64, source port 35226

proxychains firefox-esr 172.16.5.135:80
```

**Answer:** `I_L0v3_Pr0xy_Ch@ins`

---

[Back to Module Index](./README.md)
