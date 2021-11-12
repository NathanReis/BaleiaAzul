from docker.models.images import Image
from src.helpers.docker_helper import get_docker_client
from src.services import container_service


def get_all() -> list:
    return get_docker_client().images.list(all=True)


def get_by_id(id: str) -> Image:
    return get_docker_client().images.get(id)


def pull(image_name: str, tag: str) -> Image:
    return get_docker_client().images.pull(image_name, tag)


def delete(id: str) -> bool:
    containers = container_service.get_all()
    image_is_in_use = False

    for container in containers:
        if container.image.short_id == id:
            image_is_in_use = True
            break

    if not image_is_in_use:
        get_docker_client().images.remove(id, force=True, noprune=False)

    return not image_is_in_use
