# Section 07: Cracking Protected Archives

Module: 10. Password Attacks

---

## Questions & Answers

### 1. Run the above target then navigate to http://ip:port/download, then extract the downloaded file. Inside, you will find a password-protected VHD file. Crack the password for the VHD and submit the recovered password as your answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ unzip cracking-protected-archives.zip 
Archive:  cracking-protected-archives.zip
  inflating: Private.vhd    
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ bitlocker2john -i Private.vhd > private.hashes

Signature found at 0x10003
Version: 8 
Invalid version, looking for a signature with valid version...

Signature found at 0x2200000
Version: 2 (Windows 7 or later)

VMK entry found at 0x22000bb

VMK encrypted with User Password found at 22000dc
VMK encrypted with AES-CCM

VMK entry found at 0x220019b

VMK encrypted with Recovery Password found at 0x22001bc
Searching AES-CCM from 0x22001d8
Trying offset 0x220026b....
VMK encrypted with AES-CCM!!

Signature found at 0x2956000
Version: 2 (Windows 7 or later)

VMK entry found at 0x29560bb

VMK entry found at 0x295619b

Signature found at 0x30ab000
Version: 2 (Windows 7 or later)

VMK entry found at 0x30ab0bb

VMK entry found at 0x30ab19b
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ grep "bitlocker\$0" private.hashes > private.hash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ cat private.hash
$bitlocker$0$16$b3c105c7ab7faaf544e84d712810da65$1048576$12$b020fe18bbb1db0103000000$60$e9c6b548788aeff190e517b0d85ada5daad7a0a3f40c4467307011ac17f79f8c99768419903025fd7072ee78b15a729afcf54b8c2e3af05bb18d4ba0
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ hashcat -a 0 -m 22100 '$bitlocker$0$16$b3c105c7ab7faaf544e84d712810da65$1048576$12$b020fe18bbb1db0103000000$60$e9c6b548788aeff190e517b0d85ada5daad7a0a3f40c4467307011ac17f79f8c99768419903025fd7072ee78b15a729afcf54b8c2e3af05bb18d4ba0' /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

/usr/share/wordlists/rockyou.txt: No such file or directory

Started: Tue Aug  4 07:56:21 2026
Stopped: Tue Aug  4 07:56:21 2026
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ ls /usr/share/wordlists/
brutespray  dnsmap.txt     john.lst    rockyou.txt.gz  wfuzz
dirb        fasttrack.txt  metasploit  seclists        wifite.txt
dirbuster   fern-wifi      nmap.lst    sqlmap.txt
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ gzip -d /usr/share/wordlists/rockyou.txt.gz 

gzip: /usr/share/wordlists/rockyou.txt: Permission denied
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo gzip -d /usr/share/wordlists/rockyou.txt.gz 
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ hashcat -a 0 -m 22100 '$bitlocker$0$16$b3c105c7ab7faaf544e84d712810da65$1048576$12$b020fe18bbb1db0103000000$60$e9c6b548788aeff190e517b0d85ada5daad7a0a3f40c4467307011ac17f79f8c99768419903025fd7072ee78b15a729afcf54b8c2e3af05bb18d4ba0' /usr/share/wordlists/rockyou.txt
hashcat (v6.2.6) starting

OpenCL API (OpenCL 2.1 LINUX) - Platform #1 [Intel(R) Corporation]
==================================================================
* Device #1: AMD EPYC 7543 32-Core Processor, 3921/7907 MB (988 MB allocatable), 4MCU

OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, SPIR-V, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #2 [The pocl project]
====================================================================================================================================================
* Device #2: cpu-haswell-AMD EPYC 7543 32-Core Processor, skipped

Minimum password length supported by kernel: 4
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Single-Hash
* Single-Salt
* Slow-Hash-SIMD-LOOP

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache building /usr/share/wordlists/rockyou.txt: 33553434 bytes (23.9Dictionary cache built:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344392
* Bytes.....: 139921507
* Keyspace..: 14344385
* Runtime...: 0 secs

$bitlocker$0$16$b3c105c7ab7faaf544e84d712810da65$1048576$12$b020fe18bbb1db0103000000$60$e9c6b548788aeff190e517b0d85ada5daad7a0a3f40c4467307011ac17f79f8c99768419903025fd7072ee78b15a729afcf54b8c2e3af05bb18d4ba0:francisco
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 22100 (BitLocker)
Hash.Target......: $bitlocker$0$16$b3c105c7ab7faaf544e84d712810da65$10...8d4ba0
Time.Started.....: Tue Aug  4 07:57:19 2026 (10 secs)
Time.Estimated...: Tue Aug  4 07:57:29 2026 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:       57 H/s (8.67ms) @ Accel:128 Loops:4096 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 512/14344385 (0.00%)
Rejected.........: 0/512 (0.00%)
Restore.Point....: 384/14344385 (0.00%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:1044480-1048576
Candidate.Engine.: Device Generator
Candidates.#1....: jeffrey -> letmein

Started: Tue Aug  4 07:57:02 2026
Stopped: Tue Aug  4 07:57:29 2026
```

**Answer:** `francisco`

---

### 2. Mount the BitLocker-encrypted VHD and enter the contents of flag.txt as your answer.

Context:
```bash
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo apt-get install dislocker
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
dislocker is already the newest version (0.7.3+git20240607-3+b1).
The following package was automatically installed and is no longer required:
  linux-image-6.12.73+deb13-amd64
Use 'sudo apt autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 499 not upgraded.
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo mkdir -p /media/bitlocker
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo mkdir -p /media/bitlockermount
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo losetup -f -P Private.vhd 
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo dislocker /dev/loop0p2 -ufrancisco -- /media/bitlocker
Tue Aug  4 07:58:54 2026 [CRITICAL] Failed to open /dev/loop0p2: No such file or directory
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo mount -o loop /media/bitlocker/dislocker-file /media/bitlockermount
mount: /media/bitlockermount: failed to setup loop device for /media/bitlocker/dislocker-file.
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ losetup -a
/dev/loop0: []: (/home/htb-ac-2162140/Downloads/Private.vhd)
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo dislocker /dev/loop0 -ufrancisco -- /media/bitlocker
Tue Aug  4 08:01:53 2026 [CRITICAL] Cannot parse volume header. Abort.
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo fdisk -lu /dev/loop0
Disk /dev/loop0: 64 MiB, 67109376 bytes, 131073 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x1d6fbd57

Device       Boot Start    End Sectors Size Id Type
/dev/loop0p1        128 125055  124928  61M  7 HPFS/NTFS/exFAT
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo dislocker /dev/loop0p1 -ufrancisco -- /media/bitlocker
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ sudo mount -o loop /media/bitlocker/dislocker-file /media/bitlockermount
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[~/Downloads]
└──╼ [★]$ cd /media/bitlockermount/
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[/media/bitlockermount]
└──╼ [★]$ ls -la
total 17
drwxrwxrwx 1 root root 4096 Apr 20  2025  .
drwxr-xr-x 5 root root 4096 Aug  4 07:58  ..
-rwxrwxrwx 1 root root   32 Apr 20  2025  flag.txt
drwxrwxrwx 1 root root 8192 Apr 20  2025 'System Volume Information'
┌─[eu-academy-2]─[10.10.14.98]─[htb-ac-2162140@htb-y3nt6hf04j]─[/media/bitlockermount]
└──╼ [★]$ cat flag.txt 
43d95aeed3114a53ac66f01265f9b7af
```

**Answer:** `43d95aeed3114a53ac66f01265f9b7af`

---

[Back to Module Index](./README.md)
