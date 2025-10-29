# Makefile for FINCOUNT

.PHONY: help install install-dev test lint format clean docs run

help:
	@echo "FINCOUNT - Development Commands"
	@echo "================================"
	@echo "install      - Install production dependencies"
	@echo "install-dev  - Install development dependencies"
	@echo "test         - Run test suite"
	@echo "lint         - Run linters (flake8, mypy)"
	@echo "format       - Format code with black"
	@echo "clean        - Remove build artifacts"
	@echo "docs         - Build documentation"
	@echo "run          - Run the application"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pre-commit install

test:
	pytest tests/ -v --cov=src/fincount --cov-report=term-missing

lint:
	flake8 src/ tests/
	mypy src/

format:
	black src/ tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".coverage" -delete
	rm -rf build/ dist/ htmlcov/

docs:
	cd docs && make html

run:
	python -m fincount
