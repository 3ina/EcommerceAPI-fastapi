import docker
from docker.errors import NotFound
from docker.models.containers import Container

def is_container_ready(container : Container) -> bool:
    container.reload()
    return container.status == 'running'


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