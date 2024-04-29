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
        ],
    )
    assert result.exit_code == 0
    expected_string_command = 'docker run \
    --env BITBUCKET_PASSWORD=contraseña \
    --env BITBUCKET_USERNAME=analislas \
    --name testmake_hola_develop \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume ./hola/:/workdir \
    islasgeci/hola bash -c "\
      umask 000; \
      make mundo \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
    assert expected_string_command in result.stdout
