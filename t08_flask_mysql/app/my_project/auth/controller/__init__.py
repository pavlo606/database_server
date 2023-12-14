from .orders.region_controller import RegionController
from .orders.city_controller import CityController
from .orders.busstops_controller import BusStopsController
from .orders.passangers_controller import PassangersController
from .orders.drivers_controller import DriversController
from .orders.buses_controller import BusesController
from .orders.routes_controller import RoutesController
from .orders.subroutes_controller import SubRoutesController
from .orders.ticket_controller import TicketController

region_controller = RegionController()
city_controller = CityController()
busstops_controller = BusStopsController()
passangers_controller = PassangersController()
drivers_controller = DriversController()
buses_controller = BusesController()
routes_controller = RoutesController()
subroutes_controller = SubRoutesController()
ticket_controller = TicketController()
