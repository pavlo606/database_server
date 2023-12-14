from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import BusProducer


class BusProducerDAO(GeneralDAO):
    """
    Realisation of BusProducer data access layer.
    """

    _domain_type = BusProducer
