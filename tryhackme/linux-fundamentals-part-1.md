# Linux Fundamentals Part 1 – TryHackMe

## Overview
- **Room URL:** [https://tryhackme.com/room/linuxfundamentalspart1](https://tryhackme.com/room/linuxfundamentalspart1)  
- **Difficulty:** Easy
- **Category:** Linux

## Learning Objectives
- Key skills learned in this room:  
  - Linux history
  - Linux based thinking
  - Linux basic commands

## Walkthrough (Hints & Notes)
### 1. Introduction
*No hints needed.*

### 2. A Bit of Background on Linux
- Research: What year was the first release of a Linux operating system?

**=> Answer: `1991`**

### 3. Interacting With Your First Linux Machine (In-Browser)
*No hints needed.*

### 4. Running Your First Few Commands
- If we wanted to output the text "TryHackMe", what would our command be?

**=> Answer: `echo TryHackMe`**

- What is the username of who you're logged in as on your deployed Linux machine?
```bash
tryhackme@linux1:~$ whoami
tryhackme
```
**=> Answer: `tryhackme`**

### 5. Interacting With the Filesystem!
- On the Linux machine that you deploy, how many folders are there?
```bash
tryhackme@linux1:~$ ls
access.log folder1 folder2 folder3 folder4
```

**=> Answer: `4`**

- Which directory contains a file? 
```bash
tryhackme@linux1:~$ ls folder4
note.txt
```
**=> Answer: `folder4`**

- What is the contents of this file?
```bash
tryhackme@linux1:~$ cat folder4/note.txt
Hello World!
```
**=> Answer: `Hello World`**

- Use the cd command to navigate to this file and find out the new current working directory. What is the path?
```bash
tryhackme@linux1:~$ cd /home/tryhackme/folder4
```
**=> Answer: `/home/tryhackme/folder4`**

### 6. Searching for Files
- Use grep on "access.log" to find the flag that has a prefix of "THM". What is the flag? Note: The "access.log" file is located in the "/home/tryhackme/" directory.
```bash
tryhackme@linux1:~$ cd /home/tryhackme
tryhackme@linux1:~$ grep "THM" access.log
..."GET THM{ACCESS} lang=en HTTP/1.1"...
```

**=> Answer: `THM{ACCESS}`**

### 7. An Introduction to Shell Operators
- If we wanted to run a command in the background, what operator would we want to use?

**=> Answer: `&`**

- If I wanted to replace the contents of a file named "passwords" with the word "password123", what would my command be?

**=> Answer: `echo password123 > passwords`**

- Now if I wanted to add "tryhackme" to this file named "passwords" but also keep "passwords123", what would my command be

**=> Answer: `echo tryhackme >> passwords`**

### 8. Conclusions & Summaries
*No hints needed.*

### 9. Linux Fundamentals Part 2
*No hints needed.*