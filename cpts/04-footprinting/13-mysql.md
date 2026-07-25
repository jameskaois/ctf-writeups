# Section 13: MySQL

Module: 04. Footprinting

---

## Questions & Answers

### 1. Enumerate the MySQL server and determine the version in use. (Format: MySQL X.X.XX)

Context:
```bash
MySQL [customers]> SELECT VERSION();
+-------------------------+
| VERSION()               |
+-------------------------+
| 8.0.27-0ubuntu0.20.04.1 |
+-------------------------+
1 row in set (0.155 sec)
```

**Answer:** `MySQL 8.0.27`

---

### 2. During our penetration test, we found weak credentials "robin:robin". We should try these against the MySQL server. What is the email address of the customer "Otto Lang"?

Context:
```bash
mysql -u robin -p -h 10.129.134.80 --skip-ssl

MySQL [customers]> show databases;
+--------------------+
| Database           |
+--------------------+
| customers          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.156 sec)

MySQL [customers]> use customers
Database changed
MySQL [customers]> show tables;
+---------------------+
| Tables_in_customers |
+---------------------+
| myTable             |
+---------------------+
1 row in set (0.157 sec)

MySQL [customers]> SELECT * FROM mytable;
ERROR 1146 (42S02): Table 'customers.mytable' doesn't exist
MySQL [customers]> SELECT * FROM myTable;
# ...
| 88 | Otto Lang           | ultrices@google.htb                      | France             | 76733-267   | Belfast                       | 4708 Auctor Rd.                   | 5322224628183391    | 595  |
```

**Answer:** `ultrices@google.htb`

---

[Back to Module Index](./README.md)
