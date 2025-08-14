# Natas Level 15 → Level 16
(Updated: 14 August 2025)

## Credentials
- **Username:** `natas15`
- **Password:** `SdqIqBsFcz3yotlNYErZSZwblkm0lrvx`

## Connection
Level url: [http://natas15.natas.labs.overthewire.org/](http://natas15.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Click `View sourcecode` and we can see the `php` code:
```php
<?php

/*
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
*/

if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas15', '<censored>');
    mysqli_select_db($link, 'natas15');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        echo "This user exists.<br>";
    } else {
        echo "This user doesn't exist.<br>";
    }
    } else {
        echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {
?>
```
2. Step 2 - You can see that we can just know **if the user exists** and cannot get the password directly. Therefore, we have to `brute-force` it.
3. Step 3 - Based on the idea, you can try add the `username: natas16" OR "1" = "1` we can get `This user exists.`.
4. Step 4 - Use the `python` code that I created to **brute-force** the password. [Python code](../code/natas/level_15_to_16.py)
- Running the code you will get the result:

![Screenshot image](../screenshots/natas_level_15_to_16.png)

5. Step 5 - Take the password to the next level.

## Next Level Password
`hPkjKYviLQctEW33QmuXL6eDVfMW4sGo`