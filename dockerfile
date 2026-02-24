FROM python:3.9
WORKDIR /app
copy..
CMD ["python","-m","http.server","8080"

