from container_runner import write_docker_command


def test_write_docker_command():
    password = "$BITBUCKET_PASSWORD"
    container = "$CONTENEDOR"
    target = "$OBJETIVO"
    path = "$RUTA_CLON"
    image = "$IMAGEN"
    expected = 'docker run \
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
    obtained = write_docker_command(password, container, target, path, image)
    assert obtained == expected
