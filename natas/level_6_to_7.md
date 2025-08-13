# Natas Level 6 → Level 7
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas6`
- **Password:** `0RoJwHdSKWFTYR5WuiAewauSuNaBXned`

## Connection
Level url: [http://natas6.natas.labs.overthewire.org/](http://natas6.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - You can access the code by doing the shortcut `Cmd + Shift + C` (for Mac) or `Ctrl + Shift + C` (for Windows)
2. Step 2 - You can see there is nothing else. And it needs us to find the secret for `Input Secret`. Click `View source code`
```php
<?

include "includes/secret.inc";

    if(array_key_exists("submit", $_POST)) {
        if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
    } else {
        print "Wrong secret";
    }
    }
?>
```
**There is a `include "includes/secret.inc";` so access to [http://natas6.natas.labs.overthewire.org/includes/secret.inc](http://natas6.natas.labs.overthewire.org/includes/secret.inc)**

3. Step 3 - Take the secret `$secret = "FOEIUWGHFEEUHOFUOIU";` to the input in the main page to get the password.
4. Step 4 - Take the password to the next level.

## Next Level Password
`bmg8SvU1LizuWjx3y7xkNERkHxGre0GS`
