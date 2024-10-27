.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: superuser
superuser:
	poetry run python manage.py createsuperuser

.PHONY: update
update: install migrate ;