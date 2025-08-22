# Nmap - TryHackMe 

An in depth look at scanning with Nmap, a powerful network scanning tool.

## Overview
- **Room URL:** [https://tryhackme.com/room/furthernmap](https://tryhackme.com/room/furthernmap)
- **Difficulty:** Easy
- **Time to complete:** 50

## Walkthrough
### 1. Deploy
*No hints needed!*

### 2. Introduction
- <p>What networking constructs are used to direct traffic to the right application on a server?</p>

**=> Answer: `ports`**

- <p>How many of these are available on any network-enabled computer?</p>

**=> Answer: `65535`**

- <p><strong>[Research]</strong> How many of these are considered "well-known"? (These are the "standard" numbers mentioned in the task)</p>

**=> Answer: `1024`**

### 3. Nmap Switches
- <p>What is the first switch listed in the help menu for a 'Syn Scan' (more on this later!)?</p>


**=> Answer: `-sS`**

- <p>Which switch would you use for a "UDP scan"?</p>


**=> Answer: `-sU`**

- <p>If you wanted to detect which operating system the target is running on, which switch would you use?</p>


**=> Answer: `-O`**

- <p>Nmap provides a switch to detect the version of the services running on the target. What is this switch?</p>


**=> Answer: `-sV`**

- <p>The default output provided by nmap often does not provide enough information for a pentester. How would you increase the verbosity?</p>


**=> Answer: `-v`**

- <p>Verbosity level one is good, but verbosity level two is better! How would you set the verbosity level to two?<br />
(<strong>Note</strong>: it's highly advisable to always use <em>at least</em> this option)</p>


**=> Answer: `-vv`**

- <p>We should always save the output of our scans -- this means that we only need to run the scan once (reducing network traffic and thus chance of detection), and gives us a reference to use when writing reports for clients.</p>
<p>What switch would you use to save the nmap results in three major formats?</p>


**=> Answer: `-oA`**

- <p>What switch would you use to save the nmap results in a "normal" format?</p>


**=> Answer: `-oN`**

- <p>A very useful output format: how would you save results in a "grepable" format?</p>


**=> Answer: `-oG`**

- <p>Sometimes the results we're getting just aren't enough. If we don't care about how loud we are, we can enable "aggressive" mode. This is a shorthand switch that activates service detection, operating system detection, a traceroute and common script scanning.</p>
<p>How would you activate this setting?</p>


**=> Answer: `-A`**

- <p>Nmap offers five levels of "timing" template. These are essentially used to increase the speed your scan runs at. Be careful though: higher speeds are noisier, and can incur errors!</p>
<p>How would you set the timing template to level 5?</p>


**=> Answer: `-T5`**

- <p>We can also choose which port(s) to scan.</p>
<p>How would you tell nmap to only scan port 80?</p>


**=> Answer: `-p 80`**

- <p>How would you tell nmap to scan ports 1000-1500?</p>


**=> Answer: `-p 1000-1500`**

- <p>A very useful option that should not be ignored:</p>
<p>How would you tell nmap to scan <em>all</em> ports?</p>


**=> Answer: `-p-`**

- <p>How would you activate a script from the nmap scripting library (lots more on this later!)?</p>


**=> Answer: `--script`**

- <p>How would you activate all of the scripts in the "vuln" category?</p>


**=> Answer: `--script=vuln`**

### 4. <span class="badge badge-soft-info size-16">Scan Types</span> Overview
*No hints needed!*

### 5. <span class="badge badge-soft-info size-16">Scan Types</span> TCP Connect Scans
- <p>Which RFC defines the appropriate behaviour for the TCP protocol?</p>


**=> Answer: `RFC 9293`**

- <p>If a port is closed, which flag should the server send back to indicate this?</p>


**=> Answer: `RST`**

### 6. <span class="badge badge-soft-info size-16">Scan Types</span> SYN Scans
- There are two other names for a SYN scan, what are they?<br />

**=> Answer: `Half-Open, Stealth`**

- <p>Can Nmap use a SYN scan without Sudo permissions (Y/N)?<br /></p>

**=> Answer: `N`**

### 7. <span class="badge badge-soft-info size-16">Scan Types</span> UDP Scans
- If a UDP port doesn't respond to an Nmap scan, what will it be marked as?<br />

**=> Answer: `open|filtered`**

- <p>When a UDP port is closed, by convention the target should send back a "port unreachable" message. Which protocol would it use to do so?<br /></p>

**=> Answer: `ICMP`**

### 8. <span class="badge badge-soft-info size-16">Scan Types</span> NULL, FIN and Xmas
- Which of the three shown scan types uses the URG flag?<br />

**=> Answer: `xmas`**

- <p>Why are NULL, FIN and Xmas scans generally used?<br /></p>

**=> Answer: `Firewall Evasion`**

- <p>Which common OS may respond to a NULL, FIN or Xmas scan with a RST for every port?<br /></p>

**=> Answer: `Microsoft Windows`**

### 9. <span class="badge badge-soft-info size-16">Scan Types</span> ICMP Network Scanning
- How would you perform a ping sweep on the 172.16.x.x network (Netmask: 255.255.0.0) using Nmap? (CIDR notation)<br />

**=> Answer: `nmap -sn 172.16.0.0/16`**

### 10. <span class="badge badge-soft-warning size-16">NSE Scripts</span> Overview
- What language are NSE scripts written in?<br />

**=> Answer: `Lua`**

- <p>Which category of scripts would be a <i>very</i> bad idea to run in a production environment?<br /></p>

**=> Answer: `intrusive`**

### 11. <span class="badge badge-soft-warning size-16">NSE Scripts</span> Working with the NSE
- <p>What optional argument can the <code>ftp-anon.nse</code> script take?</p>


**=> Answer: `maxlist`**

### 12. <span class="badge badge-soft-warning size-16">NSE Scripts</span> Searching for Scripts
- Search for "smb" scripts in the <code>/usr/share/nmap/scripts/</code> directory using either of the demonstrated methods. <br />What is the filename of the script which determines the underlying OS of the SMB server?<br />

**=> Answer: `smb-os-discovery.nse`**

- <p>Read through this script. What does it depend on?<br /></p>

**=> Answer: `smb-brute`**

### 13. Firewall Evasion
- Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the <code>-Pn</code> switch?<br />

**=> Answer: `ICMP`**

- <p><b>[Research]</b> Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?<br /></p>

**=> Answer: `--data-length`**

### 14. Practical
- <p class="pw-post-body-paragraph mh mi gr mj b mk ow mm mn mo ox mq mr ms oy mu mv mw oz my mz na pa nc nd ne gk bj"><span class="mj gs">Does the target ip </span><span style="">respond to ICMP echo (ping) requests (Y/N)?</span></p>
```bash
ping <target_IP>
```
**=> Answer: `N`**

- <p>Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?</p>


**=> Answer: `999`**

- <p>There is a reason given for this -- what is it?</p>
<p><strong>Note:</strong> The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!</p>


**=> Answer: `No Response`**

- <p>Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?</p>


**=> Answer: `5`**

- <p>Open Wireshark (see <a href="https://tryhackme.com/p/Cryillic">Cryillic's</a> <a href="https://tryhackme.com/room/wireshark">Wireshark Room</a> for instructions) and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on. <span style="font-size:1rem">Deploy the</span><span style="font-size:1rem"> </span><code style="font-size:14px">ftp-anon</code><span style="font-size:1rem"> </span><span style="font-size:1rem">script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)</span></p>


**=> Answer: `Y`**

### 15. Conclusion
*No hints needed!*

