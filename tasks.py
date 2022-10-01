import subprocess

import typer

app = typer.Typer()


@app.command()
def dev():
    """
    Run the FastAPI server in development mode with hot code reloading.
    """
    command = ["uvicorn", "fastapi_starter.main:app", "--reload"]
    subprocess.run(command)


@app.command()
def format(fix: bool = False):
    """
    Check and optionally fix the format of Python files using Black.
    """
    command = ["black", "."]
    if not fix:
        command.append("--check")
    subprocess.run(command)


@app.command()
def typecheck():
    """
    Check Python files for type errors using Pyright.
    """
    command = ["pyright"]
    subprocess.run(command)


@app.command()
def lint(fix: bool = False, watch: bool = False):
    """
    Check and optionally fix linting errors in Python files using Ruff.
    """
    command = ["ruff", "."]
    if fix:
        command.append("--fix")
    if watch:
        command.append("--watch")
    subprocess.run(command)


@app.command()
def sort_imports(fix: bool = False):
    """
    Check and optionally fix the order of imports using isort.
    """
    command = ["isort", ".", "--atomic"]
    if not fix:
        command.append("-c")
    subprocess.run(command)


@app.command()
def test():
    """
    Run tests using Pytest.
    """
    command = ["pytest"]
    subprocess.run(command)


if __name__ == "__main__":
    app()
