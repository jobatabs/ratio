import unittest
from decimal import Decimal
from units.unit import Unit

class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(1000)

    def test_grams(self):
        self.assertEqual(self.unit.grams, 1000)
        self.assertIsInstance(self.unit.grams, Decimal)

    def test_ounces(self):
        self.assertEqual(self.unit.ounces, Decimal("35.27396"))
        self.assertIsInstance(self.unit.ounces, Decimal)
    
    def test_pounds(self):
        self.assertEqual(self.unit.pounds, Decimal("2.20462"))
        self.assertIsInstance(self.unit.pounds, Decimal)
