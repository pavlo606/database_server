import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Routes


class RoutesDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Routes

    def insert_routes_has_drivers_dependency(self, driver_name, route_id):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL flixbus.insert_routes_has_drivers_dependency(:p1, :p2)"),
                {"p1": driver_name, "p2": route_id})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
