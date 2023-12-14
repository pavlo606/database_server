import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Passangers


class PassangersDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Passangers

    def insert_passanger_data(self):
        try:
            result = self._session.execute(sqlalchemy.text("CALL flixbus.insert_passangers()"))
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
