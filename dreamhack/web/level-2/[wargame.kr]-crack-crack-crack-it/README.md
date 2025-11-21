# [wargame.kr] crack crack crack it — DreamHack

> **Room / Challenge:** [wargame.kr] crack crack crack it (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** [wargame.kr] crack crack crack it (web)
- **Link**: `https://dreamhack.io/wargame/challenges/330`
- **Level:** `2`
- **Date:** `21-11-2025`

---

## Goal

Brute-force the password and get the flag.

## My Solution

Based on the description:

```
oops, i forgot my password!! somebody help me T_T
(i remember that my password begin with 'G4HeulB' and the other chars is composed of number, lower alphabet only..)

notice: this .htaccess file is different each other IP Address. authentication have to be same ip plz,
```

We can create our password generator with Python and use John-the-ripper to brute-force the password:

```python
from  itertools  import  product

c =  '0123456789abcdefghijklmnopqrstuvwxyz'

for  n  in  range ( 4 , 10 ):
    for cc in  product(c,repeat= n):
        print('G4HeulB'+ "" .join(cc))
```

```bash
python3 script.py | john -stdin htpasswd
```

![Guide image](./screenshots/1.png)

![Guide image](./screenshots/2.png)
