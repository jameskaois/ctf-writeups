# Natas Level 18 → Level 19
(Updated: 15 August 2025)

## Credentials
- **Username:** `natas18`
- **Password:** `6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ`

## Connection
Level url: [http://natas18.natas.labs.overthewire.org/](http://natas18.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Click `View sourcecode` and we can see the really long `php` code, but focus on these:
```php
$maxid = 640;

function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}
```
**We can see that the authentication based on the `PHPSESSID` to determine if it is the admin.**

2. Step 2 - We have to create a `python` code to make requests with different `PHPSESSID` to the `natas18` in order to get the admin account.
3. Step 3 - Use my `python` code in order to get the admin PHPSESSID: [Python code](../code/natas/level_18_to_19.py)

![Screenshot image](../screenshots/natas_level_18_to_19.png)

4. Step 4 - Use `PHPSESSID = 119` to the `cookie` of the browser to get the password.
5. Step 5 - Take the password to the next level.

## Next Level Password
`tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr`