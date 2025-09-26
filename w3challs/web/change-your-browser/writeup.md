# Change Your Browser - Web CTF Challenge

> **Room / Challenge:** Change Your Browser (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** W3Challs
- **Challenge:** Change Your Browser (web)
- **Target / URL:** `https://w3challs.com/challenges/web/change_your_browser`
- **Difficulty:** `Baby`
- **Points:** `1`
- **Date:** `26-09-2025`

---

## My Solution

1. Let's take a look at the main page of it.

![Guide image](./1.png)

2. We can see that this challenge requires us to change our browser request to `W3Challs_browser`.

3. We can achieve this really easy via simple `curl` command:

```bash
curl -A "W3Challs_browser" "https://change-browser.hax.w3challs.com/"
```

Result:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Change your browser</title>
    <meta name="owner" content="W3Challs" />
    <meta name="publisher" content="w3challs" />
    <meta name="copyright" content="w3challs" />
    <meta name="robots" content="noindex,nofollow" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  </head>
  <body>
    <p align="center">
      Congratz! The flag to solve this challenge is
      "W3C{now_that_we_have_the_right_browser_lets_get_the_party_started}"
    </p>
  </body>
</html>
```

4. The flag is: `W3C{now_that_we_have_the_right_browser_lets_get_the_party_started}`
