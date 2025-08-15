# Bandit Level 8 → Level 9
(Updated: 30 July 2025)

## Credentials
- **Username:** `bandit8`
- **Password:** `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

## Connection
```bash
ssh bandit8@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- sort
- uniq

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cat data.txt` to find the password.

***However, there are lots of random passwords and texts in order to find password only exists once.***

3. Step 3 – Use `sort` and `uniq` => `sort data.txt | uniq -u` to get the correct password based on the requirement.
4. Step 4 - Take the password to the next level.

## Next Level Password
`4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`
