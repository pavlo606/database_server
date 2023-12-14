from my_project.auth.service import bus_producer_service
from my_project.auth.controller.general_controller import GeneralController


class BusProducerController(GeneralController):
    """
    Realisation of BusProducer controller.
    """
    _service = bus_producer_service

