from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import busstops_controller
from my_project.auth.domain import BusStops

busstops_bp = Blueprint('busstops', __name__, url_prefix='/busstops')

@busstops_bp.get('')
def get_all_busstops() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(busstops_controller.find_all()), HTTPStatus.OK)


@busstops_bp.post('')
def create_busstop() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    busstop = BusStops.create_from_dto(content)
    busstops_controller.create(busstop)
    return make_response(jsonify(busstop.put_into_dto()), HTTPStatus.CREATED)


@busstops_bp.get('/<int:busstop_id>')
def get_busstop(busstop_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(busstops_controller.find_by_id(busstop_id)), HTTPStatus.OK)


@busstops_bp.put('/<int:busstop_id>')
def update_busstop(busstop_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    busstop = BusStops.create_from_dto(content)
    busstops_controller.update(busstop_id, busstop)
    return make_response("BusStop updated", HTTPStatus.OK)


@busstops_bp.patch('/<int:busstop_id>')
def patch_busstop(busstop_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    busstops_controller.patch(busstop_id, content)
    return make_response("BusStop updated", HTTPStatus.OK)


@busstops_bp.delete('/<int:busstop_id>')
def delete_busstop(busstop_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    busstops_controller.delete(busstop_id)
    return make_response("BusStop deleted", HTTPStatus.OK)