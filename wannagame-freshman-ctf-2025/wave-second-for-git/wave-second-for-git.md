# Wave Second For Git — WannaGame Freshman CTF 2025

> **Room / Challenge:** Wave Second For Git (Misc)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** WannaGame Freshman CTF 2025
- **Challenge:** Wave Second For Git (Misc)
- **Difficulty:** `Medium`
- **Points:** `451`
- **Solves:** `8`
- **Date:** `06-10-2025`

---

## Goal

We have to get the flag by using Git cli.

## My Solution

Here is the source, you can download it [here](./Wave-second.zip)

There is the `flag.txt` with this content:

```
VzF7ZzF0aHViXw==
```

It is encoded with base64 algorithm, it is easy to decode it, result is the first part of the flag:

```
W1{g1thub_
```

Now check the source branches with `git branch -r`:

```
origin/HEAD -> origin/main
origin/main
origin/second
```

Let's move to branch `second` to see if there is any change `git checkout second`, the `flag.txt` changed:

```
INGESX3JGVPXK4ZTMZ2TO===
```

It is encoded with base32 algorithm, decode it:

```
CLI_i5_us3fu7
```

Now we got 2 parts:

```
W1{g1thub_CLI_i5_us3fu7
```

Now check the source with `git tag` there is `part3` tag let's show it `git show part3`:

```
tag part3
Tagger: KetSoSad102 <phanlamdung2006@gmail.com>
Date:   Thu Oct 2 09:24:03 2025 +0700

Zw4bm2:x
```

I use CyberChef to crack this encoding and found `_r1gh7?}`

![Guide image](../screenshots/wave-second-for-git-1.png)

Flag is: `W1{g1thub_CLI_i5_us3fu7_r1gh7?}`
