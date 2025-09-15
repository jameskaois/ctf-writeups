# Intro to Digital Forensics - TryHackMe

Learn about digital forensics and related processes and experiment with a practical example.

## Overview

- **Room URL:** [https://tryhackme.com/room/introdigitalforensics](https://tryhackme.com/room/introdigitalforensics)
- **Difficulty:** Easy
- **Time to complete:** 90

## Walkthrough

### 1. Introduction To Digital Forensics

- <p>Consider the desk in the photo above. In addition to the smartphone, camera, and SD cards, what would be interesting for digital forensics?</p>

**=> Answer: `laptop`**

### 2. Digital Forensics Process

- <p>It is essential to keep track of who is handling it at any point in time to ensure that evidence is admissible in the court of law. What is the name of the documentation that would help establish that?<br /></p>

**=> Answer: `Chain of Custody`**

### 3. Practical Example of Digital Forensics

- <p>Using <code>pdfinfo</code>, find out the author of the attached PDF file, <code>ransom-letter.pdf</code>.</p>

```bash
cd /root/Rooms/introdigitalforensics
pdfinfo ransom-letter.pdf
```

![Guide image](./screenshots/intro-to-digital-forcensics-1.png)

**=> Answer: `Ann Gree Shepherd`**

<p>Using <code>exiftool</code> or any similar tool, try to find where the kidnappers took the image they attached to their document. What is the name of the street?</p>

```bash
exiftool letter-image.jpg
```

- You can find the GPS location: `51°30'51.9"N 0°05'38.7"W`
- Search it on [Google Maps](https://www.google.com/maps/place/51%C2%B030'51.9%22N+0%C2%B005'38.7%22W/@51.5142684,-0.0945692,18.95z/data=!4m4!3m3!8m2!3d51.5144167!4d-0.0940833?entry=ttu&g_ep=EgoyMDI1MDkxMC4wIKXMDSoASAFQAw%3D%3D)

![Guide image](./screenshots/intro-to-digital-forcensics-3.png)

**=> Answer: `Milk Street`**

- <p>What is the model name of the camera used to take this photo?</p>

![Guide image](./screenshots/intro-to-digital-forcensics-2.png)

**=> Answer: `Canon EOS R6`**
