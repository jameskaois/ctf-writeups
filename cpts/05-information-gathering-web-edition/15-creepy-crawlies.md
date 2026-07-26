# Section 15: Creepy Crawlies

Module: 05. Information Gathering - Web Edition

---

## Questions & Answers

### 1. After spidering inlanefreight.com, identify the location where future reports will be stored. Respond with the full domain, e.g., files.inlanefreight.com.

Context:
```bash
┌──(jameskaois㉿kali)-[~/Documents]
└─$ python3 ./ReconSpider.py http://inlanefreight.com
# ...
┌──(jameskaois㉿kali)-[~/Documents]
└─$ cat  results.json 
{
    "emails": [
        "manuel.pernilious@inlanefreight.com",
        "support@inlanefreight.com",
        "emma.williams@inlanefreight.com",
        "freya.kartboom@inlanefreight.com",
        "jeremy-ceo@inlanefreight.com",
        "samuel.dot@inlanefreight.com",
        "hans.mueller@inlanefreight.com",
        "info@inlanefreight.com",
        "john.smith4@inlanefreight.com",
        "lily.floid@inlanefreight.com",
        "cvs@inlanefreight.com",
        "enterprise-support@inlanefreight.com",
        "info@themeansar.com",
        "fiona.dante@inlanefreight.com",
        "david.jones@inlanefreight.com",
        "enterprise@inlanefreight.com"
    ],
    "links": [
        "https://www.inlanefreight.com/#content",
        "https://www.inlanefreight.com/index.php/about-us/#content",
        "https://www.inlanefreight.com/index.php/offices/#content",
        "https://www.inlanefreight.com/index.php/contact/#content",
        "https://www.inlanefreight.com/index.php/about-us/",
        "https://www.inlanefreight.com/index.php/news/",
        "https://www.inlanefreight.com/wp-content/uploads/2020/09/goals.pdf",
        "https://www.inlanefreight.com/index.php/contact/",
        "https://www.inlanefreight.com/index.php/news/#content",
        "https://www.inlanefreight.com/index.php/career/",
        "https://www.themeansar.com",
        "https://www.inlanefreight.com/index.php/career/#content",
        "https://www.inlanefreight.com",
        "https://www.inlanefreight.com/index.php/offices/",
        "https://www.inlanefreight.com/"
    ],
    "external_files": [
        "https://www.inlanefreight.com/index.php/news/pdf",
        "https://www.inlanefreight.com/wp-content/uploads/2020/09/goals.pdf"
    ],
    "js_files": [
        "https://www.inlanefreight.com/wp-includes/js/jquery/jquery.min.js?ver=3.5.1",
        "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/jquery.smartmenus.bootstrap.js?ver=5.6.17",
        "https://www.inlanefreight.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.3.2",
        "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/bootstrap.min.js?ver=5.6.17",
        "https://www.inlanefreight.com/wp-includes/js/wp-embed.min.js?ver=5.6.17",
        "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/navigation.js?ver=5.6.17",
        "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/jquery.smartmenus.js?ver=5.6.17",
        "https://www.inlanefreight.com/wp-content/themes/ben_theme/js/owl.carousel.min.js?ver=5.6.17"
    ],
    "form_fields": [],
    "images": [
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_01-1024x810.png",
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/Career_02-300x235.jpg",
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/Offices_01-1024x359.png",
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/Career_01-300x235.jpg",
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_02-1024x810.png",
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_04-1024x810.png",
        "https://www.inlanefreight.com/wp-content/uploads/2021/03/AboutUs_03-1024x810.png"
    ],
    "videos": [],
    "audio": [],
    "comments": [
        "<!-- /navbar-toggle -->",
        "<!-- /Navigation -->",
        "<!--==================== feature-product ====================-->",
        "<!-- Right nav -->",
        "<!--==================== TOP BAR ====================-->",
        "<!-- change Jeremy's email to jeremy-ceo@inlanefreight.com -->",
        "<!-- navbar-toggle -->",
        "<!-- #secondary -->",
        "<!--Sidebar Area-->",
        "<!-- Navigation -->",
        "<!--/overlay-->",
        "<!-- /Right nav -->",
        "<!-- TO-DO: change the location of future reports to inlanefreight-comp133.s3.amazonaws.htb -->",
        "<!--==================== transportex-FOOTER AREA ====================-->",
        "<!-- Logo -->",
        "<!--\nSkip to content<div class=\"wrapper\">\n<header class=\"transportex-trhead\">\n\t<!--==================== Header ====================-->",
        "<!-- #masthead -->",
        "<!-- Blog Area -->"
    ]
}           
```
**Answer:** `inlanefreight-comp133.s3.amazonaws.htb`

---

[Back to Module Index](./README.md)
