install:
	poetry install

lint:
	poetry run black .

check:
	poetry run black . --check

test:
	poetry run pytest

test-watch:
	poetry run ptw
