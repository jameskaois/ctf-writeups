# Bandit Level 7 → Level 8
(Updated: 29 July 2025)

## Credentials
- **Username:** `bandit7`
- **Password:** `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

## Connection
```bash
ssh bandit7@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- cat

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cat data.txt` to find the password.

***However, there are lots of random passwords and texts***

3. Step 3 – Add `| grep –color=always “millionth”` to the **cat** command => `cat data.txt | grep –color=always “millionth”` to get the correct password based on the requirement.
4. Step 4 - Take the password to the next level.

## Next Level Password
`dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`
