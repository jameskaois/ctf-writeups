# HTTP in Detail - TryHackMe 

Learn about how you request content from a web server using the HTTP protocol

## Overview
- **Room URL:** [https://tryhackme.com/room/httpindetail](https://tryhackme.com/room/httpindetail)
- **Difficulty:** Easy
- **Time to complete:** 30

## Walkthrough
### 1. What is HTTP(S)?
- What does HTTP stand for?<br />

**=> Answer: `HyperText Transfer Protocol`**

- <p>What does the S in HTTPS stand for?<br /></p>

**=> Answer: `Secure`**

- <p><span style="">On the mock webpage on the right there is an issue, once you've found it, click on it. What is the challenge flag?</span><br /></p>
- Click on the lock on the URL

**=> Answer: `THM{INVALID_HTTP_CERT}`**

### 2. Requests And Responses
- What HTTP protocol is being used in the above example?<br />
```
HTTP/1.1 200 OK

Server: nginx/1.15.8
Date: Fri, 09 Apr 2021 13:34:03 GMT
Content-Type: text/html
Content-Length: 98


<html>
<head>
    <title>TryHackMe</title>
</head>
<body>
    Welcome To TryHackMe.com
</body>
</html>
```
**=> Answer: `HTTP/1.1`**

- <p>What response header tells the browser how much data to expect?<br /></p>

**=> Answer: `Content-Length`**

### 3. HTTP Methods
- What method would be used to create a new user account?<br />

**=> Answer: `POST`**

- <p>What method would be used to update your email address?<br /></p>

**=> Answer: `PUT`**

- <p>What method would be used to remove a picture you've uploaded to your account?<br /></p>

**=> Answer: `DELETE`**

- <p>What method would be used to view a news article?<br /></p>

**=> Answer: `GET`**

### 4. HTTP Status Codes
- <p>What response code might you receive if you've created a new user or blog post article?<br /></p>

**=> Answer: `201`**

- <p>What response code might you receive if you've tried to access a page that doesn't exist?</p>

**=> Answer: `404`**

- <p>What response code might you receive if the web server cannot access its database and the application crashes?<br /></p>

**=> Answer: `503`**

- <p>What response code might you receive if you try to edit your profile without logging in first?<br /></p>

**=> Answer: `401`**

### 5. Headers
- What header tells the web server what browser is being used?<br />

**=> Answer: `User-Agent`**

- <p>What header tells the browser what type of data is being returned?<br /></p>

**=> Answer: `Content-Type`**

- <p>What header tells the web server which website is being requested?<br /></p>

**=> Answer: `Host`**

### 6. Cookies
- Which header is used to save cookies to your computer?<br />

**=> Answer: `Set-Cookie`**

### 7. Making Requests
- <p>Make a <strong>GET</strong> request to <strong>/room </strong>page</p>
```bash
GET /room HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 0
```
**=> Answer: `THM{YOU'RE_IN_THE_ROOM}`**

- <p>Make a <strong>GET </strong>request to <strong>/blog</strong> page and set the <strong>id </strong>parameter to <strong>1</strong><br />Note: Use the gear button on the right to manage URI parameters</p>
```bash
GET /blog?id=1 HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 0
```
**=> Answer: `THM{YOU_FOUND_THE_BLOG}`**

- <p>Make a <strong>DELETE </strong>request to <strong>/user/1 </strong>page</p>
```bash
DELETE /user/1 HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 0
```
**=> Answer: `THM{USER_IS_DELETED}`**

- <p>Make a <strong>PUT</strong> request to <strong>/user/2</strong> page with the <strong>username </strong>parameter set to <strong>admin<br /></strong>Note: Use the gear button on the right to manage body parameters</p>
```bash
PUT /user/2 HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 14
Content-Type: application/x-www-form-urlencoded

username=admin
```
**=> Answer: `THM{USER_HAS_UPDATED}`**

- <p>Make a <strong>POST </strong>request to <strong>/login </strong>page with the <strong>username </strong>of <strong>thm </strong>and a <strong>password </strong>of <strong>letmein<br /></strong>Note: Use the gear button on the right to manage body parameters</p>
```bash
POST /login HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Content-Length: 29
Content-Type: application/x-www-form-urlencoded

username=thm&password=letmein
```
**=> Answer: `THM{HTTP_REQUEST_MASTER}`**

