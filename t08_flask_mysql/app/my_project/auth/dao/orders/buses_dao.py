import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Buses


class BusesDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Buses

    def procedure_insert_bus(self, age, capacity, milage, producer_id, route_id):
            try:
                result = self._session.execute(
                    sqlalchemy.text("CALL flixbus.insert_bus(:age, :capacity, :milage, :producer_id, :route_id)"),
                    {"age": age, "capacity": capacity, "milage": milage, "producer_id": producer_id, "route_id": route_id},
                )
                self._session.commit()
                return result.mappings()
            except Exception as e:
                print(f"Error executing stored procedure: {e}")
                self._session.rollback()
                return None