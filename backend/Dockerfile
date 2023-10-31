FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt .

# Для запуска на хостинге
# RUN apt-get update
# RUN apt-get install gcc -y
# RUN apt-get install --reinstall libpq-dev python3-dev -y
RUN pip install "setuptools<58.0.0" wheel
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "career_tracker.wsgi", "--bind", "0:8000" ]
