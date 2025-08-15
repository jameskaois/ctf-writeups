# Natas Level 5 → Level 6
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas5`
- **Password:** `0n35PkggAPm2zbEpOU802c0x0Msn1ToK`

## Connection
Level url: [http://natas5.natas.labs.overthewire.org/](http://natas5.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - You can access the code by doing the shortcut `Cmd + Shift + C` (for Mac) or `Ctrl + Shift + C` (for Windows)
2. Step 2 - You can see there is nothing else. The message says we are not logged in.
3. Step 3 - Check the `Network` section in `Developer Tools` you can see the `Response Headers` - `Set-Cookie: loggedin=0`
4. Step 4 - Change the cookie of `loggedin=1` in `Cookies` section of `Application` in Developer Tools.
5. Step 5 - Reload the page with the new cookie.
6. Step 6 - Take the password to the next level.

## Next Level Password
`0RoJwHdSKWFTYR5WuiAewauSuNaBXned`
