"""calculations.py provides functions for calculating coffee from water+recipe,
and vice versa, and calculating recipe from coffee : water.
"""

from decimal import Decimal
from units.recipe import Recipe
from units.water import Water
from units.coffee import Coffee


def calculate_recipe(coffee: Coffee, water: Water) -> Recipe:
    """Calculates brew strength from given amount of coffee and water.

    Args:
        coffee (Coffee): Desired amount of coffee.
        water (Water): Desired amount of water.

    Returns:
        Recipe: A Recipe object with the strength set to what the ratio of Coffee / Water is.
    """
    return Recipe(grams_litre=coffee.grams / water.litres)


def calculate_water(coffee: Coffee, recipe: Recipe) -> Water:
    """Calculates water needed to brew some amount of coffee at some brew strength.

    Args:
        coffee (Coffee): Desired amount of coffee to use.
        recipe (Recipe): Desired brew strength.

    Returns:
        Water: Amount of water needed to brew Coffee at Recipe strength.
    """
    return Water((recipe.one_x * coffee.grams).quantize(Decimal("1000.00000")))


def calculate_coffee(water: Water, recipe: Recipe) -> Coffee:
    """Calculates coffee needed to brew some final beverage volume at some brew strength.

    Args:
        water (Water): Desired amount of water.
        recipe (Recipe): Desired brew strength.

    Returns:
        Coffee: Amount of coffee needed to produce Water grams of coffee at Recipe strength.
    """
    return Coffee(recipe.grams_litre * water.grams / 1000)
