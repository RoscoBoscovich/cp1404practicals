"""
new fancy silverservice taxi class
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return super().__str__() + " plus flagfall ${}".format(self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return (super().get_fare() + self.flagfall)