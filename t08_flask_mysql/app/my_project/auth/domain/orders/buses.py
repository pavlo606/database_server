from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Buses(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "buses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    milage = db.Column(db.Integer)
    producer_id = db.Column(db.Integer)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))

    # bus_producer = db.relationship('bus_producer', backref='buses')

    def __repr__(self) -> str:
        return f"Buses({self.id}, {self.age}, {self.capacity}, {self.milage}, '{self.producer}', {self.route_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "age": self.age,
            "capacity": self.capacity,
            "milage": self.milage,
            "producer_id": self.producer_id,
            "Route_id": self.route_id,
            # "bus_producer": list(map(lambda a: a.put_into_dto(), self.bus_producer)),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Buses:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Buses(age=dto_dict.get("age"),
                    capacity=dto_dict.get("capacity"),
                    milage=dto_dict.get("milage"),
                    producer_id=dto_dict.get("producer_id"),
                    route_id=dto_dict.get("route_id"))
        return obj
