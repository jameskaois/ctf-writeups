# Bandit Wargame Notes

## About
Bandit is the first OverTheWire wargame focused on teaching the basics of Linux commands, SSH, and file navigation.

- **Official URL:** [https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)
- **Difficulty:** Beginner -> Intermediate.
- **Goal:** Get comfortable with the Linux shell and essential commands.

## Progress
| Level  | Notes |
|--------|--------|
| 0 → 1  | [level_0_to_1.md](./level_0_to_1.md)   |
| 1 → 2  | [level_1_to_2.md](./level_1_to_2.md)   |
| 2 → 3  | [level_2_to_3.md](./level_2_to_3.md)   |
| 3 → 4  | [level_3_to_4.md](./level_3_to_4.md)   |
| 4 → 5  | [level_4_to_5.md](./level_4_to_5.md)   |
| 5 → 6  | [level_5_to_6.md](./level_5_to_6.md)   |
| 6 → 7  | [level_6_to_7.md](./level_6_to_7.md)   |
| 7 → 8  | [level_7_to_8.md](./level_7_to_8.md)   |
| 8 → 9  | [level_8_to_9.md](./level_8_to_9.md)   |
| 9 → 10 | [level_9_to_10.md](./level_9_to_10.md) |
| 10 → 11| [level_10_to_11.md](./level_10_to_11.md) |
| 11 → 12| [level_11_to_12.md](./level_11_to_12.md) |
| 12 → 13| [level_12_to_13.md](./level_12_to_13.md) |
| 13 → 14| [level_13_to_14.md](./level_13_to_14.md) |
| 14 → 15| [level_14_to_15.md](./level_14_to_15.md) |
| 15 → 16| [level_15_to_16.md](./level_15_to_16.md) |
| 16 → 17| [level_16_to_17.md](./level_16_to_17.md) |
| 17 → 18| [level_17_to_18.md](./level_17_to_18.md) |
| 18 → 19| [level_18_to_19.md](./level_18_to_19.md) |
| 19 → 20| [level_19_to_20.md](./level_19_to_20.md) |
| 20 → 21| [level_20_to_21.md](./level_20_to_21.md) |
| 21 → 22| [level_21_to_22.md](./level_21_to_22.md) |
| 22 → 23| [level_22_to_23.md](./level_22_to_23.md) |
| 23 → 24| [level_23_to_24.md](./level_23_to_24.md) |
| 24 → 25| [level_24_to_25.md](./level_24_to_25.md) |
| 25 → 26| [level_25_to_26.md](./level_25_to_26.md) |
| 26 → 27| [level_26_to_27.md](./level_26_to_27.md) |
| 27 → 28| [level_27_to_28.md](./level_27_to_28.md) |
| 28 → 29| [level_28_to_29.md](./level_28_to_29.md) |
| 29 → 30| [level_29_to_30.md](./level_29_to_30.md) |
| 30 → 31| [level_30_to_31.md](./level_30_to_31.md) |
| 31 → 32| [level_31_to_32.md](./level_31_to_32.md) |
| 32 → 33| [level_32_to_33.md](./level_32_to_33.md) |
| 33 → 34| [level_33_to_34.md](./level_33_to_34.md) |



## Tools Learned
1. Navigating the File System
- `pwd` – Show current working directory
- `ls`, `ls -la` – List files (including hidden ones)
- `cd` – Change directory
- `file <filename>` – Identify file type

2. Viewing Files
- `cat` – View file content
- `less`, `more` – Scroll through file content
- `head`, `tail` – Show first/last lines of a file

3. Reading Special & Hidden Files
- Handling spaces in filenames:
```
cat "file name with spaces"
```
- Reading hidden files (.filename)
- Reading files with special characters using escape \ or quotes

4. Permissions & Ownership
chmod – Change file permissions
- `chown` – Change file owner
- `ls -l` – Check permissions
- Understanding permission bits (rwxr-xr--)

5. Searching & Filtering
- `grep <pattern> <file>` – Search for text in files
- `find` – Locate files by name, type, or permissions
- `grep -R <pattern> .` – Recursive search in all files

6. Working with Archives & Compression
- `tar -xf file.tar` – Extract tar files
- `gzip -d file.gz` – Decompress .gz
- `bzip2 -d file.bz2` – Decompress .bz2
- `xz -d file.xz` – Decompress .xz

7. Networking Basics
- `nc` (netcat) – Connect to ports or listen
- `telnet` – Connect to a server
- `ssh user@host -p <port>` – Connect to SSH
- Using redirection to send/receive data from network connections

8. File Redirection & Piping
- `>` – Redirect output to a file (overwrite)
- `>>` – Append output to a file
- `<` – Redirect input from a file
- `|` – Pipe output to another command

Example:
```
grep "password" data.txt | sort | uniq
```

9. Encoding & Decoding
- `base64` – Encode/decode Base64 data
- `xxd` – View/edit files in hex
- `strings` – Extract printable strings from binary files

10. Working with Processes
- `ps` – List running processes
- `top`, `htop` – Monitor system usage
- `kill` – End processes

11. Scripting & Automation
- Running shell scripts:
```
./script.sh
bash script.sh
```
- Using loops, variables, and command substitution:
```
for i in {1..10}; do echo $i; done
```

12. Privilege Escalation Basics
- Understanding setuid files
- Knowing how to switch users:
```
su <username>
```
- Using `sudo` for commands requiring root

## Disclaimer
These notes are for **educational purposes only**. You can depend on it to play OverTheWire Bandit games.