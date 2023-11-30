from my_project.auth.service import ticket_service
from my_project.auth.controller.general_controller import GeneralController


class TicketController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = ticket_service
