from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import SubRoutes


class SubRoutesDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = SubRoutes
