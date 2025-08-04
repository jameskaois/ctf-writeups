# Bandit Level 22 → Level 23
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit22`
- **Password:** `tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

## Connection
```bash
ssh bandit22@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- cd
- cat
- cronjob

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cd /etc/cron.d` to go to cronjobs directory.
3. Step 3 - Use `cat /etc/cron.d/cronjob_bandit23` (* * * * * means it is running).
4. Step 4 - Use `cat /usr/bin/cronjob_bandit23.sh` to see what it's running.
5. Step 5 - Use `cat/tmp/$(echo I am user bandit23 | md5sum | cut -d ' ' -f 1)` to get the password for the next level.
6. Step 6 - Take the password to the next level.

## Next Level Password
`0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`