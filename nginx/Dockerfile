FROM nginx:alpine

RUN apk add --no-cache openssl

# Create certificate and private key
RUN mkdir -p /etc/ssl && \
    openssl req -x509 -nodes -days 365 \
        -newkey rsa:2048 \
        -keyout /etc/ssl/server.key \
        -out /etc/ssl/server.crt \
        -subj "/CN=demo.local" && \
    chmod 600 /etc/ssl/server.key

# Config nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Start nginx 
CMD ["nginx", "-g", "daemon off;"]
