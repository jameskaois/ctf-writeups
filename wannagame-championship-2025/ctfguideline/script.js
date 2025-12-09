/* ============================================================
   Load config
   ============================================================ */

var config;
fetch("config.json")
.then(resp => resp.json())
.then(async resp => {
    config = resp
    document.body.style.backgroundColor = config.background;
    document.body.style.color = config.text_color;
    await loadContentsList(config);

    if (location.hash.length > 0) config.skin = 'Pane', initPane(config);
    else {
        const url = new URL(location.href);
        if (url.searchParams.get("doc")) config.skin = 'Modern', initModern(config);
        else config.skin = 'Default', initDefault(config);
    }
})

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

    config.contents.forEach(file => {
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
    document.querySelectorAll(".nav-item").forEach(item => {
        item.addEventListener("click", (e) => {
            e.preventDefault();
            const file = item.getAttribute("data-file");

            if (config.skin === "Pane") {
                location.hash = file;  // Pane uses hash
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
    currentHash = location.hash.substring(1)
    if (currentHash)
    {
        var decodedHash = decodeURIComponent(currentHash);
        var sanitizedHash = decodedHash.replace(/(javascript:|data:|[<>])/gi, '');
        if (decodedHash != sanitizedHash) {
            document.location.hash = encodeURI(sanitizedHash);
        }
    }
}

function loadPaneContent(config) {
    sanitizeHash()
    let file = location.hash.substring(1) || config.default;
    if (file) {

        document.getElementById("viewerLeft").innerHTML =
            `<h2>Overview</h2><p>You selected: ${encodeURIComponent(file)}</p>`;
        url = new URL(location.href)
        if (config) {
            if (!config.load_remote) {
                file = "contents/" + file;
            }
            else {
                if (!file.startsWith("http://") && !file.startsWith("https://"))
                    file = url.origin + url.pathname + "/contents" + file;
            }
        }
        document.getElementById("viewerCenter").contentWindow.location.replace(decodeURI(file));
        document.getElementById("viewerRight").innerHTML =
            `<h2>Extras</h2><p>Copyright.</p>`;
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
    const text = await fetch("contents/" + file).then(r => r.text());
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
    const text = await fetch("contents/" + file).then(r => r.text());
    document.getElementById("viewer").innerHTML =
        `<div class="modern-card">${text}</div>`;
}

/* ============================================================
   Helpers
   ============================================================ */
function hideAllViewers() {
    document.querySelectorAll("#viewer, .pane-panel").forEach(el => {
        el.style.display = "none";
    });
}