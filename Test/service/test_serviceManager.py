from unittest import TestCase

from domain.Dto import AssigmentDto
from domain.Lab_assigment import Lab_assigment
from domain.Student import Student
from repository.Repository import Repository
from service.serviceManager import ServiceManager


class TestServiceManager(TestCase):
    def setUp(self):
        self.lab_assigment = Lab_assigment(1, 1, -1)
        self.assigments_repository = Repository()
        self.student_repository = Repository()
        self.service_manager = ServiceManager(self.assigments_repository, self.student_repository)

    def test_assigne_lab_and_stud(self):
        self.service_manager.assigne_lab_and_stud(1, 1)
        self.assertEqual(self.assigments_repository.return_all(),[self.lab_assigment])

    def test_note_student(self):
        self.service_manager.assigne_lab_and_stud(1, 1)
        self.service_manager.note_student(1, 1, 10)
        self.assertTrue(self.assigments_repository.return_all()[0] == self.lab_assigment)

    def test_return_stud_for_given_lab(self):
        self.service_manager.assigne_lab_and_stud(1, 1)
        self.student_repository.save(Student(1,"P",1))
        stud = self.service_manager.return_stud_for_given_lab(1)
        self.assertEqual([stud],[[AssigmentDto("P",-1)]])

    def test_return_bad_stud(self):
        self.service_manager.assigne_lab_and_stud(1, 1)
        self.student_repository.save(Student(1, "P", 1))
        self.service_manager.note_student(1,1,4)
        self.assertEqual([self.service_manager.return_bad_stud()],[[AssigmentDto("P",4)]])
