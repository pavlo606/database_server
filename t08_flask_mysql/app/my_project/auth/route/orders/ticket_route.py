from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import ticket_controller, routes_controller
from my_project.auth.domain import Ticket

ticket_bp = Blueprint('ticket', __name__, url_prefix='/ticket')

@ticket_bp.get('')
def get_all_tickets() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(ticket_controller.find_all()), HTTPStatus.OK)


@ticket_bp.post('')
def create_ticket() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    ticket = Ticket.create_from_dto(content)
    subroutes = routes_controller.find_by_id_with_subroutes(ticket.Route_id)["subroutes"]
    total_price = 0
    is_ticket_route = False
    for subroute in subroutes:
        if subroute["Start_BusStop_id"] == ticket.Start_BusStop_id:
            is_ticket_route = True
        elif subroute["Start_BusStop_id"] == ticket.End_BusStop_id:
            is_ticket_route = False
        if is_ticket_route:
            print("yes")
            print(subroute["Start_BusStop_id"])
            print(int(subroute["price"]))
            total_price += int(subroute["price"])
    ticket.price = total_price
    ticket_controller.create(ticket)
    return make_response(jsonify(ticket.put_into_dto()), HTTPStatus.CREATED)


@ticket_bp.get('/<int:ticket_id>')
def get_ticket(ticket_id: int) -> Response:
    """
    Gets city_id by ID.
    :return: Response object
    """
    return make_response(jsonify(ticket_controller.find_by_id(ticket_id)), HTTPStatus.OK)


@ticket_bp.put('/<int:ticket_id>')
def update_ticket(ticket_id: int) -> Response:
    """
    Updates city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    ticket = Ticket.create_from_dto(content)
    ticket_controller.update(ticket_id, ticket)
    return make_response("Ticket updated", HTTPStatus.OK)


@ticket_bp.patch('/<int:ticket_id>')
def patch_ticket(ticket_id: int) -> Response:
    """
    Patches city_id by ID.
    :return: Response object
    """
    content = request.get_json()
    ticket_controller.patch(ticket_id, content)
    return make_response("Ticket updated", HTTPStatus.OK)


@ticket_bp.delete('/<int:ticket_id>')
def delete_ticket(ticket_id: int) -> Response:
    """
    Deletes city_id by ID.
    :return: Response object
    """
    ticket_controller.delete(ticket_id)
    return make_response("Ticket deleted", HTTPStatus.OK)