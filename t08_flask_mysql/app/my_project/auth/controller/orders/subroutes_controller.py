from my_project.auth.service import subroutes_service
from my_project.auth.controller.general_controller import GeneralController


class SubRoutesController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = subroutes_service
