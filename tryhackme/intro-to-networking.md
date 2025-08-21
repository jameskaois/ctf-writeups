# Introductory Networking - TryHackMe 

An introduction to networking theory and basic networking tools

## Overview
- **Room URL:** [https://tryhackme.com/room/introtonetworking](https://tryhackme.com/room/introtonetworking)
- **Difficulty:** Easy
- **Time to complete:** 20

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. The OSI Model: An Overview
- <p>Which layer would choose to send data over TCP or UDP? Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</p>

**=> Answer: `4`**

- <p>Which layer checks received information to make sure that it hasn't been corrupted? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `2`**

- <p>In which layer would data be formatted in preparation for transmission? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `2`**

- <p>Which layer transmits and receives data? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `1`**

- <p>Which layer encrypts, compresses, or otherwise transforms the initial data to give it a standardised format? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `6`**

- <p>Which layer tracks communications between the host and receiving computers? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `5`**

- <p>Which layer accepts communication requests from applications? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `7`**

- <p>Which layer handles logical addressing? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `3`**

- <p>When sending data over TCP, what would you call the "bite-sized" pieces of data? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span><br /></p>

**=> Answer: `Segments`**

- <p><b>[Research]</b> Which layer would the FTP protocol communicate with? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span><br /></p>

**=> Answer: `7`**

- <p>Which transport layer protocol would be best suited to transmit a live video? <span style="">Answer with the number of the layer: e.g. if the answer would be "the application layer", then you would enter "7".</span></p>

**=> Answer: `UDP`**

### 3. Encapsulation
- <p>How would you refer to data at layer 2 of the encapsulation process (with the OSI model)?</p>

**=> Answer: `Frames`**

- <p>How would you refer to data at layer 4 of the encapsulation process (with the OSI model), if the UDP protocol has been selected?</p>

**=> Answer: `Datagrams`**

- <p>What process would a computer perform on a received message?</p>

**=> Answer: `De-encapsulation`**

- <p>Which is the only layer of the OSI model to add a <i>trailer</i> during encapsulation?</p>

**=> Answer: `Data Link`**

- <p>Does encapsulation provide an extra layer of security <b>(Aye/Nay)</b>?</p>

**=> Answer: `Aye`**

### 4. The TCP/IP Model
- <p>Which model was introduced first, OSI or TCP/IP?</p>

**=> Answer: `TCP/IP`**

- <p>Which layer of the TCP/IP model covers the functionality of the Transport layer of the OSI model <b>(Full Name)</b>?<br /></p>

**=> Answer: `Transport`**

- <p>Which layer of the TCP/IP model covers the functionality of the Session layer of the OSI model <b>(Full Name)</b>?<br /></p>

**=> Answer: `Application`**

- <p>The Network Interface layer of the TCP/IP model covers the functionality of two layers in the OSI model. These layers are Data Link, and?.. <b>(Full Name)</b>?<br /></p>

**=> Answer: `Physical`**

- <p><span style="font-size:1rem">Which layer of the TCP/IP model handles the functionality of the OSI network layer?</span><br /></p>

**=> Answer: `Internet`**

- <p>What kind of protocol is TCP?<br /></p>

**=> Answer: `Connection-based`**

- <p>What is SYN short for?<br /></p>

**=> Answer: `Synchronise`**

- <p>What is the second step of the three way handshake?</p>

**=> Answer: `SYN/ACK`**

- <p>What is the short name for the "Acknowledgement" segment in the three-way handshake?</p>

**=> Answer: `ACK`**

### 5. <span class="badge badge-soft-warning size-16">Networking Tools</span> Ping
- <p>What command would you use to ping the bbc.co.uk website?</p>

**=> Answer: `ping bbc.co.uk`**

- <p>Ping <i>muirlandoracle.co.uk</i><br />What is the IPv4 address?<br /></p>

**=> Answer: `217.160.0.152`**

- <p>What switch lets you change the interval of sent ping requests?<br /></p>

**=> Answer: `-i`**

- <p>What switch would allow you to restrict requests to IPv4?<br /></p>

**=> Answer: `-4`**

- <p>What switch would give you a more verbose output?<br /></p>

**=> Answer: `-v`**

### 6. <span class="badge badge-soft-warning size-16">Networking Tools</span> Traceroute
- <p>What switch would you use to specify an interface when using Traceroute?<br /></p>

**=> Answer: `-i`**

- <p>What switch would you use if you wanted to use TCP SYN requests when tracing the route?<br /></p>

**=> Answer: `-T`**

- <p><b>[Lateral Thinking] </b>Which layer of the <i><b>TCP/IP</b></i> model will traceroute run on by default (Windows)?</p>

**=> Answer: `Internet`**

### 7. <span class="badge badge-soft-warning size-16">Networking Tools</span> WHOIS
- <p>What is the registrant postal code for facebook.com?</p>

**=> Answer: `94025`**

- <p>When was the facebook.com domain first registered (Format: DD/MM/YYYY)?</p>

**=> Answer: `29/03/1997`**

- <p>Which city is the registrant based in?</p>

**=> Answer: `Redmond`**

- <p><b>[OSINT] </b>What is the name of the golf course that is near the registrant address for microsoft.com?</p>

**=> Answer: `Bellevue Golf Course`**

- <p>What is the registered Tech Email for microsoft.com?</p>

**=> Answer: `msnhst@microsoft.com`**

### 8. <span class="badge badge-soft-warning size-16">Networking Tools</span> Dig
- <p>What is DNS short for?</p>


**=> Answer: `Domain Name System`**

- <p>What is the first type of DNS server your computer would query when you search for a domain?</p>


**=> Answer: `Recursive`**

- <p>What type of DNS server contains records specific to domain extensions (i.e. <em>.com,</em> .co.uk*, etc)*? Use the long version of the name.</p>


**=> Answer: `Top-Level Domain`**

- <p>Where is the very first place your computer would look to find the IP address of a domain?</p>


**=> Answer: `Hosts File`**

- <p><strong>[Research]</strong> <span class="size" style="font-size:1rem">Google runs two public DNS servers. One of them can be queried with the IP 8.8.8.8, what is the IP address of the other one?</span></p>


**=> Answer: `8.8.4.4`**

- <p>If a DNS query has a TTL of 24 hours, what number would the dig query show?</p>


**=> Answer: `86400`**

### 9. Further Reading
*No hints needed!*