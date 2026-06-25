import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Testy dla klasy Employee."""

    def setUp(self):
        """Utworzenie danych do użycia we wszystkich metodach testowych"""
        self.employee = Employee('Jan', 'Kowalski', 10000)

    def test_give_default_rise(self):
        """Sprawdzenie, czy domyślna podwyżka jest poprawnie dodawana."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 15000)

    def test_give_custom_raise(self):
        """Sprawdzenie, czy wprowadzona podwyżka jest poprawnie dodawana."""
        self.employee.give_raise(3000)
        self.assertEqual(self.employee.salary, 13000)

if __name__ == '__main__':
    unittest.main()