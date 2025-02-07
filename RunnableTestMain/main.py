import unittest

from domain.Lab_assigment import Lab_assigment
from domain.Laboratory import Laboratory
from domain.Student import Student
from repository.Repository import Repository
from repository.FileRepository import FileRepository
from service.LaboratoryProblem import LaboratoryService
from service.StudentService import StudentService
from service.serviceManager import ServiceManager
from ui.Ui import Ui



if __name__ == "__main__":

    option = 2
    if option == 1:
        student_Rep = Repository()
        lab_Rep = Repository()
        assigment_Rep = Repository()

        assigment_service = ServiceManager(assigment_Rep,student_Rep)
        stud_Service = StudentService(student_Rep)
        lab_Service = LaboratoryService(lab_Rep)
        ui = Ui(stud_Service, lab_Service,assigment_service)
        ui.Meniu()
    else:
        student_Rep = FileRepository("../Files/Student_File_Repository", Student)
        lab_Rep = FileRepository("../Files/Laboratory_File_Repository", Laboratory)
        assigment_Rep = FileRepository("../Files/Assigments_File_Repository", Lab_assigment)

        assigment_service = ServiceManager(assigment_Rep, student_Rep)
        stud_Service = StudentService(student_Rep)
        lab_Service = LaboratoryService(lab_Rep)
        ui = Ui(stud_Service, lab_Service, assigment_service)


        ui.Meniu()
