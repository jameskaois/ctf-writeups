# Section 11: Port Forwarding with Windows Netsh

Module: 12. Pivoting, Tunneling, and Port Forwarding

---

## Questions & Answers

### 1. Using the concepts covered in this section, take control of the DC (172.16.5.19) using xfreerdp by pivoting through the Windows 10 target host. Submit the approved contact's name found inside the "VendorContacts.txt" file located in the "Approved Vendors" folder on Victor's desktop (victor's credentials: victor:pass@123) . (Format: 1 space, not case-sensitive)

Context:
```bash
netsh interface portproxy add v4tov4 listenport=13389 listenaddress=0.0.0.0 connectport=3389 connectaddress=172.16.5.19

netsh interface portproxy show all

xfreerdp /v:<Windows_10_IP>:13389 /u:victor /p:pass@123 /d:HTB /gdi:hw /tls-seclevel:0 +clipboard
```

**Answer:** `Jim Flipflop`

---

[Back to Module Index](./README.md)
