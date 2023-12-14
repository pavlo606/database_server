from my_project.auth.service import route_logs_service
from my_project.auth.controller.general_controller import GeneralController


class RouteLogsController(GeneralController):
    """
    Realisation of RouteLogs controller.
    """
    _service = route_logs_service
