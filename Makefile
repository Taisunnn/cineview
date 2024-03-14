IMAGE_AIRFLOW=apifun

DIR=$(shell pwd)

stop:
	docker-compose down

start: stop
	docker-compose --env-file .env up --build

test:
	docker-compose -f docker-compose.ci.yml down
	docker-compose -f docker-compose.ci.yml build
	docker-compose -f docker-compose.ci.yml run test

lint:
	docker run --rm -v $(DIR):/apps alpine/flake8:3.5.0 --ignore=E501,F401 dags app tests

format:
	docker run --rm -v $(DIR):/src --workdir /src pyfound/black:24.2.0 black airflow app tests