from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class BusStops(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "busstops"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45))
    address: str = db.Column(db.String(45))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))

    def __repr__(self) -> str:
        return f"BusStop({self.id}, '{self.name}', '{self.address}', {self.city_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "city_id": self.city_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BusStops:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = BusStops(name=dto_dict.get("name"),
                    address=dto_dict.get("address"),
                    Region_id=dto_dict.get("region_id"))
        return obj
