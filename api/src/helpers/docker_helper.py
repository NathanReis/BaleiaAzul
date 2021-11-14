from docker import DockerClient
from docker.models.containers import Container
from docker.models.images import Image
from dotenv import load_dotenv
from os import getenv, path


def extract_container_data(container: Container) -> dict:
    ports = []

    for container_port, host_ports in container.attrs['NetworkSettings']['Ports'].items():
        if host_ports != None:
            ports.append({container_port: host_ports[0]['HostPort']})

    return {
        'created_at': container.attrs['Created'],
        'id': container.short_id,
        'image': extract_image_data(container.image),
        'name': container.name,
        'ports': ports,
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


def extract_stats_container_data(container: Container, stats: dict) -> dict:
    stats_data = {
        'id': container.short_id,
        'name': container.name,
        'status': container.status
    }

    if container.status != 'running':
        return stats_data

    stats_data['amount_pids'] = stats['pids_stats']['current']
    stats_data['cpu'] = {
        'amount_threads': stats['cpu_stats']['online_cpus'],
        'usage': stats['cpu_stats']['cpu_usage']['total_usage']
    }
    stats_data['memory'] = {
        'limit': stats['memory_stats']['limit'],
        'max_usage': stats['memory_stats']['max_usage'],
        'usage': stats['memory_stats']['usage']
    }
    stats_data['network'] = {
        'input': stats['networks']['eth0']['rx_bytes'],
        'output': stats['networks']['eth0']['tx_bytes']
    }

    return stats_data


def get_docker_client() -> DockerClient:
    load_dotenv(
        path.join(
            path.dirname(path.realpath(__file__)),
            '..',
            '..',
            '.env'
        )
    )

    HOST = getenv('DOCKER_API_HOST')
    PORT = getenv('DOCKER_API_PORT')

    return DockerClient(base_url='tcp://' + HOST + ':' + PORT, version='auto')
