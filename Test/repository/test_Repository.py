from unittest import TestCase
from repository.Repository import Repository
from domain.Student import Student

class TestRepository(TestCase):
    def setUp(self):
        self.repository = Repository()
        self.student = Student(1, "P", 3)
        self.repository.save(self.student)

    def test_return_all(self):
        return_all = self.repository.return_all()
        student1 = return_all[0]
        self.assertEquals(student1, self.student)

    def test_save(self):
        self.assertEquals(self.repository.return_all(), [self.student])

    def test_delete(self):
        self.repository.delete(self.student)
        self.assertTrue(len(self.repository.return_all()) == 0)

    def test_return_object_by_id(self):
        self.assertTrue(self.repository.return_object_by_id(1) == self.student)

    def test_update(self):
        student2 = Student(1, "P", 4)
        self.repository.update(student2)
        self.assertTrue(self.repository.return_object_by_id(1) == student2)
