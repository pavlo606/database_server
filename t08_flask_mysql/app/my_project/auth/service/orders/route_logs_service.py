from my_project.auth.dao import route_logs_dao
from my_project.auth.service.general_service import GeneralService


class RouteLogsService(GeneralService):
    """
    Realisation of RouteLogs service.
    """
    _dao = route_logs_dao