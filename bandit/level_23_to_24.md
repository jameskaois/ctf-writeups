# Bandit Level 23 → Level 24
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit23`
- **Password:** `0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

## Connection
```bash
ssh bandit23@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- cd
- cat
- vim
- cronjob

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `cd /etc/cron.d` to go to cronjobs directory.
3. Step 3 - Use `cat /usr/bin/cronjob_bandit23.sh` to see what it's running.
4. Step 4 - Use `vim /var/spool/bandit24/foo/foo.txt` to create a file that runs as `bandit24` user.
5. Step 5 - Add content for `foo.txt`: 
```
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/bandit24pass
```
6. Step 6 - Use `cat bandit24pass` to get the password.

## Next Level Password
`gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`