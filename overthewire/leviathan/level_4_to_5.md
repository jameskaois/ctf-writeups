# Leviathan Level 4 → Level 5
(Updated: 12 August 2025)

## Credentials
- **Username:** `leviathan4`
- **Password:** `WG1egElCvO`

## Connection
```bash
ssh leviathan4@leviathan.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- ltrace
- Binary reader

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list files and you can see that we have a `.trash` folder.
3. Step 3 - `cd .trash` then run `ls -la` and you can see a `bin` binary file.
4. Step 4 - Run `./bin` and you get back a binary string.
5. Step 5 - Run `ltrace ./bin` you can see it opens the `leviathan5` password file so we can sure that the `./bin` return the password for the next level.
6. Step 6 - Open [Binary Reader](https://www.rapidtables.com/convert/number/binary-to-ascii.html) and paste the binary **without space**.
7. Step 7 - Take the password to the next level.

## Next Level Password
`0dyxT7F4QD`
