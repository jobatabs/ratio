import unittest
from decimal import Decimal
from services.calculations import calculate_coffee, calculate_recipe, calculate_water
from units.coffee import Coffee
from units.water import Water
from units.recipe import Recipe


class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee(Decimal(65))
        self.water = Water(Decimal(1000))
        self.recipe = Recipe(grams_litre=Decimal(65))

    def test_calculate_coffee(self):
        self.assertEqual(calculate_coffee(
            self.water, self.recipe).grams, Decimal(65))

    def test_calculate_water(self):
        self.assertEqual(calculate_water(
            self.coffee, self.recipe).millilitres, Decimal(1000))

    def test_calculate_recipe(self):
        self.assertEqual(calculate_recipe(
            self.coffee, self.water).grams_litre, Decimal(65))
