from docker.errors import ImageNotFound, NotFound
from flask import Request
from src.enums.docker_model_enum import DockerModelEnum
from src.helpers.docker_helper import extract_container_data, extract_containers_data, extract_stats_container_data
from src.helpers.response_helper import create_fail_response, create_not_found_response, create_success_response, create_unexpected_error_response
from src.services import container_service


def get_all(request: Request) -> dict:
    try:
        return create_success_response(
            extract_containers_data(
                container_service.get_all()
            )
        )
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def get_by_id(request: Request, id: str) -> dict:
    try:
        return create_success_response(
            extract_container_data(
                container_service.get_by_id(id)
            )
        )
    except NotFound as exception:
        return create_not_found_response(DockerModelEnum.CONTAINER)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def get_stats(request: Request, id: str) -> dict:
    try:
        container = container_service.get_by_id(id)

        return create_success_response(
            extract_stats_container_data(
                container_service.get_stats(container)
            )
        )
    except NotFound as exception:
        return create_not_found_response(DockerModelEnum.CONTAINER)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def run(request: Request) -> dict:
    try:
        request_data = request.get_json(cache=False)

        image = request_data['image']
        port = request_data['port']

        return create_success_response(
            extract_container_data(
                container_service.run(image, port)
            )
        )
    except ImageNotFound as exception:
        return create_not_found_response(DockerModelEnum.IMAGE, image)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def stop(request: Request, id: str) -> dict:
    try:
        container = container_service.get_by_id(id)

        container_service.stop(container)

        return create_success_response(True)
    except NotFound as exception:
        return create_not_found_response(DockerModelEnum.CONTAINER)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def start(request: Request, id: str) -> dict:
    try:
        container = container_service.get_by_id(id)

        container_service.start(container)

        return create_success_response(True)
    except NotFound as exception:
        return create_not_found_response(DockerModelEnum.CONTAINER)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def delete(request: Request, id: str) -> dict:
    try:
        container = container_service.get_by_id(id)
        was_deleted = container_service.delete(container)

        if was_deleted:
            return create_success_response(True)

        return create_fail_response('Container em execução')
    except NotFound as exception:
        return create_not_found_response(DockerModelEnum.CONTAINER)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def delete_all(request: Request) -> dict:
    try:
        containers = container_service.get_all()
        containers_running = []

        for container in containers:
            was_deleted = container_service.delete(container)

            if not was_deleted:
                containers_running.append(container.id)

        amount_containers_running = len(containers_running)

        if amount_containers_running == 0:
            return create_success_response(True)
        elif amount_containers_running == 1:
            return create_fail_response('Container ' + containers_running[0] + ' está sendo executado')

        return create_fail_response('Containers ' + ', '.join(containers_running) + ' estão sendo executados')
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()
