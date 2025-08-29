# Windows Fundamentals 2 - TryHackMe 

In part 2 of the Windows Fundamentals module, discover more about System Configuration, UAC Settings, Resource Monitoring, the Windows Registry and more..

## Overview
- **Room URL:** [https://tryhackme.com/room/windowsfundamentals2x0x](https://tryhackme.com/room/windowsfundamentals2x0x)
- **Difficulty:** Info
- **Time to complete:** 30

## Walkthrough
### 1. Introduction
*No hints needed!*

### 2. System Configuration
- What is the name of the service that lists Systems Internals as the manufacturer?

**=> Answer: `PsShutdown`**

- <p>Whom is the Windows license registered to?<br /></p>
```
- Launch About Windows in Tools tab
```

![Guide image](./screenshots/windows-fundamentals-2-1.png)

**=> Answer: `Windows User`**

- What is the command for Windows Troubleshooting?
```
- Choose Windows Troubleshooting in Tools tab
```
![Guide image](./screenshots/windows-fundamentals-2-2.png)

**=> Answer: `C:\Windows\System32\control.exe /name Microsoft.Troubleshooting`**

- <p>What command will open the Control Panel? (The answer is  the name of .exe, not the full path)</p>
```
- Choose System Properties in Tools tab
```
**=> Answer: `control.exe`**

### 3. Change UAC Settings
- What is the command to open User Account Control Settings? (The answer is the name of the .exe file, not the full path)
```
- Choose Change UAC Settings in Tools tab
```

**=> Answer: `UserAccountControlSettings.exe`**

### 4. Computer Management
- <p>What is the command to open Computer Management? (The answer is the name of the .msc file, not the full path)</p>
```
- Choose Computer Management in Tools tab
```
**=> Answer: `compmgmt.msc`**

- At what time every day is the GoogleUpdateTaskMachineUA task configured to run?
```
- Launch Computer Management in Tools tab
- Choose Task Scheduler > Task Scheduler Library > GoogleUpdateTaskMachineUA
- You can see the repeated time in the description
```
![Guide image](./screenshots/windows-fundamentals-2-3.png)
**=> Answer: `6:15 AM`**

- <p>What is the name of the hidden folder that is shared?<br /></p>
```
- In Computer Management, choose Shared Folder > Shares
- You can see a hidden shared folder.
```
![Guide image](./screenshots/windows-fundamentals-2-4.png)
**=> Answer: `sh4r3dF0ld3r`**

### 5. System Information
- What is the command to open System Information? (The answer is the name of the .exe file, not the full path)
```
- Choose System Information in Tools tab
```

![Guide image](./screenshots/windows-fundamentals-2-5.png)

**=> Answer: `msinfo32.exe`**

- <p>What is listed under System Name?</p>
```
- Launch System Information in Tools tab
- You can see the System Name
```
![Guide image](./screenshots/windows-fundamentals-2-6.png)

**=> Answer: `THM-WINFUN2`**

- Under Environment Variables, what is the value for ComSpec?
```
- In System Information, choose Software Environment > Environment Variables
- You can see the ComSpec field
```
![Guide image](./screenshots/windows-fundamentals-2-7.png)
**=> Answer: `%SystemRoot%\system32\cmd.exe`**

### 6. Resource Monitor
- What is the command to open Resource Monitor? (The answer is the name of the .exe file, not the full path)
```
- Choose Resource Monitor in Tools tab
```
![Guide image](./screenshots/windows-fundamentals-2-8.png)
**=> Answer: `resmon.exe`**

### 7. Command Prompt
- In System Configuration, what is the full command for Internet Protocol Configuration?
```
- Choose Internet Protocol Configuration in System Configuration
```
![Guide image](./screenshots/windows-fundamentals-2-9.png)
**=> Answer: `C:\Windows\System32\cmd.exe /k %windir%\system32\ipconfig.exe`**

- <p>For the ipconfig command, how do you show detailed information?</p>
```
- In Command Prompt, run ipconfig /? to see the guide
- You will see the command to show detailed information
```
![Guide image](./screenshots/windows-fundamentals-2-10.png)
**=> Answer: `ipconfig /all`**

### 8. Registry Editor
- What is the command to open the Registry Editor? (The answer is the name of  the .exe file, not the full path)
```
- Choose Registry Editor in System Configuration
```
![Guide image](./screenshots/windows-fundamentals-2-11.png)
**=> Answer: `regedt32.exe`**

### 9. Conclusion
*No hints needed!*