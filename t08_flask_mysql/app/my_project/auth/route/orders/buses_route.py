from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import buses_controller
from my_project.auth.domain import Buses

buses_bp = Blueprint('buses', __name__, url_prefix='/buses')

@buses_bp.get('')
def get_all_buses() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(buses_controller.find_all()), HTTPStatus.OK)


@buses_bp.post('')
def create_bus() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    bus = Buses.create_from_dto(content)
    buses_controller.create(bus)
    return make_response(jsonify(bus.put_into_dto()), HTTPStatus.CREATED)

@buses_bp.post('/insert_procedure')
def create_bus_by_procedure() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    bus = Buses.create_from_dto(content)
    buses_controller.procedure_insert_bus(bus.age, bus.capacity, bus.milage, bus.producer_id, bus.route_id)
    return make_response(jsonify(bus.put_into_dto()), HTTPStatus.CREATED)


@buses_bp.get('/<int:bus_id>')
def get_bus(bus_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(buses_controller.find_by_id(bus_id)), HTTPStatus.OK)


@buses_bp.put('/<int:bus_id>')
def update_bus(bus_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    bus = Buses.create_from_dto(content)
    buses_controller.update(bus_id, bus)
    return make_response("Bus updated", HTTPStatus.OK)


@buses_bp.patch('/<int:bus_id>')
def patch_bus(bus_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    buses_controller.patch(bus_id, content)
    return make_response("Bus updated", HTTPStatus.OK)


@buses_bp.delete('/<int:bus_id>')
def delete_bus(bus_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    buses_controller.delete(bus_id)
    return make_response("Bus deleted", HTTPStatus.OK)