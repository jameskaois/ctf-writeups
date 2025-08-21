# Google Dorking - TryHackMe 

Explaining how Search Engines work and leveraging them into finding hidden content!

## Overview
- **Room URL:** [https://tryhackme.com/room/googledorking](https://tryhackme.com/room/googledorking)
- **Difficulty:** Easy
- **Time to complete:** 45

## Walkthrough
### 1. Ye Ol' Search Engine
*No hints needed!*

### 2. Let's Learn About Crawlers
- <p>Name the key term of what a "Crawler" is used to do. This is known as a collection of resources and their locations</p>

**=> Answer: `Index`**

- <p>What is the name of the technique that "Search Engines" use to retrieve this information about websites?</p>

**=> Answer: `Crawling`**

- <p>What is an example of the type of contents that could be gathered from a website?</p>

**=> Answer: `Keywords`**

### 3. Enter: Search Engine Optimisation
*No hints needed!*

### 4. Beepboop - Robots.txt
- <p>Where would "robots.txt" be located on the domain "<b>ablog.com</b>"</p>

**=> Answer: `ablog.com/robots.txt`**

- <p>If a website was to have a sitemap, where would that be located?</p>

**=> Answer: `/sitemap.xml`**

- How would we only allow "Bingbot" to index the website?

**=> Answer: `User-agent: Bingbot`**

- <p>How would we prevent a "Crawler" from indexing the directory "/dont-index-me/"?<br /></p>

**=> Answer: `Disallow: /dont-index-me/`**

- <p>What is the extension of a Unix/Linux system configuration file that we might want to hide from "Crawlers"?</p>

**=> Answer: `.conf`**

### 5. Sitemaps
- <p>What is the typical file structure of a "Sitemap"?</p>

**=> Answer: `XML`**

- <p>What real life example can "Sitemaps" be compared to?</p>

**=> Answer: `Map`**

- <p>Name the keyword for the path taken for content on a website</p>

**=> Answer: `route`**

### 6. What is Google Dorking?
- <p>What would be the format used to query the site bbc.co.uk about flood defences<br /></p>

**=> Answer: `site: bbc.co.uk flood defences`**

- <p>What term would you use to search by file type?</p>

**=> Answer: `filetype:`**

- <p>What term can we use to look for login pages?</p>

**=> Answer: `intitle: login`**

