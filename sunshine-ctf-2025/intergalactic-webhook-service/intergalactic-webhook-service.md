# Intergalactic Webhook Service — SunShine CTF 2025

> **Room / Challenge:** Intergalactic Webhook Service (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** SunShine CTF 2025
- **Challenge:** Intergalactic Webhook Service (web)
- **Target / URL:** `https://supernova.sunshinectf.games/`
- **Difficulty:** `Easy`
- **Points:** `10`
- **Date:** `01-10-2025`

---

## Goal

We have to get the flag by leveraging the vuln in webhook service.

## My Solution

Here is the source code, you can download it [here](./intergalactic-webhook-service.zip).

The backend has this vulnerable code:

```python
def is_ip_allowed(url):
    parsed = urlparse(url)
    host = parsed.hostname or ''
    try:
        ip = socket.gethostbyname(host)
    except Exception:
        return False, f'Could not resolve host'
    ip_obj = ipaddress.ip_address(ip)
    if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_reserved:
        return False, f'IP "{ip}" not allowed'
    return True, None
```

This code takes the URL, if hostnames -> IP address using the DNS. If IP is private (like 192.168.x.x), loopback (127.0.0.1) it will be blocked.

However, this check just begins during registeration. Therefore, for example if the DNS answer changes later (via DNS rebinding), the same hostname can first point to a public IP (allowed), then later point to 127.0.0.1 (blocked but too late).

We can use rbndr.us: https://lock.cmpxchg8b.com/rebinder.html which provides DNS rebinding hostnames.

We create a hostnames first IP is `1.1.1.1`, the second is `127.0.0.1`

Created hostname:

```
01010101.7f000001.rbndr.us
```

![Guide image](../screenshots/webhook-1.png)

Now take that hostname to register a webhook:

```
http://01010101.7f000001.rbndr.us:5001/flag
```

Later we just submit the webhook ID to get the flag:

![Guide image](../screenshots/webhook-2.png)

```
sun{dns_r3b1nd1ng_1s_sup3r_c00l!_ff4bd67cd1}
```
