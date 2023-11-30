from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Drivers(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(45))
    age: int = db.Column(db.Integer)
    experience: int = db.Column(db.Integer)

    def __repr__(self) -> str:
        return f"Drivers({self.id}, '{self.name}', {self.age}, {self.experience})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "experience": self.experience,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Drivers:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Drivers(name=dto_dict.get("name"),
                    age=dto_dict.get("age"),
                    experience=dto_dict.get("experience"))
        return obj
