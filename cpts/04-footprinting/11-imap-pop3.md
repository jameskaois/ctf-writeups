# Section 11: IMAP / POP3

Module: 04. Footprinting

---

## Questions & Answers

### 1. Figure out the exact organization name from the IMAP/POP3 service and submit it as the answer.

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ sudo nmap 10.129.134.70 -sV -p110,143,993,995 -sC
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 21:38 EDT
Nmap scan report for 10.129.134.70
Host is up (0.16s latency).

PORT    STATE SERVICE  VERSION
110/tcp open  pop3     Dovecot pop3d
|_pop3-capabilities: TOP RESP-CODES UIDL SASL PIPELINING STLS AUTH-RESP-CODE CAPA
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_ssl-date: TLS randomness does not represent time
143/tcp open  imap     Dovecot imapd
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: IMAP4rev1 more STARTTLS Pre-login have post-login listed SASL-IR ID LOGINDISABLEDA0001 OK capabilities LOGIN-REFERRALS LITERAL+ ENABLE IDLE
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
993/tcp open  ssl/imap Dovecot imapd
|_imap-capabilities: IMAP4rev1 ENABLE Pre-login AUTH=PLAINA0001 post-login more SASL-IR ID have listed capabilities OK LITERAL+ LOGIN-REFERRALS IDLE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
995/tcp open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: TOP RESP-CODES UIDL SASL(PLAIN) PIPELINING USER AUTH-RESP-CODE CAPA
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.71 seconds
```

**Answer:** `InlaneFreight Ltd`

---

### 2. What is the FQDN that the IMAP and POP3 servers are assigned to?\

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ sudo nmap 10.129.134.70 -sV -p110,143,993,995 -sC
Starting Nmap 7.95 ( https://nmap.org ) at 2026-07-23 21:38 EDT
Nmap scan report for 10.129.134.70
Host is up (0.16s latency).

PORT    STATE SERVICE  VERSION
110/tcp open  pop3     Dovecot pop3d
|_pop3-capabilities: TOP RESP-CODES UIDL SASL PIPELINING STLS AUTH-RESP-CODE CAPA
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_ssl-date: TLS randomness does not represent time
143/tcp open  imap     Dovecot imapd
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: IMAP4rev1 more STARTTLS Pre-login have post-login listed SASL-IR ID LOGINDISABLEDA0001 OK capabilities LOGIN-REFERRALS LITERAL+ ENABLE IDLE
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
993/tcp open  ssl/imap Dovecot imapd
|_imap-capabilities: IMAP4rev1 ENABLE Pre-login AUTH=PLAINA0001 post-login more SASL-IR ID have listed capabilities OK LITERAL+ LOGIN-REFERRALS IDLE
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
995/tcp open  ssl/pop3 Dovecot pop3d
|_pop3-capabilities: TOP RESP-CODES UIDL SASL(PLAIN) PIPELINING USER AUTH-RESP-CODE CAPA
| ssl-cert: Subject: commonName=dev.inlanefreight.htb/organizationName=InlaneFreight Ltd/stateOrProvinceName=London/countryName=UK
| Not valid before: 2021-11-08T23:10:05
|_Not valid after:  2295-08-23T23:10:05
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 19.71 seconds
```

**Answer:** `dev.inlanefreight.htb`

---

### 3. Enumerate the IMAP service and submit the flag as the answer. (Format: HTB{...})

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ openssl s_client -connect 10.129.134.70:imaps
Connecting to 10.129.134.70
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify error:num=18:self-signed certificate
verify return:1
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify return:1
---
Certificate chain
 0 s:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   i:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Nov  8 23:10:05 2021 GMT; NotAfter: Aug 23 23:10:05 2295 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEUzCCAzugAwIBAgIUDf35PqFuv6Uv0EECM8dFmNSZoY8wDQYJKoZIhvcNAQEL
BQAwgbcxCzAJBgNVBAYTAlVLMQ8wDQYDVQQIDAZMb25kb24xDzANBgNVBAcMBkxv
bmRvbjEaMBgGA1UECgwRSW5sYW5lRnJlaWdodCBMdGQxHDAaBgNVBAsME0Rldk9w
cyBEZXDDg2FydG1lbnQxHjAcBgNVBAMMFWRldi5pbmxhbmVmcmVpZ2h0Lmh0YjEs
MCoGCSqGSIb3DQEJARYdY3RvLmRldkBkZXYuaW5sYW5lZnJlaWdodC5odGIwIBcN
MjExMTA4MjMxMDA1WhgPMjI5NTA4MjMyMzEwMDVaMIG3MQswCQYDVQQGEwJVSzEP
MA0GA1UECAwGTG9uZG9uMQ8wDQYDVQQHDAZMb25kb24xGjAYBgNVBAoMEUlubGFu
ZUZyZWlnaHQgTHRkMRwwGgYDVQQLDBNEZXZPcHMgRGVww4NhcnRtZW50MR4wHAYD
VQQDDBVkZXYuaW5sYW5lZnJlaWdodC5odGIxLDAqBgkqhkiG9w0BCQEWHWN0by5k
ZXZAZGV2LmlubGFuZWZyZWlnaHQuaHRiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAxvMwFE6m+iBUSujb5d6DUy1xDYR5awzQRwddyvq6iBrMxbnptSrn
+j0UOKWHCOpD5LREwP26ghUg0lVJzfo+v5pQJGnxEXKg0OFlzWEd8xgx/JWW/z1/
rDsWlNa2yYZkCy68YWJlC7UZxvcDFrI0V0pDJIkrjForw26laoYDkrh1A5F8uUXD
1TwRLLYo+NGmtNHT3BADJpv6aFUZ4CGrqBQNi7XpsTZ948WLhUwQvWmebiK06Dai
TvMNKBctjWAiNI4xvq34W9hIUaPxT1JJzuujRslep6nHGHW00QEWTWgyOMYThc3b
HtKIHMfDLTUMz7s8RhVVwlWE6+ly1DMRgQIDAQABo1MwUTAdBgNVHQ4EFgQUGDTC
9B5KCKPWT7vXbnMunL/mEE4wHwYDVR0jBBgwFoAUGDTC9B5KCKPWT7vXbnMunL/m
EE4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEADh0v5XWCf3KO
atrWcoiIOC67Z0ZIO7yEF+fQo8z+Wx1dWzmCFVu7u4+l7slcdJICCGBbOX8eItWS
chwzgnWJToyX8PWY8lSaB8ifMDQcr457Y7O6NmvgU35sRcLnYYqXzu2oh0lxsFLR
vL1wpyDLPhhoI++j1fELhiJ3GWiUQrb0vfJPcbSkHTgzf0hm7mLJTaqt3WfS/Gr2
8Oh7vSfzvqvHLE7HHAO0G5Q81zo+wWsrQF0s40HEF/raEMfOy2Htm79YjyjAlLWf
ueS+u8rX2smOYdRIpL3UPx7+yZPGu47vYoetde1Z5cfTCgmeS05BQ2qMOp6Tw6+G
xUuqg8nK1Q==
-----END CERTIFICATE-----
subject=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
issuer=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: rsa_pss_rsae_sha256
Peer Temp Key: X25519, 253 bits
---
SSL handshake has read 1667 bytes and written 1613 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol: TLSv1.3
Server public key is 2048 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: F964B78CD7BDF3B64A96BFCB25C133D8969914D28608D566AD3FF6F2291C30FB
    Session-ID-ctx: 
    Resumption PSK: 57021D842BA014AD681CCD6A082184C05D6C97CA2BB990097F7C68CA7F5F5FC9ABDA6B494552845CDEBDE2FFEE9E5E4B
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - fd 7c 10 c2 22 bf 13 86-8b 3b d6 95 a6 09 d5 7a   .|.."....;.....z
    0010 - 80 4e 10 32 11 af 08 ca-cf 37 31 b4 e8 a5 5f 33   .N.2.....71..._3
    0020 - 0c 7f 3d bd 0c 79 5d b9-ac 58 bd 58 12 f4 31 dd   ..=..y]..X.X..1.
    0030 - 73 48 8e 52 e4 d1 f8 67-ef 80 91 d1 b4 1b 50 4f   sH.R...g......PO
    0040 - 29 fb da 99 12 44 52 0a-e4 dc d3 8e 13 bc 7f 1c   )....DR.........
    0050 - 1e 74 b2 ea d9 47 09 53-ea fc fe 16 e1 06 a3 ce   .t...G.S........
    0060 - 6f 41 ea 5f 8f 76 ad 7c-65 e0 12 da d4 5d d4 99   oA._.v.|e....]..
    0070 - fb 79 9c 81 62 86 dd 51-13 d8 44 55 27 47 bc a6   .y..b..Q..DU'G..
    0080 - ec f7 06 9b 48 a0 8f c2-f4 1a 69 98 a6 76 22 ba   ....H.....i..v".
    0090 - ed 3f a6 3a ac f9 9a f7-28 c4 1e d4 4f b4 1d 90   .?.:....(...O...
    00a0 - 43 90 7f ba 05 01 16 4f-c5 87 6d 0c 73 d9 45 36   C......O..m.s.E6
    00b0 - dc 43 a2 6f 3d ab 4b be-a7 f5 0d 7d 3e 82 7e 82   .C.o=.K....}>.~.

    Start Time: 1784857277
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: EBDF129E5C6875185442CF66515A3AB8FB14E6A47543F5A59911DCB2CCC6D1B9
    Session-ID-ctx: 
    Resumption PSK: 3A664CCDE4FBFFE9D5BC6615D9D10981B93EA3187DA4DC714C994EB2474E462EDF3331B9445654CBB77616C95CB53DAD
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - fd 7c 10 c2 22 bf 13 86-8b 3b d6 95 a6 09 d5 7a   .|.."....;.....z
    0010 - ef e1 6a 5f 56 42 0d 3e-11 86 80 2c 78 18 8e 4d   ..j_VB.>...,x..M
    0020 - 74 24 bc 3e c6 f3 11 aa-9f c7 4a 95 a8 88 ca 9e   t$.>......J.....
    0030 - 9c 2a 52 dd fb a0 2c 8e-14 2d 3d b2 64 0f 3a 99   .*R...,..-=.d.:.
    0040 - 3e 5b 1d ec 36 a1 0b 38-cf 30 3a 84 d3 43 e2 75   >[..6..8.0:..C.u
    0050 - 54 c6 f1 29 60 1a 85 3f-2b a6 6e 8f 23 b3 43 3a   T..)`..?+.n.#.C:
    0060 - e4 6e 78 ac 8d 98 3b c2-aa f3 a3 ae b2 4f ed e5   .nx...;......O..
    0070 - 8b 14 a4 2b 4e db 3e cc-66 22 4e 89 28 ea 56 28   ...+N.>.f"N.(.V(
    0080 - 04 ad 09 5d 3e 79 5e 7f-08 c3 80 e5 d9 be aa 4f   ...]>y^........O
    0090 - 7c c2 08 ec bf 1c f4 34-c6 38 aa 32 48 6b 3c cc   |......4.8.2Hk<.
    00a0 - be dd a3 bd 66 06 7e 0b-25 d9 6d e0 db 1d 67 79   ....f.~.%.m...gy
    00b0 - 65 61 80 c2 b2 12 24 76-9a 45 82 04 63 e9 c5 12   ea....$v.E..c...

    Start Time: 1784857277
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN] HTB{roncfbw7iszerd7shni7jr2343zhrj}
```

**Answer:** `HTB{roncfbw7iszerd7shni7jr2343zhrj}`

---

### 4. What is the customized version of the POP3 server?

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ openssl s_client -connect 10.129.134.70:pop3s
Connecting to 10.129.134.70
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify error:num=18:self-signed certificate
verify return:1
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify return:1
---
Certificate chain
 0 s:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   i:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Nov  8 23:10:05 2021 GMT; NotAfter: Aug 23 23:10:05 2295 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEUzCCAzugAwIBAgIUDf35PqFuv6Uv0EECM8dFmNSZoY8wDQYJKoZIhvcNAQEL
BQAwgbcxCzAJBgNVBAYTAlVLMQ8wDQYDVQQIDAZMb25kb24xDzANBgNVBAcMBkxv
bmRvbjEaMBgGA1UECgwRSW5sYW5lRnJlaWdodCBMdGQxHDAaBgNVBAsME0Rldk9w
cyBEZXDDg2FydG1lbnQxHjAcBgNVBAMMFWRldi5pbmxhbmVmcmVpZ2h0Lmh0YjEs
MCoGCSqGSIb3DQEJARYdY3RvLmRldkBkZXYuaW5sYW5lZnJlaWdodC5odGIwIBcN
MjExMTA4MjMxMDA1WhgPMjI5NTA4MjMyMzEwMDVaMIG3MQswCQYDVQQGEwJVSzEP
MA0GA1UECAwGTG9uZG9uMQ8wDQYDVQQHDAZMb25kb24xGjAYBgNVBAoMEUlubGFu
ZUZyZWlnaHQgTHRkMRwwGgYDVQQLDBNEZXZPcHMgRGVww4NhcnRtZW50MR4wHAYD
VQQDDBVkZXYuaW5sYW5lZnJlaWdodC5odGIxLDAqBgkqhkiG9w0BCQEWHWN0by5k
ZXZAZGV2LmlubGFuZWZyZWlnaHQuaHRiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAxvMwFE6m+iBUSujb5d6DUy1xDYR5awzQRwddyvq6iBrMxbnptSrn
+j0UOKWHCOpD5LREwP26ghUg0lVJzfo+v5pQJGnxEXKg0OFlzWEd8xgx/JWW/z1/
rDsWlNa2yYZkCy68YWJlC7UZxvcDFrI0V0pDJIkrjForw26laoYDkrh1A5F8uUXD
1TwRLLYo+NGmtNHT3BADJpv6aFUZ4CGrqBQNi7XpsTZ948WLhUwQvWmebiK06Dai
TvMNKBctjWAiNI4xvq34W9hIUaPxT1JJzuujRslep6nHGHW00QEWTWgyOMYThc3b
HtKIHMfDLTUMz7s8RhVVwlWE6+ly1DMRgQIDAQABo1MwUTAdBgNVHQ4EFgQUGDTC
9B5KCKPWT7vXbnMunL/mEE4wHwYDVR0jBBgwFoAUGDTC9B5KCKPWT7vXbnMunL/m
EE4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEADh0v5XWCf3KO
atrWcoiIOC67Z0ZIO7yEF+fQo8z+Wx1dWzmCFVu7u4+l7slcdJICCGBbOX8eItWS
chwzgnWJToyX8PWY8lSaB8ifMDQcr457Y7O6NmvgU35sRcLnYYqXzu2oh0lxsFLR
vL1wpyDLPhhoI++j1fELhiJ3GWiUQrb0vfJPcbSkHTgzf0hm7mLJTaqt3WfS/Gr2
8Oh7vSfzvqvHLE7HHAO0G5Q81zo+wWsrQF0s40HEF/raEMfOy2Htm79YjyjAlLWf
ueS+u8rX2smOYdRIpL3UPx7+yZPGu47vYoetde1Z5cfTCgmeS05BQ2qMOp6Tw6+G
xUuqg8nK1Q==
-----END CERTIFICATE-----
subject=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
issuer=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: rsa_pss_rsae_sha256
Peer Temp Key: X25519, 253 bits
---
SSL handshake has read 1667 bytes and written 1613 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol: TLSv1.3
Server public key is 2048 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 7D998D5A82E4ED5D35DECBF5FCDA18E4B7AD0E57518DB64CA12F3EBE8576FDE4
    Session-ID-ctx: 
    Resumption PSK: E5566D846B98FAA95F2301FB12590CF880B9F5226A437C8752BFEFB154E03D58CAA1E6E7D59742AAC6F38BB067BAB053
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 3e 1f f0 9b f7 23 bd 8b-0a 67 e4 dd e8 a5 70 a3   >....#...g....p.
    0010 - 78 c2 d8 6c f1 16 b1 83-97 0e b3 8f 8a eb db 9f   x..l............
    0020 - 54 19 91 f8 d4 f2 a7 6e-15 59 45 c5 3a 79 ba 82   T......n.YE.:y..
    0030 - 34 4c 1c 54 2d 0e 6c e7-1a d5 ab a2 0b ed 2f a4   4L.T-.l......./.
    0040 - e8 50 e0 41 1e f5 35 a3-cb d5 2b 69 6f db be 6f   .P.A..5...+io..o
    0050 - fd a6 56 32 5a 4a c8 a1-ba eb fd 33 29 a2 8e ed   ..V2ZJ.....3)...
    0060 - c5 79 62 54 e3 19 bc 90-07 e0 9c 20 65 af e1 b7   .ybT....... e...
    0070 - 61 2f b3 eb e7 b5 47 ab-bf 8d 77 e6 97 10 e3 70   a/....G...w....p
    0080 - 89 aa dc 50 16 4d 2d 83-40 61 87 3d 56 56 34 4a   ...P.M-.@a.=VV4J
    0090 - 0a 71 dd 70 33 b0 0a aa-cf 4b aa 5c 17 8a ab 31   .q.p3....K.\...1
    00a0 - 40 22 31 d7 b9 ce 32 60-83 c1 24 c9 1a 84 3c 50   @"1...2`..$...<P
    00b0 - ae ff f9 77 7f 14 b6 30-8f 14 a8 9f 67 bf 99 3e   ...w...0....g..>

    Start Time: 1784857361
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: C9948F7070B2B89D1D44A8461D8805B9C90EB761B936A7EE1B62877F2447DA24
    Session-ID-ctx: 
    Resumption PSK: 52940A6192669AA69E1B0933590944B6F5B0A095F1987A9740C0CB5B0EA093A6B042F9B429CEDBD443FA95534DF25D6D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 3e 1f f0 9b f7 23 bd 8b-0a 67 e4 dd e8 a5 70 a3   >....#...g....p.
    0010 - 7e 94 cc 8a 55 a1 68 a0-a7 87 6e c4 31 cc 15 31   ~...U.h...n.1..1
    0020 - 71 99 da 49 d3 a2 5e 0f-de b3 3e 15 bd 16 17 d3   q..I..^...>.....
    0030 - 62 77 54 5e 95 e2 66 e2-a3 2e 41 3e 56 db 4e 8b   bwT^..f...A>V.N.
    0040 - d9 e2 89 6d 0f cb 13 85-61 2b e4 4d fd 45 64 60   ...m....a+.M.Ed`
    0050 - d0 a2 84 7d 14 ce 69 2a-4c 9b 68 a8 17 21 e1 da   ...}..i*L.h..!..
    0060 - aa be fb b2 02 3a 6c 42-ad 58 d3 2b c6 37 3d 74   .....:lB.X.+.7=t
    0070 - a5 3a c0 38 a2 38 41 79-07 f9 59 a0 d9 a1 2d ef   .:.8.8Ay..Y...-.
    0080 - b7 88 8e ec 2d 25 db aa-a1 1d 03 86 bb 74 eb f0   ....-%.......t..
    0090 - b6 8b bd 47 4c c0 6e e4-fb 4b e8 7a a8 3a d0 2b   ...GL.n..K.z.:.+
    00a0 - cb 38 79 3d 8c 66 b4 ac-cd 54 f4 7b dc fe 6e de   .8y=.f...T.{..n.
    00b0 - 99 03 6a ef 51 fb 67 5e-06 7b af c3 66 0d c0 c0   ..j.Q.g^.{..f...

    Start Time: 1784857361
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
+OK InFreight POP3 v9.188
```

**Answer:** `InFreight POP3 v9.188`

---

### 5. What is the admin email address?

Context:
```bash
┌─[eu-academy-1]─[10.10.14.112]─[htb-ac-2162140@htb-mntqrvxduq]─[~]
└──╼ [★]$ openssl s_client -connect 10.129.134.70:993 -crlf
Connecting to 10.129.134.70
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify error:num=18:self-signed certificate
verify return:1
depth=0 C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
verify return:1
---
Certificate chain
 0 s:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   i:C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
   a:PKEY: RSA, 2048 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Nov  8 23:10:05 2021 GMT; NotAfter: Aug 23 23:10:05 2295 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIEUzCCAzugAwIBAgIUDf35PqFuv6Uv0EECM8dFmNSZoY8wDQYJKoZIhvcNAQEL
BQAwgbcxCzAJBgNVBAYTAlVLMQ8wDQYDVQQIDAZMb25kb24xDzANBgNVBAcMBkxv
bmRvbjEaMBgGA1UECgwRSW5sYW5lRnJlaWdodCBMdGQxHDAaBgNVBAsME0Rldk9w
cyBEZXDDg2FydG1lbnQxHjAcBgNVBAMMFWRldi5pbmxhbmVmcmVpZ2h0Lmh0YjEs
MCoGCSqGSIb3DQEJARYdY3RvLmRldkBkZXYuaW5sYW5lZnJlaWdodC5odGIwIBcN
MjExMTA4MjMxMDA1WhgPMjI5NTA4MjMyMzEwMDVaMIG3MQswCQYDVQQGEwJVSzEP
MA0GA1UECAwGTG9uZG9uMQ8wDQYDVQQHDAZMb25kb24xGjAYBgNVBAoMEUlubGFu
ZUZyZWlnaHQgTHRkMRwwGgYDVQQLDBNEZXZPcHMgRGVww4NhcnRtZW50MR4wHAYD
VQQDDBVkZXYuaW5sYW5lZnJlaWdodC5odGIxLDAqBgkqhkiG9w0BCQEWHWN0by5k
ZXZAZGV2LmlubGFuZWZyZWlnaHQuaHRiMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A
MIIBCgKCAQEAxvMwFE6m+iBUSujb5d6DUy1xDYR5awzQRwddyvq6iBrMxbnptSrn
+j0UOKWHCOpD5LREwP26ghUg0lVJzfo+v5pQJGnxEXKg0OFlzWEd8xgx/JWW/z1/
rDsWlNa2yYZkCy68YWJlC7UZxvcDFrI0V0pDJIkrjForw26laoYDkrh1A5F8uUXD
1TwRLLYo+NGmtNHT3BADJpv6aFUZ4CGrqBQNi7XpsTZ948WLhUwQvWmebiK06Dai
TvMNKBctjWAiNI4xvq34W9hIUaPxT1JJzuujRslep6nHGHW00QEWTWgyOMYThc3b
HtKIHMfDLTUMz7s8RhVVwlWE6+ly1DMRgQIDAQABo1MwUTAdBgNVHQ4EFgQUGDTC
9B5KCKPWT7vXbnMunL/mEE4wHwYDVR0jBBgwFoAUGDTC9B5KCKPWT7vXbnMunL/m
EE4wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOCAQEADh0v5XWCf3KO
atrWcoiIOC67Z0ZIO7yEF+fQo8z+Wx1dWzmCFVu7u4+l7slcdJICCGBbOX8eItWS
chwzgnWJToyX8PWY8lSaB8ifMDQcr457Y7O6NmvgU35sRcLnYYqXzu2oh0lxsFLR
vL1wpyDLPhhoI++j1fELhiJ3GWiUQrb0vfJPcbSkHTgzf0hm7mLJTaqt3WfS/Gr2
8Oh7vSfzvqvHLE7HHAO0G5Q81zo+wWsrQF0s40HEF/raEMfOy2Htm79YjyjAlLWf
ueS+u8rX2smOYdRIpL3UPx7+yZPGu47vYoetde1Z5cfTCgmeS05BQ2qMOp6Tw6+G
xUuqg8nK1Q==
-----END CERTIFICATE-----
subject=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
issuer=C=UK, ST=London, L=London, O=InlaneFreight Ltd, OU=DevOps DepÃartment, CN=dev.inlanefreight.htb, emailAddress=cto.dev@dev.inlanefreight.htb
---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: rsa_pss_rsae_sha256
Peer Temp Key: X25519, 253 bits
---
SSL handshake has read 1667 bytes and written 1613 bytes
Verification error: self-signed certificate
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Protocol: TLSv1.3
Server public key is 2048 bit
This TLS version forbids renegotiation.
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 18 (self-signed certificate)
---
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: 6A3CC4BACB04A730E8F6DB0525151F2CDE60F931B8D8B7C2E9E84F71A37163B0
    Session-ID-ctx: 
    Resumption PSK: 309B9D1A418F747AD4B5DCBE2CFBC8B674110C55A449D7A801A827210F91FA89480E289162870ACD155E42D53C03D2C8
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 45 f9 23 af 95 78 5a 38-0b 2d 20 1e af e1 70 ba   E.#..xZ8.- ...p.
    0010 - 5c 7d cc f8 62 44 a5 ca-cb 61 26 44 17 0c c0 39   \}..bD...a&D...9
    0020 - 74 79 f7 d5 e1 fc 36 1f-c0 40 8f 7e cd 48 95 b8   ty....6..@.~.H..
    0030 - 18 4d d2 8a 91 1a f8 a0-dc cc bd 66 c7 3e 2c 79   .M.........f.>,y
    0040 - 72 f0 81 1b 3b 4a 96 9c-bf c4 ef 64 5f cc 50 b8   r...;J.....d_.P.
    0050 - 35 b8 81 d4 88 ce 57 a6-9d d7 4b 72 a0 ec a2 c4   5.....W...Kr....
    0060 - fa c8 15 c2 f9 59 f6 79-71 d2 a3 7c 55 02 ca 1a   .....Y.yq..|U...
    0070 - bc b1 76 32 e1 c8 62 9a-b7 b4 fe 80 d7 7d 42 4a   ..v2..b......}BJ
    0080 - 12 ce 1b a6 c7 8b 62 c1-c6 42 77 ac 5e 30 cb 61   ......b..Bw.^0.a
    0090 - a6 7e 31 93 0d d6 a7 1d-35 62 56 a8 c4 a6 53 f8   .~1.....5bV...S.
    00a0 - e8 c1 6f 92 b8 16 61 0d-7d 21 0d 8e 65 c7 1d 0d   ..o...a.}!..e...
    00b0 - e1 2b 0a 27 a5 1f 21 07-a7 30 ce 99 1c 48 1c dc   .+.'..!..0...H..

    Start Time: 1784857721
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
---
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
    Session-ID: B3BCAEE1A9167945CCE3D5F3027C2B463CFF5CF5FA5534BD0BB4930EA9CE126B
    Session-ID-ctx: 
    Resumption PSK: 794673A979CD7DEAF24470A76F04B8DFE3670EA5AF02C98EC67202A39FAB075FA9EC99F60FDDDA68A03F7582A6DFCD1E
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 45 f9 23 af 95 78 5a 38-0b 2d 20 1e af e1 70 ba   E.#..xZ8.- ...p.
    0010 - 49 2c 9d 54 66 0b 99 5c-a2 a7 16 36 e1 74 17 19   I,.Tf..\...6.t..
    0020 - 7c aa 4a 32 2b 55 12 8d-00 30 08 4b 23 ad 1c 8e   |.J2+U...0.K#...
    0030 - d5 1c 95 00 56 60 71 d8-2c c5 01 a6 40 aa 83 b7   ....V`q.,...@...
    0040 - 89 6c 50 0b 45 c0 17 04-74 76 e2 a5 65 9a 88 c9   .lP.E...tv..e...
    0050 - bc 9a b7 2d c1 39 2b 4f-92 c8 72 95 da 90 5a 0e   ...-.9+O..r...Z.
    0060 - a0 00 14 d8 5a 8d a3 32-e3 f7 96 71 94 cc 39 15   ....Z..2...q..9.
    0070 - cb ec 19 fb b5 7e d3 25-09 c8 1f 99 ac 45 b7 7d   .....~.%.....E.}
    0080 - 82 39 0f a2 0c df cc 1b-9d 4e 83 d3 9c 7c e6 9b   .9.......N...|..
    0090 - c0 35 d7 9c a2 8f e2 0a-20 d5 01 c0 a6 90 39 20   .5...... .....9 
    00a0 - af 84 88 37 7f 4d c9 cb-2f 11 7c a2 b3 a9 05 e9   ...7.M../.|.....
    00b0 - ef 78 76 8e 5a 02 99 3c-44 c0 56 3a 4c a5 8f 62   .xv.Z..<D.V:L..b

    Start Time: 1784857721
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
    Max Early Data: 0
---
read R BLOCK
* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ AUTH=PLAIN] HTB{roncfbw7iszerd7shni7jr2343zhrj}
A1 LOGIN robin robin
A1 OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY LITERAL+ NOTIFY SPECIAL-USE] Logged in
A2 LIST "" "*"
* LIST (\Noselect \HasChildren) "." DEV
* LIST (\Noselect \HasChildren) "." DEV.DEPARTMENT
* LIST (\HasNoChildren) "." DEV.DEPARTMENT.INT
* LIST (\HasNoChildren) "." INBOX
A2 OK List completed (0.001 + 0.000 secs).
A3 SELECT INBOX
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 0 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1636414280] UIDs valid
* OK [UIDNEXT 1] Predicted next UID
A3 OK [READ-WRITE] Select completed (0.005 + 0.000 + 0.004 secs).
A4 FETCH 1:* (FLAGS BODY[HEADER.FIELDS (FROM SUBJECT DATE)])
A4 BAD Error in IMAP command FETCH: Invalid messageset (0.001 + 0.000 secs).
A3 SELECT DEV.DEPARTMENT.INT
* OK [CLOSED] Previous mailbox closed.
* FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
* OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
* 1 EXISTS
* 0 RECENT
* OK [UIDVALIDITY 1636414279] UIDs valid
* OK [UIDNEXT 2] Predicted next UID
A3 OK [READ-WRITE] Select completed (0.009 + 0.000 + 0.009 secs).
A4 FETCH 1:* (FLAGS BODY[HEADER.FIELDS (FROM SUBJECT DATE)])
* 1 FETCH (FLAGS (\Seen) BODY[HEADER.FIELDS (FROM SUBJECT DATE)] {96}
Subject: Flag
From: CTO <devadmin@inlanefreight.htb>
Date: Wed, 03 Nov 2021 16:13:27 +0200

)
A4 OK Fetch completed (0.006 + 0.000 + 0.005 secs).
```

**Answer:** `devadmin@inlanefreight.htb`

---

### 6. Try to access the emails on the IMAP server and submit the flag as the answer. (Format: HTB{...})

Context:
```bash
A5 FETCH 1 BODY[]
* 1 FETCH (BODY[] {167}
Subject: Flag
To: Robin <robin@inlanefreight.htb>
From: CTO <devadmin@inlanefreight.htb>
Date: Wed, 03 Nov 2021 16:13:27 +0200

HTB{983uzn8jmfgpd8jmof8c34n7zio}
)
A5 OK Fetch completed (0.002 + 0.000 + 0.001 secs).
```

**Answer:** `HTB{983uzn8jmfgpd8jmof8c34n7zio}`

---

[Back to Module Index](./README.md)
