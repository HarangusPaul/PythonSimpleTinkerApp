from domain.Lab_assigment import Lab_assigment
from service.Repository import Repository


class ServiceManager:
    def __init__(self, assigment_repo:Repository, student_repo:Repository):
        self.__assiment = assigment_repo
        self.__repo_student = student_repo

    def assigne_lab_and_stud(self,stud_id,lab_id):
        asigment = Lab_assigment(stud_id, lab_id, -1)
        self.__assiment.save(asigment)


    def note_student(self,stud_id,lab_id,grade):
        pass

    def return_stud_for_given_lab(self,lab_id):
        assigments = [stud for stud in self.__assiment.return_all() if stud.id_lab == lab_id]
        list_of_ass = []

        for assigment in assigments:
            pass

        list_of_ass.sort(key=lambda x: (x.name, x.grade))
        return list_of_ass

    def return_bad_stud(self):
        assigments = [stud.id_stud for stud in self.__assiment.return_all()]
        assigments = list(set(assigments))

        list_of_bad_stud = []

        for stud_id in assigments:
            pass

        return list_of_bad_stud





