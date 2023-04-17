import unittest
from units.water import Water
from decimal import Decimal


class TestWater(unittest.TestCase):
    def setUp(self):
        self.water = Water(1000)

    def test_litres(self):
        self.assertEqual(self.water.litres, 1)
        self.assertIsInstance(self.water.litres, Decimal)

    def test_millitres(self):
        self.assertEqual(self.water.millilitres, 1000)
        self.assertIsInstance(self.water.millilitres, Decimal)

    def test_fluid_ounces(self):
        self.assertEqual(self.water.fluid_ounces, Decimal("33.81402"))
        self.assertIsInstance(self.water.fluid_ounces, Decimal)
