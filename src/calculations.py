from decimal import Decimal
from units.recipe import Recipe
from units.water import Water
from units.coffee import Coffee


def calculate_recipe(coffee: Coffee, water: Water) -> Recipe:
    return Recipe(grams_litre=coffee.grams / water.litres)


def calculate_water(coffee: Coffee, recipe: Recipe) -> Water:
    return Water((recipe.one_x * coffee.grams).quantize(Decimal("1000.00000")))


def calculate_coffee(water: Water, recipe: Recipe) -> Coffee:
    return Coffee(recipe.grams_litre * water.grams / 1000)
