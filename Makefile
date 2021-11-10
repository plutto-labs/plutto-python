# Env stuff
.PHONY: get-poetry
get-poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

.PHONY: build-env
build-env:
	python3 -m venv .venv
	poetry run pip install --upgrade pip
	poetry run poetry install

# Tests
.PHONY: tests
tests:
	poetry run pytest -rP --cov=plutto --cov-report=term-missing --cov-report=xml tests

# Passive linters
.PHONY: black
black:
	poetry run black plutto tests --check

.PHONY: flake8
flake8:
	poetry run flake8 plutto tests

.PHONY: isort
isort:
	poetry run isort plutto tests --profile=black --check

.PHONY: pylint
pylint:
	poetry run pylint plutto

# Aggresive linters
.PHONY: black!
black!:
	poetry run black plutto tests

.PHONY: isort!
isort!:
	poetry run isort plutto tests --profile=black

# Utilities
.PHONY: bump!
bump!:
	sh scripts/bump.sh $(filter-out $@,$(MAKECMDGOALS))

# Receive args (use like `$(filter-out $@,$(MAKECMDGOALS))`)
%:
	@: