from my_project.auth.service import buses_service
from my_project.auth.controller.general_controller import GeneralController


class BusesController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = buses_service

    def procedure_insert_bus(self, age, capacity, milage, producer_id, route_id):
        return self._service.procedure_insert_bus(age, capacity, milage, producer_id, route_id)