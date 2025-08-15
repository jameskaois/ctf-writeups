# Bandit Level 29 → Level 30
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit29`
- **Password:** `4pT1t5DENaYuqnqvadYs1oE4QLCdjmJ7`

## Connection
```bash
ssh bandit29@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- git

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Clone the repo like level 27, 28.
3. Step 3 - Run `cat README.md` -> cannot get the password.
4. Step 4 - Run `git branch -r` to see all the branches.
5. Step 5 - Run `git switch origin/dev` to switch to `dev` branch.
6. Step 6 - Run `Git reset --hard 4a754d10ab4e0246b06b76cb0a561257a3b6bf22` to reset to the commit of `dev` branch.
7. Step 7 - Run `cat README.md` and take the password to the next level.

## Next Level Password
`qp30ex3VLz5MDG1n91YowTv4Q8l7CDZL`