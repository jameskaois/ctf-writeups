# Leviathan Level 3 → Level 4
(Updated: 12 August 2025)

## Credentials
- **Username:** `leviathan3`
- **Password:** `f0n8h2iWLP`

## Connection
```bash
ssh leviathan3@leviathan.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- ltrace

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list files and you can see that we have a `level3` binary files (which owned by `leviathan4`).
3. Step 3 - Call `./level3` and it need you to have a passsword.
4. Step 4 - Like Level 2 call `ltrace ./level3` you can see a line `strcmp("asdf\n", "snlprintf\n")`
5. Step 5 - Now run `./level3` and type `snlprintf` as a password so you can get a shell of `leviathan4`.
6. Step 6 - Run `cat /etc/leviathan_pass/leviathan4` to get the password.
7. Step 7 - Take the password to the next level.

## Next Level Password
`WG1egElCvO`
