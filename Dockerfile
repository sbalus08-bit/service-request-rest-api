FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip instll -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
