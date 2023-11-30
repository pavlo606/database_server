from my_project.auth.service import buses_service
from my_project.auth.controller.general_controller import GeneralController


class BusesController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = buses_service
