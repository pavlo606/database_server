from typing import List

from http import HTTPStatus
from flask import abort

from my_project.auth.service import routes_srvice
from my_project.auth.controller.general_controller import GeneralController


class RoutesController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = routes_srvice

    def insert_routes_has_drivers_dependency(self, driver_name, route_id):
        return self._service.insert_routes_has_drivers_dependency(driver_name, route_id)

    def find_all_subroutes(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: x.get_subroutes(), self._service.find_all()))
    
    def find_by_id_with_subroutes(self, key: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.get_subroutes()

    def find_all_drivers(self) -> List[object]:
        """
        Gets all objects from table using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: x.get_drivers(), self._service.find_all()))
    
    def find_by_id_with_drivers(self, key: int) -> object:
        """
        Gets object from database table by integer key using from Service layer.
        :param key: integer key (surrogate primary key)
        :return: DTO for search object
        """
        obj = self._service.find_by_id(key)
        if obj is None:
            abort(HTTPStatus.NOT_FOUND)
        return obj.get_drivers()
