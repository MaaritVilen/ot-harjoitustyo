from invoke import task

@task
def start(ctx):
	ctx.run("python3 mainbody.py",pty=True)

@task
def coverage_report(ctx):
	ctx.run("coverage run --branch -m pytest tests", pty=True)
