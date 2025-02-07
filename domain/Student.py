class Student:
    def __init__(self, id_student, name, grup):
        self.__id_student = int(id_student)
        self.__name_student = str(name)
        self.__group_student = str(grup)

    def get_id(self):
        return self.__id_student

    def get_name(self):
        return self.__name_student

    def get_group(self):
        return self.__group_student

    def set_id(self, value):
        self.__id_student = value

    def set_name(self, value):
        self.__name_student = value

    def set_group(self, value):
        self.__group_student = value

    def __str__(self):
        return "{0}/{1}/{2}\n".format(self.__id_student, self.__name_student, self.__group_student)

    def __eq__(self, other):
        return self.__id_student == other.get_id() and self.__name_student == other.get_name() \
               and self.__group_student == other.get_group()

    def __repr__(self):
        return "{0}.Name:{1} in group:{2}".format(self.__id_student, self.__name_student, self.__group_student)
