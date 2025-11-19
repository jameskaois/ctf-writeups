import zlib
import base64

cookie_str = ".eJwtxrsVgCAMAMBdWADzAYLbhJDYWImdz91tvOqetNwuv9P-Z2Vh9lDGVtCosFhM7tLrxIYwQwywMo-tU3UgpzZsq0GjAbCKao5Tj_R-x7QaKg.aR1oqg.aWvFAJLBMzsbfdBzGnqWWJVUaVE"

payload = cookie_str.split('.')[1]

padding = len(payload) % 4
if padding > 0:
    payload += '=' * (4 - padding)

try:
    decoded_bytes = base64.urlsafe_b64decode(payload)
    decompressed_data = zlib.decompress(decoded_bytes)
    print(f"Decoded Session: {decompressed_data.decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")