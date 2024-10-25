FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && pip cache purge

COPY . .

RUN apt-get update && apt-get install -y procps && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

CMD ["python", "app.py"]
