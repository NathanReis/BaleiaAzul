from flask import Flask, request
from flask_cors import CORS
from src.controllers import container_controller, image_controller

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return {'message': 'Hello, World!'}


# Start - Image routes
@app.route('/images')
def get_all_images():
    return image_controller.get_all(request)


@app.route('/images/<string:id>')
def get_image(id: str):
    return image_controller.get_by_id(request, id)


@app.route('/images', methods=['DELETE'])
def delete_all_images():
    return image_controller.delete_all(request)


@app.route('/images/<string:id>', methods=['DELETE'])
def delete_image(id: str):
    return image_controller.delete(request, id)


@app.route('/images', methods=['POST'])
def pull_image():
    return image_controller.pull(request)
# End - Image routes


# Start - Container routes
@app.route('/containers')
def get_all_containers():
    return container_controller.get_all(request)


@app.route('/containers/<string:id>')
def get_container(id: str):
    return container_controller.get_by_id(request, id)


@app.route('/containers', methods=['DELETE'])
def delete_all_containers():
    return container_controller.delete_all(request)


@app.route('/containers/<string:id>', methods=['DELETE'])
def delete_container(id: str):
    return container_controller.delete(request, id)


@app.route('/containers/run', methods=['POST'])
def run_container():
    return container_controller.run(request)


@app.route('/containers/stop/<string:id>', methods=['POST'])
def stop_container(id: str):
    return container_controller.stop(request, id)


@app.route('/containers/start/<string:id>', methods=['POST'])
def start_container(id: str):
    return container_controller.start(request, id)


@app.route('/containers/stats/<string:id>')
def get_stats_container(id: str):
    return container_controller.get_stats(request, id)
# End - Container routes
