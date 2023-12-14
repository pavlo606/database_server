from my_project.auth.dao import drivers_dao
from my_project.auth.service.general_service import GeneralService


class DriversService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = drivers_dao