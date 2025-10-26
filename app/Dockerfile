FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y openssl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Create private key and public key in certs/ folder (that will be mounted to )
RUN mkdir -p /app/certs
RUN openssl req -x509 -newkey rsa:2048 \
    -keyout /app/certs/server.key \
    -out /app/certs/server.crt \
    -days 365 -nodes \
    -subj "/C=VN/ST=HCM/L=HCM/O=DemoSSL/OU=IT/CN=localhost"

    
EXPOSE 5000
CMD ["python", "app.py"]
