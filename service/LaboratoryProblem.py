from domain.Laboratory import Laboratory
from domain.Validators import EntityValidator
from repository.Repository import Repository


class LaboratoryService:
    def __init__(self,repository: Repository):
        self.__Laboratory_Service = repository

    def add_lab(self, id_lab, lab_number, problem_number, description, deadline):
        """
        This function adds a thing in other things
        :param id_lab: int
        :param lab_number: int
        :param problem_number: int
        :param description: str
        :param deadline: date
        :return: none
        """
        validator = EntityValidator()
        validator.validate_student(self.__Laboratory_Service.return_all(),id_lab)

        lab = Laboratory(id_lab, lab_number, problem_number, description, deadline)
        self.__Laboratory_Service.save(lab)

    def del_lab(self,id_lab):
        lab = self.__Laboratory_Service.return_object_by_id(id_lab)
        self.__Laboratory_Service.delete(lab)

    def update_lab(self, id_lab, lab_number, problem_number, description, deadline):
        updated_lab = Laboratory(id_lab, lab_number, problem_number, description, deadline)
        self.__Laboratory_Service.update(updated_lab)

    def return_lab_by_id(self, id_lab):
        """

        :param id_lab:
        :return: self.__Laboratory_Service.return_object_by_id(id_lab) wich has type lab
        """
        return self.__Laboratory_Service.return_object_by_id(id_lab)

    def return_all_labs(self):
        return self.__Laboratory_Service.return_all()

    # def add_labs(self):
    #     self.add_lab(1, 1, 3, "Plm", "10:10")
    #     self.add_lab(2, 3, 2, "Plm", "10:11")
    #     self.add_lab(3, 2, 1, "Plm", "10:9")