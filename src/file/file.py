"""file.py provides functions write_recipe() and read_recipe(), which handle application data I/O.
"""

import io
from decimal import Decimal
from units.coffee import Coffee
from units.water import Water
from units.recipe import Recipe


def write_recipe(file: io.TextIOWrapper, coffee: Coffee, water: Water, recipe: Recipe) -> bool:
    """write_recipe() stores all application data into a file, then closes the file.
    Data is written line by line; the first line is Coffee.grams,
    the second line is Water.grams, and the third is Recipe.grams_litre.

    Args:
        file (io.TextIOWrapper): A file reference in write mode.
        coffee (Coffee): A Coffee object.
        water (Water): A Water object.
        recipe (Recipe): A Recipe object.

    Returns:
        bool: If file could be written to, True. If the file is not available, False.
    """
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
    """read_recipe() reads the contents of a .ratio file and returns the resulting
    data as reconstructed instances of application logic classes. The file is then closed.

    Args:
        file (io.TextIOWrapper): A file reference in read mode.

    Returns:
        tuple[Coffee, Water, Recipe]: A tuple containing instances of classes
        Coffee, Water, Recipe with their values initialized to data read.
    """
    if file is not None:
        lines = file.readlines()
        file.close()
        coffee = Coffee(Decimal(lines[0]))
        water = Water(Decimal(lines[1]))
        recipe = Recipe(grams_litre=Decimal(lines[2]))
        return coffee, water, recipe
    return None
