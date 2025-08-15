.PHONY: up up-build down watch restart restart-build install migrate makemigrations runserver superuser update

up:
	docker compose up -d

up-build:
	docker compose up -d --build

down:
	docker compose down -v

watch:
	docker compose up --watch

install:
	poetry install

migrate:
	uv run python src/manage.py migrate

makemigrations:
	uv run python src/manage.py makemigrations

runserver:
	uv run python src/manage.py runserver

superuser:
	uv run python src/manage.py createsuperuser

update: install migrate ;

restart: down up

restart-build: down up-build