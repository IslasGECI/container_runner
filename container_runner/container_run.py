def write_docker_command(password, container="container", username="analislas"):
    return f'docker run \
    --env BITBUCKET_PASSWORD={password} \
    --env BITBUCKET_USERNAME={username} \
    --name {container} \
    --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume path:/workdir \
    image bash -c "\
      umask 000; \
      make target \
        && echo $(date) > .make_succeeded \
        || rm --force .make_succeeded"'
