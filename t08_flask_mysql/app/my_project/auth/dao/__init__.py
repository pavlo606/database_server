# orders DB
from .orders.region_dao import RegionDAO
from .orders.city_dao import CityDAO
from .orders.busstops_dao import BusStopsDAO
from .orders.passangers_dao import PassangersDAO
from .orders.drivers_dao import DriversDAO
from .orders.buses_dao import BusesDAO
from .orders.routes_dao import RoutesDAO
from .orders.subroutes_dao import SubRoutesDAO
from .orders.ticket_dao import TicketDAO
from .orders.bus_producer_dao import BusProducerDAO
from .orders.route_logs_dao import RouteLogsDAO

region_dao = RegionDAO()
city_dao = CityDAO()
busstops_dao = BusStopsDAO()
passangers_dao = PassangersDAO()
drivers_dao = DriversDAO()
buses_dao = BusesDAO()
routes_dao = RoutesDAO()
subroutes_dao = SubRoutesDAO()
ticket_dao = TicketDAO()
bus_producer_dao = BusProducerDAO()
route_logs_dao = RouteLogsDAO()
