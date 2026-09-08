# Section 05: SQL Statements

Module: 17. SQL Injection Fundamentals

---

## Questions & Answers

### 1. What is the department number for the 'Development' department?

Context:
```bash
MariaDB [(none)]> use employees
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [employees]> show tables;
+----------------------+
| Tables_in_employees  |
+----------------------+
| current_dept_emp     |
| departments          |
| dept_emp             |
| dept_emp_latest_date |
| dept_manager         |
| employees            |
| salaries             |
| titles               |
+----------------------+
8 rows in set (0.168 sec)

MariaDB [employees]> SELECT * FROM departments;
+---------+--------------------+
| dept_no | dept_name          |
+---------+--------------------+
| d009    | Customer Service   |
| d005    | Development        |
| d002    | Finance            |
| d003    | Human Resources    |
| d001    | Marketing          |
| d004    | Production         |
| d006    | Quality Management |
| d008    | Research           |
| d007    | Sales              |
+---------+--------------------+
9 rows in set (0.168 sec)

MariaDB [employees]> 
```

**Answer:** `d005`

---

[Back to Module Index](./README.md)
