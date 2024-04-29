from .container_run import write_docker_command
import typer

cli = typer.Typer()


@cli.command()
def run_container(
    target: str = typer.Option(),
    container: str = typer.Option(),
    image: str = typer.Option(),
    path: str = typer.Option(),
    password: str = typer.Option(),
):
    print(write_docker_command(target, container, image, path, password))


@cli.command()
def version():
    pass
