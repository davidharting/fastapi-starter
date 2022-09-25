from invoke import task


@task(help={"fix": "Fix problems found in files."})
def format(c, fix=False):
    if fix:
        c.run("black .")
    else:
        c.run("black . --check")
