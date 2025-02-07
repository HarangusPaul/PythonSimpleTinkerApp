from unittest import TestCase

from domain.Student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student(1, "P", 3)

    def test_get_id(self):
        self.assertEquals(self.student.get_id(), 1)

    def test_get_name(self):
        self.assertEquals(self.student.get_name(), "P")

    def test_get_group(self):
        self.assertEquals(self.student.get_group(), "3")

    def test_set_id(self):
        self.student.set_id(2)
        self.assertEquals(self.student.get_id(), 2)

    def test_set_name(self):
        self.student.set_name("n")
        self.assertEquals(self.student.get_name(), "n")

    def test_set_group(self):
        self.student.set_group(2)
        self.assertEquals(self.student.get_group(), 2)

    def test__eq__(self):
        student = Student(1, "P", 3)
        self.assertTrue(self.student == student)

    def test___str__(self):
        self.assertEquals(str(self.student), "1/P/3\n")

    def test___repr__(self):
        self.assertEquals(repr(self.student), "1.Name:P in group:3")

    def tearDown(self) -> None:
        pass  # cleanup code after each test
