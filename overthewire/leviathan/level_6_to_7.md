# Leviathan Level 6 → Level 7
(Updated: 12 August 2025)

## Credentials
- **Username:** `leviathan6`
- **Password:** `szo7HDB88w`

## Connection
```bash
ssh leviathan6@leviathan.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- Brute-force

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list files and you can see that we have a `leviathan6` binary file (which owned by `leviathan7`).
3. Step 3 - Run `./leviathan6` and it need us to type a correct 4-digit code, so we have to brute-force it.
4. Step 4 - `mktemp -d` to create a temp directory, `vim brute-force.sh` with the content:
```
for value in {1000..9999}
do
	~/leviathan6 $value
done
```
5. Step 5 - You will have access to the `leviathan7` and run `cat /etc/leviathan_pass/leviathan7` to get the password.
6. Step 6 - Take the password to the next level.

## Next Level Password
`qEs5Io5yM8`
