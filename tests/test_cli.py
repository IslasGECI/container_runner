from container_runner import cli

from typer.testing import CliRunner

runner = CliRunner()


def test_run_container():
    result = runner.invoke(cli, "--help")
    assert result.exit_code == 0
