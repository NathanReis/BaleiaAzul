from docker.models.containers import Container
from src.helpers.docker_helper import get_docker_client


def get_all() -> list:
    return get_docker_client().containers.list(all=True)


def get_by_id(id: str) -> Container:
    return get_docker_client().containers.get(id)


def run(image: str, port: dict) -> Container:
    return get_docker_client().containers.run(image, detach=True, ports=port)


def stop(container: Container):
    container.stop()


def start(container: Container):
    container.start()


def delete(container: Container) -> bool:
    if container.status == 'running':
        return False

    container.remove(v=True)

    return True
