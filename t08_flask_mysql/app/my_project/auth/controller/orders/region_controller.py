from typing import List

from my_project.auth.service import region_service
from my_project.auth.controller.general_controller import GeneralController


class RegionController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = region_service
