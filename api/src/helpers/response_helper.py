from src.enums.docker_enums import DockerModelEnum


def create_fail_response(error, status_code=400):
    return {
        'error': error,
        'code': status_code
    }


def create_not_found_response(docker_model: DockerModelEnum, identifier=''):
    message = docker_model.value

    if len(identifier) > 0:
        message = message + ' ' + identifier

    if docker_model == DockerModelEnum.CONTAINER:
        message = message + ' não encontrado'
    else:
        message = message + ' não encontrada'

    return create_fail_response(message, 404)


def create_success_response(data, status_code=200):
    return {
        'data': data,
        'code': status_code
    }


def create_unexpected_error_response():
    return create_fail_response('Erro inesperado', 500)
