from invoke import task

@task
def start(ctx):
	ctx.run("python3 program/mainbody.py",pty=True)

@task
def coverage_report(ctx):
	ctx.run("coverage run --branch -m pytest tests", pty=True)

@task
def lint(ctx):
	ctx.run("pylint src",pty=True)
