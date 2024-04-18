from container_runner import write_docker_command


def test_write_docker_command():
    password = "password"
    container = "new_container"
    target = "$OBJETIVO"
    expected = 'docker run \
    --env BITBUCKET_PASSWORD=password \
    --env BITBUCKET_USERNAME=analislas \
    --name new_container \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume path:/workdir \
    image bash -c "\
      umask 000; \
      make $OBJETIVO \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
    obtained = write_docker_command(password, container, target)
    assert obtained == expected

    password = "new_password"
    username = "new_username"
    obtained = write_docker_command(password, container, target, username)
    assert username in obtained
    assert password in obtained
    assert target in obtained
