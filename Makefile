IMAGE_AIRFLOW=apifun

DIR=$(shell pwd)

stop:
	docker-compose down

start: stop
	docker-compose --env-file .env up --build

test:
	docker build -t $(IMAGE_AIRFLOW) -f Dockerfile.app .;
	docker run --rm -t -v $(DIR)/app:/src/app \
		-v $(DIR)/tests:/src/tests \
		--env-file .env $(IMAGE_AIRFLOW) test

lint:
	docker run --rm -v $(DIR):/apps alpine/flake8:3.5.0 --ignore=E501,F401 dags app tests

format:
	docker run --rm -v $(DIR):/src --workdir /src pyfound/black:24.2.0 black airflow app tests