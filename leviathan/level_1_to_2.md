# Leviathan Level 1 → Level 2
(Updated: 11 August 2025)

## Credentials
- **Username:** `leviathan1`
- **Password:** `3QJ3TgzHDq`

## Connection
```bash
ssh leviathan1@leviathan.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- ltrace

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list files and you can see that we have a `check` binary files (which owned by `leviathan2`).
3. Step 3 - Call `./check` and you can see it need a password.
5. Step 5 - Try `ltrace check` and type something to the password and we get `strcmp("a\na", "sex")` really suspicious.
6. Step 6 - Call `./check` and type `sex` for the password and we pass it as a `leviathan2`.
7. Step 7 - Use `cat /etc/leviathan_pass/leviathan2` to get the password.
8. Step 8 - Take the password to the next level.

## Next Level Password
`NsN1HwFoyN`
