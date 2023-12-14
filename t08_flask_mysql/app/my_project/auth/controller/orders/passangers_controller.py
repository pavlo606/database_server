from typing import List

from my_project.auth.service import passangers_service
from my_project.auth.controller.general_controller import GeneralController


class PassangersController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = passangers_service
