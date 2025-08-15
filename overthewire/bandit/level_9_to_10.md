# Bandit Level 9 → Level 10
(Updated: 30 July 2025)

## Credentials
- **Username:** `bandit9`
- **Password:** `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

## Connection
```bash
ssh bandit9@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- grep
- strings

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cat data.txt` to find the password.

***However, there are lots of random passwords and texts which are non-human-readable.***

3. Step 3 – Use `strings -a data.txt` to get format of text. 
4. Step 4 – Add `grep` => `strings -a data.txt | grep "==="` to get the correct password based on the requirement. 
5. Step 5 - Take the password to the next level.

## Next Level Password
`FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`
