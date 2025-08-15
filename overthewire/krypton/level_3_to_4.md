# Krypton Level 3 → Level 4
(Updated: 12 August 2025)

## Credentials
- **Username:** `krypton3`
- **Password:** `CAESARISEASY`

## Connection
```bash
ssh krypton3@krypton.labs.overthewire.org -p 2231
```

## Hints & Commands Learned
- Decryption

## Steps to Solve
1. Step 1 - Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Call `cd /krypton/krypton3` and `cat HINT1 HINT2` you will get the hints.
3. Step 3 - Base on the README and hints we have to know the frequency of letters so call:
```
cat found1 found2 found3 | tr '[:upper:]' '[:lower:]' | grep -o . | sort | uniq -c | sort -nr
```
In order to get the frequency of words in 3 found files.
4. Step 4 - Call `cat found1 found2 found3 | tr -d '\n' | fold -w1 | sort | uniq -c | sort -nr | awk '{printf $2}'` to get the list of it without space and counts. Also, visit [Wikipedia](https://en.wikipedia.org/wiki/Letter_frequency) to get the list of most frequent letters from most to least.
5. Step 5 - Run `cat /krypton/krypton3/krypton4 | tr 'SQJUBNGCDZVWMYTXKELAFIORHP' 'ETAONRISHDLFCMUGYPWBVKJXZQ'` to get the password based on the logic.

***Note: If the password doesn't work in the next level you can try this instead `cat /krypton/krypton3/krypton4 | tr 'SQJUBNGCDZVWMYTXKELAFIORHP' 'EATSORNIHCLDUPYFWGMBKVXQJZ'`***

6. Step 6 - Take the password to the next level.

## Next Level Password
`BRUTE`
