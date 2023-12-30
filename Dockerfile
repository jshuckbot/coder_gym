FROM python:3.11.4

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . /code

RUN pip install --upgrade pip && pip install poetry && cd /code && poetry install

