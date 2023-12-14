from my_project.auth.dao import routes_dao
from my_project.auth.service.general_service import GeneralService


class RoutesService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = routes_dao