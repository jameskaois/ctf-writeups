# funjs — DreamHack

> **Room / Challenge:** funjs (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** funjs (web)
- **Link**: `https://dreamhack.io/wargame/challenges/116`
- **Level:** `2`
- **Date:** `10-11-2025`

---

## Goal

Examining the `index.html` and solving the flag.

## My Solution

The web app is the [index.html](./index.html). I will comment the `moveBox` function to test more comfortably:

```html
function init() { box = document.getElementById("formbox"); {{ /*
setInterval(moveBox,1000); */ }} }
```

We have to submit the correct flag in order to get the flag, if not we will received `NOP!`:

![Guide image](./screenshots/1.png)

The `main` function has obfuscation logic so we can deobfuscation this code and received:

```javascript
var flag = document.getElementById("flag").value;
if (flag.length != 36) {
  text2img("NOP !");
  return;
}

for (var i = 0; i < flag.length; i++) {
  var current_operator = operator[i % operator.length];

  var expected_char_code = current_operator(_0x4949[i], _0x42931[i]);

  if (flag.charCodeAt(i) == expected_char_code) {
  } else {
    text2img("NOP !");
    return;
  }
}

text2img(flag);
```

Here, deobfuscating the main code:

```javascript
// The two key arrays from the source code
var _0x4949 = [
  0x20, 0x5e, 0x7b, 0xd2, 0x59, 0xb1, 0x34, 0x72, 0x1b, 0x69, 0x61, 0x3c, 0x11,
  0x35, 0x65, 0x80, 0x9, 0x9d, 0x9, 0x3d, 0x22, 0x7b, 0x1, 0x9d, 0x59, 0xaa,
  0x2, 0x6a, 0x53, 0xa7, 0xb, 0xcd, 0x25, 0xdf, 0x1, 0x9c,
];
var _0x42931 = [
  0x24, 0x16, 0x1, 0xb1, 0xd, 0x4d, 0x1, 0x13, 0x1c, 0x32, 0x1, 0xc, 0x20, 0x2,
  0x1, 0xe1, 0x2d, 0x6c, 0x6, 0x59, 0x11, 0x17, 0x35, 0xfe, 0xa, 0x7a, 0x32,
  0xe, 0x13, 0x6f, 0x5, 0xae, 0xc, 0x7a, 0x61, 0xe1,
];

// The operators from the source code
var operator = [
  (a, b) => {
    return a + b;
  }, // +
  (a, b) => {
    return a - b;
  }, // -
  (a, b) => {
    return a * b;
  }, // *
  (a, b) => {
    return a ^ b;
  }, // ^
];

var flag = "";
for (var i = 0; i < 36; i++) {
  var char_code = operator[i % 4](_0x4949[i], _0x42931[i]);

  flag += String.fromCharCode(char_code);
}

console.log(flag);
```

Run this we will get the flag

![Guide image](./screenshots/2.png)
