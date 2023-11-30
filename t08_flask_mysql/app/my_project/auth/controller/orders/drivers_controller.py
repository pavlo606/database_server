from typing import List

from http import HTTPStatus
from flask import abort

from my_project.auth.service import drivers_service
from my_project.auth.controller.general_controller import GeneralController


class DriversController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = drivers_service

    def find_all_routes(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: x.get_routes(), self._service.find_all()))
    
    def find_by_id_with_routes(self, key: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.get_routes()

