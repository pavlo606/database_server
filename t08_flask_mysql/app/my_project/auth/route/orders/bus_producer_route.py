from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import bus_producer_controller
from my_project.auth.domain import BusProducer

bus_producer_bp = Blueprint('bus_producer', __name__, url_prefix='/bus_producer')

@bus_producer_bp.get('')
def get_all_bus_producers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(bus_producer_controller.find_all()), HTTPStatus.OK)


@bus_producer_bp.post('')
def create_bus_producer() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    bus_producer = BusProducer.create_from_dto(content)
    bus_producer_controller.create(bus_producer)
    return make_response(jsonify(bus_producer.put_into_dto()), HTTPStatus.CREATED)


@bus_producer_bp.get('/<int:bus_producer_id>')
def get_bus_producer(bus_producer_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(bus_producer_controller.find_by_id(bus_producer_id)), HTTPStatus.OK)


@bus_producer_bp.put('/<int:bus_producer_id>')
def update_bus_producer(bus_producer_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    bus_producer = BusProducer.create_from_dto(content)
    bus_producer_controller.update(bus_producer_id, bus_producer)
    return make_response("Bus producer updated", HTTPStatus.OK)


@bus_producer_bp.patch('/<int:bus_producer_id>')
def patch_bus_producer(bus_producer_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    bus_producer_controller.patch(bus_producer_id, content)
    return make_response("Bus producer updated", HTTPStatus.OK)


@bus_producer_bp.delete('/<int:bus_producer_id>')
def delete_bus_producer(bus_producer_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    bus_producer_controller.delete(bus_producer_id)
    return make_response("Bus producer deleted", HTTPStatus.OK)