import traceback

from service.StudentService import StudentService
from service.LaboratoryProblem import LaboratoryService
from service.serviceManager import ServiceManager
from domain.Validators import StudentExeption


class Ui:
    def __init__(self, student_Service: StudentService, laboratory_Service: LaboratoryService,service_manager:ServiceManager):
        self.__lab_service = laboratory_Service
        self.__student_service = student_Service
        self.__joined_Service = service_manager

    def print_meniu(self):
        list_menu = [
            "1.Adaugare student",
            "2.Stergere student",
            "3.Adaugare lab",
            "4.Stergere lab",
            "5.Modificare student",
            "6.Modificare lab",
            "7.Returneaza student dupa id",
            "8.Returneaza lab dupa id",
            "9.Asignare laborator",
            "10.Notare laborator",
            "11.Studetii asignati unui laborator",
            "12.Studentii cu note rele",
        ]
        for request in list_menu:
            print(request)

    def add_new_stud(self):
        student = input("Student = (Id)/(Name)/(group):")
        student = list(student.split("/"))

        self.__student_service.add_Student(int(student[0]), student[1], student[2])

    def del_stud(self):
        id_stud = int(input("Id student:"))
        self.__student_service.del_student(id_stud)

    def add_new_lab(self):
        lab = input("Lab = (id_lab)/(lab_number)/(problem_number)/(description)/(deadline in format DD:MM):")
        lab = list(lab.split("/"))
        self.__lab_service.add_lab(int(lab[0]), int(lab[1]), int(lab[2]), lab[3], lab[4])

    def del_lab(self):
        id_lab = int(input("Id lab:"))
        self.__lab_service.del_lab(id_lab)

    def update_stud(self):
        student = input("Student for update = (Id)/(Name)/(group):")
        student = list(student.split("/"))
        self.__student_service.update_student(int(student[0]), student[1], student[2])

    def update_lab(self):
        lab = input("Lab to update = (id_lab)/(lab_number)/(problem_number)/(description)/(deadline in format DD:MM):")
        lab = list(lab.split("/"))
        self.__lab_service.update_lab(int(lab[0]), int(lab[1]), int(lab[2]), lab[3], lab[4])

    def find_stud(self):
        id_stud = int(input("Id student:"))
        student = self.__student_service.return_student_by_id(id_stud)
        print(student)

    def find_problem(self):
        id_lab = int(input("Id laborator:"))
        lab = self.__lab_service.return_lab_by_id(id_lab)
        print(lab)


    def add_grade(self):
        student_id = int(input("Student id:"))
        lab_id = input("Lab id:")
        grade = input("Grade:")

        self.__joined_Service.note_student(student_id,lab_id,grade)

    def add_assignment(self):
        student_id = int(input("Student id:"))
        lab_id = int(input("Lab id:"))

        self.__joined_Service.assigne_lab_and_stud(student_id,lab_id)

    def raport_per_lab(self):
        lab_id = int(input("Lab id:"))

        print(self.__joined_Service.return_stud_for_given_lab(lab_id))

    def raport_bad_grades(self):
        students = self.__joined_Service.return_bad_stud()
        print(students)

    def add_entities(self):
        self.__lab_service.add_labs()
        self.__student_service.add_students()

    def Meniu(self):
        dict_of_func = {
            "1": self.add_new_stud,
            "2": self.del_stud,
            "3": self.add_new_lab,
            "4": self.del_lab,
            "5": self.update_stud,
            "6": self.update_lab,
            "7": self.find_stud,
            "8": self.find_problem,
            "10": self.add_grade,
            "9": self.add_assignment,
            "11": self.raport_per_lab,
            "12": self.raport_bad_grades
        }
        # self.add_entities()
        while True:
            try:
                self.print_meniu()
                option = input("Optiune din meniu:")

                if option == "X" or option == "x":
                    break

                dict_of_func[option]()

                # input()

            except StudentExeption as err:
                traceback.print_exc()
                print(err)
            except Exception as er:
                traceback.print_exc()
                print(er)


