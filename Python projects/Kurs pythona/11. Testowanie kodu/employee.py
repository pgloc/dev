class Employee():
    """Przechowuje dane o pracowniku."""

    def __init__(self, first, last, salary):
        """Inizjalizacja atrybutów imię, nazwisko i roczna pensja."""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """Zwiększa wynagrodzenie pracownika."""
        self.salary += amount