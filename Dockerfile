#Poner docker-compose build para crear la imagen de la aplicacion
FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . /app/

#Para actualizar e poder instalar bien mysqlclient
RUN apt-get update && \
    apt install -y default-libmysqlclient-dev build-essential pkg-config
#Para instalar psycopg2
RUN apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000