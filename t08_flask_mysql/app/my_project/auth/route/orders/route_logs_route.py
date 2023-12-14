from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import route_logs_controller
from my_project.auth.domain import RouteLogs

route_logs_bp = Blueprint('route_logs', __name__, url_prefix='/route_logs')

@route_logs_bp.get('')
def get_all_route_logs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(route_logs_controller.find_all()), HTTPStatus.OK)


@route_logs_bp.post('')
def create_route_logs() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    route_logs = RouteLogs.create_from_dto(content)
    route_logs_controller.create(route_logs)
    return make_response(jsonify(route_logs.put_into_dto()), HTTPStatus.CREATED)


@route_logs_bp.get('/<int:route_logs_id>')
def get_route_logs(route_logs_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(route_logs_controller.find_by_id(route_logs_id)), HTTPStatus.OK)


@route_logs_bp.put('/<int:route_logs_id>')
def update_route_logs(route_logs_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    route_logs = RouteLogs.create_from_dto(content)
    route_logs_controller.update(route_logs_id, route_logs)
    return make_response("Route logs updated", HTTPStatus.OK)


@route_logs_bp.patch('/<int:route_logs_id>')
def patch_route_logs(route_logs_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    route_logs_controller.patch(route_logs_id, content)
    return make_response("Route logs updated", HTTPStatus.OK)


@route_logs_bp.delete('/<int:route_logs_id>')
def delete_route_logs(route_logs_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    route_logs_controller.delete(route_logs_id)
    return make_response("Route logs deleted", HTTPStatus.OK)