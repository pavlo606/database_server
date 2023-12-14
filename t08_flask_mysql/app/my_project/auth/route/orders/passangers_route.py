from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import passangers_controller
from my_project.auth.domain import Passangers

passangers_bp = Blueprint('passangers', __name__, url_prefix='/passangers')

@passangers_bp.get('')
def get_all_passangers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(passangers_controller.find_all()), HTTPStatus.OK)


@passangers_bp.post('')
def create_passanger() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    passanger = Passangers.create_from_dto(content)
    passangers_controller.create(passanger)
    return make_response(jsonify(passanger.put_into_dto()), HTTPStatus.CREATED)

@passangers_bp.get('/insert_data')
def insert_passangers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    passangers_controller.insert_passanger_data()
    return make_response("Successfuly inserted data into passangers", HTTPStatus.CREATED)

@passangers_bp.get('/<int:passanger_id>')
def get_passanger(passanger_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(passangers_controller.find_by_id(passanger_id)), HTTPStatus.OK)


@passangers_bp.put('/<int:passanger_id>')
def update_passanger(passanger_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    passanger = Passangers.create_from_dto(content)
    passangers_controller.update(passanger_id, passanger)
    return make_response("Passanger updated", HTTPStatus.OK)


@passangers_bp.patch('/<int:passanger_id>')
def patch_passanger(passanger_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    passangers_controller.patch(passanger_id, content)
    return make_response("Passanger updated", HTTPStatus.OK)


@passangers_bp.delete('/<int:passanger_id>')
def delete_passanger(passanger_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    passangers_controller.delete(passanger_id)
    return make_response("Passanger deleted", HTTPStatus.OK)