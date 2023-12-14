from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import City


class CityDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = City
