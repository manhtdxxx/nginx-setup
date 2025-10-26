check-certs:
	docker exec -it nginx-proxy ls -l /etc/ssl/

curl-http:
	curl -k http://localhost:5000

curl-https:
	curl -k https://localhost:5000

delete-all:
	docker compose down -v --rmi all
	docker image prune -af
	docker volume prune -f