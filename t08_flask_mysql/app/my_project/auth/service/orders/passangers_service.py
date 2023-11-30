from my_project.auth.dao import passangers_dao
from my_project.auth.service.general_service import GeneralService


class PassangersService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = passangers_dao