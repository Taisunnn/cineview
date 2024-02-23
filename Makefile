stop:
	docker-compose down

start: stop
	docker-compose up --build