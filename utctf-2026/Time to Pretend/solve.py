
import time
import requests

BASE_URL = "http://challenge.utctf.live:9382"
TARGET_USERNAME = "timothy"

def generate_otp(username, epoch_time):
    add_val = epoch_time % 26

    mults = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    mult_val = mults[epoch_time % 12]

    otp = ""
    for char in username.lower():
        if char.isalpha():
            idx = ord(char) - ord('a')
            enc_idx = (idx * mult_val + add_val) % 26
            otp += chr(enc_idx + ord('a'))
        else:
            otp += char

    return otp

def main():
    session = requests.Session()

    current_epoch = int(time.time())
    otp = generate_otp(TARGET_USERNAME, current_epoch)

    payload = {
        "username": TARGET_USERNAME,
        "otp": otp
    }

    r_auth = session.post(f"{BASE_URL}/auth", json=payload)

    if r_auth.status_code == 200:

        r_portal = session.get(f"{BASE_URL}/portal")
        print(r_portal.text)
    else:
        print("Login failed")

if __name__ == "__main__":
    main()

