# Natas Level 23 → Level 24
(Updated: 16 August 2025)

## Credentials
- **Username:** `natas23`
- **Password:** `dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs`

## Connection
Level url: [http://natas23.natas.labs.overthewire.org/](http://natas23.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Click `View sourcecode` in order to see the source:
```php
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
```

2. Step 2 - It requires us to have `iloveyou` also the `passwd > 10` this is a `php` logic.
- A string is bigger than `10` when it has `11`, `12` at the front

3. Step 3 - Submit `11iloveyou` in the input to get the password.
4. Step 4 - Take the password to the next level.

## Next Level Password
`MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd`