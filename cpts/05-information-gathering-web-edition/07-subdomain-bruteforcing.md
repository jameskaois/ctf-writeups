# Section 07: Subdomain Bruteforcing

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. Using the known subdomains for inlanefreight.com (www, ns1, ns2, ns3, blog, support, customer), find any missing subdomains by brute-forcing possible domain names. Provide your answer with the complete subdomain, e.g., www.inlanefreight.com.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Downloads]
└─$ dnsenum --enum inlanefreight.com -f /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt
dnsenum VERSION:1.3.1

-----   inlanefreight.com   -----                                                                                                  
                                                                                                                                   
                                                                                                                                   
Host's addresses:                                                                                                                  
__________________                                                                                                                 
                                                                                                                                   
inlanefreight.com.                       300      IN    A        134.209.24.248                                                    

                                                                                                                                   
Name Servers:                                                                                                                      
______________                                                                                                                     
                                                                                                                                   
ns1.inlanefreight.com.                   300      IN    A        178.128.39.165                                                    
ns2.inlanefreight.com.                   300      IN    A        206.189.119.186

                                                                                                                                   
Mail (MX) Servers:                                                                                                                 
___________________                                                                                                                
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
Trying Zone Transfers and getting Bind Versions:                                                                                   
_________________________________________________                                                                                  
                                                                                                                                   
                                                                                                                                   
Trying Zone Transfer for inlanefreight.com on ns1.inlanefreight.com ... 
AXFR record query failed: Connection timed out

Trying Zone Transfer for inlanefreight.com on ns2.inlanefreight.com ... 
AXFR record query failed: Connection timed out

                                                                                                                                   
Scraping inlanefreight.com subdomains from Google:                                                                                 
___________________________________________________                                                                                
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
Brute forcing with /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt:                                             
_______________________________________________________________________________________                                            
                                                                                                                                   
www.inlanefreight.com.                   300      IN    A        134.209.24.248                                                    
ns2.inlanefreight.com.                   264      IN    A        206.189.119.186
ns1.inlanefreight.com.                   300      IN    A        178.128.39.165
blog.inlanefreight.com.                  300      IN    A        134.209.24.248
ns3.inlanefreight.com.                   300      IN    A        134.209.24.248
support.inlanefreight.com.               300      IN    A        134.209.24.248
my.inlanefreight.com.                    300      IN    A        134.209.24.248
```
**Answer:** `my.inlanefreight.com`

---

[Back to Module Index](./README.md)
