# Section 14: Antak Webshell

Module: 08. Shells & Payloads

---

## Questions & Answers

### 1. Where is the Antak webshell located on Pwnbox? Submit the full path. (Format:/path/to/antakwebshell)


**Answer:** `/usr/share/nishang/Antak-WebShell/antak.aspx`

---

### 2. Establish a web shell with the target using the concepts covered in this section. Submit the name of the user on the target that the commands are being issued as. In order to get the correct answer you must navigate to the web shell you upload using the vHost name. (Format: ****\****, 1 space)

Context:
- Upload the `Upload.aspx` based on learning material and submit `whoami`
```bash
PS> whoami
iis apppool\status
```

**Answer:** `iis apppool\status`

---

[Back to Module Index](./README.md)
