from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class SubRoutes(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "subroutes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    distance = db.Column(db.Integer)
    price = db.Column(db.Integer)
    Start_BusStop_id = db.Column(db.Integer, db.ForeignKey('busstops.id'))
    End_BusStop_id = db.Column(db.Integer, db.ForeignKey('busstops.id'))

    def __repr__(self) -> str:
        return f"SubRoutes({self.id}, {self.distance}, {self.price}, {self.milage}, '{self.producer}', {self.route_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "distance": self.distance,
            "price": self.price,
            "Start_BusStop_id": self.Start_BusStop_id,
            "End_BusStop_id": self.End_BusStop_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SubRoutes:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SubRoutes(distance=dto_dict.get("distance"),
                        price=dto_dict.get("price"),
                        Start_BusStop_id=dto_dict.get("Start_BusStop_id"),
                        End_BusStop_id=dto_dict.get("End_BusStop_id"))
        return obj
