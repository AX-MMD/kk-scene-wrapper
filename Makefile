.DEFAULT_GOAL := all
project_path = kk_scene_wrapper
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
    pytest

.PHONY: install
install:
    poetry build
    pip install --force-reinstall --user dist/kk_scene_wrapper-0.1.0-py3-none-any.whl

.PHONY: publish
publish:
    poetry build
    poetry publish

.PHONY: all
all: format test