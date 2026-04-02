FROM python:3.11

WORKDIR /code

# Install netcat (nc)
RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY wait-for-postgres.sh .

RUN chmod +x wait-for-postgres.sh

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]