import subprocess
import typing

import typer

app = typer.Typer()


def run_command(command: typing.List[str]) -> None:
    result = subprocess.run(command)
    if result.returncode > 0:
        raise typer.Exit(result.returncode)


@app.command()
def dev():
    """
    Run the FastAPI server in development mode with hot code reloading.
    """
    command = ["uvicorn", "fastapi_starter.main:app", "--reload"]
    run_command(command)


@app.command()
def format(fix: bool = False):
    """
    Check and optionally fix the format of Python files using Black.
    """
    command = ["black", "."]
    if not fix:
        command.append("--check")
    run_command(command)


@app.command()
def typecheck():
    """
    Check Python files for type errors using Pyright.
    """
    command = ["pyright"]
    run_command(command)


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
    run_command(command)


@app.command()
def sort_imports(fix: bool = False):
    """
    Check and optionally fix the order of imports using isort.
    """
    command = ["isort", ".", "--atomic"]
    if not fix:
        command.append("-c")
    run_command(command)


@app.command()
def test():
    """
    Run tests using Pytest.
    """
    command = ["pytest"]
    run_command(command)


if __name__ == "__main__":
    app()
