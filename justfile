# Development commands for gear-generator

# Install development dependencies
install-dev:
    uv sync --dev

# Install pre-commit hooks
install-hooks:
    pre-commit install

# Run all linting and type checking
lint:
    uv run ruff check --fix .
    uv run ruff format .
    uv run mypy .

# Fix linting issues automatically
lint-fix:
    uv run ruff check --fix .
    uv run ruff format .

# Run tests
test:
    uv run pytest -m "unit or integration"

# Run tests with coverage
test-cov:
    uv run pytest --cov=generators --cov-report=html --cov-report=term

# Run all checks (lint, test)
check: test-cov lint

# Clean up generated files
clean:
    rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/ bandit-report.json

# Format code
format:
    uv run ruff format .

# Show project info
info:
    @echo "Project: gear-generator"
    @echo "Python: $(uv run python --version)"
    @echo "UV: $(uv --version)"

# Setup development environment
setup: install-dev install-hooks
    @echo "Development environment setup complete! 🎉"

# Run the main application
run:
    uv run python main.py
