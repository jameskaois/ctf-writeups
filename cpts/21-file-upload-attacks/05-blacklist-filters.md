# Section 05: Blacklist Filters

Module: 21. File Upload Attacks

---

## Questions & Answers

### 1. Try to find an extension that is not blacklisted and can execute PHP code on the web server, and use it to read "/flag.txt"

Context:
- Catch the request to `upload.php` and fuzzing for allowed extensions:
![Guide image](../screenshots/file-upload-attacks-3.png)
- `229` and `230` in the raw response indicates the file was uploaded successfully, all extensions allowed:
![Guide image](../screenshots/file-upload-attacks-4.png)
- The only extension that works correctly is `.phar`:
![Guide image](../screenshots/file-upload-attacks-5.png)

**Answer:** `HTB{1_c4n_n3v3r_b3_bl4ckl1573d}`

---

[Back to Module Index](./README.md)
