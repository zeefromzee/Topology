# Contributing Guidelines

Thank you for your interest in contributing to this project. The following guidelines ensure a smooth collaboration process.

## Reporting Issues

- Use the GitHub Issues tab to report bugs or request features.
- Provide a clear description, steps to reproduce (for bugs), and expected vs. actual behavior.
- Include your Python version, SageMath version, and operating system.

## Development Setup

1. Fork and clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Ensure SageMath is installed and accessible from your PATH.
4. Run the test suite to verify your setup: `python -m pytest tests/ -v`.

## Code Standards

- Follow PEP 8 for Python code style.
- Use type hints for all function signatures.
- Write docstrings for all public functions and classes.
- Keep functions focused and under 50 lines where possible.

## Testing

- All new functionality must include corresponding tests in the `tests/` directory.
- Tests must pass before a pull request will be reviewed.
- Aim for at least 80% code coverage on new modules.

## Pull Request Process

1. Create a feature branch from `main`.
2. Make your changes with clear, atomic commits.
3. Update documentation if your changes affect the API or usage.
4. Submit a pull request with a description of what was changed and why.
5. Respond to review feedback promptly.

## Naming Conventions

- Branches: `feature/description`, `fix/description`, `docs/description`
- Commits: Use imperative mood ("Add homology computation" not "Added homology computation")
