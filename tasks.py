import subprocess
import typer


app = typer.Typer()


@app.command()
def format(fix: bool = False):
    command = ["black", "."]
    if not fix:
        command.append("--check")
    subprocess.run(command)


@app.command()
def typecheck():
    print("type check")


if __name__ == "__main__":
    app()
