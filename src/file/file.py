import io
from decimal import Decimal
from units.coffee import Coffee
from units.water import Water
from units.recipe import Recipe


def write_recipe(file: io.TextIOWrapper, coffee: Coffee, water: Water, recipe: Recipe) -> bool:
    if file is not None:
        try:
            file.write(f"{coffee.grams}\n")
            file.write(f"{water.grams}\n")
            file.write(f"{recipe.grams_litre}\n")
            file.close()
        except io.UnsupportedOperation:
            return False
        return True
    return False


def read_recipe(file: io.TextIOWrapper) -> tuple[Coffee, Water, Recipe]:
    if file is not None:
        lines = file.readlines()
        file.close()
        coffee = Coffee(Decimal(lines[0]))
        water = Water(Decimal(lines[1]))
        recipe = Recipe(grams_litre=Decimal(lines[2]))
        return coffee, water, recipe
    return None
