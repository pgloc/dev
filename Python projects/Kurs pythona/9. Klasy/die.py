"""Klasa używana do zaprezentowania kostki do gry."""
from random import randint

class Die():
    """Próba zaprezentowania kostki do gry."""

    def __init__(self, sides=6):
        """Inicjalizacja atrybutów kostki."""
        self.sides = sides

    def roll_die(self):
        """Symulacja rzutu kostką."""
        print(f"{randint(1, self.sides)}")