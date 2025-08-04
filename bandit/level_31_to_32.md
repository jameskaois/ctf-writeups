# Bandit Level 31 → Level 32
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit31`
- **Password:** `fb5S2xb7bRyFmAvQYQGEqsbhVyJqhnDy`

## Connection
```bash
ssh bandit31@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- git

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Clone the repo like level 27, 28, 29, 30.
3. Step 3 - Run `cat README.md` -> cannot get the passwor. It require us to push a `key.txt` file with content “May I come in?”.
4. Step 4 - Run `echo “May I come in?” >> key.txt` to create the required file.
5. Step 5 - Check the `.gitignore` remove line *.txt with `vim` or `nano`.
6. Step 6 - Run `git add .` -> `git commit -m “May I come in?”` `git push`.
7. Step 7 - Get the password via the message.

## Next Level Password
`3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`