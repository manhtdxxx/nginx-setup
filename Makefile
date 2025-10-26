check-certs-in-app:
	docker exec -it flask-app ls -l /app/certs/

check-certs-in-nginx:
	docker exec -it nginx-proxy ls -l /etc/ssl/

curl-http:
	curl -k http://localhost:5000

curl-https:
	curl -k https://localhost:5000
