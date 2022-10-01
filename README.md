# FastAPI starter

A template repository for quickly starting new FastAPI projects with comfortable and productive tooling.

## 🚀 Use this repository to start your own project

### Set up your repository

- Click the green Use this Template button
- Fill out the form to create your new repository
- Clone the repository locally

### Rename

Globally search for "fastapi_starter" and "fastapi-starter." Replace these with the name of your own application.

## 👩‍💻 Set up your development environment

### Global dependencies

You will need Python and Poetry to work with this project.

- Install `pyenv` to manage Python versions.
  - `brew install pyenv`
  - Or, follow [these steps](https://github.com/pyenv/pyenv#homebrew-in-macos).
- Install Python. `cat .python-version | pyenv install`
- Install pipx.
  - We will use this to install Poetry
  - `brew install pipx`, or follow [these instructions](https://pypa.github.io/pipx/installation/)
- Install [Poetry](https://python-poetry.org)
  - We will use this to manage project dependencies
  - `pipx install poetry`

### Project dependencies

Now you are ready to install the dependencies for this project. From the root directory:

```bash
poetry install
```

The first time you do this, it may take a long time. Poetry may do some initial work to resolve dependencies and cache information from pypi.

After install dependencies, you can run commands against the virtual environment with:

```bash
poetry run [your command]
```

Or, activate the environment in your shell with

```bash
poetry shell
```

## 🥳 Start developing!

Activate the virtual environment.

```bash
poetry shell
```

Now, see what commands are availabile to you.

```bash
python tasks.py --help
```

To start the dev server:

```bash
python tasks.py dev
```

## Set up VS Code

This project comes with a `.vscode` folder which will recommend extensions to install and automatically configure. Simply install the recommended extensions when prompted!

## ✅ Features

### Project setup

- [x] Pyenv for Python version management
- [x] Poetry for dependency management
- [x] Typer for project tasks

### Code hygiene

- [x] Ruff for linting
- [x] Black for code formatting
- [x] Pyright for type-checking
- [x] isort for import sorting

### Testing

- [x] Pytest
- [x] Example API client test

### Logging

- [x] [Loguru](https://github.com/Delgan/loguru)
- [ ] Middleware to bind a logger per request

### FastAPI

- [x] Multi-file / multi-router setup
- [x] Health check endpoint
- [ ] Abstraction for consistent background jobs

### Config

- [x] Use Pydant `BaseSetting` subclass to read and parse environment variables (e.g., LOG_LEVEL)

### CI

- [x] GitHub actions for lint, type-check, format, test
