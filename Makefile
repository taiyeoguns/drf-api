.PHONY: help
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST)  | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

##

.PHONY: install
install: ## Install requirements in virtual environment
	pip install -r requirements-dev.txt && pre-commit install;

.PHONY: db-migrations
db-migrations: ## Create migrations file(s) for database
	python manage.py makemigrations;

.PHONY: db-migrate
db-migrate: ## Perform migration update to database
	python manage.py migrate;

.PHONY: seed
seed: ## Seed the database with sample data
	python manage.py seed;

.PHONY: run
run: db-migrate ## Start the local web server
	python manage.py runserver;

.PHONY: test
test: ## Run tests with pytest
	pytest -vv;

.PHONY: docker-up
docker-up: ## Bring up environment in Docker
	docker-compose up --build;

.PHONY: docker-up-detached
docker-up-detached: ## Bring up environment in Docker detached mode
	docker-compose up --build -d;

.PHONY: docker-migrate-collectstatic
docker-migrate-collectstatic: ## Migrate database and collect static files in Docker
	docker-compose exec web_service python manage.py migrate --no-input;
	docker-compose exec web_service python manage.py collectstatic --no-input;

.PHONY: docker-seed
docker-seed: ## Seed database with sample data in Docker
	docker-compose exec web_service python manage.py seed;

.PHONY: docker-run
docker-run: docker-up-detached docker-migrate-collectstatic ## Run the application in docker
