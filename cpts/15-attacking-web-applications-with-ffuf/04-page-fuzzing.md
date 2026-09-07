# Section 04: Page Fuzzing

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Try to use what you learned in this section to fuzz the '/blog' directory and find all pages. One of them should contain a flag. What is the flag?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt:FUZZ -u http://154.57.164.82:30474/blog/FUZZ.php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://154.57.164.82:30474/blog/FUZZ.php
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

                        [Status: 403, Size: 281, Words: 20, Lines: 10, Duration: 167ms]
# directory-list-2.3-small.txt [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
# on at least 3 different hosts [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
index                   [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
#                       [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
# Copyright 2007 James Fisher [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
# or send a letter to Creative Commons, 171 Second Street, [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 168ms]
# This work is licensed under the Creative Commons [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 1478ms]
#                       [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 2482ms]
# license, visit http://creativecommons.org/licenses/by-sa/3.0/ [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 3493ms]
home                    [Status: 200, Size: 1046, Words: 438, Lines: 58, Duration: 3496ms]
#                       [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4500ms]
#                       [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4500ms]
# Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4500ms]
# Priority-ordered case-sensitive list, where entries were found [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 4504ms]

┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ curl http://154.57.164.82:30474/blog/home.php
<html>
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
            background-color: orange;
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
        <h1>Admin panel moved to academy.htb</h1>
        <br>
        <p>HTB{bru73_f0r_c0mm0n_p455w0rd5}</p>
    </div>
</body>

</html>
```

**Answer:** `HTB{bru73_f0r_c0mm0n_p455w0rd5}`

---

[Back to Module Index](./README.md)
