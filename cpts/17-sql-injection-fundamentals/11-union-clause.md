# Section 11: Union Clause

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. Connect to the above MySQL server with the 'mysql' tool, and find the number of records returned when doing a 'Union' of all records in the 'employees' table and all records in the 'departments' table.

Context:
```bash
┌─[eu-academy-2]─[10.10.15.219]─[htb-ac-2162140@htb-wmxiq20pt2-htb-cloud-com]─[~]
└──╼ [★]$ mysql -u root -h 154.57.164.82 -P 30812 -p --skip-ssl
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
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
5 rows in set (0.171 sec)

MariaDB [(none)]> use employees;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [employees]> SELECT * FROM employees UNION SELECT * FROM departments;
ERROR 1222 (21000): The used SELECT statements have a different number of columns
MariaDB [employees]> describe employees;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| emp_no     | int(11)       | NO   | PRI | NULL    |       |
| birth_date | date          | NO   |     | NULL    |       |
| first_name | varchar(14)   | NO   |     | NULL    |       |
| last_name  | varchar(16)   | NO   |     | NULL    |       |
| gender     | enum('M','F') | NO   |     | NULL    |       |
| hire_date  | date          | NO   |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
6 rows in set (0.172 sec)

MariaDB [employees]> describe departments;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| dept_no   | char(4)     | NO   | PRI | NULL    |       |
| dept_name | varchar(40) | NO   | UNI | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
2 rows in set (0.175 sec)

MariaDB [employees]> SELECT * FROM employees UNION SELECT dept_no, dept_name, 3, 4, 5, 6 FROM departments;
+--------+--------------------+--------------+-----------------+--------+------------+
| emp_no | birth_date         | first_name   | last_name       | gender | hire_date  |
+--------+--------------------+--------------+-----------------+--------+------------+
| 10001  | 1953-09-02         | Georgi       | Facello         | M      | 1986-06-26 |
| 10002  | 1952-12-03         | Vivian       | Billawala       | F      | 1986-12-11 |
<SNIP>
| d004   | Production         | 3            | 4               | 5      | 6          |
| d006   | Quality Management | 3            | 4               | 5      | 6          |
| d008   | Research           | 3            | 4               | 5      | 6          |
| d007   | Sales              | 3            | 4               | 5      | 6          |
+--------+--------------------+--------------+-----------------+--------+------------+
663 rows in set (0.342 sec)
```


**Answer:** `663`

---

[Back to Module Index](./README.md)
