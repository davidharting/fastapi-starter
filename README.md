# FastAPI starter

My goal is to provide myself with a starter repo so that I can quickly build new Fast API applications with all the bells and whistles of a modern Python project.

## Project setup

- [x] Pyenv for Python version management
- [x] Poetry for dependency management
- [x] Typer for project tasks

## Code hygiene

- [x] Ruff for linting
- [x] Black for code formatting
- [x] Pyright for type-checking
- [x] isort for import sorting

## Testing

- [x] Pytest
- [x] Example API client test

## Logging

- [ ] [Loguru](https://github.com/Delgan/loguru)
- [ ] Middleware to bind a logger per request

## FastAPI

- [x] Multi-file / multi-router setup
- [x] Health check endpoint
- [ ] Docs generation
- [ ] Client generation
- [ ] Abstraction for consistent background jobs

## Config

- [ ] Use Pydant `BaseSetting` subclass to read and parse environment variables (e.g., LOG_LEVEL)

## CI

- [x] GitHub actions for lint, type-check, format, test
