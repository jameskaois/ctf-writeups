# Natas Level 8 → Level 9
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas8`
- **Password:** `xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q`

## Connection
Level url: [http://natas8.natas.labs.overthewire.org/](http://natas8.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - You can access the code by doing the shortcut `Cmd + Shift + C` (for Mac) or `Ctrl + Shift + C` (for Windows)
2. Step 2 - You can see there is a `Input secret` so we have to find the secret, click `View sourcecode`, you'll find a PHP code:
```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
    print "Access granted. The password for natas9 is <censored>";
    } else {
    print "Wrong secret";
    }
}
?>
```
**Look at the code we have to decode the `secret` to its original to submit and get the password.**

3. Step 3 - Decode the secret using the terminal:
- Decode `bin2hex`:
```bash
echo "3d3d516343746d4d6d6c315669563362" | xxd -r -p
> ==QcCtmMml1ViV3b
```
- Decode `strrev`:
```bash
echo "==QcCtmMml1ViV3b" | rev
> b3ViV1lmMmtCcQ==
```
- Decode `base64_encode`:
```bash
echo "b3ViV1lmMmtCcQ==" | base64 -d
> oubWYf2kBq
```
**=> The secret is: `oubWYf2kBq`**

4. Step 4 - Submit the secret to the `Input secret` to get the password.
5. Step 5 - Take the password to the next level.

## Next Level Password
`ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t`
