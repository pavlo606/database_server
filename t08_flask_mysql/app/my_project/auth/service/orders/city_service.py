from my_project.auth.dao import city_dao
from my_project.auth.service.general_service import GeneralService


class CityService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = city_dao