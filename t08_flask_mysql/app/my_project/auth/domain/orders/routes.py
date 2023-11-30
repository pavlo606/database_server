from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


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

    def __repr__(self) -> str:
        return f"Routes({self.id}, {self.age}, {self.capacity}, {self.milage}, '{self.producer}', {self.route_id})"

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
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Routes:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Routes(stops=dto_dict.get("stops"),
                    total_distance=dto_dict.get("total_distance"),
                    Start_BusStop_id=dto_dict.get("Start_BusStop_id"),
                    End_BusStop_id=dto_dict.get("End_BusStop_id"))
        return obj
