"""Defines Coffee, a child class of Unit that adds conversion to coffee spoons.
"""

from decimal import Decimal, ROUND_HALF_UP
from units.unit import Unit


class Coffee(Unit):
    """A subclass of Unit that adds conversion to coffee spoons.
    """
    @property
    def coffee_spoons(self) -> int:
        """Calculates volume in amount of coffee spoons.

        Returns:
            int: Amount of coffee spoons, rounded to nearest full spoon.
        """
        return int((self._mass_g / 12).quantize(Decimal("0"), rounding=ROUND_HALF_UP))
