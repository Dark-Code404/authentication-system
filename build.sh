#!/bin/sh

poetry run python manage.py makemigrations --no-input

poetry run python manage.py migrate --no-input

poetry run python manage.py collectstatic --no-input

poetry run python manage.py runserver 0.0.0.0:8000