# Download the client certificate & key
curl -k -H "Host: public.trustboundary.local" https://challenge.cnsc.com.vn:31507/download/client.crt -o client.crt
curl -k -H "Host: public.trustboundary.local" https://challenge.cnsc.com.vn:31507/download/client.key -o client.key

# Getting verfied by the Public service and get the session.pem
openssl s_client -connect challenge.cnsc.com.vn:31507 \
    -servername public.trustboundary.local \
    -cert client.crt \
    -key client.key \
    -sess_out session.pem