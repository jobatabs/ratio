import unittest
from decimal import Decimal
from units.recipe import Recipe


class TestRecipe(unittest.TestCase):
    def setUp(self):
        self.recipe_one_x = Recipe(one_x=Decimal(17))
        self.recipe_grams_litre = Recipe(grams_litre=Decimal(65))

    def test_grams_litre(self):
        self.assertEqual(self.recipe_one_x.grams_litre,
                         Decimal(1000)/Decimal(17))

    def test_one_x(self):
        self.assertEqual(self.recipe_grams_litre.one_x,
                         Decimal(1000)/Decimal(65))

    def test_overloaded_recipe(self):
        self.assertRaises(TypeError, Recipe, Decimal(17), Decimal(65))

    def test_empty_recipe(self):
        self.assertRaises(TypeError, Recipe)
