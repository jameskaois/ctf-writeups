# Bandit Level 20 → Level 21
(Updated: 31 July 2025)

## Credentials
- **Username:** `bandit20`
- **Password:** `0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

## Connection
```bash
ssh bandit20@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- echo
- nc
- setuid binary

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `echo -n "0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO" | nc -l -p 10000 &` to connect with port 10000 (you can change this to whatever you want).

***Note: Let the process run in the background (&. -n flag is to prevent newline characters)***

3. Step 3 - Use `./suconnect 10000` to connect to that port and you can get the password.
4. Step 4 - Take the password to the next level.

## Next Level Password
`EeoULMCra2q0dSkYj561DX7s1CpBuOBt`