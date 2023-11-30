from typing import List

from my_project.auth.service import region_service
from my_project.auth.controller.general_controller import GeneralController


class RegionController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = region_service

    def find_all_cities(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: x.put_into_dto_with_cities(), self._service.find_all()))
