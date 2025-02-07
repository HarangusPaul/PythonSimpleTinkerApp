from dataclasses import dataclass


@dataclass
class AssigmentDto:
    name: str
    grade: float

    # def __repr__(self):
    #     return "Name:{0} Grade:{1}".format(self.name, self.grade)