"""tasks.py sets up tasks for the invoke helper.
"""

from invoke import task

@task
def start(ctx):
    """Starts the program.
    """
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    """Runs tests.
    """
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    """Generates coverage analysis.
    """
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    """Generates coverage html files.
    """
    ctx.run("coverage html", pty=True)

@task
def autopep(ctx):
    """Runs autopep8 on source code.
    """
    ctx.run("autopep8 --in-place --recursive src")

@task
def lint(ctx):
    """Runs pylint on source code.
    """
    ctx.run("pylint src")
