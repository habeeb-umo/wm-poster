FROM python:3.9-alpine

WORKDIR /app
COPY poster.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python3 poster.py