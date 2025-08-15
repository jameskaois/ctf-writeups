# Natas Level 17 → Level 18
(Updated: 14 August 2025)

## Credentials
- **Username:** `natas17`
- **Password:** `EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC`

## Connection
Level url: [http://natas17.natas.labs.overthewire.org/](http://natas17.natas.labs.overthewire.org/)

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
    $link = mysqli_connect('localhost', 'natas17', '<censored>');
    mysqli_select_db($link, 'natas17');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    $res = mysqli_query($link, $query);
    if($res) {
    if(mysqli_num_rows($res) > 0) {
        //echo "This user exists.<br>";
    } else {
        //echo "This user doesn't exist.<br>";
    }
    } else {
        //echo "Error in query.<br>";
    }

    mysqli_close($link);
} else {}
?>
```
**Now it doesn't have any messages for us to know if we get the correct character.**

2. Step 2 - Use my `python` code in order to the correct password: [Python code](../code/natas/level_17_to_18.py).
- Idea: `sleep(5)` when find the correct character and check `r.elapsed.total_seconds() > 5` in order to get that character.

3. Step 3 - Run the `python` code to brute-force `natas18` password:

![Screenshot image](../screenshots/natas_level_17_to_18.png)

4. Step 4 - Take the password to the next level.

## Next Level Password
`6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ`