from dataclasses import dataclass


@dataclass
class Lab_assigment:
    __id_stud: int
    __id_lab: int
    grade: float

    def get_id(self):
        return "({0},{1})".format(self.__id_stud, self.__id_lab)

    @property
    def id_stud(self):
        return self.__id_stud

    @property
    def id_lab(self):
        return self.__id_lab

    def __str__(self):
        return "{0}/{1}/{2}\n".format(self.__id_stud, self.__id_lab, self.grade)

    def __repr__(self):
        return "{0}/{1}/{2}".format(self.__id_stud, self.__id_lab, self.grade)

    def __eq__(self, other):
        return self.get_id() == other.get_id()
