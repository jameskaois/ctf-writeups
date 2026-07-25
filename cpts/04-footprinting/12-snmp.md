# Section 12: SNMP

Module: 04. Footprinting

---

## Questions & Answers

### 1. Enumerate the SNMP service and obtain the email address of the admin. Submit it as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ snmpwalk -v2c -c public 10.129.134.70
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIX02 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (280178) 0:46:41.78
iso.3.6.1.2.1.1.4.0 = STRING: "devadmin <devadmin@inlanefreight.htb>"
iso.3.6.1.2.1.1.5.0 = STRING: "NIX02"
iso.3.6.1.2.1.1.6.0 = STRING: "InFreight SNMP v0.91"
# ...
```

**Answer:** `devadmin@inlanefreight.htb`

---

### 2. What is the customized version of the SNMP server?

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ snmpwalk -v2c -c public 10.129.134.70
iso.3.6.1.2.1.1.1.0 = STRING: "Linux NIX02 5.4.0-90-generic #101-Ubuntu SMP Fri Oct 15 20:00:55 UTC 2021 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (280178) 0:46:41.78
iso.3.6.1.2.1.1.4.0 = STRING: "devadmin <devadmin@inlanefreight.htb>"
iso.3.6.1.2.1.1.5.0 = STRING: "NIX02"
iso.3.6.1.2.1.1.6.0 = STRING: "InFreight SNMP v0.91"
# ...
```

**Answer:** `InFreight SNMP v0.91`

---

### 3. Enumerate the custom script that is running on the system and submit its output as the answer.

Context:
```bash
snmpwalk -v2c -c public 10.129.134.70 .1 
# ...
iso.3.6.1.2.1.25.1.7.1.2.1.5.4.70.76.65.71 = INTEGER: 5
iso.3.6.1.2.1.25.1.7.1.2.1.6.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.7.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.2.1.20.4.70.76.65.71 = INTEGER: 4
iso.3.6.1.2.1.25.1.7.1.2.1.21.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.1.4.70.76.65.71 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
iso.3.6.1.2.1.25.1.7.1.3.1.2.4.70.76.65.71 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
iso.3.6.1.2.1.25.1.7.1.3.1.3.4.70.76.65.71 = INTEGER: 1
iso.3.6.1.2.1.25.1.7.1.3.1.4.4.70.76.65.71 = INTEGER: 0
iso.3.6.1.2.1.25.1.7.1.4.1.2.4.70.76.65.71.1 = STRING: "HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}"
iso.3.6.1.2.1.25.2.2.0 = INTEGER: 2034728
iso.3.6.1.2.1.25.2.3.1.1.1 = INTEGER: 1
iso.3.6.1.2.1.25.2.3.1.1.3 = INTEGER: 3
iso.3.6.1.2.1.25.2.3.1.1.6 = INTEGER: 6
iso.3.6.1.2.1.25.2.3.1.1.7 = INTEGER: 7
iso.3.6.1.2.1.25.2.3.1.1.8 = INTEGER: 8
iso.3.6.1.2.1.25.2.3.1.1.10 = INTEGER: 10
iso.3.6.1.2.1.25.2.3.1.1.35 = INTEGER: 35
iso.3.6.1.2.1.25.2.3.1.1.36 = INTEGER: 36
iso.3.6.1.2.1.25.2.3.1.1.38 = INTEGER: 38
iso.3.6.1.2.1.25.2.3.1.1.39 = INTEGER: 39
```

**Answer:** `HTB{5nMp_fl4g_uidhfljnsldiuhbfsdij44738b2u763g}`

---



[Back to Module Index](./README.md)
