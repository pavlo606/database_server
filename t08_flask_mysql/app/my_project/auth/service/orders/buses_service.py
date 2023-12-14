from my_project.auth.dao import buses_dao
from my_project.auth.service.general_service import GeneralService


class BusesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = buses_dao
    
    def procedure_insert_bus(self, age, capacity, milage, producer_id, route_id):
        return self._dao.procedure_insert_bus(age, capacity, milage, producer_id, route_id)