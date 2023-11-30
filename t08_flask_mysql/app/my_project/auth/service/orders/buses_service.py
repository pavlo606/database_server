from my_project.auth.dao import buses_dao
from my_project.auth.service.general_service import GeneralService


class BusesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = buses_dao