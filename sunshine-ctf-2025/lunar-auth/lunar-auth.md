# Lunar Auth — SunShine CTF 2025

> **Room / Challenge:** Lunar Auth (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** SunShine CTF 2025
- **Challenge:** Lunar Auth (web)
- **Target / URL:** `https://comet.sunshinectf.games`
- **Difficulty:** `Easy`
- **Points:** `10`
- **Date:** `30-09-2025`

---

## Goal

We have to get the flag by bypass the admin authentication.

## My Solution

This is the home page, there aren't any useful information.

![Guide image](../screenshots/lunar-auth-1.png)

Try access `https://comet.sunshinectf.games/robots.txt`, the content is:

```
# tired of these annoying search engine bots scraping the admin panel page logins:

Disallow: /admin
```

This is the content of `/admin`, there is a login form, we have to bypass this to get access as admin.

![Guide image](../screenshots/lunar-auth-2.png)

Click **View page source** this page, we can easily see a `<script>` tag

![Guide image](../screenshots/lunar-auth-3.png)

```html
<script>
  /*
    To reduce load on our servers from the recent space DDOS-ers we have lowered login attempts by using Base64 encoded encryption
    ("encryption" 💀) on the client side.
    
    TODO: implement proper encryption.
    */
  const real_username = atob("YWxpbXVoYW1tYWRzZWN1cmVk");
  const real_passwd = atob("UzNjdXI0X1BAJCR3MFJEIQ==");

  document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    function handleSubmit(evt) {
      evt.preventDefault();

      const username = form.elements["username"].value;
      const password = form.elements["password"].value;

      if (username === real_username && password === real_passwd) {
        // remove this handler and allow form submission
        form.removeEventListener("submit", handleSubmit);
        form.submit();
      } else {
        alert("[ Invalid credentials ]");
      }
    }

    form.addEventListener("submit", handleSubmit);
  });
</script>
```

The username and password is defined like this:

```javascript
const real_username = atob("YWxpbXVoYW1tYWRzZWN1cmVk");
const real_passwd = atob("UzNjdXI0X1BAJCR3MFJEIQ==");
```

We can retrieve these two variables through `Console` tab of `Dev Tools`.

![Guide image](../screenshots/lunar-auth-4.png)

This is a known problem of **Global Variable** in Javascript, it should be in a function and cannot be access by users.

![Guide image](../screenshots/lunar-auth-5.png)

Flag is: `sun{cl1ent_s1d3_auth_1s_N3V3R_a_g00d_1d3A_983765367890393232}`
