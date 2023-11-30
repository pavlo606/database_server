from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import drivers_controller
from my_project.auth.domain import Drivers

drivers_bp = Blueprint('drivers', __name__, url_prefix='/drivers')

@drivers_bp.get('')
def get_all_drivers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(drivers_controller.find_all()), HTTPStatus.OK)


@drivers_bp.post('')
def create_driver() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    driver = Drivers.create_from_dto(content)
    drivers_controller.create(driver)
    return make_response(jsonify(driver.put_into_dto()), HTTPStatus.CREATED)


@drivers_bp.get('/<int:driver_id>')
def get_driver(driver_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(drivers_controller.find_by_id(driver_id)), HTTPStatus.OK)


@drivers_bp.put('/<int:driver_id>')
def update_driver(driver_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    driver = Drivers.create_from_dto(content)
    drivers_controller.update(driver_id, driver)
    return make_response("Driver updated", HTTPStatus.OK)


@drivers_bp.patch('/<int:driver_id>')
def patch_driver(driver_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    drivers_controller.patch(driver_id, content)
    return make_response("Driver updated", HTTPStatus.OK)


@drivers_bp.delete('/<int:driver_id>')
def delete_driver(driver_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    drivers_controller.delete(driver_id)
    return make_response("Driver deleted", HTTPStatus.OK)