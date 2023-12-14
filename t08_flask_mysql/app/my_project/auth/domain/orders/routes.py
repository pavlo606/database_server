from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

routes_has_subroutes = db.Table('routes_has_subroutes',
    db.Column('Route_id', db.Integer, db.ForeignKey('routes.id'), primary_key=True),
    db.Column('SubRoute_id', db.Integer, db.ForeignKey('subroutes.id'), primary_key=True)
)

drivers_has_routes = db.Table('drivers_has_routes',
    db.Column('Driver_id', db.Integer, db.ForeignKey('drivers.id'), primary_key=True),
    db.Column('Route_id', db.Integer, db.ForeignKey('routes.id'), primary_key=True)
)

class Routes(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    stops = db.Column(db.Integer)
    total_distance = db.Column(db.Integer)
    Start_BusStop_id = db.Column(db.Integer, db.ForeignKey('busstops.id'))
    End_BusStop_id = db.Column(db.Integer, db.ForeignKey('busstops.id'))
    
    start_busstop = db.relationship('BusStops', backref='routes_start', foreign_keys=[Start_BusStop_id])
    end_busstop = db.relationship('BusStops', backref='routes_end', foreign_keys=[End_BusStop_id])
    buses = db.relationship('Buses', backref='routes_buses')
    subroutes = db.relationship('SubRoutes', secondary=routes_has_subroutes, backref='routes_subroutes')
    drivers = db.relationship('Drivers', secondary=drivers_has_routes, backref='routes_drivers')

    def __repr__(self) -> str:
        return f"Routes({self.id}, {self.stops}, {self.total_distance}, {self.Start_BusStop_id}, '{self.End_BusStop_id}')"

    def get_drivers(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "stops": self.stops,
            "total_dastance": self.total_distance,
            "Start_BusStop_id": self.Start_BusStop_id,
            "End_BusStop_id": self.End_BusStop_id,
            "start_busstop":self.start_busstop.put_into_dto(),
            "end_busstop":self.end_busstop.put_into_dto(),
            "buses": list(map(lambda a: a.put_into_dto(), self.buses)),
            "drivers": list(map(lambda a: a.put_into_dto(), self.drivers)),
        }

    def get_subroutes(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "stops": self.stops,
            "total_dastance": self.total_distance,
            "Start_BusStop_id": self.Start_BusStop_id,
            "End_BusStop_id": self.End_BusStop_id,
            "start_busstop":self.start_busstop.put_into_dto(),
            "end_busstop":self.end_busstop.put_into_dto(),
            "buses": list(map(lambda a: a.put_into_dto(), self.buses)),
            "subroutes": list(map(lambda a: a.put_into_dto(), self.subroutes)),
        }

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "stops": self.stops,
            "total_dastance": self.total_distance,
            "Start_BusStop_id": self.Start_BusStop_id,
            "End_BusStop_id": self.End_BusStop_id,
            "start_busstop":self.start_busstop.put_into_dto(),
            "end_busstop":self.end_busstop.put_into_dto(),
            "buses": list(map(lambda a: a.put_into_dto(), self.buses)),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> tuple[Routes, list[int]]:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Routes(stops=dto_dict.get("stops"),
                    total_distance=dto_dict.get("total_distance"),
                    Start_BusStop_id=dto_dict.get("Start_BusStop_id"),
                    End_BusStop_id=dto_dict.get("End_BusStop_id"))
        return obj, dto_dict.get("Subroutes")
