from my_project.auth.dao import passangers_dao
from my_project.auth.service.general_service import GeneralService


class PassangersService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = passangers_dao

    def insert_passanger_data(self):
        return self._dao.insert_passanger_data()