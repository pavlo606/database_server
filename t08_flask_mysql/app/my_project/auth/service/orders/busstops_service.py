from my_project.auth.dao import busstops_dao
from my_project.auth.service.general_service import GeneralService


class BusStopsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = busstops_dao