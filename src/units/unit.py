"""Defines Unit, a class used as a base for unit conversions.
"""
from decimal import Decimal

class Unit:
    """Base class for unit conversions
    """
    def __init__(self, mass_g: Decimal) -> None:
        self._mass_g = Decimal(mass_g)

    @property
    def grams(self) -> Decimal:
        """Calculates mass in grams.

        Returns:
            Decimal: The instance's mass in grams.
        """
        return self._mass_g

    @property
    def ounces(self) -> Decimal:
        """Calculates mass in ounces.

        Returns:
            Decimal: The instance's mass in ounces.
        """
        return (self._mass_g / Decimal(28.349523125)).quantize(Decimal("10.00000"))

    @property
    def pounds(self) -> Decimal:
        """Calculates mass in pounds.

        Returns:
            Decimal: The instance's mass in pounds.
        """
        return (self._mass_g / 1000 / Decimal(0.45359237)).quantize(Decimal("10.00000"))
