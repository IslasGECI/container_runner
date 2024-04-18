from container_runner import write_docker_command


def test_write_docker_command():
    password = "password"
    container = "$CONTENEDOR"
    target = "$OBJETIVO"
    path = "$RUTA_CLON"
    expected = 'docker run \
    --env BITBUCKET_PASSWORD=password \
    --env BITBUCKET_USERNAME=analislas \
    --name $CONTENEDOR \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume $RUTA_CLON:/workdir \
    image bash -c "\
      umask 000; \
      make $OBJETIVO \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
    obtained = write_docker_command(password, container, target, path)
    assert obtained == expected

    password = "new_password"
    username = "new_username"
    image = "$IMAGEN"
    obtained = write_docker_command(password, container, target, path, image, username)
    assert username in obtained
    assert password in obtained
    assert target in obtained
    assert image in obtained
    assert path in obtained
