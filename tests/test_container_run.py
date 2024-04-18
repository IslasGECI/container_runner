from container_runner import write_docker_command


def test_write_docker_command():
    password = "password"
    container = "new_container"
    target = "$OBJETIVO"
    path = "new_path"
    expected = 'docker run \
    --env BITBUCKET_PASSWORD=password \
    --env BITBUCKET_USERNAME=analislas \
    --name new_container \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume new_path:/workdir \
    image bash -c "\
      umask 000; \
      make $OBJETIVO \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
    obtained = write_docker_command(password, container, target, path)
    assert obtained == expected

    password = "new_password"
    username = "new_username"
    obtained = write_docker_command(password, container, target, path, username)
    assert username in obtained
    assert password in obtained
    assert target in obtained
    assert path in obtained
