FROM python:3.9-slim-buster

RUN pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8008:8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]