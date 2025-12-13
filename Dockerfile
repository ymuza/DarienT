FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
    curl \
    && apt-get clean


RUN pip install --upgrade pip poetry poetry-plugin-export


COPY pyproject.toml poetry.lock ./


RUN poetry export -f requirements.txt --without dev --output requirements.txt


RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
