# Natas Level 16 → Level 17
(Updated: 14 August 2025)

## Credentials
- **Username:** `natas16`
- **Password:** `hPkjKYviLQctEW33QmuXL6eDVfMW4sGo`

## Connection
Level url: [http://natas16.natas.labs.overthewire.org/](http://natas16.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Click `View sourcecode` and we can see the `php` code:
```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&`\'"]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i \"$key\" dictionary.txt");
    }
}
?>
```
**Now it has restricted more characters that require us to brute-force in order to get the password**

2. Step 2 - Use my `python` code in order to the correct password: [Python code](../code/natas/level_16_to_17.py)
- Idea: `grep ^guess /etc/natas_webpass_natas17` to guess the password through each characters until get the result

3. Step 3 - Run the `python` code to brute-force `natas17` password:

![Screenshot image](../screenshots/natas_level_16_to_17.png)

4. Step 4 - Take the password to the next level.

## Next Level Password
`EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC`