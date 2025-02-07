from unittest import TestCase

from domain.Dto import AssigmentDto


class TestAssigmentDto(TestCase):
    def setUp(self):
        self.assigment_dto = AssigmentDto("P", 1)
        self.assertIsInstance(self.assigment_dto,AssigmentDto)
        self.assertEqual(self.assigment_dto,AssigmentDto("P", 1))
