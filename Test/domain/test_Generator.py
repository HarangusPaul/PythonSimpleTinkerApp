from unittest import TestCase

from domain.Generator import Generator
from domain.Lab_assigment import Lab_assigment
from domain.Laboratory import Laboratory
from domain.Student import Student


class TestGenerator(TestCase):
    def setUp(self):
        self.generator = Generator()
        self.lab_generator = Laboratory
        self.student_generator = Student
        self.assigment_generator = Lab_assigment


    def test_generate_class(self):
        stud = self.generator.generate_class(self.student_generator,"1/p/3")
        lab = self.generator.generate_class(self.lab_generator,"1/1/1/1/10:10")
        assigment = self.generator.generate_class(self.assigment_generator,"1/1/1")
        self.assertIsInstance(stud, Student)
        self.assertIsInstance(lab,Laboratory)
        self.assertIsInstance(assigment,Lab_assigment)

    def test_generate_student_class(self):
        stud = self.generator.generate_student_class("1/p/1", self.student_generator)
        self.assertIsInstance(stud, Student)

    def test_generate_laboratory_class(self):
        stud = self.generator.generate_laboratory_class("1/1/1/1/10:10", self.lab_generator)
        self.assertIsInstance(stud, Laboratory)

    def test_generate_assigment_class(self):
        stud = self.generator.generate_assigment_class("1/1/1", self.assigment_generator)
        self.assertIsInstance(stud, Lab_assigment)
