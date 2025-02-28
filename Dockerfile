FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN pip install --upgrade pip 

RUN pip install poetry==2.1.1

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root; 
 
COPY . .
 
EXPOSE 8000

ENTRYPOINT ["sh", "build.sh"]
