from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class RouteLogs(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "route_logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime)
    route_id = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"BusProducer({self.id}, {self.date_time}, {self.route_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "date_time": self.date_time,
            "route_id": self.route_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RouteLogs:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = RouteLogs(date_time=dto_dict.get("date_time"),
                        route_id=dto_dict.get("route_id"))
        return obj
