# Network Traffic Basics - TryHackMe

This room teaches the basics of Network Traffic Analysis.

## Overview

- **Room URL:** [https://tryhackme.com/room/networktrafficbasics](https://tryhackme.com/room/networktrafficbasics)
- **Difficulty:** Easy
- **Time to complete:** 60

## Walkthrough

### 1. Introduction

_No hints needed!_

### 2. What is the Purpose of Network Traffic Analysis?

- <p>What is the name of the technique used to smuggle C2 commands via DNS?</p>

**=> Answer: `DNS Tunneling`**

### 3. What Network Traffic Can We Observe?

- <p>Look at the HTTP example in the task and answer the following question: What is the size of the ZIP attachment included in the HTTP response? Note down the answer in bytes.</p>

**=> Answer: `10485760`**

- <p>Which attack do attackers use to try to evade an IDS?</p>

**=> Answer: `fragmentation`**

- <p>What field in the TCP header can we use to detect session hijacking?</p>

**=> Answer: `sequence number`**

### 4. Network Traffic Sources and Flows

- <p>Which category of devices generates the most traffic in a network?</p>

**=> Answer: `endpoint`**

- <p>Before an SMB session can be established, which service needs to be contacted first for authentication?</p>

**=> Answer: `kerberos`**

- <p>What does TLS stand for?</p>

**=> Answer: `Transport Layer Security`**

### 5. How Can We Observe Network Traffic?

- <p>What is the flag found in the HTTP traffic in scenario 1? The flag has the format THM{}.</p>

**=> Answer: `THM{FoundTheMalware}`**

- <p>What is the flag found in the DNS traffic in scenario 2? The flag has the format THM{}.</p>

**=> Answer: `THM{C2CommandFound}`**

### 6. Conclusion

_No hints needed!_
