url = "http://dreamhack.io@127.0.0.1:8000/api/v1/test/internal?bypass=true"

ALLOWED_HOSTS = ['dreamhack.io', 'tools.dreamhack.io']

for host in ALLOWED_HOSTS:
        if url.startswith('http://' + host):
            break

        print('NOT PASS HOST CHECK')

if url.endswith('/test/internal'):
    print('NOT PASS ENDPOINT CHECK')
