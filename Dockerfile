FROM python:3.11

ENV PORT=5000

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh

COPY ./app ./app

ENTRYPOINT ["./docker-entrypoint.sh"]