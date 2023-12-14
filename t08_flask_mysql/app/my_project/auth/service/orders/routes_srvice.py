from my_project.auth.dao import routes_dao
from my_project.auth.service.general_service import GeneralService


class RoutesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = routes_dao

    def insert_routes_has_drivers_dependency(self, driver_name, route_id):
        return self._dao.insert_routes_has_drivers_dependency(driver_name, route_id)