from my_project.auth.service import busstops_service
from my_project.auth.controller.general_controller import GeneralController


class BusStopsController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = busstops_service
