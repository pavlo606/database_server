from my_project.auth.dao import bus_producer_dao
from my_project.auth.service.general_service import GeneralService


class BusProducerService(GeneralService):
    """
    Realisation of BusProducer service.
    """
    _dao = bus_producer_dao
