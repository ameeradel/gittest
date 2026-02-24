FROM python:3.10-slim

WORKDIR /app

COPY app/app.py .

EXPOSE 8000

CMD ["python", "app.py"]
