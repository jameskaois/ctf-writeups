# Linux Modules – TryHackMe

## Overview
- **Room URL:** [https://tryhackme.com/room/linuxmodules](https://tryhackme.com/room/linuxmodules)  
- **Difficulty:** Easy
- **Category:** Linux

## Learning Objectives
- Key skills learned in this room:  
  - Common commands to use in Linux: du, grep, tr, ...  
  - Linux based thinking

## Walkthrough (Hints & Notes)
### 1. Let's Introduce
*No hints needed.*

### 2. du
*No hints needed.*

### 3. Grep, Egrep, Fgrep
- What user did you find in that file?

```bash
grep -i "user" grep_1611752025618.txt

uxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7FuSeR:bobthebuilder6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6fuxx6x84XZw5VsQTHzVMN7F6f
```

**=> Answer: `bobthebuilder`**

- What is the password of that user?
```bash
grep "sen" grep_1611752025618.txt

qEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTthispAsSwOrDistoosensitive:'LinuxIsGawd'XqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTXqEqbDkrSFzmhRdDSQNWqaMTX
```

**=> Answer: `LinuxIsGawd`**

- Can you find the comment that user just left?
```bash
grep "comment" grep_1611752025618.txt

8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2comment:'fs0ciety'u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM8gmdNXTN4gn2u73SuX5cewcM
```

**=> Answer: `fs0ciety`**

### 4. Did someone said STROPS?
*No hints needed.*

### 5. tr
- Run tr --help command and tell how will you select any digit character in the string?

**=> Answer: `:digit:`**

- What sequence is equivalent to [a-zA-Z] set?

**=> Answer: `:alpha:`**

- What sequence is equivalent to selecting hexadecimal characters?

**=> Answer: `:xdigit:`**

### 6. awk
- Download the above given file awk.txt, and use the awk command to print the following output:
```
ippsec:34024
john:50024
thecybermentor:25923
liveoverflow:45345
nahamsec:12365
stok:1234
```

**=> Answer: `awk 'BEGIN{OFS=":"} {print $1, $4}' awk.txt`**

- How will you make the output as following (there can be multiple; answer it using the above specified variables in BEGIN pattern):
```
ippsec, john, thecybermentor, liveoverflow, nahamsec, stok,
```

**=> Answer: `awk 'BEGIN{ORS=","} {print $1}' awk.txt`**

### 7. sed
- How would you substitute every 3rd occurrence of the word 'hack' to 'back' on every line inside the file file.txt?

**=> Answer: `sed 's/hack/back/3g' file.txt`**

- How will you do the same operation only on 3rd and 4th line in file.txt?

**=> Answer: `sed '3,4 s/hack/back/3g' file.txt`**

- Download the given file, and try formatting the trailing spaces in sed1.txt with a colon(:).

**=> Answer: `sed 's/  */:/g' sed1.txt`**

- View the  sed2 file in the directory. Try putting all alphabetical values together, to get the answer for this question.

**=> Answer: `CONGRATULATIONS YOU MADE IT THROUGH THIS SMALL LITTLE CHALLENGE`**

- What pattern did you use to reach that answer string?

**=> Answer: `'s/[[:digit:]]//g'`**

- What did she sed?(In double quotes)

**=> Answer: `"That's What"`**

### 8. xargs
- You're working in a team and your team leader sent you a list of files that needs to be created ASAP within current directory so that he can fake the synopsis report (that needs to be submitted within a minute or 2) to the invigilator and change the permissions to read-only to only you(Numberic representation). You can find the files list in the "one" folder.

- Use the following flags in ASCII order:
    - Verbose
    - Take argument as "files"

**=> Answer: `cat file | xargs -I files -t sh -c “touch files; chmod 400 files”`**

- Your friend trying to run multiple commands in one line, and wanting to create a short version of rockyou.txt, messed up by creating files instead of redirecting the output into "shortrockyou". Now he messed up his home directory by creating a ton of files. He deleted rockyou wordlist in that one liner and can't seem to download it and do all that long process again.

- He now seeks help from you, to create the wordlist and remove those extra files in his directory. You being a pro in linux, show him how it's done in one liner way.

- Use the following flags in ASCII order:

    - Take argument as "word"
    - Verbose
    - Max number of arguments should be 1 in for each file
- You can find the files for this task in two folder.

**=> Answer: `ls | xargs -I word -n 1 -t sh -c ‘echo word >> shortrockyou; rm word’`**

- Which flag to use to specify max number of arguments in one line.

**=> Answer: `-n`**

- How will you escape command line flags to positional arguments?

**=> Answer: `--`**

### 9. sort and uniq
- Download the file given for this task, find the uniq items after sorting the file. What is the 2271st word in the output.
```bash
sort test_1611747033664.test | uniq | sed -n '2270p'
```

**=> Answer: `lollol`**

- What was the index of term 'michele'
```bash
sort test_1611747033664.test| grep -n "michele"
```

**=> Answer: `2550`**

### 10. cURL
- Which flag allows you to limit the download/upload rate of a file?

**=> Answer: `--limit-rate`**

- How will you curl the webpage of https://tryhackme.com/ specifying user-agent as 'juzztesting'

**=> Answer: `curl -A "juzztesting" https://tryhackme.com/`**

- Can curl perform upload operations?(Yea/Nah)

**=> Answer: `Yea`**

### 11. wget
- How will you enable time logging at every new activity that this tool initiates?

**=> Answer: `-N`**

- What command will you use to download https://xyz.com/mypackage.zip using wget, appending logs to an existing file named "package-logs.txt"

**=> Answer: `wget -a package-logs.txt https://xyz.com/mypackage.zip`**

- Write the command to read URLs from "file.txt" and limit the download speed to 1mbps.

**=> Answer: `wget -i file.txt --limit-rate=1m`**

### 12. xxd
- How will you seek at 10th byte(in hex) in file.txt and display only 50 bytes?

**=> Answer: `xxd -s 0xa -l 50 -b file.txt`**

- How to display a n bytes of hexdump in 3 columns with a group of 3 octets per row from file.txt? (Use flags alphabetically)

**=> Answer: `xxd -c 9 -g 3 file.txt`**

- Which has more precedence over the other -c flag or -g flag?

**=> Answer: `-c`**

- Download the file and find the value of flag.
```bash
echo "666c61677b776833736477306c7731676c396f7161736164326673343861737d0a" | xxd -r -p
```
**=> Answer: `flag{wh3sdw0lw1gl9oqasad2fs48as}`**

### 13. Other modules
- It's safe to run systemctl command and experiment on your main linux system neither following a proper guide or having any prior knowledge? (Right/Wrong)

**=> Answer: `Wrong`**

- How will you import a given PGP private key. (Suppose the name of the file is key.gpg)

**=> Answer: `gpg --import key.gpg`**

- How will you list all port activity if netstat is not available on a machine? (Full Name)

**=> Answer: `Socket Statistics`**

- What command can be used to fix a broken/irregular/weird acting terminal shell?

**=> Answer: `reset`**

### 14. Is it night yet?
- Press F to pay respect

**=> Answer: `F`**