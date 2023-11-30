from __future__ import annotations
from typing import Dict, Any
from flask import jsonify

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Region(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "region"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45))
    cities = db.relationship('City', backref='region')

    def __repr__(self) -> str:
        return f"Region({self.id}, '{self.name}')"

    def put_into_dto_with_cities(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "cities": list(map(lambda a: a.put_into_dto(), self.cities)),
        }
    
    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Region:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Region(name=dto_dict.get("name"))
        return obj
