check-certs:
	docker exec -it nginx-proxy ls -l /etc/ssl/

curl-http:
	curl -k http://localhost

curl-https:
	curl -k https://localhost

delete-all:
	docker compose down -v --rmi all
	docker image prune -af
	docker volume prune -f
