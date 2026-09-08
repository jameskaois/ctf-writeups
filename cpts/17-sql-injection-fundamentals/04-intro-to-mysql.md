# Section 04: Intro to MySQL

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. Connect to the database using the MySQL client from the command line. Use the 'show databases;' command to list databases in the DBMS. What is the name of the first database?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.219]─[htb-ac-2162140@htb-wmxiq20pt2-htb-cloud-com]─[~]
└──╼ [★]$ mysql -u root -h 154.57.164.82 -P 32227 -p --skip-ssl
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 10.7.3-MariaDB-1:10.7.3+maria~focal mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| employees          |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.168 sec)

MariaDB [(none)]> 
```

**Answer:** `employees`

---

[Back to Module Index](./README.md)
