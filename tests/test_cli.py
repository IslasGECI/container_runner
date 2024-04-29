from container_runner import cli

from typer.testing import CliRunner

runner = CliRunner()


def test_run_container():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0

    result = runner.invoke(
        cli,
        ["run-container", "--help"],
    )

    assert result.exit_code == 0
    assert "run-container" in result.stdout

    image = "islasgeci/hola"
    container = "testmake_hola_develop"
    target = "mundo"
    path = "./hola/"
    password = "contraseña"
    username = "usuario"
    result = runner.invoke(
        cli,
        [
            "run-container",
            "--image",
            image,
            "--target",
            target,
            "--path",
            path,
            "--container",
            container,
            "--password",
            password,
            "--username",
            username,
        ],
    )
    assert result.exit_code == 0
