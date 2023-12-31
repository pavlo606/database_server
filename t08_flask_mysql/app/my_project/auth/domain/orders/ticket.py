from __future__ import annotations
from typing import Dict, Any
from datetime import datetime

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Ticket(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime)
    price = db.Column(db.Integer)
    seat_place = db.Column(db.Integer)
    Passanger_id = db.Column(db.Integer, db.ForeignKey('passangers.id'))
    Route_id = db.Column(db.Integer, db.ForeignKey('routes.id'))
    Start_BusStop_id = db.Column(db.Integer, db.ForeignKey('busstops.id'))
    End_BusStop_id = db.Column(db.Integer, db.ForeignKey('busstops.id'))
    
    start_busstop = db.relationship('BusStops', backref='ticket_start', foreign_keys=[Start_BusStop_id])
    end_busstop = db.relationship('BusStops', backref='ticket_end', foreign_keys=[End_BusStop_id])

    def __repr__(self) -> str:
        return f"Ticket({self.id}, {self.date}, {self.price}, {self.price}, '{self.seat_place}', {self.Passanger_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "date": self.date,
            "price": self.price,
            "seat_place": self.seat_place,
            "Passanger_id": self.Passanger_id,
            "Route_id": self.Route_id,
            "Start_BusStop_id": self.Start_BusStop_id,
            "End_BusStop_id": self.End_BusStop_id,
            "start_busstop":self.start_busstop.put_into_dto(),
            "end_busstop":self.end_busstop.put_into_dto(),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ticket:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Ticket(date=datetime.now(),
                    price=dto_dict.get("price"),
                    seat_place=dto_dict.get("seat_place"),
                    Passanger_id=dto_dict.get("Passanger_id"),
                    Route_id=dto_dict.get("Route_id"),
                    Start_BusStop_id=dto_dict.get("Start_BusStop_id"),
                    End_BusStop_id=dto_dict.get("End_BusStop_id"))
        return obj
