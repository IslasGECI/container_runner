from container_runner import write_docker_command


def test_write_docker_command():
    expected = 'docker run \
    --env BITBUCKET_PASSWORD=password \
    --env BITBUCKET_USERNAME=username \
    --name container \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume path:/workdir \
    image bash -c "\
      umask 000; \
      make target \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
    obtained = write_docker_command()
    assert obtained == expected
