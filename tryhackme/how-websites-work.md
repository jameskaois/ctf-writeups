# How Websites Work - TryHackMe

To exploit a website, you first need to know how they are created.

## Overview

- **Room URL:** [https://tryhackme.com/room/howwebsiteswork](https://tryhackme.com/room/howwebsiteswork)
- **Difficulty:** Easy
- **Time to complete:** 25

## Walkthrough

### 1. How websites work

- <p>What term best describes the component of a web application rendered by your browser?</p>

**=> Answer: `Front End`**

### 2. HTML

- <p>One of the images on the cat website is broken - fix it, and the image will reveal the hidden text answer!</p>

Change the `<img src='img/cat-2'>` to `<img src='img/cat-2.jpg'>`:
![Guide image](./screenshots/how-websites-work-1.png)

**=> Answer: `HTMLHERO`**

- <p>Add a dog image to the page by adding another img tag (&lt;img&gt;) on line 11. The dog image location is img/dog-1.png. What is the text in the dog image?</p>

Add a new `<img src='img/dog-1.png'>`
![Guide image](./screenshots/how-websites-work-2.png)

**=> Answer: `DOGHTML`**

### 3. JavaScript

- Click the "View Site" button on this task. On the right-hand side, add JavaScript that changes the demo element's content to "Hack the Planet"

Change `<div id="demo">Hi there!</div>` to `<div id="demo">Hack the Planet</div>`
![Guide image](./screenshots/how-websites-work-3.png)

**=> Answer: `JSISFUN`**

### 4. Sensitive Data Exposure

- View the website on <a href="https://static-labs.tryhackme.cloud/sites/howwebsiteswork/html_data_exposure/" target="_blank">this link</a>. What is the password hidden in the source code?<br />

Visit https://static-labs.tryhackme.cloud/sites/howwebsiteswork/html_data_exposure/ and click `View page source`, you should see the credentials

![Guide image](./screenshots/how-websites-work-4.png)

**=> Answer: `testpasswd`**

### 5. HTML Injection

- View the website on this task and inject HTML so that a malicious link to http://hacker.com is shown.

Submit the payload `<a href="http://hacker.com">Safe content</a>`

![Guide image](./screenshots/how-websites-work-5.png)

**=> Answer: `HTML_INJ3CTI0N`**
