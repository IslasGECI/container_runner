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
    --env BITBUCKET_PASSWORD=$BITBUCKET_PASSWORD \
    --env BITBUCKET_USERNAME=analislas \
    --name $CONTENEDOR \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume $RUTA_CLON:/workdir \
    $IMAGEN bash -c "\
      umask 000; \
      make $OBJETIVO \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
    # assert expected_string_command in result.stdout
