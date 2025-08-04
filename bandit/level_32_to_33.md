# Bandit Level 32 → Level 33
(Updated: 04 August 2025)

## Credentials
- **Username:** `bandit32`
- **Password:** `3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`

## Connection
```bash
ssh bandit32@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- whoami
- cat

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.

***Note: Stuck in uppercase shell***

2. Step 2 - Run `$0` to create a new shell.
3. Step 3 - Use `whoami` and you can see that we're currently `bandit33` user.
4. Step 4 - Run `cat /etc/bandit_pass/bandit33` to get the password for the next level.
5. Step 5 - Take the password to the next level.

## Next Level Password
`tQdtbs5D5i2vJwkO8mEyYEyTL8izoeJ0`