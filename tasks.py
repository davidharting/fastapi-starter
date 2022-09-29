import subprocess

import typer

app = typer.Typer()


@app.command()
def dev():
    command = ["uvicorn", "fastapi_starter.main:app", "--reload"]
    subprocess.run(command)


@app.command()
def format(fix: bool = False):
    command = ["black", "."]
    if not fix:
        command.append("--check")
    subprocess.run(command)


@app.command()
def typecheck():
    command = ["pyright"]
    subprocess.run(command)


@app.command()
def lint(fix: bool = False, watch: bool = False):
    command = ["ruff", "."]
    if fix:
        command.append("--fix")
    if watch:
        command.append("--watch")
    subprocess.run(command)


@app.command()
def sort_imports(fix: bool = False):
    """
    Check if imports are sorted. Optionally, automatically fix problems.
    """
    command = ["isort", ".", "--atomic"]
    if not fix:
        command.append("-c")
    subprocess.run(command)


if __name__ == "__main__":
    app()
