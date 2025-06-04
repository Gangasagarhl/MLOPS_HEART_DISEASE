FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get install -y awscli && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python3", "app.py"]