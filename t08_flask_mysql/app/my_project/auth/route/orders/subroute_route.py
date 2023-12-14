from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import subroutes_controller
from my_project.auth.domain import SubRoutes

subroutes_bp = Blueprint('subroutes', __name__, url_prefix='/subroutes')

@subroutes_bp.get('')
def get_all_subroutes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(subroutes_controller.find_all()), HTTPStatus.OK)

@subroutes_bp.get('/routes')
def get_all_subroutes_routes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(subroutes_controller.find_all_routes()), HTTPStatus.OK)


@subroutes_bp.post('')
def create_subroute() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    subroute = SubRoutes.create_from_dto(content)
    subroutes_controller.create(subroute)
    return make_response(jsonify(subroute.put_into_dto()), HTTPStatus.CREATED)


@subroutes_bp.get('/<int:subroute_id>')
def get_subroute(subroute_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(subroutes_controller.find_by_id(subroute_id)), HTTPStatus.OK)

@subroutes_bp.get('/routes/<int:subroute_id>')
def get_subroute_route(subroute_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(subroutes_controller.find_by_id_with_routes(subroute_id)), HTTPStatus.OK)


@subroutes_bp.put('/<int:subroute_id>')
def update_subroute(subroute_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    subroute = SubRoutes.create_from_dto(content)
    subroutes_controller.update(subroute_id, subroute)
    return make_response("Subroute updated", HTTPStatus.OK)


@subroutes_bp.patch('/<int:subroute_id>')
def patch_subroute(subroute_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    subroutes_controller.patch(subroute_id, content)
    return make_response("Subroute updated", HTTPStatus.OK)


@subroutes_bp.delete('/<int:subroute_id>')
def delete_subroute(subroute_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    subroutes_controller.delete(subroute_id)
    return make_response("Subroute deleted", HTTPStatus.OK)