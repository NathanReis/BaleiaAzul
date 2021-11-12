from docker import DockerClient
from docker.models.containers import Container
from docker.models.images import Image
import os


def extract_container_data(container: Container) -> dict:
    return {
        'created_at': container.attrs['Created'],
        'id': container.short_id,
        'image': extract_image_data(container.image),
        'name': container.name,
        'status': container.status
    }


def extract_containers_data(containers: list) -> dict:
    containers_data = []

    for container in containers:
        containers_data.append(extract_container_data(container))

    return containers_data


def extract_image_data(image: Image) -> dict:
    return {
        'downloaded_at': image.attrs['Created'],
        'id': image.short_id,
        'os': image.attrs['Os'],
        'size': image.attrs['Size'],
        'tags': image.tags
    }


def extract_images_data(images: list) -> list:
    images_data = []

    for image in images:
        images_data.append(extract_image_data(image))

    return images_data


def extract_stats_container_data(stats: dict) -> dict:
    return {
        'cpu': {
            'amount_threads': stats['cpu_stats']['online_cpus'],
            'usage': stats['cpu_stats']['cpu_usage']['total_usage']
        },
        'memory': {
            'limit': stats['memory_stats']['limit'],
            'max_usage': stats['memory_stats']['max_usage'],
            'usage': stats['memory_stats']['usage']
        }
    }


def get_docker_client() -> DockerClient:
    DOCKER_HOST = os.getenv('DOCKER_API_HOST')
    DOCKER_PORT = os.getenv('DOCKER_API_PORT')

    return DockerClient(
        base_url='tcp://' + DOCKER_HOST + ':' + DOCKER_PORT,
        version='auto'
    )
