from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import routes_controller
from my_project.auth.domain import Routes

routes_bp = Blueprint('routes', __name__, url_prefix='/routes')

@routes_bp.get('')
def get_all_routes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_all()), HTTPStatus.OK)


@routes_bp.post('')
def create_route() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    route = Routes.create_from_dto(content)
    routes_controller.create(route)
    return make_response(jsonify(route.put_into_dto()), HTTPStatus.CREATED)


@routes_bp.get('/<int:route_id>')
def get_route(route_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_by_id(route_id)), HTTPStatus.OK)


@routes_bp.put('/<int:route_id>')
def update_route(route_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    route = Routes.create_from_dto(content)
    routes_controller.update(route_id, route)
    return make_response("Route updated", HTTPStatus.OK)


@routes_bp.patch('/<int:route_id>')
def patch_route(route_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    routes_controller.patch(route_id, content)
    return make_response("Route updated", HTTPStatus.OK)


@routes_bp.delete('/<int:route_id>')
def delete_route(route_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    routes_controller.delete(route_id)
    return make_response("Route deleted", HTTPStatus.OK)