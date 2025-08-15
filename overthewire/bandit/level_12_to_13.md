# Bandit Level 12 → Level 13
(Updated: 30 July 2025)

## Credentials
- **Username:** `bandit12`
- **Password:** `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`

## Connection
```bash
ssh bandit12@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- xxd
- tar
- gzip
- bzip2
- cat
- file

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cat data.txt` and you can see the content is encoded.
3. Step 3 – Use `xxd -r <filename>` to decode the hexdump.
4. Step 4 - Based on the filetype decode it until get the password.
    - Tar achieve: `tar xf <filename>`
    - Gzip compressed data: `gzip -d <filename>`
    - Bzip2 compressed data: `bzip2 -d <filename>`

5. Step 5 - Take the password to the next level.

## Next Level Password
`FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn`
