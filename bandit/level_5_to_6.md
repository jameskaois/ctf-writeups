# Bandit Level 5 → Level 6
(Updated: 29 July 2025)

## Credentials
- **Username:** `bandit5`
- **Password:** `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

## Connection
```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- find
- cd
- cat

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cd inhere` to get to the directory containing password file.
3. Step 3 - Use `find . -type f -size 1033c -not -executable` to get the file containing the password

***Explain: Find under this directory, type is file, size is 1033 bytes, not-executable***

4. Step 4 – Use `cat ./maybehere07/.file2` to get the password
5. Step 5 – Take the password to the next level.

## Next Level Password
`HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`
