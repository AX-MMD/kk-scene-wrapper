.DEFAULT_GOAL := all
project_path = src
mypylint = mypy $(project_path) --ignore-missing-imports --no-warn-unused-ignores --warn-redundant-casts --warn-unused-ignores --pretty --show-error-codes --check-untyped-defs

.PHONY: pretty
pretty:
	ruff format $(project_path)

.PHONY: format
format:
	ruff format $(project_path)
	ruff check --fix
	$(mypylint)

.PHONY: lint
lint:
	ruff check
	$(mypylint)

.PHONY: test
test:
	pytest $(project_path)

.PHONY: all

all: format test
