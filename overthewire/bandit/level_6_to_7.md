# Bandit Level 6 → Level 7
(Updated: 29 July 2025)

## Credentials
- **Username:** `bandit6`
- **Password:** `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

## Connection
```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- find
- cat

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `find / -type f -user bandit7 -group bandit6 -size 33c` to find the files matching the requirements

***However, there are lots of files with Permission Denied***

3. Step 3 – Add `2>/dev/null` to the **find** command => `find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null` to get the correct file
4. Step 4 – Use `cat /var/lib/dpkg/info/bandit7.password` to get the password
5. Step 5 - Take the password to the next level.

## Next Level Password
`morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`
