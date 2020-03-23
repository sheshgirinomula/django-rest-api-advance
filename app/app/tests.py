from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Testing of two numbers addition"""
        self.assertEqual(add(3,8), 11)

    def test_subtract_numbers(self):
        """Testing of two numbers subtraction"""
        self.assertEqual(subtract(3,8), 5)