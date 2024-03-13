install:
	poetry install

lint:
	poetry run black .

check:
	poetry run black . --check

test:
	poetry run pytest -vv

test-watch:
	poetry run ptw
