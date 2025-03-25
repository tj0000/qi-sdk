#!/bin/bash
if [ "$*" = "--no-tests" ]
then
    echo "Skipping tests..."
else
    uv run coverage run -m pytest -vv $@
fi

uv run mypy quartier_intelligence/
uv run ruff check quartier_intelligence/ --no-cache
uv run ruff format .
uv run coverage html