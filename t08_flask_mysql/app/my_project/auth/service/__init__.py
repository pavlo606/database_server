
from .orders.region_service import RegionService
from .orders.city_service import CityService
from .orders.busstops_service import BusStopsService
from .orders.passangers_service import PassangersService
from .orders.drivers_service import DriversService
from .orders.buses_service import BusesService
from .orders.routes_srvice import RoutesService
from .orders.subroutes_service import SubRoutesService
from .orders.ticket_service import TicketService
from .orders.bus_producer_service import BusProducerService
from .orders.route_logs_service import RouteLogsService

region_service = RegionService()
city_service = CityService()
busstops_service = BusStopsService()
passangers_service = PassangersService()
drivers_service = DriversService()
buses_service = BusesService()
routes_srvice = RoutesService()
subroutes_service = SubRoutesService()
ticket_service = TicketService()
bus_producer_service = BusProducerService()
route_logs_service = RouteLogsService()
