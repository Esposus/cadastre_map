# дополнительный сервис/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /external_app

COPY requirements.txt /external_app/
RUN pip install -r requirements.txt

COPY . /external_app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]