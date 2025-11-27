url = "file:///app/flag.txt"

def get_host_port(url):
    return url.split('://')[1].split('/')[0].lower().split(':')

(host, port) = get_host_port(url)
if 'localhost' == host:
    print('cant use localhost\n'.encode())
if 'dreamhack.io' != host:
    if '.' in host:
        print('cant use .\n'.encode())
        