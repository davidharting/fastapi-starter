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


if __name__ == "__main__":
    app()
