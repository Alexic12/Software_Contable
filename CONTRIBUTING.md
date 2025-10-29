# Contributing to FINCOUNT

Thank you for your interest in contributing to FINCOUNT! This document provides guidelines and instructions for contributing.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please be respectful and professional in all interactions.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Screenshots** if applicable

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Clear title and description**
- **Use case and rationale**
- **Proposed implementation** (if you have ideas)
- **Impact on existing features**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Follow coding standards** (PEP 8, type hints, docstrings)
3. **Add tests** for new functionality
4. **Update documentation** as needed
5. **Ensure all tests pass**
6. **Submit your pull request**

## Development Setup

See the [README.md](README.md#development) for detailed setup instructions.

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/)
- Use [Black](https://github.com/psf/black) for formatting
- Maximum line length: 88 characters
- Use type hints for all functions

### Documentation

- Use Google-style docstrings
- Document all public APIs
- Include examples in docstrings
- Keep documentation up-to-date

### Testing

- Write unit tests for new features
- Maintain 80%+ code coverage
- Use pytest for testing
- Mock external dependencies

### Commit Messages

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(accounting): add multi-currency support

Implemented support for multiple currencies in transactions
with automatic conversion based on exchange rates.

Closes #123
```

## Review Process

1. **Automated checks** must pass (linting, tests, type checking)
2. **Code review** by at least one maintainer
3. **Testing** in staging environment
4. **Approval** and merge by maintainer

## Questions?

Feel free to open an issue for questions or clarifications.

Thank you for contributing to FINCOUNT! 🎉
