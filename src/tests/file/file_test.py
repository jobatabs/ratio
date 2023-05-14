import unittest, os
from file.file import write_recipe, read_recipe
from units.coffee import Coffee
from units.water import Water
from units.recipe import Recipe

class TestFile(unittest.TestCase):
    def setUp(self):
        self._water = Water(250)
        self._coffee = Coffee(15)
        self._recipe = Recipe(grams_litre=60)

    def test_write_read(self):
        with open("ratio.test", "w", encoding="UTF-8") as file:
            write_recipe(file, self._coffee, self._water, self._recipe)
        with open("ratio.test", "r", encoding="UTF-8") as file:
            coffee, water, recipe = read_recipe(file)

        self.assertEqual(coffee.grams, self._coffee.grams)
        self.assertEqual(water.millilitres, self._water.millilitres)
        self.assertEqual(recipe.one_x, self._recipe.one_x)

    def tearDown(self):
        try:
            os.remove("ratio.test")
        except OSError as error:
            print(error)
