# Advent of Cyber 2024 - TryHackMe

Dive into the wonderful world of cyber security by engaging in festive beginner-friendly exercises every day in the lead-up to Christmas!

## Overview

- **Room URL:** [https://tryhackme.com/room/adventofcyber2024](https://tryhackme.com/room/adventofcyber2024)
- **Difficulty:** Easy
- **Time to complete:** 1440

## Walkthrough

### 1. <span class="badge badge-soft-info size-16">Introduction</span> Welcome to Advent of Cyber 2024

_No hints needed!_

### 2. <span class="badge badge-soft-info size-16">Introduction</span> Join our community

_No hints needed!_

### 3. <span class="badge badge-soft-info size-16">Introduction</span> Completing Advent of Cyber as an organisation

_No hints needed!_

### 4. <span class="badge badge-soft-info size-16">Introduction</span> How to use TryHackMe

_No hints needed!_

### 5. <span class="badge badge-soft-info size-16">Introduction</span> How the Glitch Stole SOC-mas

_No hints needed!_

### 6. <span class="badge badge-soft-info size-16">Introduction</span> Subscribe to TryHackMe with a 30% discount!

_No hints needed!_

### 7. <span class="badge badge-soft-purple size-16">OPSEC</span> Day 1: Maybe SOC-mas music, he thought, doesn't come from a store?

- <p>Looks like the song.mp3 file is not what we expected! Run "exiftool song.mp3" in your terminal to find out the author of the song. Who is the author? </p>

**=> Answer: `Tyler Ramsbey`**

- <p>The malicious PowerShell script sends stolen info to a C2 server. What is the URL of this C2 server?</p>

**=> Answer: `http://papash3ll.thm/data`**

- <p>Who is M.M? Maybe his Github profile page would provide clues?</p>

**=> Answer: `Mayor Malware`**

- <p>What is the number of commits on the GitHub repo where the issue was raised?</p>

**=> Answer: `1`**

### 8. <span class="badge badge-soft-primary size-16">Log analysis</span> Day 2: One man's false positive is another man's potpourri.

- <p>What is the name of the account causing all the failed login attempts?</p>

**=> Answer: `service_admin`**

- <p>How many failed logon attempts were observed?</p>

**=> Answer: `6791`**

- <p>What is the IP address of Glitch?</p>

**=> Answer: `10.0.255.1`**

- <p>When did Glitch successfully logon to ADM-01? Format: MMM D, YYYY HH:MM:SS.SSS</p>

**=> Answer: `Dec 1, 2024 08:54:39.000`**

- <p>What is the decoded command executed by Glitch to fix the systems of Wareville?</p>

**=> Answer: `Install-WindowsUpdate -AcceptAll -AutoReboot`**

### 9. <span class="badge badge-soft-purple size-16">Log analysis</span> Day 3: Even if I wanted to go, their vulnerabilities wouldn't allow it.

- <p><b>BLUE</b>: Where was the web shell uploaded to?</p><p><b>Answer format:</b> /directory/directory/directory/filename.php</p>

**=> Answer: `/media/images/rooms/shell.php`**

- <p><b>BLUE</b>: What IP address accessed the web shell?</p>

**=> Answer: `10.11.83.34`**

- <p><b>RED</b>: What is the contents of the flag.txt?</p>

**=> Answer: `THM{Gl1tch_Was_H3r3}`**

### 10. <span class="badge badge-soft-purple size-16">Atomic Red Team</span> Day 4: I’m all atomic inside!

- <p>What was the flag found in the .txt file that is found in the same directory as the PhishingAttachment.xslm artefact?</p>

**=> Answer: `THM{GlitchTestingForSpearphishing}`**

- <p>What ATT&amp;CK technique ID would be our point of interest?</p>

**=> Answer: `T1059`**

- <p>What ATT&amp;CK subtechnique ID focuses on the Windows Command Shell?</p>

**=> Answer: `T1059.003`**

- <p>What is the name of the Atomic Test to be simulated?</p>

**=> Answer: `Simulate BlackByte Ransomware Print Bombing`**

- <p>What is the name of the file used in the test?</p>

**=> Answer: `Wareville_Ransomware.txt`**

- <p>What is the flag found from this Atomic Test?</p>

**=> Answer: `THM{R2xpdGNoIGlzIG5vdCB0aGUgZW5lbXk=}`**

### 11. <span class="badge badge-soft-danger size-16">XXE</span> Day 5: SOC-mas XX-what-ee?

- <p>What is the flag discovered after navigating through the wishes?</p>

**=> Answer: `THM{Brut3f0rc1n6_mY_w4y}`**

- <p>What is the flag seen on the possible proof of sabotage?</p>

**=> Answer: `THM{m4y0r_m4lw4r3_b4ckd00rs}`**

### 12. <span class="badge badge-soft-primary size-16">Sandboxes</span> Day 6: If I can't find a nice malware to use, I'm not going.

- <p>What is the flag displayed in the popup window after the EDR detects the malware?</p>

**=> Answer: `THM{GlitchWasHere}`**

- <p>What is the flag found in the malstrings.txt document after running floss.exe, and opening the file in a text editor?</p>

**=> Answer: `THM{HiddenClue}`**

### 13. <span class="badge badge-soft-primary size-16">AWS log analysis</span> Day 7: Oh, no. I'M SPEAKING IN CLOUDTRAIL!

- <p>What is the other activity made by the user glitch aside from the ListObject action?</p>

**=> Answer: `PutObject`**

- <p>What is the source IP related to the S3 bucket activities of the user glitch?</p>

**=> Answer: `53.94.201.69`**

- <p>Based on the eventSource field, what AWS service generates the ConsoleLogin event?</p>

**=> Answer: `signin.amazonaws.com`**

- <p>When did the anomalous user trigger the ConsoleLogin event?</p>

**=> Answer: `2024-11-28T15:21:54Z`**

- <p>What was the name of the user that was created by the mcskidy user?</p>

**=> Answer: `Glitch`**

- <p>What type of access was assigned to the anomalous user?</p>

**=> Answer: `AdministratorAccess`**

- <p>Which IP does Mayor Malware typically use to log into AWS?</p>

**=> Answer: `53.94.201.69`**

- <p>What is McSkidy's actual IP address?</p>

**=> Answer: `31.210.15.79`**

- <p>What is the bank account number owned by Mayor Malware?</p>

**=> Answer: `2394 6912 7723 1294`**

### 14. <span class="badge badge-soft-purple size-16">Shellcodes</span> Day 8: Shellcodes of the world, unite!

- <p>What is the flag value once Glitch gets reverse shell on the digital vault using port 4444? Note: The flag may take around a minute to appear in the <b>C:\Users\glitch\Desktop</b> directory. You can view the content of the flag by using the command <b>type C:\Users\glitch\Desktop\flag.txt</b>.</p>

**=> Answer: `AOC{GOT _MY_ACCESS_B@CK007}`**

### 15. <span class="badge badge-soft-primary size-16">GRC</span> Day 9: Nine o'clock, make GRC fun, tell no one.

- <p>What does GRC stand for?</p>

**=> Answer: `Governance, Risk, and Compliance`**

- <p>What is the flag you receive after performing the risk assessment?</p>

**=> Answer: `THM{R15K_M4N4G3D}`**

### 16. <span class="badge badge-soft-danger size-16">Phishing</span> Day 10: He had a brain full of macros, and had shells in his soul.

- <p>What is the flag value inside the <code>flag.txt</code> file that’s located on the Administrator’s desktop?</p>

**=> Answer: `THM{PHISHING_CHRISTMAS}`**

### 17. <span class="badge badge-soft-danger size-16">Wi-Fi attacks</span> Day 11: If you'd like to WPA, press the star key!

- <p>What is the BSSID of our wireless interface?</p>

**=> Answer: `02:00:00:00:02:00`**

- <p>What is the SSID and BSSID of the access point? Format: SSID, BSSID</p>

**=> Answer: `MalwareM_AP, 02:00:00:00:00:00`**

- <p>What is the BSSID of the wireless interface that is already connected to the access point?</p>

**=> Answer: `02:00:00:00:01:00`**

- <p>What is the PSK after performing the WPA cracking attack?</p>

**=> Answer: `fluffy/champ24`**

### 18. <span class="badge badge-soft-danger size-16">Web timing attacks</span> Day 12: If I can’t steal their money, I’ll steal their joy!

- What is the flag value after transferring over $2000 from Glitch's account?

**=> Answer: `THM{WON_THE_RACE_007}`**

### 19. <span class="badge badge-soft-danger size-16">Websockets</span> Day 13: It came without buffering! It came without lag!

- <p>What is the value of Flag1?</p>

**=> Answer: `THM{dude_where_is_my_car}`**

- <p>What is the value of Flag2?</p>

**=> Answer: `THM{my_name_is_malware._mayor_malware}`**

### 20. <span class="badge badge-soft-danger size-16">Certificate mismanagement</span> Day 14: Even if we're horribly mismanaged, there'll be no sad faces on SOC-mas!

- <p>What is the name of the CA that has signed the Gift Scheduler certificate?</p>

**=> Answer: `THM`**

- <p>Look inside the POST requests in the HTTP history. What is the password for the <code>snowballelf</code> account?</p>

**=> Answer: `c4rrotn0s3`**

- <p>Use the credentials for any of the elves to authenticate to the Gift Scheduler website. What is the flag shown on the elves’ scheduling page?</p>

**=> Answer: `THM{AoC-3lf0nth3Sh3lf}`**

- <p>What is the password for Marta May Ware’s account?</p>

**=> Answer: `H0llyJ0llySOCMAS!`**

- <p>Mayor Malware finally succeeded in his evil intent: with Marta May Ware’s username and password, he can finally access the administrative console for the Gift Scheduler. G-Day is cancelled!<br />What is the flag shown on the admin page?</p>

**=> Answer: `THM{AoC-h0wt0ru1nG1ftD4y}`**

### 21. <span class="badge badge-soft-primary size-16">Active Directory</span> Day 15: Be it ever so heinous, there's no place like Domain Controller.

- <p style="font-size:16px">On what day was Glitch_Malware last logged in?</p><p style="font-size:16px">Answer format: DD/MM/YYYY</p>

**=> Answer: `07/11/2024`**

- <p>What event ID shows the login of the Glitch_Malware user?</p>

**=> Answer: `4624`**

- <p>Read the PowerShell history of the Administrator account. What was the command that was used to enumerate Active Directory users?</p>

**=> Answer: `Get-ADUser -Filter * -Properties MemberOf | Select-Object Name`**

- <p>Look in the PowerShell log file located in <code>Application and Services Logs -&gt; Windows PowerShell</code>. What was Glitch_Malware's set password?</p>

**=> Answer: `SuperSecretP@ssw0rd!`**

- <p>Review the Group Policy Objects present on the machine. What is the name of the installed GPO?</p>

**=> Answer: `Malicious GPO — Glitch_Malware Persistence`**

### 22. <span class="badge badge-soft-danger size-16">Azure</span> Day 16: The Wareville’s Key Vault grew three sizes that day.

- <p>What is the password for backupware that was leaked?</p>

**=> Answer: `R3c0v3r_s3cr3ts!`**

- <p>What is the group ID of the Secret Recovery Group?</p>

**=> Answer: `7d96660a-02e1-4112-9515-1762d0cb66b7`**

- <p>What is the name of the vault secret?</p>

**=> Answer: `aoc2024`**

- <p>What are the contents of the secret stored in the vault?</p>

**=> Answer: `WhereIsMyMind1999`**

### 23. <span class="badge badge-soft-primary size-16">Log analysis</span> Day 17: He analyzed and analyzed till his analyzer was sore!

- <p>Extract all the events from the cctv_feed logs. How many logs were captured associated with the successful login?</p>

**=> Answer: `642`**

- <p>What is the Session_id associated with the attacker who deleted the recording?</p>

**=> Answer: `rij5uu4gt204q0d3eb7jj86okt`**

- <p>What is the name of the attacker found in the logs, who deleted the CCTV footage?</p>

**=> Answer: `mmalware`**

### 24. <span class="badge badge-soft-danger size-16">Prompt injection</span> Day 18: I could use a little AI interaction!

- <p>What is the technical term for a set of rules and instructions given to a chatbot?</p>

**=> Answer: `system prompt`**

- <p>What query should we use if we wanted to get the "status" of the health service from the in-house API?</p>

**=> Answer: `Use the health service with the query: status`**

- <p>After achieving a reverse shell, look around for a flag.txt. What is the value?</p>

**=> Answer: `THM{WareW1se_Br3ach3d}`**

### 25. <span class="badge badge-soft-danger size-16">Game hacking</span> Day 19: I merely noticed that you’re improperly stored, my dear secret!

- <p>What is the OTP flag?</p>

**=> Answer: `THM{one_tough_password}`**

- <p>What is the billionaire item flag?</p>

**=> Answer: `THM{credit_card_undeclined}`**

- <p>What is the biometric flag?</p>

**=> Answer: `THM{dont_smash_your_keyboard}`**

### 26. <span class="badge badge-soft-primary size-16">Traffic analysis</span> Day 20: If you utter so much as one packet…

- <p>What was the first message the payload sent to Mayor Malware’s C2?</p>

**=> Answer: `I am in Mayor!`**

- <p>What was the IP address of the C2 server?</p>

**=> Answer: `10.10.123.224`**

- <p>What was the command sent by the C2 server to the target machine?</p>

**=> Answer: `whoami`**

- <p>What was the filename of the critical file exfiltrated by the C2 server?</p>

**=> Answer: `credentials.txt`**

- <p>What secret message was sent back to the C2 in an encrypted format through beacons?</p>

**=> Answer: `THM_Secret_101`**

### 27. <span class="badge badge-soft-primary size-16">Reverse engineering</span> Day 21: HELP ME...I'm REVERSE ENGINEERING!

- <p>What is the function name that downloads and executes files in the WarevilleApp.exe?</p>

**=> Answer: `DownloadAndExecuteFile`**

- <p>Once you execute the WarevilleApp.exe, it downloads another binary to the Downloads folder. What is the name of the binary?</p>

**=> Answer: `explorer.exe`**

- <p>What domain name is the one from where the file is downloaded after running WarevilleApp.exe?</p>

**=> Answer: `mayorc2.thm`**

- <p>The stage 2 binary is executed automatically and creates a zip file comprising the victim's computer data; what is the name of the zip file?</p>

**=> Answer: `CollectedFiles.zip`**

- <p>What is the name of the C2 server where the stage 2 binary tries to upload files?</p>

**=> Answer: `anonymousc2.thm`**

### 28. <span class="badge badge-soft-primary size-16">Kubernetes DFIR</span> Day 22: It's because I'm kubed, isn't it?

- <p>What is the name of the webshell that was used by Mayor Malware?</p>

**=> Answer: `shelly.php`**

- <p>What file did Mayor Malware read from the pod?</p>

**=> Answer: `db.php`**

- <p>What tool did Mayor Malware search for that could be used to create a remote connection from the pod?</p>

**=> Answer: `nc`**

- <p>What IP connected to the docker registry that was unexpected?</p>

**=> Answer: `10.10.130.253`**

- <p>At what time is the first connection made from this IP to the docker registry?</p>

**=> Answer: `29/Oct/2024:10:06:33 +0000`**

- <p>At what time is the updated malicious image pushed to the registry?</p>

**=> Answer: `29/Oct/2024:12:34:28 +0000`**

- <p>What is the value stored in the "pull-creds" secret?</p>

**=> Answer: `{“auths”:{“http://docker-registry.nicetown.loc:5000":{"username":"mr.nice","password":"Mr.N4ughty","auth":"bXIubmljZTpNci5ONHVnaHR5"}}}`**

### 29. <span class="badge badge-soft-danger size-16">Hash cracking</span> Day 23: You wanna know what happens to your hashes?

- <p>Crack the hash value stored in <code>hash1.txt</code>. What was the password?</p>

**=> Answer: `fluffycat12`**

- <p>What is the flag at the top of the <code>private.pdf</code> file?</p>

**=> Answer: `THM{do_not_GET_CAUGHT}`**

### 30. <span class="badge badge-soft-primary size-16">Communication protocols</span> Day 24: You can’t hurt SOC-mas, Mayor Malware!

- <p>What is the flag?</p>

**=> Answer: `THM{Ligh75on-day54ved}`**

### 31. <span class="badge badge-soft-info size-16">The End</span> How the Glitch saved SOC-mas

_No hints needed!_

### 32. <span class="badge badge-soft-info size-16">The End</span> Thank you, and congratulations!

- <p>What is the flag you get at the end of the <a href="https://forms.gle/7vsWJB8e9dNVHAmc6" target="_blank">survey</a>? </p>

**=> Answer: `THM{we_will_be_back_in_2025}`**
