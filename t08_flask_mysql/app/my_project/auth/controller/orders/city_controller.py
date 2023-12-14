from my_project.auth.service import city_service
from my_project.auth.controller.general_controller import GeneralController


class CityController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = city_service
