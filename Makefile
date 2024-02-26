stop:
	docker-compose down

start: stop
	docker-compose --env-file .env up --build