from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import RouteLogs


class RouteLogsDAO(GeneralDAO):
    """
    Realisation of BusProducer data access layer.
    """
    _domain_type = RouteLogs
