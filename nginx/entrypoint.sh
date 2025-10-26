#!/bin/sh
# entrypoint.sh - wait for SSL certificate then start nginx

CERT_FILE="/etc/ssl/server.crt"
KEY_FILE="/etc/ssl/server.key"

echo "Starting entrypoint script for nginx..."

while [ ! -f "$CERT_FILE" ] || [ ! -f "$KEY_FILE" ]; do
  echo "Waiting for SSL certificate and key to be available..."
  sleep 1
done

echo "SSL certificate and key found. Starting nginx..."
exec nginx -g "daemon off;"
