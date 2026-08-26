# Section 10: Burp Intruder

Module: 14. Using Web Proxies

---

## Questions & Answers

### 1. Use Burp Intruder to fuzz for '.html' files under the /admin directory, to find a file containing the flag.

Context:
- Send captured request to Intruder
```
GET /admin/$$filename$$.html HTTP/1.1
Host: 154.57.164.78:31002
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i
```
- Load the wordlist `/usr/share/seclists/Discovery/Web-Content/common.txt`, start Attack and found `2010.html`, get the flag:
```
GET /admin/2010.html HTTP/1.1
Host: 154.57.164.78:31002
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
DNT: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i

HTTP/1.1 200 OK
Date: Tue, 25 Aug 2026 13:42:26 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Wed, 14 Oct 2020 13:28:04 GMT
ETag: "3db-5b1a1804e0100-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Length: 987
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

</html>
<!DOCTYPE html>

<head>
    <title>HTB Academy</title>
    <style>
        *,
        html {
            margin: 0;
            padding: 0;
            border: 0;
        }

        html {
            width: 100%;
            height: 100%;
        }

        body {
            width: 100%;
            height: 100%;
            position: relative;
            background-color: rgb(42, 48, 66);
        }

        .center {
            width: 100%;
            height: 50%;
            margin: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-family: "Helvetica", Helvetica, sans-serif;
            text-align: center;
        }

        h1 {
            font-size: 144px;
        }

        p {
            font-size: 64px;
        }
    </style>
</head>

<body>
    <div class="center">
        <p>HTB{burp_1n7rud3r_fuzz3r!}</p>
    </div>
</body>

</html>
```

**Answer:** `HTB{burp_1n7rud3r_fuzz3r!}`

---

[Back to Module Index](./README.md)
