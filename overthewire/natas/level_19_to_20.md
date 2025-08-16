# Natas Level 19 → Level 20
(Updated: 16 August 2025)

## Credentials
- **Username:** `natas19`
- **Password:** `tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr`

## Connection
Level url: [http://natas19.natas.labs.overthewire.org/](http://natas19.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - Try login with account `Username: test`, `Password: test`.
2. Step 2 - Open `Dev Tools -> Application -> Cookies` you can see that the browser has cookie: `PHPSESSID: 37342d74657374`.
3. Step 3 - Use [CyberChef](https://gchq.github.io/CyberChef) to decode that text `From Hex`. You get something like this `74-test`.
4. Step 4 - Now try login with account `Username: admin`, `Password: something`. Decode the text `From Hex`, get `344-admin`

**We can see that the ID has format `id-username` so now we can try different `ids` with `admin`**

5. Step 5 - Use the my `python` code to brute-force the `ids` and get the correct `hex_data`. [Python code](../code/natas/level_19_to_20.py)

![Screenshot image](../screenshots/natas_level_19_to_20.png)

6. Step 6 - Take the correct admin `hex_data` and change the cookie value in browser in order to get the password.
7. Step 7 - Take the password to the next level.

## Next Level Password
`p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw`