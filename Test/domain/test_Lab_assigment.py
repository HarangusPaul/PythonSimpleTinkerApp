from unittest import TestCase

from domain.Lab_assigment import Lab_assigment


class TestLab_assigment(TestCase):
    def setUp(self):
        self.laboratory = Lab_assigment(1, 1, 10)

    def test_grade(self):
        self.assertEqual(self.laboratory.grade, 10)

    def test_get_id(self):
        self.assertEqual(self.laboratory.get_id(), "(1,1)")

    def test_id_stud(self):
        self.assertIsInstance(self.laboratory.id_stud, int)
        self.assertFalse(self.laboratory.id_stud == 2)
        self.assertEqual(self.laboratory.id_stud, 1)

    def test_id_lab(self):
        self.assertEqual(self.laboratory.id_lab, 1)

    def test___str__(self):
        self.assertEqual(str(self.laboratory), "1/1/10\n")

    def test___repr__(self):
        self.assertEqual(repr(self.laboratory), "1/1/10")

    def test___eq__(self):
        student2 = Lab_assigment(1, 1, 10)
        self.assertTrue(self.laboratory == student2)

    def tearDown(self) -> None:
        pass