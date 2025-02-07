from dataclasses import dataclass

from domain.Lab_assigment import Lab_assigment
from domain.Laboratory import Laboratory
from domain.Student import Student


@dataclass
class AssigmentDto:
    name: str
    grade: float

    # def __repr__(self):
    #     return "Name:{0} Grade:{1}".format(self.name, self.grade)