# Active Reconnaissance - TryHackMe

Learn how to use simple tools such as traceroute, ping, telnet, and a web browser to gather information.

## Overview

- **Room URL:** [https://tryhackme.com/room/activerecon](https://tryhackme.com/room/activerecon)
- **Difficulty:** Easy
- **Time to complete:** 60

## Walkthrough

### 1. Introduction

_No answer needed!_

### 2. Web Browser

- <p>Browse to the <a href="https://static-labs.tryhackme.cloud/sites/networking-tcp/" target="_blank">following website</a> and ensure that you have opened your Developer Tools on AttackBox Firefox, or the browser on your computer. Using the Developer Tools, figure out the total number of questions.</p>

Browse the `script.js`:

```javascript
let questions = {
  1: {
    speaking: "alice",
    answer_1: "SYN : Can you hear me Bob?",
    answer_2: "FIN : Goodbye",
    answer_3: "ACK : Erm... What?",
    answer: 1,
  },
  2: {
    speaking: "bob",
    answer_1: "RST : Cya Later",
    answer_2: "PING : 77",
    answer_3: "SYN/ACK : Yes, I can hear you!",
    answer: 3,
  },
  3: {
    speaking: "alice",
    answer_1: "FAIL : SEGMENTATION FAULT",
    answer_2: "ACK : Okay Great",
    answer_3: "SYN : x = 3?",
    answer: 2,
  },
  4: {
    speaking: "alice",
    answer_1: "ICMP : 99",
    answer_2: "SYN : Yes, I can hear you!",
    answer_3: "DATA : Cheesecake is on sale!",
    answer: 3,
  },
  5: {
    speaking: "bob",
    answer_1: "ACK : I Hear ya!",
    answer_2: "REPEAT : What?",
    answer_3: "RESET : Help!",
    answer: 1,
  },
  6: {
    speaking: "alice",
    answer_1: "ACK : OK",
    answer_2: "FIN/ACK : I'm all done",
    answer_3: "ECHO : Retry",
    answer: 2,
  },
  7: {
    speaking: "bob",
    answer_1: "SYN : Received",
    answer_2: "WIRE : Reset Connection",
    answer_3: "FIN/ACK : Yeah Me Too",
    answer: 3,
  },
  8: {
    speaking: "alice",
    answer_1: "SYN : Connected",
    answer_2: "ACK : Okay, Goodbye",
    answer_3: "SYN/ACK : Not Received",
    answer: 2,
  },
};
```

**=> Answer: `8`**

### 3. Ping

- Which option would you use to set the size of the data carried by the ICMP echo request?<br />

**=> Answer: `-s`**

- <p>What is the size of the ICMP header in bytes?<br /></p>

**=> Answer: `8`**

- <p>Does MS Windows Firewall block ping by default? (Y/N)</p>

**=> Answer: `Y`**

- <p>Deploy the VM for this task and using the AttackBox terminal, issue the command <code style="font-size:14px">ping -c 10 MACHINE_IP</code>. How many ping replies did you get back?<br /></p>

![Guide image](./screenshots/active-reconnaissance-1.png)

**=> Answer: `10`**

### 4. Traceroute

- In Traceroute A, what is the IP address of the last router/hop before reaching tryhackme.com?<br />

**=> Answer: `172.67.69.208`**

- <p>In Traceroute B, what is the IP address of the last router/hop before reaching tryhackme.com?<br /></p>

**=> Answer: `104.26.11.229`**

- <p>In Traceroute B, how many routers are between the two systems?<br /></p>

**=> Answer: `26`**

### 5. Telnet

- Start the attached VM from Task 3 if it is not already started. On the AttackBox, open the terminal and use the telnet client to connect to the VM on port 80. What is the name of the running server?<br />

```bash
telnet <MACHINE_IP> 80
```

**=> Answer: `Apache`**

- <p>What is the version of the running server (on port 80 of the VM)?<br /></p>

```bash
nmap -sV <MACHINE_IP>
```

**=> Answer: `2.4.61`**

### 6. Netcat

- <p>Start the VM and open the AttackBox. Once the AttackBox loads, use Netcat to connect to the VM port 21. What is the version of the running server?</p>

**=> Answer: `0.17`**

### 7. Putting It All Together

_No answer needed!_
