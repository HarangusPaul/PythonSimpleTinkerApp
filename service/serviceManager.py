from domain.Dto import AssigmentDto
from domain.Lab_assigment import Lab_assigment
from repository.Repository import Repository


class ServiceManager:
    def __init__(self, assigment_repo:Repository, student_repo:Repository):
        self.__assiment = assigment_repo
        self.__repo_student = student_repo

    def assigne_lab_and_stud(self,stud_id,lab_id):
        asigment = Lab_assigment(stud_id, lab_id, -1)
        self.__assiment.save(asigment)


    def note_student(self,stud_id,lab_id,grade):
        asigment = [assigment for assigment in self.__assiment.return_all() if assigment.id_stud == int(stud_id) and
                    assigment.id_lab == int(lab_id)]
        asigment[0].grade = grade
        self.__assiment.update(asigment[0])

    def return_stud_for_given_lab(self,lab_id):
        assigments = [stud for stud in self.__assiment.return_all() if stud.id_lab == lab_id]
        list_of_ass = []

        for assigment in assigments:
            stud = self.__repo_student.return_object_by_id(assigment.id_stud)
            dto = AssigmentDto(stud.get_name(), assigment.grade)
            list_of_ass.append(dto)

        list_of_ass.sort(key=lambda x: (x.name, x.grade))
        return list_of_ass

    def return_bad_stud(self):
        assigments = [stud.id_stud for stud in self.__assiment.return_all()]
        assigments = list(set(assigments))

        list_of_bad_stud = []

        for stud_id in assigments:
            grades = [float(assig.grade) for assig in self.__assiment.return_all() if assig.id_stud == stud_id and
                      assig.grade != (-1)]
            student = self.__repo_student.return_object_by_id(stud_id)
            if len(grades) != 0:
                if sum(grades)/len(grades) < 5:
                    list_of_bad_stud.append(AssigmentDto(student.get_name(),sum(grades)/len(grades)))

        return list_of_bad_stud





