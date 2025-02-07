from unittest import TestCase

from domain.Laboratory import Laboratory
from repository.Repository import Repository
from service.LaboratoryProblem import LaboratoryService


class TestLaboratoryService(TestCase):
    def setUp(self):
        self.repository_lab = Repository()
        self.service_lab = LaboratoryService(self.repository_lab)
        self.lab = Laboratory(1,1,1,1,"10:10")

    def test_add_lab(self):
        self.service_lab.add_lab(1,1,1,1,"10:10")
        self.assertTrue(self.service_lab.return_all_labs() == self.repository_lab.return_all())

    def test_del_lab(self):
        self.service_lab.add_lab(1,1,1,1,"10:10")
        self.service_lab.del_lab(1)
        self.assertTrue(self.service_lab.return_all_labs() == self.repository_lab.return_all())

    def test_update_lab(self):
        self.service_lab.add_lab(1, 1, 1, 1, "10:10")
        self.service_lab.update_lab(1, 2, 1, 1, "10:10")
        self.assertTrue(self.service_lab.return_all_labs() == self.repository_lab.return_all())

    def test_return_lab_by_id(self):
        self.service_lab.add_lab(1, 1, 1, 1, "10:10")
        lab = Laboratory(1, 1, 1, 1, "10:10")
        self.assertEqual(self.service_lab.return_lab_by_id(1),lab)

    def test_return_all_labs(self):
        self.service_lab.add_lab(1, 1, 1, 1, "10:10")
        self.assertTrue(self.service_lab.return_all_labs() == self.repository_lab.return_all())
