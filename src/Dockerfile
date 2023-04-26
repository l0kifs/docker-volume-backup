FROM python:3.9-slim-buster

LABEL name="DockerVolumeBackup"
LABEL version="1.0"

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "backup.py"]