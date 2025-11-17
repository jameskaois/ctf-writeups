import hashlib, random, string

target = b"\x27\x2d\x2d"

chars = string.ascii_letters + string.digits

i = 0
while True:
    i += 1
    s = ''.join(random.choice(chars) for _ in range(8))
    h = hashlib.md5(s.encode()).digest()

    if target in h:
        print("FOUND:", s)
        print(h.hex())
        break

    if i % 1000000 == 0:
        print("Tried:", i)
