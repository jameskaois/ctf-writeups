# Trust Fall — Patriot CTF 2025

> **Room / Challenge:** Trust Fall (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** Patriot CTF 2025
- **Challenge:** Trust Fall (web)
- **Date:** `24-11-2025`

---

## Goal

Examining and emunerating the web app to find the correct API endpoint and get the flag.

## My Solution

Logged in as `testuser` and `pass123` to log in to the app, the app has a check for admin however we're not admin yet, examining the source found `app.js`:

```javascript
const AUTH_TOKEN = "trustfall-readonly";

const productTable = document.getElementById("product-table");

const detailCard = document.getElementById("detail-card");

const adminLink = document.getElementById("admin-link");

const adminStatus = document.getElementById("admin-status");

async function fetchJson(url, options = {}) {
  const response = await fetch(url, {
    credentials: "same-origin",

    ...options,

    headers: {
      ...(options.headers || {}),

      Authorization: `Bearer ${AUTH_TOKEN}`,
    },
  });

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return response.json();
}

function renderProducts(products) {
  productTable.innerHTML = "";

  products.forEach((product) => {
    const row = document.createElement("tr");

    const skuCell = document.createElement("td");

    const skuLink = document.createElement("a");

    skuLink.href = `#${product.sku}`;

    skuLink.textContent = product.sku;

    skuLink.addEventListener("click", (event) => {
      event.preventDefault();

      loadProductDetails(product.sku);
    });

    skuCell.appendChild(skuLink);

    const nameCell = document.createElement("td");

    nameCell.textContent = product.name;

    const priceCell = document.createElement("td");

    priceCell.textContent = product.price
      ? `$${product.price.toFixed(2)}`
      : "—";

    const updatedByCell = document.createElement("td");

    updatedByCell.textContent =
      typeof product.updatedBy === "number" ? product.updatedBy : "unknown";

    row.appendChild(skuCell);

    row.appendChild(nameCell);

    row.appendChild(priceCell);

    row.appendChild(updatedByCell);

    productTable.appendChild(row);
  });
}

function renderProductDetails(product) {
  detailCard.innerHTML = "";

  const title = document.createElement("h3");

  title.textContent = product.name;

  const skuMeta = document.createElement("p");

  skuMeta.className = "meta";

  skuMeta.textContent = `SKU: ${product.sku}`;

  const updatedMeta = document.createElement("p");

  updatedMeta.className = "meta";

  const updatedByLabel =
    typeof product.updatedBy === "number" ? product.updatedBy : "unknown";

  updatedMeta.textContent = `Updated By: User ${updatedByLabel}`;

  const description = document.createElement("p");

  description.textContent = product.description || "No description available.";

  detailCard.appendChild(title);

  detailCard.appendChild(skuMeta);

  detailCard.appendChild(updatedMeta);

  detailCard.appendChild(description);
}

function renderError(message) {
  detailCard.innerHTML = "";

  const error = document.createElement("p");

  error.className = "placeholder";

  error.textContent = message;

  detailCard.appendChild(error);
}

async function loadProductDetails(sku) {
  try {
    const product = await fetchJson(`/api/products/${encodeURIComponent(sku)}`);

    renderProductDetails(product);
  } catch (error) {
    renderError("Unable to load product details.");

    // eslint-disable-next-line no-console

    console.error(error);
  }
}

async function bootstrap() {
  try {
    const products = await fetchJson("/api/products");

    renderProducts(products);
  } catch (error) {
    productTable.innerHTML = "";

    const row = document.createElement("tr");

    const cell = document.createElement("td");

    cell.colSpan = 4;

    cell.className = "placeholder";

    cell.textContent = "Catalog unavailable.";

    row.appendChild(cell);

    productTable.appendChild(row);

    // eslint-disable-next-line no-console

    console.error(error);
  }
}

function wireAdminLink() {
  if (!adminLink || !adminStatus) {
    return;
  }

  adminLink.addEventListener("click", async (event) => {
    event.preventDefault();

    adminStatus.className = "admin-status";

    adminStatus.textContent = "Checking admin privileges...";

    try {
      const response = await fetch("/admin", {
        credentials: "same-origin",

        headers: { Authorization: `Bearer ${AUTH_TOKEN}` },
      });

      if (response.status === 403) {
        adminStatus.textContent =
          "Unauthorized: admin console restricted to leadership.";
      } else if (response.ok) {
        adminStatus.className = "admin-status success";

        adminStatus.textContent = "Admin console accessible.";
      } else {
        adminStatus.textContent = `Unexpected response: ${response.status}`;
      }
    } catch (error) {
      adminStatus.textContent = "Unable to reach admin console.";

      // eslint-disable-next-line no-console

      console.error(error);
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  bootstrap();

  wireAdminLink();
});
```

This Javascript code is the logic for the website working, however after testing and examining the endpoints related to this file, I didn't find anything although I have tried SQL Injection and more. Then I tried blind testing other popular endpoints and find this API endpoint `/api/users/:id`. Use `curl`:

```bash
curl http://SERVER/api/users/0
```

Got the response:

```json
{
  "id": 0,
  "username": "root",
  "role": "superuser",
  "flag": "PCTF{authz_misconfig_owns_u}"
}
```
