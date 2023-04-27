FROM python:3.9-slim-buster

LABEL name="docker-volume-backup"
LABEL version="1.0"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "backup.py"]