# Bandit Level 28 → Level 29
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit28`
- **Password:** `Yz9IpL0sBcCeuG7m9uQFt8ZNpS4HZRcN`

## Connection
```bash
ssh bandit28@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- git

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Clone the repo like level 27.
3. Step 3 - Run `cat README.md` -> cannot get the password.
4. Step 4 - Run `git log` to see all the commits.
5. Step 5 - Use the commit `f257900db7c134cb5224c91013817e76d18457e0 (add missing data)` to get the password.
6. Step 6 - Run `git reset --hard f257900db7c134cb5224c91013817e76d18457e0` to reset to that commit.
7. Step 7 - Run `cat README.md` and take the password to the next level.

## Next Level Password
`4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`