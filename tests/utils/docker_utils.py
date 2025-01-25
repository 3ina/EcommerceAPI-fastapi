import time

import docker
from docker.errors import NotFound
from docker.models.containers import Container

def is_container_ready(container : Container) -> bool:
    container.reload()
    return container.status == 'running'


def wait_for_stable_status(container : Container,stable_duration=3,interval=1) -> bool:
    start_time = time.time()
    stable_count = 0
    while time.time() - start_time < stable_duration:
        if is_container_ready(container):
            stable_count += 1
        else:
            stable_count = 0

        if stable_count >= stable_duration / interval:
            return True

        time.sleep(interval)

    return False


def start_database_container():
    client = docker.from_env()
    container_name = "test-db"

    try:
        existing_container = client.containers.get(container_name)
        print(f"Existing container {container_name}. Stopping and removing it.")
        existing_container.stop()
        existing_container.remove()
        print(f"Container {container_name} stopped and removed.")
    except NotFound:
        print(f"Container {container_name} not found.")

    container_config = {
        "name":container_name,
        "image":"postgres:16.1-alpine3.19",
        "detach": True,
        "ports":{"5432":"5434"},
        "environment":{
            "POSTGRES_USER":"postgres",
            "POSTGRES_PASSWORD":"postgres",
        }
    }

    container = client.containers.run(**container_config)

    while not is_container_ready(container):
        time.sleep(1)