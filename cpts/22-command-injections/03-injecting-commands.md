# Section 03: Injecting Commands

Module: 22. Command Injections

---

## Questions & Answers

### 1. Review the HTML source code of the page to find where the front-end input validation is happening. On which line number is it?

Context:
- View the page source, got:
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Host Checker</title>
  <link rel="stylesheet" href="./style.css">

</head>

<body>
  <div class="main">
    <h1>Host Checker</h1>

    <form method="post" action="">
      <label>Enter an IP Address</label>
      <input type="text" name="ip" placeholder="127.0.0.1" pattern="^((\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$">
      <button type="submit">Check</button>
    </form>

    <p>
    <pre>
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.050 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.050/0.050/0.050/0.000 ms
</pre>
    </p>

  </div>
  <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js'></script>
</body>

</html>
```

**Answer:** `17`

---

[Back to Module Index](./README.md)
