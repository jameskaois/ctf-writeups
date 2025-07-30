# Bandit Level 11 → Level 12
(Updated: 30 July 2025)

## Credentials
- **Username:** `bandit11`
- **Password:** `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

## Connection
```bash
ssh bandit11@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- cat
- tr

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cat data.txt` and you can see the content is rotated.
3. Step 3 – Access [Rot13 Decoder](https://cryptii.com/pipes/rot13-decoder) to decode the content or use `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'` to get the password. 
4. Step 4 - Take the password to the next level.

## Next Level Password
`7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`
