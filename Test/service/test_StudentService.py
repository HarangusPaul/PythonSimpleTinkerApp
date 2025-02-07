from unittest import TestCase

from domain.Student import Student
from repository.Repository import Repository
from service.StudentService import StudentService


class TestStudentService(TestCase):
    def setUp(self):
        self.repository_lab = Repository()
        self.service_lab = StudentService(self.repository_lab)
        self.lab = Student(1,1,1)

    def test_add_lab(self):
        self.service_lab.add_Student(1,1,1)
        self.assertTrue(self.service_lab.return_all_students() == self.repository_lab.return_all())

    def test_del_lab(self):
        self.service_lab.add_Student(1,1,1)
        self.service_lab.del_student(1)
        self.assertTrue(self.service_lab.return_all_students() == self.repository_lab.return_all())

    def test_update_lab(self):
        self.service_lab.add_Student(1, 1, 1)
        self.service_lab.update_student(1, 2, 1)
        self.assertTrue(self.service_lab.return_all_students() == self.repository_lab.return_all())

    def test_return_lab_by_id(self):
        self.service_lab.add_Student(1, 1, 1)
        lab = Student(1, 1, 1)
        self.assertEqual(self.service_lab.return_student_by_id(1),lab)

    def test_return_all_labs(self):
        self.service_lab.add_Student(1, 1, 1)
        self.assertTrue(self.service_lab.return_all_students() == self.repository_lab.return_all())
