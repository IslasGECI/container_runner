from container_runner import write_docker_command


def test_write_docker_command():
    expected = 'docker run \
    --env BITBUCKET_PASSWORD=password \
    --env BITBUCKET_USERNAME=analislas \
    --name container \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume path:/workdir \
    image bash -c "\
      umask 000; \
      make target \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'

    password_2 = "new_password"
    username = "new_username"
    container = "new_container"
    obtained = write_docker_command(password_2, container, username)
    assert username in obtained
    assert password_2 in obtained
    assert container in obtained
