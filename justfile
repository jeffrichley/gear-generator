# Development commands for gear-generator

# Install development dependencies
install-dev:
    uv sync --dev

# Install pre-commit hooks
install-hooks:
    pre-commit install

# Run all linting and type checking
lint:
    ruff check .
    ruff format --check .
    mypy .

# Fix linting issues automatically
lint-fix:
    ruff check --fix .
    ruff format .

# Run tests
test:
    pytest

# Run tests with coverage
test-cov:
    pytest --cov=gear_generator --cov-report=html --cov-report=term

# Run security checks
security:
    bandit -r . -f json -o bandit-report.json
    safety check

# Run all checks (lint, test, security)
check: lint test security

# Clean up generated files
clean:
    rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/ bandit-report.json

# Format code
format:
    ruff format .

# Show project info
info:
    @echo "Project: gear-generator"
    @echo "Python: $(python --version)"
    @echo "UV: $(uv --version)"

# Setup development environment
setup: install-dev install-hooks
    @echo "Development environment setup complete! 🎉"

# Run the main application
run:
    python main.py
