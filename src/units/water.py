"""Defines Water, a subclass of Unit that adds fluid volume conversions.
"""

from decimal import Decimal
from units.unit import Unit


class Water(Unit):
    """Water supplements Unit with fluid volume conversions.
    """
    @property
    def millilitres(self) -> Decimal:
        """Calculates volume in millilitres.

        Returns:
            Decimal: Volume in millilitres.
        """
        return self._mass_g

    @property
    def fluid_ounces(self) -> Decimal:
        """Calculates volume in US fluid ounces.

        Returns:
            Decimal: Volume in US fluid ounces.
        """
        return (self._mass_g / Decimal("29.57353")).quantize(Decimal("10.00000"))

    @property
    def litres(self) -> Decimal:
        """Calculates volume in litres

        Returns:
            Decimal: Volume in litres.
        """
        return self._mass_g / 1000
