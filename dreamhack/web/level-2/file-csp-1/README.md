# file-csp-1 — DreamHack

> **Room / Challenge:** file-csp-1 (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** file-csp-1 (web)
- **Link**: `https://dreamhack.io/wargame/challenges/36`
- **Level:** `2`
- **Date:** `14-11-2025`

---

## Goal

Crafted the correct CSP satisfying the needs to get the flag.

## My Solution

There are 3 routes in this challenge `/test`, `/live` and `/verify`. The `/verify` is the route we need to satisfy to get the flag:

```python
@APP.route('/verify', methods=['GET', 'POST'])
def verify_csp():
    global CSP
    if request.method == 'POST':
        csp = request.form.get('csp')
        try:
            options = webdriver.ChromeOptions()
            for _ in ['headless', 'window-size=1920x1080', 'disable-gpu', 'no-sandbox', 'disable-dev-shm-usage']:
                options.add_argument(_)
            driver = webdriver.Chrome('/chromedriver', options=options)
            driver.implicitly_wait(3)
            driver.set_page_load_timeout(3)
            driver.get(f'http://localhost:8000/live?csp={quote(csp)}')
            try:
                a = driver.execute_script('return a()');
            except:
                a = 'error'
            try:
                b = driver.execute_script('return b()');
            except:
                b = 'error'
            try:
                c = driver.execute_script('return c()');
            except Exception as e:
                c = 'error'
                c = e
            try:
                d = driver.execute_script('return $(document)');
            except:
                d = 'error'

            if a == 'error' and b == 'error' and c == 'c' and d != 'error':
                return FLAG

            return f'Try again!, {a}, {b}, {c}, {d}'
        except Exception as e:
            return f'An error occured!, {e}'

    return render_template('verify.html')
```

The `/test` and `/live` is where we can use to test our payloads. The app requirements is we have to crafted the correct CSP policy which satisfy the needs in the `csp.html`:

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- block me -->
    <script>
      function a() {
        return "a";
      }
      document.write("a: block me!<br>");
    </script>
    <!-- block me -->
    <script nonce="i_am_super_random">
      function b() {
        return "b";
      }
      document.write("b: block me!<br>");
    </script>
    <!-- allow me -->
    <script
      src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
      integrity="sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8="
      crossorigin="anonymous"
    ></script>
    <!-- allow me -->
    <script nonce="i_am_super_random">
      function c() {
        return "c";
      }
      document.write("c: allow me!<br>");
      try {
        $(document);
        document.write("jquery: allow me!<br>");
      } catch (e) {}
    </script>
  </head>
</html>
```

You can see that the first two scripts tag must be blocked, and the other two must be allowed. However the tricky part is here, the second and the last script tags has the same `nonce="i_am_super_random"`. Therefore, it is not easy to block the second but allow the last. We can tried this CSP in `/test`: `script-src 'sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8='`, which will just allow the third one:

![Guide image](./screenshots/1.png)

![Guide image](./screenshots/2.png)

You can see that just the third script tag is allowed to run, now to allow the last one we have a method which is SHA-256 allowed in CSP. To create this, I use this [CSP Hash Calculator](https://centralcsp.com/features/hashes), to create the correct SHA-256 hash for the last script, we have to paste the exact content of that script to the hash calculator:

```javascript
function c() {
  return "c";
}
document.write("c: allow me!<br>");
try {
  $(document);
  document.write("jquery: allow me!<br>");
} catch (e) {}
```

It has to be correct byte-to-byte in order to create the correct hash, every new line (\n) and tab (\t) has to be totally the same:

![Guide image](./screenshots/3.png)

Combining these two we have:

```
script-src 'sha256-pasqAKBDmFT4eHoN2ndd6lN370kFiGUFyTiUHWhU7k8=' 'sha256-l1OSKODxxxxxxx'
```

Submit this CSP policy in `/verify`:
![Guide image](./screenshots/4.png)
