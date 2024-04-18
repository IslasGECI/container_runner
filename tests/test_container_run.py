from container_runner import write_docker_command


def test_write_docker_command():
    password = "password"
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
    obtained = write_docker_command(password)
    assert obtained == expected

    password_2 = "new_password"
    username = "new_username"
    obtained = write_docker_command(password_2, username)
    assert username in obtained
    assert password_2 in obtained
