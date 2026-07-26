# Section 19: Skills Assessment

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. What is the IANA ID of the registrar of the inlanefreight.com domain?

Context:
```bash
─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ whois inlanefreight.com
   Domain Name: INLANEFREIGHT.COM
   Registry Domain ID: 2420436757_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.registrar.amazon
   Registrar URL: http://registrar.amazon.com
   Updated Date: 2026-07-01T22:45:41Z
   Creation Date: 2019-08-05T22:43:09Z
   Registry Expiry Date: 2027-08-05T22:43:09Z
   Registrar: Amazon Registrar, Inc.
   Registrar IANA ID: 468
   Registrar Abuse Contact Email: trustandsafety@support.aws.com
   Registrar Abuse Contact Phone: +1.2024422253
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Name Server: NS-1303.AWSDNS-34.ORG
   Name Server: NS-1580.AWSDNS-05.CO.UK
   Name Server: NS-161.AWSDNS-20.COM
   Name Server: NS-671.AWSDNS-19.NET
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2026-07-26T01:13:39Z <<<

#....
Registrar IANA ID: 468
# ...
```

**Answer:** `468`

---

### 2. What http server software is powering the inlanefreight.htb site on the target system? Respond with the name of the software, not the version, e.g., Apache.

Context:
```bash
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ sudo vim /etc/hosts
# add 154.57.164.67 inlanefreight.htb
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl -s -I http://inlanefreight.htb:30949
HTTP/1.1 200 OK
Server: nginx/1.26.1
Date: Sun, 26 Jul 2026 01:16:31 GMT
Content-Type: text/html
Content-Length: 120
Last-Modified: Thu, 01 Aug 2024 09:35:23 GMT
Connection: keep-alive
ETag: "66ab56db-78"
Accept-Ranges: bytes
```

**Answer:** `nginx`

---

### 3. What is the API key in the hidden admin directory that you have discovered on the target system?

Context:
```bash
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://inlanefreight.htb:30949 -H "Host: FUZZ.inlanefreight.htb" -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://inlanefreight.htb:30949
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.inlanefreight.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

web1337                 [Status: 200, Size: 104, Words: 4, Lines: 2, Duration: 156ms]
```
```bash
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ sudo vim /etc/hosts
# add 154.57.164.67 web1337.inlanefreight.htb
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://web1337.inlanefreight.htb:30949
<!DOCTYPE html><html><head><title>web1337</title></head><body><h1>Welcome to web1337</h1></body></html>
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://web1337.inlanefreight.htb:30949/robots.txt
User-agent: *
Allow: /index.html
Allow: /index-2.html
Allow: /index-3.html
Disallow: /admin_h1dd3n
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://web1337.inlanefreight.htb:30949/admin_hi1dd3n
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.26.1</center>
</body>
</html>
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://web1337.inlanefreight.htb:30949/admin_h1dd3n
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.26.1</center>
</body>
</html>
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ curl http://web1337.inlanefreight.htb:30949/admin_h1dd3n/
<!DOCTYPE html><html><head><title>web1337 admin</title></head><body><h1>Welcome to web1337 admin site</h1><h2>The admin panel is currently under maintenance, but the API is still accessible with the key e963d863ee0e82ba7080fbf558ca0d3f</h2></body></html>
```

**Answer:** `e963d863ee0e82ba7080fbf558ca0d3f`

---

### 4. After crawling the inlanefreight.htb domain on the target system, what is the email address you have found? Respond with the full email, e.g., mail@inlanefreight.htb.

Context:
```bash
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://web1337.inlanefreight.htb:30949 -H "Host: FUZZ.web1337.inlanefreight.htb" -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://web1337.inlanefreight.htb:30949
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.web1337.inlanefreight.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

dev                     [Status: 200, Size: 123, Words: 5, Lines: 1, Duration: 158ms]
```
```bash
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ sudo vim /etc/hosts
# add 154.57.164.67 dev.web1337.inlanefreight.htb
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ python3 ReconSpider.py http://dev.web1337.inlanefreight.htb:30949
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ cat results.json
{
    "emails": [
        "1337testing@inlanefreight.htb"
    ],
    "links": [
        # ...
    ]
}
```

**Answer:** `1337testing@inlanefreight.htb`

---

### 5. What is the API key the inlanefreight.htb developers will be changing too?

Context:
```bash
┌─[eu-academy-1]─[10.10.15.38]─[htb-ac-2162140@pwnbox7]─[~]
└──╼ [★]$ cat results.json
{
    "emails": [
        "1337testing@inlanefreight.htb"
    ],
    "links": [
        # ...
    ],
    "external_files": [],
    "js_files": [],
    "form_fields": [],
    "images": [],
    "videos": [],
    "audio": [],
    "comments": [
        "<!-- Remember to change the API key to ba988b835be4aa97d068941dc852ff33 -->"
    ]
```

**Answer:** `ba988b835be4aa97d068941dc852ff33`

---

[Back to Module Index](./README.md)
