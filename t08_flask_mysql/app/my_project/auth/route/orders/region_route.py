from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import region_controller
from my_project.auth.domain import Region

region_bp = Blueprint('region', __name__, url_prefix='/region')

@region_bp.get('')
def get_all_regions() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_all()), HTTPStatus.OK)


@region_bp.post('')
def create_region() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    region = Region.create_from_dto(content)
    region_controller.create(region)
    return make_response(jsonify(region.put_into_dto()), HTTPStatus.CREATED)


@region_bp.get('/city')
def get_all_regions_city() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_all_cities()), HTTPStatus.OK)


@region_bp.get('/<int:region_id>')
def get_region(region_id: int) -> Response:
    """
    Gets region by ID.
    :return: Response object
    """
    return make_response(jsonify(region_controller.find_by_id(region_id)), HTTPStatus.OK)


@region_bp.put('/<int:region_id>')
def update_region(region_id: int) -> Response:
    """
    Updates region by ID.
    :return: Response object
    """
    content = request.get_json()
    client_type = Region.create_from_dto(content)
    region_controller.update(region_id, client_type)
    return make_response("Client updated", HTTPStatus.OK)


@region_bp.patch('/<int:region_id>')
def patch_region(region_id: int) -> Response:
    """
    Patches region by ID.
    :return: Response object
    """
    content = request.get_json()
    region_controller.patch(region_id, content)
    return make_response("Client updated", HTTPStatus.OK)

#client_type_id
@region_bp.delete('/<int:region_id>')
def delete_region(region_id: int) -> Response:
    """
    Deletes region by ID.
    :return: Response object
    """
    region_controller.delete(region_id)
    return make_response("Client deleted", HTTPStatus.OK)
