run:
	PYTHONPATH=src poetry run python src/manage.py runserver

makemigrations:
	@read -p "Enter migration name: " name; \
	poetry run python src/manage.py makemigrations movies --name $$name


migrate:
	PYTHONPATH=src poetry run python src/manage.py migrate

shell:
	PYTHONPATH=src poetry run python src/manage.py shell

createsuperuser:
	PYTHONPATH=src poetry run python src/manage.py createsuperuser
create_test_db:
	psql -U postgres -h localhost -c "CREATE DATABASE test_cinema_booking OWNER cinema_user;" || true

# Run tests with coverage
# Run tests with test environment and coverage
test:
	DJANGO_ENV=test PYTHONPATH=src poetry run pytest --reuse-db --cov=apps --cov-report=term-missing

shell:
	poetry run python src/manage.py shell