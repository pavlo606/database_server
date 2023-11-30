from my_project.auth.dao import subroutes_dao
from my_project.auth.service.general_service import GeneralService


class SubRoutesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = subroutes_dao