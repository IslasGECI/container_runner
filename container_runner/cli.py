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
    return write_docker_command("", "", "", "", "")


@cli.command()
def version():
    pass
