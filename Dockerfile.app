FROM python:3.11

ENV PORT=5000

WORKDIR /src

COPY requirements_app.txt requirements_app.txt
RUN pip install -r requirements_app.txt

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

COPY ./app ./app

ENTRYPOINT ["./docker-entrypoint.sh"]