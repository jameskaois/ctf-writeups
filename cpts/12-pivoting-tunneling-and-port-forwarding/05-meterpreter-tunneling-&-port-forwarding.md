# Section 05: Meterpreter Tunneling & Port Forwarding

Module: 12. Pivoting, Tunneling, and Port Forwarding

---

## Questions & Answers

### 1. What two IP addresses can be discovered when attempting a ping sweep from the Ubuntu pivot host? (Format: x.x.x.x,x.x.x.x)

Context:
```bash
ubuntu@WEB01:~$ for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
64 bytes from 172.16.5.19: icmp_seq=1 ttl=128 time=0.659 ms
64 bytes from 172.16.5.129: icmp_seq=1 ttl=64 time=0.026 ms
```

**Answer:** `172.16.5.19,172.16.5.129`

---

### 2. Which of the routes that AutoRoute adds allows 172.16.5.19 to be reachable from the attack host? (Format: x.x.x.x/x.x.x.x)

**Answer:** `172.16.5.0/255.255.254.0`

---

[Back to Module Index](./README.md)
