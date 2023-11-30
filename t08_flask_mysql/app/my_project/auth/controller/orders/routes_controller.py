from my_project.auth.service import routes_srvice
from my_project.auth.controller.general_controller import GeneralController


class RoutesController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = routes_srvice
