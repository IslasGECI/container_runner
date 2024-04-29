from .container_run import write_docker_command
import typer
import os

cli = typer.Typer()


@cli.command()
def run_container(
    target: str = typer.Option(),
    container: str = typer.Option(),
    image: str = typer.Option(),
    path: str = typer.Option(),
    password: str = typer.Option(),
):
    command = write_docker_command(target, container, image, path, password)
    os.system(command)


@cli.command()
def version():
    pass
