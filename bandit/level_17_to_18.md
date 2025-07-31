# Bandit Level 17 → Level 18
(Updated: 31 July 2025)

## Credentials
- **Username:** `bandit17`
- **Password:** `EReVavePLFHtFlFsjn3hyzMlvSuSAcRD`

## Connection
```bash
ssh bandit17@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- diff

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `diff passwords.old passwords.new` to compare 2 files.
3. Step 3 - You will get `< ...` and `> ...` which means the `< ...` in `passwords.old` has changed to `> ...` in `passwords.new`
4. Step 4 - Take the password to the next level.

## Next Level Password
`x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO`