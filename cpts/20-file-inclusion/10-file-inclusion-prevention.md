# Section 10: File Inclusion Preventing

Module: 20. File Inclusion

---

## Questions & Answers

### 1. What is the full path to the php.ini file for Apache?

Context:
```bash
htb-student@lfi-harden:~$ find / -type f -name "php.ini" 2>/dev/null
/etc/php/7.4/cli/php.ini
/etc/php/7.4/apache2/php.ini
```

**Answer:** `/etc/php/7.4/apache2/php.ini`

---

### 2. Edit the php.ini file to block system(), then try to execute PHP Code that uses system. Read the /var/log/apache2/error.log file and fill in the blank: system() has been disabled for ________ reasons.

**Answer:** `security`

---

[Back to Module Index](./README.md)
