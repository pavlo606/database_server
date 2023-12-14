from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import routes_controller
from my_project.auth.service import subroutes_service
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
    route, subroutes = Routes.create_from_dto(content)
    route.stops = len(subroutes)
    total_distance = 0
    for i in subroutes:
        subroute = subroutes_service.find_by_id(i)
        total_distance += subroute.distance
        route.subroutes.append(subroute)
    route.total_distance = total_distance
    routes_controller.create(route)
    return make_response(jsonify(route.put_into_dto()), HTTPStatus.CREATED)


@routes_bp.get('/<int:route_id>/driver_name/<string:driver_name>')
def insert_routes_has_drivers(route_id, driver_name) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    routes_controller.insert_routes_has_drivers_dependency(driver_name, route_id)
    return make_response("Successfuly inserted into routes_has_drivers", HTTPStatus.OK)


@routes_bp.get('/subroutes')
def get_all_routes_subroutes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_all_subroutes()), HTTPStatus.OK)


@routes_bp.get('/drivers')
def get_all_routes_drivers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_all_drivers()), HTTPStatus.OK)


@routes_bp.get('/<int:route_id>')
def get_route(route_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_by_id(route_id)), HTTPStatus.OK)


@routes_bp.get('/subroutes/<int:route_id>')
def get_routes_subroutes(route_id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_by_id_with_subroutes(route_id)), HTTPStatus.OK)


@routes_bp.get('/drivers/<int:route_id>')
def get_routes_drivers(route_id: int) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(routes_controller.find_by_id_with_drivers(route_id)), HTTPStatus.OK)


@routes_bp.put('/<int:route_id>')
def update_route(route_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    route, _ = Routes.create_from_dto(content)
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