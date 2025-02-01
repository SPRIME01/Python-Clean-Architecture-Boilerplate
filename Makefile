init:
    uv venv
    uv pip install -e .[dev]
    pre-commit install

test:
    pytest -v --cov=src --cov-report=html --bdd-format=progress

lint:
    ruff check src
    mypy src
    yamllint . -c pyproject.toml
    interrogate src

docs:
    mkdocs serve

clean:
    find . -type d -name '__pycache__' -exec rm -rf {} +
    rm -rf .coverage htmlcov
