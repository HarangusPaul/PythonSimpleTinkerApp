from domain.Lab_assigment import Lab_assigment
from domain.Laboratory import Laboratory
from repository.Student import Student

class Generator:
    def generate_class(self, class_type, string: str):
        if class_type == Student:
            return self.generate_student_class(string,Student)
        if class_type == Laboratory:
            return self.generate_laboratory_class(string, Laboratory)
        if class_type == Lab_assigment:
            return self.generate_assigment_class(string, Lab_assigment)

    @staticmethod
    def generate_student_class(string_attributes: str, class_constructor):
        string_attributes = string_attributes.strip()
        string_attributes = string_attributes.split("/")
        return class_constructor(int(string_attributes[0]), string_attributes[1], string_attributes[2])

    @staticmethod
    def generate_laboratory_class(string_attributes: str, class_constructor):
        string_attributes = string_attributes.strip()
        string_attributes = string_attributes.split("/")
        return class_constructor(int(string_attributes[0]), string_attributes[1], string_attributes[2],
                                 string_attributes[3], string_attributes[4])

    @staticmethod
    def generate_assigment_class(string_attributes: str, class_constructor):
        string_attributes = string_attributes.strip()
        string_attributes = string_attributes.split("/")
        return class_constructor(int(string_attributes[0]), int(string_attributes[1]), float(string_attributes[2]))