# Section 13: SOCKS5 Tunneling with Chisel

Module: 12. Pivoting, Tunneling, and Port Forwarding

---

## Questions & Answers

### 1. Using the concepts taught in this section, connect to the target and establish a SOCKS5 Tunnel that can be used to RDP into the domain controller (172.16.5.19, victor:pass@123). Submit the contents of C:\Users\victor\Documents\flag.txt as the answer.

Context:
```bash
CGO_ENABLED=0 go build -o chisel .

chmod u+x chisel
./chisel server -v -p 1234 --socks5

./chisel client <target-IP>:1234 socks

proxychains xfreerdp /v:172.16.5.19 /u:victor /p:pass@123
```

**Answer:** `Th3$eTunne1$@rent8oring!`

---

[Back to Module Index](./README.md)
