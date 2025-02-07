from unittest import TestCase

from domain.Laboratory import Laboratory


class TestLaboratory(TestCase):
    def setUp(self):
        self.laboratory = Laboratory(1, 1, 1, "1", "10:10")

    def test_get_id(self):
        self.assertEquals(self.laboratory.get_id(), 1)

    def test_get_number_lab(self):
        self.assertEquals(self.laboratory.get_number_lab(), 1)

    def test_get_number_problem(self):
        self.assertEquals(self.laboratory.get_number_problem(), 1)

    def test_get_description(self):
        self.assertEquals(self.laboratory.get_description(), "1")

    def test_get_deadline(self):
        self.assertEquals(self.laboratory.get_deadline(), "10:10")

    def test_set_id(self):
        self.laboratory.set_id(2)
        self.assertEquals(self.laboratory.get_id(), 2)

    def test_set_number_lab(self):
        self.laboratory.set_number_lab(2)
        self.assertEquals(self.laboratory.get_number_lab(), 2)

    def test_set_number_problem(self):
        self.laboratory.set_number_problem(2)
        self.assertEquals(self.laboratory.get_number_problem(), 2)

    def test_set_description(self):
        self.laboratory.set_description("12")
        self.assertEquals(self.laboratory.get_description(), "12")

    def test_set_deadline(self):
        self.laboratory.set_deadline("10:11")
        self.assertEquals(self.laboratory.get_deadline(), "10:11")

    def test__eq__(self):
        lab = Laboratory(1, 1, 1, "1", "10:10")
        self.assertTrue(self.laboratory == lab)

    def test___str__(self):
        self.assertEquals(str(self.laboratory), "1/1/1/1")

    def test___repr__(self):
        self.assertEquals(repr(self.laboratory), "1/1/1/1\n")

    def tearDown(self) -> None:
        pass
