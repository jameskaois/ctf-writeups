# Krypton Level 2 → Level 3
(Updated: 12 August 2025)

## Credentials
- **Username:** `krypton2`
- **Password:** `ROTTEN`

## Connection
```bash
ssh krypton2@krypton.labs.overthewire.org -p 2231
```

## Hints & Commands Learned
- Decryption

## Steps to Solve
1. Step 1 - Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Call `cd /krypton/krypton2` and `cat krypton3` you will get a encoded one.
3. Step 3 - Do like the example to create a temp directory and `echo "AAABBB" >> test.txt` and run `/krypton/krypton2/encrypt ./test.txt` to test the encrypt.
4. Step 4 - `cat test.txt` and you will see something like `OOOPPP` so the logic is like `a -> O`, `b -> B`, ...
5. Step 5 - Run `cat /krypton/krypton2/krypton3 |tr 'A-Z' 'O-ZA-N'` to get the password based on the logic.
6. Step 6 - Take the password to the next level.

## Next Level Password
`CAESARISEASY`
