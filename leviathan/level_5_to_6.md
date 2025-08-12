# Leviathan Level 5 → Level 6
(Updated: 12 August 2025)

## Credentials
- **Username:** `leviathan5`
- **Password:** `0dyxT7F4QD`

## Connection
```bash
ssh leviathan5@leviathan.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- ln -s

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list files and you can see that we have a `leviathan5` binary file (which owned by `leviathan6`).
3. Step 3 - Run `./leviathan5` you get a message `Cannot find /tmp/file.log`.
4. Step 4 - We can test `touch /tmp/file.log` and run again `./leviathan5` we don't get anything
5. Step 5 - Run `ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log` to link the `file.log` to the password
6. Step 6 - Run again `./leviathan5` to get the password.
7. Step 7 - Take the password to the next level.

## Next Level Password
`szo7HDB88w`
