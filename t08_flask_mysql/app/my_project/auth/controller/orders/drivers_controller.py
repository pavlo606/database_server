from typing import List

from my_project.auth.service import drivers_service
from my_project.auth.controller.general_controller import GeneralController


class DriversController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = drivers_service
