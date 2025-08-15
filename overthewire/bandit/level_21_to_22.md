# Bandit Level 21 → Level 22
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit21`
- **Password:** `EeoULMCra2q0dSkYj561DX7s1CpBuOBt`

## Connection
```bash
ssh bandit21@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- cd
- cat
- cronjob

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cd /etc/cron.d` to go to cronjobs directory.
3. Step 3 - Use `cat cronjob_bandit22` (* * * * * means it is running).
4. Step 4 - Use `cat /usr/bin/cronjob_bandit22.sh` to see what it's running.
5. Step 5 - Use `cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv` to get the password for the next level.
6. Step 6 - Take the password to the next level.

## Next Level Password
`tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`