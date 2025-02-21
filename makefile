.PHONY: run
run:
	poetry run python manage.py runserver

.PHONY: migrations
migrations:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser


.PHONY: combined
combined: migrations migrate ;