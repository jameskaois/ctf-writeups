# Section 07: SQL Operators

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. In the 'titles' table, what is the number of records WHERE the employee number is greater than 10000 OR their title does NOT contain 'engineer'?

Context:
```bash
MariaDB [employees]> describe titles;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| emp_no    | int(11)     | NO   | PRI | NULL    |       |
| title     | varchar(50) | NO   | PRI | NULL    |       |
| from_date | date        | NO   | PRI | NULL    |       |
| to_date   | date        | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
4 rows in set (0.169 sec)

MariaDB [employees]> SELECT * FROM titles WHERE title NOT LIKE "%engineer%" OR emp_no > 10000;
+--------+--------------------+------------+------------+
| emp_no | title              | from_date  | to_date    |
+--------+--------------------+------------+------------+
|  10001 | Senior Engineer    | 1986-06-26 | 9999-01-01 |
|  10002 | Senior Engineer    | 1995-12-03 | 9999-01-01 |
|  10003 | Engineer           | 1986-12-01 | 1995-12-01 |
<SNIP>
|  10652 | Engineer           | 1997-12-29 | 2000-11-15 |
|  10653 | Senior Staff       | 2000-03-12 | 9999-01-01 |
|  10654 | Staff              | 1992-03-12 | 2000-03-12 |
+--------+--------------------+------------+------------+
654 rows in set (0.336 sec)
```

**Answer:** `654`

---

[Back to Module Index](./README.md)
