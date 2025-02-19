FROM python:3.12-slim

 
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

WORKDIR /app

RUN pip install --upgrade pip 

RUN pip install poetry==2.1.1

COPY pyproject.toml poetry.lock* requirements.txt* ./


RUN if [ -f "pyproject.toml" ]; then \
        poetry install --no-root; \
    elif [ -f "requirements.txt" ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    fi
 

 
COPY . .

 
EXPOSE 8000

 
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]