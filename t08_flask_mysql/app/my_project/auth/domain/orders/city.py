from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class City(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "city"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45))
    Region_id = db.Column(db.Integer, db.ForeignKey('region.id'))

    busstops = db.relationship('BusStops', backref='city')

    def __repr__(self) -> str:
        return f"City({self.id}, '{self.name}', {self.Region_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "region_id": self.Region_id,
            "busstops": list(map(lambda a: a.put_into_dto(), self.busstops)),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> City:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = City(name=dto_dict.get("name"),
                    Region_id=dto_dict.get("region_id"))
        return obj
