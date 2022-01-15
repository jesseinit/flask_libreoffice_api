FROM python:3.8-slim

RUN apt-get update && apt-get install -y libreoffice

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-c", "gunicorn.py", "app:app"]
