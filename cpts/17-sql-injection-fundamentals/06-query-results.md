# Section 06: Query Results

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. What is the last name of the employee whose first name starts with "Bar" AND who was hired on 1990-01-01?

Context:
```bash
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
6 rows in set (0.169 sec)

MariaDB [employees]> SELECT * FROM employees WHERE first_name LIKE "Bar%" AND hire_date = "1990-01-01";
+--------+------------+------------+-----------+--------+------------+
| emp_no | birth_date | first_name | last_name | gender | hire_date  |
+--------+------------+------------+-----------+--------+------------+
|  10227 | 1953-10-09 | Barton     | Mitchem   | M      | 1990-01-01 |
+--------+------------+------------+-----------+--------+------------+
1 row in set (0.168 sec)
```

**Answer:** `Mitchem`

---

[Back to Module Index](./README.md)
