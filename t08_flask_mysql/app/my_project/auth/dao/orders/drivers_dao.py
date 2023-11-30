from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Drivers


class DriversDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = Drivers
