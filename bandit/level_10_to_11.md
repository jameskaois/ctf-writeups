# Bandit Level 10 → Level 11
(Updated: 30 July 2025)

## Credentials
- **Username:** `bandit10`
- **Password:** `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

## Connection
```bash
ssh bandit10@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- base64

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cat data.txt` and you can see the content is encoded.
3. Step 3 – Use `base64 -d data.txt` to decode the data. 
4. Step 4 - Take the password to the next level.

## Next Level Password
`dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`
