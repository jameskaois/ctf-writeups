# Bandit Level 27 → Level 28
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit27`
- **Password:** `upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`

## Connection
```bash
ssh bandit27@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- git

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `mktemp -d` to create temp directory and `cd /tmp/tmp.XXX`.
3. Step 3 - Clone `git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo` and paste the password of current level.
4. Step 4 - Run `cat repo/README` to get the password.
5. Step 5 - Take the password to the next level.

## Next Level Password
`Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`