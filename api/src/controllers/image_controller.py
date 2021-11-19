from docker.errors import ImageNotFound
from flask import Request
from src.enums.docker_model_enum import DockerModelEnum
from src.helpers.docker_helper import extract_image_data, extract_images_data
from src.helpers.response_helper import create_fail_response, create_not_found_response, create_success_response, create_unexpected_error_response
from src.services import image_service


def get_all(request: Request) -> dict:
    try:
        return create_success_response(
            extract_images_data(
                image_service.get_all()
            )
        )
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def get_by_id(request: Request, id: str) -> dict:
    try:
        return create_success_response(
            extract_image_data(
                image_service.get_by_id(id)
            )
        )
    except ImageNotFound as exception:
        return create_not_found_response(DockerModelEnum.IMAGE)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def pull(request: Request) -> dict:
    try:
        request_data = request.get_json(cache=False)

        name = request_data['name']
        tag = request_data['tag']

        return create_success_response(
            extract_image_data(
                image_service.pull(name, tag)
            )
        )
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def delete(request: Request, id: str) -> dict:
    try:
        image_service.get_by_id(id)
        was_deleted = image_service.delete(id)

        if was_deleted:
            return create_success_response(True)

        return create_fail_response('Imagem sendo usada em algum container')
    except ImageNotFound as exception:
        return create_not_found_response(DockerModelEnum.IMAGE)
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()


def delete_all(request: Request) -> dict:
    try:
        images = image_service.get_all()
        images_in_use = []

        for image in images:
            was_deleted = image_service.delete(image.short_id)

            if not was_deleted:
                images_in_use.append(image.short_id)

        amount_images_in_use = len(images_in_use)

        if amount_images_in_use == 0:
            return create_success_response(True)
        elif amount_images_in_use == 1:
            return create_success_response('Imagem ' + images_in_use[0] + ' sendo usada em algum container')

        return create_success_response('Imagens ' + ', '.join(images_in_use) + ' sendo usadas em alguns containers')
    except Exception as exception:
        print(exception)
        return create_unexpected_error_response()
