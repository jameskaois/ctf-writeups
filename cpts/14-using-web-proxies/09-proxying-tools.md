# Section 09: Proxying Tools

Module: 14. Using Web Proxies

---

## Questions & Answers

### 1. Try running 'auxiliary/scanner/http/http_put' in Metasploit on any website, while routing the traffic through Burp. Once you view the requests sent, what is the last line in the request?

Context:
- Run Metasploit
```bash
┌─[eu-academy-2]─[10.10.14.91]─[htb-ac-2162140@htb-rfpvkxbcle-htb-cloud-com]─[~]
└──╼ [★]$ msfconsole -q
[msf](Jobs:0 Agents:0) >> use auxiliary/scanner/http/http_put
[*] Setting default action PUT - view all 2 actions with the show actions command
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/http_put) >> set PROXIES HTTP:127.0.0.1:8080
PROXIES => HTTP:127.0.0.1:8080
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/http_put) >> set RHOST SERVER_[msf](Jobs:0 Agents:0) auxiliary(scanner/http/http_put) >> set RHOST SERVER_IP
RHOST => SERVER_IP
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/http_put) >> set RPORT PORT
[-] The following options failed to validate: Value 'PORT' is not valid for option 'RPORT'.
RPORT => 80
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/http_put) >> run
[-] SERVER_IP: File doesn't seem to exist. The upload probably failed
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
[msf](Jobs:0 Agents:0) auxiliary(scanner/http/http_put) >> 
```
- In Burp Suite captured request:
```
PUT /msf_http_put_test.txt HTTP/1.1
Host: SERVER_IP
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36
Content-Type: text/plain
Content-Length: 13
Connection: keep-alive

msf test file
```

**Answer:** `msf test file`

---

[Back to Module Index](./README.md)
