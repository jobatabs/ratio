"""Defines Recipe, a class containing information on brewing ratios.
"""

from decimal import Decimal


class Recipe:
    """Recipe encapsulates a brewing ratio, which can be expressed as either g/L or 1:X.
    """

    def __init__(self, one_x: Decimal = None, grams_litre: Decimal = None) -> None:
        if one_x and grams_litre:
            raise TypeError("Cannot init from both recipe types at once")
        if one_x:
            self._one_x = one_x
            self._grams_litre = Decimal(Decimal(1000)/one_x)
        if grams_litre:
            self._grams_litre = grams_litre
            self._one_x = Decimal(Decimal(1000)/grams_litre)
        if not one_x and not grams_litre:
            raise TypeError("A recipe must be passed")

    @property
    def one_x(self) -> Decimal:
        """Calculates recipe in 1:x format.

        Returns:
            Decimal: 1:x.
        """
        return self._one_x

    @property
    def grams_litre(self) -> Decimal:
        """Calculates recipe in g/L format.

        Returns:
            Decimal: x g/1L.
        """
        return self._grams_litre
