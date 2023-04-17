import unittest
from units.coffee import Coffee


class TestCoffee(unittest.TestCase):
    def setUp(self):
        self.coffee = Coffee(12)

    def test_coffee_spoons(self):
        self.assertEqual(self.coffee.coffee_spoons, 1)
        self.assertIsInstance(self.coffee.coffee_spoons, int)

    def test_coffee_spoons_fraction(self):
        coffee = Coffee(11)
        self.assertEqual(coffee.coffee_spoons, 1)
        coffee = Coffee(2)
        self.assertEqual(coffee.coffee_spoons, 0)
