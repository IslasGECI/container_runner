from container_runner import cli

from typer.testing import CliRunner

runner = CliRunner()


def test_run_container():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0


    #obtained = write_docker_command( container, path, password)
    image = "islasgeci/hola"
    container = "testmake_hola_develop"
    target = "mundo"
    path = "~/.testmake/hola"
    result = runner.invoke(cli, [ "run-container", "--image", image, "--target", target, "--path", path, "--container", container, "--password", password])
    assert result.exit_code == 0

