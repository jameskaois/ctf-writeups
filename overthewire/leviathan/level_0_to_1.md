# Leviathan Level 0 → Level 1
(Updated: 11 August 2025)

## Credentials
- **Username:** `leviathan0`
- **Password:** `leviathan0`

## Connection
```bash
ssh leviathan0@leviathan.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- ls -la
- cat
- grep

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list file and you can see that we have a directory `.backup`.
3. Step 3 – Go to the `.backup` directory we can see just a `bookmarks.html`.

***However, this is a really large file, so we can use `grep` to find something we want.***

4. Step 4 - Use `cat bookmarks.html | grep "leviathan"` and we can see a line `the password for leviathan1 is xxxx`.
5. Step 5 - Take the password to the next level.

## Next Level Password
`3QJ3TgzHDq`
