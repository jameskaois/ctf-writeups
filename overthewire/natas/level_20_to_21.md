# Natas Level 20 → Level 21
(Updated: 16 August 2025)

## Credentials
- **Username:** `natas20`
- **Password:** `p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw`

## Connection
Level url: [http://natas20.natas.labs.overthewire.org/](http://natas20.natas.labs.overthewire.org/)

## Steps to Solve
1. Step 1 - In this level we cannot do brute-force `PHPSESSID` because it uses random keys.
2. Step 2 - Investigate the source code we can see that the most thing we have to do is set the `admin = 1`.
3. Step 3 - Add `admin%0Aadmin 1` to `Your name` input and submit to get the password.
4. Step 4 - Take the password to the next level.

## Next Level Password
`BPhv63cKE1lkQl04cE5CuFTzXe15NfiH`