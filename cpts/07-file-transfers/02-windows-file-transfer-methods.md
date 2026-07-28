# Section 02: Windows File Transfer Methods

Module: 07. File Transfers

---

## Questions & Answers

### 1. Download the file flag.txt from the web root using wget from the Pwnbox. Submit the contents of the file as your answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.184]─[htb-ac-2162140@htb-efv5zomuca]─[~]
└──╼ [★]$ curl http://10.129.201.55/flag.txt
b1a4ca918282fcd96004565521944a3b
```

**Answer:** `b1a4ca918282fcd96004565521944a3b`

---

### 2. Upload the attached file named upload_win.zip to the target using the method of your choice. Once uploaded, unzip the archive, and run "hasher upload_win.txt" from the command line. Submit the generated hash as your answer.

Context:
- Create the file in Pwnbox
```bash
┌─[eu-academy-1]─[10.10.14.184]─[htb-ac-2162140@htb-efv5zomuca]─[~]
└──╼ [★]$ echo "e4feec466d5de701089b5cc1bf6d592a" > upload_win.txt
┌─[eu-academy-1]─[10.10.14.184]─[htb-ac-2162140@htb-efv5zomuca]─[~]
└──╼ [★]$ cat upload_win.txt 
e4feec466d5de701089b5cc1bf6d592a
```
```bash
xfreerdp /v:10.129.201.55 /u:htb-student /p:'HTB_@cademy_stdnt!' /dynamic-resolution /cert:ignore
```
Then open Windows Powershell:
```powershell
PS C:\Users\htb-student> [IO.File]::WriteAllBytes("C:\Users\htb-student\upload.zip", [Convert]::FromBase64String("UE
oAAAAAAFmEKVFHXocmIAAAACAAAAAOAAAAdXBsb2FkX3dpbi50eHRlNGZlZWM0NjZkNWRlNzAxMDg5YjVjYzFiZjZkNTkyYVBLAQI/AAoAAAAAAFmEKV
cmIAAAACAAAAAOACQAAAAAAAAAIAAAAAAAAAB1cGxvYWRfd2luLnR4dAoAIAAAAAAAAQAYAHjm8KnohtYBzETj5fqG1gEXkIab6IbWAVBLBQYAAAAAAQ
AAAABMAAAAAAA="))
PS C:\Users\htb-student> Get-FileHash C:\Users\htb-student\upload.zip -Algorithm md5
>>

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             2EDF25B27B268445694276C20D55449E                                       C:\Users\htb-student\upload.z

PS C:\Users\htb-student> Expand-Archive -Path "C:\Users\htb-student\upload.zip" -DestinationPath "C:\Users\htb-stude
-Force
PS C:\Users\htb-student> ls


    Directory: C:\Users\htb-student


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---         9/9/2020   1:55 PM                Contacts
d-r---         9/9/2020   1:56 PM                Desktop
d-r---         9/9/2020   1:55 PM                Documents
d-r---         9/9/2020   1:55 PM                Downloads
d-r---         9/9/2020   1:55 PM                Favorites
d-r---         9/9/2020   1:55 PM                Links
d-r---         9/9/2020   1:55 PM                Music
d-r---         9/9/2020   1:55 PM                Pictures
d-r---         9/9/2020   1:55 PM                Saved Games
d-r---         9/9/2020   1:55 PM                Searches
d-r---         9/9/2020   1:55 PM                Videos
-a----        7/27/2026  12:19 AM            194 upload.zip
-a----         9/9/2020   4:34 PM             32 upload_win.txt


PS C:\Users\htb-student> hasher upload_win.txt
f458303ea783c224c6b4e7ef7f17eb9d
PS C:\Users\htb-student>
```


**Answer:** `f458303ea783c224c6b4e7ef7f17eb9d`

---

[Back to Module Index](./README.md)
